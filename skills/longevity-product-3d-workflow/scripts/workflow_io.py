"""Shared deterministic file helpers (Python standard library only)."""
import hashlib, json, re, struct, uuid, zlib
from pathlib import Path

def sha256(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
    return h.hexdigest()

def atomic_json(path, data):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name('.'+path.name+'.'+uuid.uuid4().hex+'.tmp')
    try:
        tmp.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        tmp.replace(path)
    finally:tmp.unlink(missing_ok=True)

def safe_id(value):
    if not isinstance(value,str) or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]{0,79}',value):
        raise ValueError(f'Use a short ASCII file identifier: {value!r}; Unicode is supported in labels.')
    return value

def check_png(path, expected=None):
    """Check PNG structure, every chunk CRC, dimensions and complete IEND."""
    size=None;data_seen=False
    with Path(path).open('rb') as f:
        if f.read(8)!=b'\x89PNG\r\n\x1a\n':raise ValueError(f'Not PNG: {path}')
        while True:
            head=f.read(8)
            if len(head)!=8:raise ValueError(f'Truncated PNG: {path}')
            length,kind=struct.unpack('>I4s',head)
            data=f.read(length);crc=f.read(4)
            if len(data)!=length or len(crc)!=4:raise ValueError(f'Truncated chunk: {path}')
            if zlib.crc32(kind+data)&0xffffffff!=struct.unpack('>I',crc)[0]:raise ValueError(f'CRC mismatch: {path}')
            if kind==b'IHDR':size=list(struct.unpack('>II',data[:8]))
            if kind==b'IDAT':data_seen=True
            if kind==b'IEND':break
    if size is None or not data_seen or (expected is not None and size!=list(expected)):
        raise ValueError(f'Invalid PNG dimensions/content: {path}: {size}, expected {expected}')
    return size
