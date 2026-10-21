"""Validate public skill packaging and community configuration without production tools."""
from pathlib import Path
import ast
import json
import re
import sys
from urllib.parse import unquote
import yaml

ROOT = Path(__file__).resolve().parents[2]

def main():
    errors = []
    files = [p for p in ROOT.rglob('*') if p.is_file()
             and not any(part in {'.git', '__pycache__'} for part in p.relative_to(ROOT).parts)
             and p.suffix != '.pyc']
    links = 0
    for path in files:
        relative = path.relative_to(ROOT)
        try:
            if path.suffix == '.py':
                ast.parse(path.read_text(encoding='utf-8'), filename=str(relative))
            elif path.suffix == '.json':
                json.loads(path.read_text(encoding='utf-8'))
            elif path.suffix in {'.yaml', '.yml'}:
                yaml.safe_load(path.read_text(encoding='utf-8'))
            elif path.suffix == '.md':
                for target in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
                    target = target.strip('<>').split('#', 1)[0]
                    if not target or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target):
                        continue
                    links += 1
                    destination = ROOT / unquote(target.lstrip('/')) if target.startswith('/') else path.parent / unquote(target)
                    if not destination.exists():
                        errors.append(f'{relative}: missing local link {target}')
        except (ValueError, SyntaxError, yaml.YAMLError) as exc:
            errors.append(f'{relative}: {exc}')

    catalog = json.loads((ROOT / 'catalog.json').read_text())
    entries = catalog['skills']
    names = [item['name'] for item in entries]
    folders = sorted(p.name for p in (ROOT / 'skills').iterdir() if p.is_dir() and p.name != '__pycache__')
    if len(names) != len(set(names)) or sorted(names) != folders:
        errors.append('Catalog names must be unique and match skill folders')
    for item in entries:
        name = item['name']
        if not re.fullmatch(r'longevity-[a-z0-9]+(?:-[a-z0-9]+)*', name):
            errors.append(f'{name}: installation name must use longevity-*')
        folder = ROOT / 'skills' / name
        for key in ('entry_en', 'entry_zh'):
            if not (ROOT / item[key]).is_file():
                errors.append(f'{name}: missing {key}')
        for filename in ('SKILL.md', 'SKILL.en.md', 'SKILL.zh-CN.md'):
            path = folder / filename
            if not path.is_file():
                errors.append(f'{name}: missing {filename}')
                continue
            text = path.read_text(encoding='utf-8')
            match = re.match(r'^---\n(.*?)\n---(?:\n|$)', text, re.S)
            meta = yaml.safe_load(match[1]) if match else {}
            if not isinstance(meta, dict) or meta.get('name') != name or not isinstance(meta.get('description'), str) or not meta['description'].strip():
                errors.append(f'{name}/{filename}: invalid name or description')
        if (folder / 'SKILL.md').read_bytes() != (folder / 'SKILL.en.md').read_bytes():
            errors.append(f'{name}: English compatibility copy differs')

    for path in (ROOT / '.github/ISSUE_TEMPLATE').glob('*.yml'):
        form = yaml.safe_load(path.read_text())
        if path.name == 'config.yml':
            continue
        if not all(form.get(key) for key in ('name', 'description', 'body')):
            errors.append(f'{path.name}: incomplete issue form')
        ids = [field['id'] for field in form['body'] if 'id' in field]
        if len(ids) != len(set(ids)):
            errors.append(f'{path.name}: duplicate field IDs')
        dropdown = next(field for field in form['body'] if field.get('id') == 'skill')
        if not set(names).issubset(dropdown['attributes']['options']):
            errors.append(f'{path.name}: missing skills in selector')
    if (ROOT / 'README.md').read_bytes() != (ROOT / 'README.en.md').read_bytes():
        errors.append('English README compatibility copy differs')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'PASS: {len(entries)} skills, {len(files)} files, {links} local Markdown links; JSON/YAML and Python syntax valid.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
