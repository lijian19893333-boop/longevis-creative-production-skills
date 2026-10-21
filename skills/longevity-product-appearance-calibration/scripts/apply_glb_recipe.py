#!/usr/bin/env python3
"""Apply an explicit appearance recipe while preserving original geometry bytes."""
import argparse,copy,hashlib,json,struct
from pathlib import Path

def digest(data):return hashlib.sha256(data).hexdigest()
def load(path):
 raw=Path(path).read_bytes()
 if len(raw)<20 or raw[:4]!=b'glTF' or struct.unpack_from('<II',raw,4)!=(2,len(raw)):raise ValueError('Invalid GLB 2.0 header')
 chunks=[];offset=12
 while offset<len(raw):
  size,kind=struct.unpack_from('<II',raw,offset);offset+=8
  if offset+size>len(raw):raise ValueError('Truncated chunk')
  chunks.append((kind,raw[offset:offset+size]));offset+=size
 if chunks[0][0]!=0x4e4f534a:raise ValueError('First chunk must be JSON')
 if len(chunks)>2 or (len(chunks)==2 and chunks[1][0]!=0x004e4942):raise ValueError('Unsupported extra chunk; preserve through another pipeline')
 return json.loads(chunks[0][1]),chunks[1][1] if len(chunks)==2 else b'',digest(raw)
def merge(target,patch):
 for k,v in patch.items():
  if isinstance(v,dict):merge(target.setdefault(k,{}),v)
  else:target[k]=copy.deepcopy(v)
def remove_path(obj,path):
 keys=path.split('.')
 for k in keys[:-1]:
  if k not in obj:return
  obj=obj[k]
 obj.pop(keys[-1],None)
def encode(doc,binary):
 j=json.dumps(doc,ensure_ascii=False,separators=(',',':')).encode();j+=b' '*(-len(j)%4)
 b=binary+b'\0'*(-len(binary)%4)
 out=struct.pack('<4sII',b'glTF',2,20+len(j)+(8+len(b) if b else 0))+struct.pack('<II',len(j),0x4e4f534a)+j
 return out+(struct.pack('<II',len(b),0x004e4942)+b if b else b'')
def apply(source,recipe_path,output,overwrite=False):
 source=Path(source);output=Path(output);recipe_path=Path(recipe_path)
 if output.exists() and not overwrite:raise ValueError('Output exists; supply --overwrite only for an authorized replacement')
 doc,binary,source_hash=load(source);before=copy.deepcopy(doc);original_binary=binary
 buffers=doc.get('buffers',[])
 if len(buffers)>1 or any('uri' in buffer for buffer in buffers):raise ValueError('Only a single embedded buffer is supported; resolve external buffers through another pipeline')
 recipe=json.loads(recipe_path.read_text());rid=recipe['id']
 if doc.get('asset',{}).get('extras',{}).get('appearanceRecipe')==rid:
  if recipe.get('source_sha256') and recipe['source_sha256']!=doc['asset']['extras'].get('appearanceSourceSHA256'):raise ValueError('Applied recipe origin hash mismatch')
  output.parent.mkdir(parents=True,exist_ok=True);output.write_bytes(source.read_bytes());return {'id':rid,'already_applied':True,'source_sha256':source_hash,'output_sha256':source_hash}
 if recipe.get('source_sha256') and recipe['source_sha256']!=source_hash:raise ValueError('Recipe source hash mismatch')
 names={}
 for i,m in enumerate(doc.get('materials',[])):names.setdefault(m.get('name'),[]).append(i)
 missing=set(recipe.get('materials',{}))-set(names)
 if missing:raise ValueError('Unknown material names: '+', '.join(sorted(missing)))
 duplicates={n:names[n] for n in recipe.get('materials',{}) if len(names[n])>1}
 if duplicates and not recipe.get('match_all_material_names'):raise ValueError('Duplicate material names; explicitly set match_all_material_names to modify all matches: '+str(duplicates))
 texture_ids={}
 for name,spec in recipe.get('textures',{}).items():
  path=(recipe_path.parent/spec['file']).resolve();payload=path.read_bytes();binary+=b'\0'*(-len(binary)%4);offset=len(binary);binary+=payload
  views=doc.setdefault('bufferViews',[]);vi=len(views);views.append({'buffer':0,'byteOffset':offset,'byteLength':len(payload)})
  images=doc.setdefault('images',[]);ii=len(images);images.append({'name':name,'mimeType':spec.get('mimeType','image/png'),'bufferView':vi})
  samplers=doc.setdefault('samplers',[]);si=len(samplers);samplers.append(spec.get('sampler',{'magFilter':9729,'minFilter':9987,'wrapS':10497,'wrapT':10497}))
  textures=doc.setdefault('textures',[]);texture_ids[name]=len(textures);textures.append({'name':name,'source':ii,'sampler':si})
 def resolve(value):
  if isinstance(value,dict):return {k:(texture_ids[v] if k=='index' and isinstance(v,str) and v in texture_ids else resolve(v)) for k,v in value.items()}
  if isinstance(value,list):return [resolve(v) for v in value]
  return value
 for name,patch in recipe.get('materials',{}).items():
  if 'roughnessTexture' in patch.get('set',{}).get('pbrMetallicRoughness',{}):raise ValueError('Use metallicRoughnessTexture with roughness in G, not roughnessTexture')
  for index in names[name]:
   mat=doc['materials'][index]
   for path in patch.get('remove',[]):remove_path(mat,path)
   merge(mat,resolve(patch.get('set',{})))
 def validate_textures(value):
  if isinstance(value,dict):
   for key,item in value.items():
    if key.endswith('Texture') and isinstance(item,dict) and 'index' in item:
     index=item['index']
     if not isinstance(index,int) or isinstance(index,bool) or not 0<=index<len(doc.get('textures',[])):raise ValueError('Invalid texture reference: '+str(item))
    validate_textures(item)
  elif isinstance(value,list):
   for item in value:validate_textures(item)
 validate_textures(doc.get('materials',[]))
 used=set(doc.get('extensionsUsed',[]))
 for mat in doc.get('materials',[]):used.update(mat.get('extensions',{}))
 lights=recipe.get('lights',[])
 if lights:
  used.add('KHR_lights_punctual');store=doc.setdefault('extensions',{}).setdefault('KHR_lights_punctual',{}).setdefault('lights',[])
  nodes=doc.setdefault('nodes',[]);scene=doc.setdefault('scenes',[{'nodes':[]}])[doc.get('scene',0)]
  for light in lights:
   li=len(store);entry={k:copy.deepcopy(v) for k,v in light.items() if k not in ['translation','rotation','group','controlMaterial']};store.append(entry)
   node={'name':light['name'],'translation':light.get('translation',[0,0,0]),'extensions':{'KHR_lights_punctual':{'light':li}},'extras':{'appearanceLightGroup':light.get('group','interior'),'controlMaterial':light.get('controlMaterial'),'appearanceRecipe':rid}}
   if 'rotation' in light:node['rotation']=light['rotation']
   scene.setdefault('nodes',[]).append(len(nodes));nodes.append(node)
 doc['extensionsUsed']=sorted(used)
 doc.setdefault('asset',{}).setdefault('extras',{}).update(appearanceRecipe=rid,appearanceSourceSHA256=source_hash,appearanceNote=recipe.get('note','Material and lighting calibration; geometry unchanged'))
 if doc.get('scenes'):doc['scenes'][doc.get('scene',0)].setdefault('extras',{})['appearanceRecipe']=rid
 if binary:doc.setdefault('buffers',[{}])[0]['byteLength']=len(binary)
 # Guard both numeric geometry/animation declarations and their exact bytes.
 for key in ['meshes','accessors','animations','skins']:
  if doc.get(key)!=before.get(key):raise AssertionError('Geometry or motion changed: '+key)
 if doc.get('nodes',[])[:len(before.get('nodes',[]))]!=before.get('nodes',[]):raise AssertionError('Original node hierarchy changed')
 if binary[:len(original_binary)]!=original_binary:raise AssertionError('Original geometry/image binary changed')
 raw=encode(doc,binary);output.parent.mkdir(parents=True,exist_ok=True);output.write_bytes(raw)
 return {'id':rid,'source_sha256':source_hash,'output_sha256':digest(raw),'source_bytes':source.stat().st_size,'output_bytes':len(raw),'changed_materials':list(recipe.get('materials',{})),'changed_material_indices':{n:names[n] for n in recipe.get('materials',{})},'added_textures':list(texture_ids),'added_lights':len(lights),'original_binary_preserved':True,'geometry_and_animation_preserved':True}
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('source',type=Path);ap.add_argument('recipe',type=Path);ap.add_argument('output',type=Path);ap.add_argument('--report',type=Path);ap.add_argument('--overwrite',action='store_true');a=ap.parse_args()
 if a.report and a.report.resolve() in {p.resolve() for p in [a.source,a.recipe,a.output]}:ap.error('Report path must differ from source, recipe and output')
 result=apply(a.source,a.recipe,a.output,a.overwrite)
 if a.report:a.report.parent.mkdir(parents=True,exist_ok=True);a.report.write_text(json.dumps(result,ensure_ascii=False,indent=2))
 print(json.dumps(result,ensure_ascii=False))
if __name__=='__main__':main()
