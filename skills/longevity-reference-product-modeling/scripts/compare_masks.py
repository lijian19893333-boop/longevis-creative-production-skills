#!/usr/bin/env python3
"""Compare calibrated grayscale silhouettes, without fitting away shape errors."""
import argparse
import hashlib
import json
import math
from pathlib import Path
from PIL import Image, ImageChops


def mask(path):
    with Image.open(path) as image:
        if image.mode not in ('1', 'L'):
            raise ValueError('Use a grayscale black-background/white-object mask, not a beauty image.')
        return image.convert('L').point(lambda value: 255 if value >= 128 else 0)


def run(args):
    if not math.isfinite(args.scale) or args.scale <= 0:
        raise ValueError('scale must be positive and finite')
    if not all(math.isfinite(v) for v in args.reference_anchor + args.model_anchor):
        raise ValueError('anchors must be finite')
    ref, model = mask(args.reference), mask(args.model)
    if not ref.getbbox() or not model.getbbox():
        raise ValueError('Both input masks must contain a nonempty product silhouette.')
    rx, ry = args.reference_anchor
    mx, my = args.model_anchor
    inverse = (1/args.scale, 0, mx-rx/args.scale, 0, 1/args.scale, my-ry/args.scale)
    aligned = model.transform(ref.size, Image.Transform.AFFINE, inverse,
                              resample=Image.Resampling.NEAREST, fillcolor=0)
    common = ImageChops.multiply(ref, aligned)
    union = ImageChops.lighter(ref, aligned)
    overlay = Image.new('RGB', ref.size, (245,245,245))
    overlay.paste((220,45,60), mask=ref)
    overlay.paste((35,105,220), mask=aligned)
    overlay.paste((145,55,175), mask=common)
    intersection_area = common.histogram()[255]
    union_area = union.histogram()[255]
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    overlay.save(output/'overlay.png')
    aligned.save(output/'model-aligned.png')
    report = {
        'basis': args.basis, 'uniform_scale': args.scale,
        'reference_anchor_px': args.reference_anchor, 'model_anchor_px': args.model_anchor,
        'reference_dimensions_px': list(ref.size), 'model_dimensions_px': list(model.size),
        'reference_sha256': hashlib.sha256(Path(args.reference).read_bytes()).hexdigest(),
        'model_sha256': hashlib.sha256(Path(args.model).read_bytes()).hexdigest(),
        'silhouette_iou': intersection_area/union_area,
        'reference_only_px': ref.histogram()[255]-intersection_area,
        'model_only_px': aligned.histogram()[255]-intersection_area,
        'scope': 'One calibrated projected silhouette only; not whole-model accuracy, hidden geometry or CAD tolerance.',
    }
    (output/'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reference', required=True)
    parser.add_argument('--model', required=True)
    parser.add_argument('--scale', required=True, type=float)
    parser.add_argument('--reference-anchor', nargs=2, required=True, type=float)
    parser.add_argument('--model-anchor', nargs=2, required=True, type=float)
    parser.add_argument('--basis', required=True, help='Actual dimension/camera evidence for the scale and anchors')
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    try:
        run(args)
    except (ValueError, OSError) as error:
        parser.exit(2, str(error)+'\n')

if __name__ == '__main__':
    main()
