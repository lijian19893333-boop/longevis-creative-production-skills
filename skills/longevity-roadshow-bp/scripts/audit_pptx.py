#!/usr/bin/env python3
"""Read-only PPTX audit: cross-slide image reuse, missing images, native evidence."""
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import posixpath
import re
import sys
import xml.etree.ElementTree as ET
from zipfile import ZipFile

NS = {
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'c': 'http://schemas.openxmlformats.org/drawingml/2006/chart',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
}

def resolve_part(owner, target):
    if target.startswith('/'):
        return posixpath.normpath(target.lstrip('/'))
    return posixpath.normpath(posixpath.join(posixpath.dirname(owner), target))

def audit(pptx, allowed):
    report = {
        'pptx': str(Path(pptx).resolve()), 'slide_count': 0,
        'native_tables': 0, 'native_charts': 0, 'chart_owner_slides': [],
        'embedded_workbooks': 0, 'image_uses': [], 'unique_content_images': 0,
        'reused_images': [], 'broken_image_references': [],
        'allowed_reuse_media': sorted(allowed),
    }
    grouped = defaultdict(list)
    with ZipFile(pptx) as z:
        parts = set(z.namelist())
        slides = sorted((p for p in parts if re.fullmatch(r'ppt/slides/slide\d+\.xml', p)),
                        key=lambda p: int(re.search(r'slide(\d+)', p).group(1)))
        report['slide_count'] = len(slides)
        report['embedded_workbooks'] = sum('/embeddings/' in p and p.lower().endswith('.xlsx') for p in parts)
        for part in slides:
            n = int(re.search(r'slide(\d+)', part).group(1))
            root = ET.fromstring(z.read(part))
            report['native_tables'] += len(root.findall('.//a:tbl', NS))
            charts = len(root.findall('.//c:chart', NS))
            report['native_charts'] += charts
            if charts:
                report['chart_owner_slides'].append(n)
            rp = posixpath.join(posixpath.dirname(part), '_rels', posixpath.basename(part)+'.rels')
            rels = {}
            if rp in parts:
                for e in ET.fromstring(z.read(rp)):
                    rels[e.get('Id')] = e.attrib
            for blip in root.findall('.//a:blip', NS):
                rid = blip.get('{'+NS['r']+'}embed') or blip.get('{'+NS['r']+'}link')
                relation = rels.get(rid)
                if relation is None or relation.get('TargetMode') == 'External':
                    report['broken_image_references'].append({'slide': n, 'relationship': rid,
                        'reason': 'missing relationship or external image not embedded'})
                    continue
                target = resolve_part(part, relation.get('Target', ''))
                if target not in parts:
                    report['broken_image_references'].append({'slide': n, 'media': target,
                        'reason': 'referenced image part is missing'})
                    continue
                digest = hashlib.sha256(z.read(target)).hexdigest()
                use = {'slide': n, 'media': target, 'sha256': digest,
                       'allowed_reuse': target in allowed}
                report['image_uses'].append(use)
                if target not in allowed:
                    grouped[digest].append(use)
    report['unique_content_images'] = len(grouped)
    for digest, uses in grouped.items():
        pages = sorted({u['slide'] for u in uses})
        if len(pages) > 1:
            report['reused_images'].append({'sha256': digest, 'slides': pages,
                'media_parts': sorted({u['media'] for u in uses})})
    report['status'] = 'pass' if not (report['reused_images'] or report['broken_image_references']) else 'needs_review'
    report['limitations'] = 'Byte-identical reuse only; visually inspect crops, recolors, repeated scenes, product consistency and legibility.'
    return report

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('pptx', help='PPTX to inspect; never modified')
    p.add_argument('--allow-reuse-media', action='append', default=[],
                   help='Exact package part for a verified reusable logo/icon; repeat for each')
    p.add_argument('--report', help='Optional JSON report path, normally a private work directory')
    args = p.parse_args()
    try:
        result = audit(args.pptx, {s.lstrip('/') for s in args.allow_reuse_media})
    except Exception as exc:
        print(json.dumps({'status': 'error', 'error': str(exc)}, ensure_ascii=False))
        return 2
    content = json.dumps(result, ensure_ascii=False, indent=2)
    if args.report:
        target = Path(args.report)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding='utf-8')
    print(content)
    return 0 if result['status'] == 'pass' else 2

if __name__ == '__main__':
    sys.exit(main())
