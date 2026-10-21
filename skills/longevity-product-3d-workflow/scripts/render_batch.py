"""Blender 4.2+/5.x: render configured cameras without saving source models.
Example: blender --background --factory-startup --python render_batch.py -- job.json --proof
"""
import argparse, hashlib, importlib.util, json, math, os, sys, time, uuid
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from workflow_io import sha256, atomic_json, safe_id, check_png
import bpy
from mathutils import Vector

def resolve(base,path):return (base/Path(path)).resolve()

def select_device(request):
    pref=bpy.context.preferences.addons['cycles'].preferences
    if request=='CPU':return 'CPU'
    choices=(['METAL'] if sys.platform=='darwin' else ['OPTIX','CUDA','HIP','ONEAPI']) if request=='AUTO' else [request]
    for kind in choices:
        try:
            pref.compute_device_type=kind;pref.get_devices()
            devices=[d for d in pref.devices if d.type==kind]
            if devices:
                for d in pref.devices:d.use=d in devices
                return kind
        except (TypeError,RuntimeError):continue
    if request!='AUTO':raise RuntimeError(f'No usable {request} device; select AUTO or CPU')
    return 'CPU'

def dimensions(job,shot,proof):
    w,h=shot.get('size',job.get('size',[3600,2700]))
    if min(w,h)<1 or max(w,h)>32000:raise ValueError('Invalid image dimensions')
    scale=min(1,job.get('proof_long_edge',900)/max(w,h)) if proof else 1
    return [max(1,round(w*scale)),max(1,round(h*scale))]

def setup_render(job,shot,proof,device):
    scene=bpy.context.scene;settings=job.get('render',{})
    scene.render.engine='CYCLES';scene.cycles.device='CPU' if device=='CPU' else 'GPU'
    scene.cycles.samples=settings.get('proof_samples',24) if proof else shot.get('samples',settings.get('samples',64))
    scene.cycles.use_denoising=True;scene.cycles.use_adaptive_sampling=True
    scene.cycles.adaptive_threshold=.055 if proof else settings.get('adaptive_threshold',.03)
    scene.cycles.max_bounces=settings.get('max_bounces',8)
    scene.cycles.transmission_bounces=settings.get('transmission_bounces',6)
    scene.cycles.time_limit=settings.get('time_limit_seconds',0)
    scene.render.threads_mode='FIXED';scene.render.threads=settings.get('threads',min(8,os.cpu_count() or 1))
    scene.render.use_persistent_data=True
    scene.display_settings.display_device='sRGB';scene.view_settings.view_transform=settings.get('view_transform','AgX')
    scene.view_settings.look=settings.get('look','AgX - Medium High Contrast')
    scene.view_settings.exposure=shot.get('exposure',settings.get('exposure',0))
    scene.render.resolution_x,scene.render.resolution_y=dimensions(job,shot,proof)
    scene.render.resolution_percentage=100;scene.render.film_transparent=False
    scene.render.image_settings.file_format='PNG';scene.render.image_settings.color_mode='RGB'
    scene.render.image_settings.color_depth='8';scene.render.image_settings.compression=40
    c=shot['camera'];data=bpy.data.cameras.new('Workflow render camera')
    camera=bpy.data.objects.new(data.name,data);scene.collection.objects.link(camera)
    camera.location=c['location'];direction=Vector(c['target'])-camera.location
    if direction.length<1e-6:raise ValueError('Camera location and target coincide')
    camera.rotation_euler=direction.to_track_quat('-Z','Y').to_euler()
    if 'ortho_scale' in c:data.type='ORTHO';data.ortho_scale=c['ortho_scale']
    else:data.type='PERSP';data.lens=c.get('lens',55);data.sensor_width=36;data.sensor_fit='HORIZONTAL'
    data.clip_start=c.get('clip_start',.01);data.clip_end=c.get('clip_end',1000);scene.camera=camera
    scene.frame_set(shot.get('frame',1))
    return scene

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('job',type=Path)
    p.add_argument('--proof',action='store_true');p.add_argument('--resume',action='store_true')
    p.add_argument('--variants');p.add_argument('--shots');p.add_argument('--device',default='AUTO',choices=['AUTO','CPU','METAL','OPTIX','CUDA','HIP','ONEAPI'])
    a=p.parse_args(sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else [])
    config=a.job.resolve();base=config.parent;job=json.loads(config.read_text(encoding='utf-8'))
    out=resolve(base,job['output']);mode='proof' if a.proof else 'final'
    variants=job['variants'];shots=job['shots']
    for group in [variants,shots]:
        ids=[safe_id(v['id']) for v in group]
        if not ids or len(ids)!=len(set(ids)):raise ValueError('Variant/shot identifiers must be nonempty and unique')
    selected_v=set(a.variants.split(',')) if a.variants else {v['id'] for v in variants}
    selected_s=set(a.shots.split(',')) if a.shots else {s['id'] for s in shots}
    if not selected_v<={v['id'] for v in variants} or not selected_s<={s['id'] for s in shots}:raise ValueError('Unknown selected identifier')
    recipe_path=resolve(base,job['recipe']) if job.get('recipe') else None
    inputs={}
    for v in variants:
        for rel in [v['source'],*v.get('dependencies',[])]:
            path=resolve(base,rel)
            if not path.is_file():raise FileNotFoundError(path)
            inputs[str(path)]=sha256(path)
    for rel in job.get('dependencies',[]):
        path=resolve(base,rel);inputs[str(path)]=sha256(path)
    if recipe_path:inputs[str(recipe_path)]=sha256(recipe_path)
    script_hash=sha256(__file__);helper_hash=sha256(Path(__file__).with_name('workflow_io.py'))
    recipe=None
    if recipe_path:
        spec=importlib.util.spec_from_file_location('product_render_recipe',recipe_path)
        recipe=importlib.util.module_from_spec(spec);spec.loader.exec_module(recipe)
    def fingerprint(v,s):
        relevant=[resolve(base,x) for x in [v['source'],*v.get('dependencies',[]),*job.get('dependencies',[])]]
        if recipe_path:relevant.append(recipe_path)
        global_settings={k:value for k,value in job.items() if k not in ['variants','shots','output','title']}
        payload=dict(settings=global_settings,variant=v,shot=s,proof=a.proof,inputs={str(x):inputs[str(x)] for x in relevant},runner=script_hash,helper=helper_hash,blender=bpy.app.version_string)
        return hashlib.sha256(json.dumps(payload,sort_keys=True).encode()).hexdigest()
    def record_path(v,s):return out/'.records'/mode/v['id']/(s['id']+'.json')
    def valid_record(v,s):
        path=record_path(v,s)
        try:
            r=json.loads(path.read_text());image_path=(out/r['image']).resolve()
            if not image_path.is_relative_to(out) or r['fingerprint']!=fingerprint(v,s) or r['status']!='complete':return None
            check_png(image_path,dimensions(job,s,a.proof))
            return r if sha256(image_path)==r['image_sha256'] else None
        except (OSError,ValueError,KeyError):return None
    def verify_inputs():
        for path,h in inputs.items():
            if sha256(path)!=h:raise RuntimeError(f'Source/dependency changed during render: {path}')
    def write_manifest():
        records=[];expected=0
        for v in variants:
            for s in shots:
                if s.get('variants') and v['id'] not in s['variants']:continue
                expected+=1;r=valid_record(v,s)
                if r:records.append(r)
        atomic_json(out/f'manifest-{mode}.json',dict(schema_version=1,title=job.get('title','Product renders'),proof=a.proof,complete=len(records)==expected,expected_count=expected,source_hashes=inputs,records=records))
    device=select_device(a.device);print('DEVICE',device,flush=True)
    out.mkdir(parents=True,exist_ok=True)
    try:
        for v in variants:
            for s in shots:
                if v['id'] not in selected_v or s['id'] not in selected_s or (s.get('variants') and v['id'] not in s['variants']):continue
                if a.resume and valid_record(v,s):print('RESUME_SKIP',v['id'],s['id'],flush=True);continue
                verify_inputs();bpy.ops.wm.open_mainfile(filepath=str(resolve(base,v['source'])))
                scene=setup_render(job,s,a.proof,device)
                if recipe:recipe.configure(scene,job,v,s)
                # The recipe may configure lighting/materials, but output colour is explicit.
                scene.display_settings.display_device='sRGB'
                folder=out/('proofs' if a.proof else 'raw')/v['id'];folder.mkdir(parents=True,exist_ok=True)
                dest=folder/(s['id']+'.png');tmp=folder/('.'+s['id']+'.'+uuid.uuid4().hex+'.partial.png')
                state={'complete':False,'cancelled':False}
                def completed(*_):state['complete']=True
                def cancelled(*_):state['cancelled']=True
                bpy.app.handlers.render_complete.append(completed);bpy.app.handlers.render_cancel.append(cancelled)
                print('SHOT_START',v['id'],s['id'],flush=True);start=time.time()
                try:
                    scene.render.filepath=str(tmp);result=bpy.ops.render.render(write_still=True)
                    if 'FINISHED' not in result or not state['complete'] or state['cancelled']:raise RuntimeError('Render cancelled; no completion record written')
                    check_png(tmp,dimensions(job,s,a.proof));verify_inputs();tmp.replace(dest)
                    record=dict(status='complete',variant=v['id'],variant_label=v.get('label',v['id']),source_version=v.get('version',''),shot=s['id'],label=s.get('label',s['id']),image=str(dest.relative_to(out)),image_sha256=sha256(dest),pixels=dimensions(job,s,a.proof),output_color_space='sRGB',fingerprint=fingerprint(v,s),camera=s['camera'],seconds=round(time.time()-start,2),device=device,samples=scene.cycles.samples)
                    atomic_json(record_path(v,s),record);print('SHOT_DONE',v['id'],s['id'],record['seconds'],flush=True)
                finally:
                    bpy.app.handlers.render_complete.remove(completed);bpy.app.handlers.render_cancel.remove(cancelled)
                    tmp.unlink(missing_ok=True)
                write_manifest()
    finally:
        verify_inputs();write_manifest()
    print('MANIFEST',out/f'manifest-{mode}.json',flush=True)

if __name__=='__main__':main()
