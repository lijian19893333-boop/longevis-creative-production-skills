"""Snapshot and verify model/source/texture files; never edit source files."""
import argparse, json
from pathlib import Path
from workflow_io import sha256, atomic_json

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('action',choices=['create','verify']);p.add_argument('snapshot',type=Path)
    p.add_argument('--root',type=Path);p.add_argument('--strict',action='store_true')
    p.add_argument('--suffixes',default='.blend,.glb,.gltf,.obj,.mtl,.py,.json,.png,.jpg,.jpeg,.exr,.hdr')
    a=p.parse_args();snapshot=a.snapshot.resolve()
    if a.action=='create':
        if snapshot.exists():raise ValueError('Snapshot already exists; choose a new name to retain the baseline.')
        if a.root is None:raise ValueError('--root is required for create')
        root=a.root.resolve();suffixes=set(a.suffixes.lower().split(','))
        if not root.is_dir():raise ValueError(f'Not a directory: {root}')
        files={str(f.relative_to(root)):sha256(f) for f in sorted(root.rglob('*')) if f.is_file() and f.resolve()!=snapshot and f.suffix.lower() in suffixes and not any(x in f.parts for x in ['.git','__pycache__'])}
        if not files:raise ValueError('No matching source files')
        atomic_json(snapshot,dict(root=str(root),suffixes=sorted(suffixes),files=files))
        print(json.dumps(dict(snapshot=str(snapshot),file_count=len(files)),ensure_ascii=False));return
    data=json.loads(snapshot.read_text());root=(a.root or Path(data['root'])).resolve()
    missing=[];changed=[]
    for name,h in data['files'].items():
        f=(root/name).resolve()
        if not f.is_relative_to(root):raise ValueError('Snapshot path escapes root')
        if not f.is_file():missing.append(name)
        elif sha256(f)!=h:changed.append(name)
    added=[str(f.relative_to(root)) for f in root.rglob('*') if f.is_file() and f.resolve()!=snapshot and f.suffix.lower() in data['suffixes'] and str(f.relative_to(root)) not in data['files'] and not any(x in f.parts for x in ['.git','__pycache__'])]
    ok=not missing and not changed and not(a.strict and added)
    print(json.dumps(dict(unchanged=ok,missing=missing,changed=changed,added=sorted(added)),ensure_ascii=False,indent=2))
    if not ok:raise SystemExit(1)

if __name__=='__main__':main()
