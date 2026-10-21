"""Package a complete render manifest into colour-tagged PNG/JPG and contact sheets.
Requires Pillow. Original renders and source models are never rewritten.
"""
import argparse, io, json, math, os, uuid, zipfile
from pathlib import Path
from PIL import Image, ImageCms, ImageDraw, ImageFont, ImageOps
from workflow_io import sha256, atomic_json, safe_id, check_png

def choose_font(given, texts):
    cjk=any('\u3400'<=c<='\u9fff' for t in texts for c in t)
    options=[given] if given else []
    options += ['/System/Library/Fonts/STHeiti Light.ttc','/System/Library/Fonts/PingFang.ttc','C:/Windows/Fonts/msyh.ttc','/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc']
    if not cjk:options += ['/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf','/System/Library/Fonts/Helvetica.ttc','C:/Windows/Fonts/arial.ttf']
    for path in options:
        if path and Path(path).is_file():return path
    raise RuntimeError('No suitable font found; supply --font with a font covering the labels')

def fit_font(path,text,width,size):
    while size>10:
        font=ImageFont.truetype(path,size)
        if font.getlength(text)<=width:return font
        size-=1
    raise ValueError('Label too long for contact sheet; shorten it')

def overview(out,title,variant,records,font_path,icc):
    cols=min(4,len(records));cellw=540;cellh=475;rows=math.ceil(len(records)/cols)
    canvas=Image.new('RGB',(80+cols*cellw,180+rows*cellh),'#f3f0eb');draw=ImageDraw.Draw(canvas)
    heading=title+' / '+records[0]['variant_label']
    draw.text((40,30),heading,font=fit_font(font_path,heading,canvas.width-80,38),fill='#302b26')
    detail=f"{len(records)} views / PNG + JPG / sRGB"
    draw.text((40,95),detail,font=ImageFont.truetype(font_path,22),fill='#82776b')
    for i,r in enumerate(records):
        x=40+(i%cols)*cellw;y=150+(i//cols)*cellh
        with Image.open(out/r['png']) as source:thumb=ImageOps.contain(source,(510,390),Image.Resampling.LANCZOS)
        draw.rectangle((x,y,x+510,y+390),fill='#e7e2db');canvas.paste(thumb,(x+(510-thumb.width)//2,y+(390-thumb.height)//2))
        label=f"{i+1:02d}  {r['label']}";draw.text((x,y+412),label,font=fit_font(font_path,label,510,25),fill='#453d34')
    dest=out/'overview'/f'{variant}.jpg';dest.parent.mkdir(parents=True,exist_ok=True)
    canvas.save(dest,quality=94,subsampling=0,icc_profile=icc,dpi=(300,300))
    return dest

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('manifest',type=Path)
    p.add_argument('--out',type=Path);p.add_argument('--dpi',type=int,default=300);p.add_argument('--font')
    a=p.parse_args();manifest=a.manifest.resolve();base=manifest.parent
    data=json.loads(manifest.read_text(encoding='utf-8'));out=(a.out or base/'delivery').resolve()
    records=data['records']
    if data.get('proof') or not data.get('complete') or len(records)!=data['expected_count'] or not records:
        raise ValueError('Only a complete final manifest can be packaged')
    if not 1<=a.dpi<=2400:raise ValueError('Invalid dpi')
    keys=set();input_paths=[]
    for r in records:
        key=(safe_id(r['variant']),safe_id(r['shot']))
        if key in keys:raise ValueError('Duplicate variant/shot')
        keys.add(key);src=(base/r['image']).resolve()
        if not src.is_relative_to(base) or src.is_relative_to(out):raise ValueError('Image path escapes render folder or overlaps delivery folder')
        if r['status']!='complete' or r['output_color_space']!='sRGB':raise ValueError('Unsupported completion/colour state')
        check_png(src,r['pixels'])
        if sha256(src)!=r['image_sha256']:raise ValueError(f'Render checksum mismatch: {src}')
        with Image.open(src) as im:im.verify()
        input_paths.append(src)
    # Validate every input and font before creating the delivery directory.
    font_path=choose_font(a.font,[data['title'],*[r['label']+r['variant_label'] for r in records]])
    icc=ImageCms.ImageCmsProfile(ImageCms.createProfile('sRGB')).tobytes()
    out.mkdir(parents=True,exist_ok=True);exported=[];files=[]
    for r,src in zip(records,input_paths):
        paths={kind:out/kind.upper()/r['variant']/(r['shot']+'.'+kind) for kind in ['png','jpg']}
        with Image.open(src) as image:im=image.convert('RGB')
        for kind,dest in paths.items():
            dest.parent.mkdir(parents=True,exist_ok=True);tmp=dest.with_name('.'+dest.stem+'.'+uuid.uuid4().hex+'.'+kind)
            try:
                kwargs=dict(icc_profile=icc,dpi=(a.dpi,a.dpi))
                if kind=='png':kwargs['compress_level']=6
                else:kwargs.update(quality=96,subsampling=0)
                im.save(tmp,**kwargs)
                with Image.open(tmp) as test:test.verify()
                tmp.replace(dest)
            finally:tmp.unlink(missing_ok=True)
            files.append(dest)
        e=dict(variant=r['variant'],variant_label=r['variant_label'],shot=r['shot'],label=r['label'],source_version=r.get('source_version',''),pixels=list(im.size),dpi=a.dpi,colour_space='sRGB',print_mm=[round(n/a.dpi*25.4,2) for n in im.size])
        for kind,path in paths.items():e[kind]=str(path.relative_to(out));e[kind+'_sha256']=sha256(path)
        if r.get('reused_from'):e['reused_from']=r['reused_from']
        exported.append(e);print('EXPORTED',r['variant'],r['shot'],flush=True)
    for variant in sorted({r['variant'] for r in exported}):
        files.append(overview(out,data['title'],variant,[r for r in exported if r['variant']==variant],font_path,icc))
    delivery=dict(title=data['title'],view_count=len(exported),format_count=2,images=exported,source_hashes=data.get('source_hashes',{}))
    atomic_json(out/'image-manifest.json',delivery);files.append(out/'image-manifest.json')
    usage=out/'usage.txt';usage.write_text(f"{data['title']}\n{len(exported)} views; each available as lossless PNG and quality-96 JPG.\nsRGB ICC; {a.dpi} dpi metadata. Print size = pixels / dpi × 25.4 mm.\nIndependent images have no added text. Contact sheets are for selection.\nConvert to CMYK using the printer's paper/output profile when required.\nSource models and raw renders were not overwritten.\n",encoding='utf-8');files.append(usage)
    archive=out/'brochure-images.zip';tmp=out/('.archive-'+uuid.uuid4().hex+'.zip')
    try:
        with zipfile.ZipFile(tmp,'w',zipfile.ZIP_DEFLATED,compresslevel=2) as z:
            for f in files:z.write(f,f.relative_to(out))
        with zipfile.ZipFile(tmp) as z:
            if z.testzip() is not None:raise ValueError('ZIP integrity check failed')
        tmp.replace(archive)
    finally:tmp.unlink(missing_ok=True)
    print(json.dumps(dict(views=len(exported),archive=str(archive)),ensure_ascii=False),flush=True)

if __name__=='__main__':main()
