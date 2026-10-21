"""Optional warm studio recipe. Copy beside the job JSON and adapt selectors.
All changes are transient. Camera coordinates remain in the model's metre units.
"""
import bpy, math
from mathutils import Vector

def hide_selectors(selectors):
    names=selectors.get('names',[]);prefixes=tuple(selectors.get('prefixes',[]))
    for o in bpy.data.objects:
        if o.name in names or (prefixes and o.name.startswith(prefixes)) or any(t in o.name for t in selectors.get('contains',[])):o.hide_render=True
    for name in names:
        if name not in bpy.data.objects:raise ValueError(f'Unknown object in hide.names: {name}')
    for name in selectors.get('collections',[]):
        if name not in bpy.data.collections:raise ValueError(f'Unknown collection: {name}')
        for o in bpy.data.collections[name].all_objects:o.hide_render=True

def area(name,loc,target,energy,size,color,scale=1,glossy=False):
    d=bpy.data.lights.new(name,'AREA');d.energy=energy*scale*scale;d.color=color
    d.shape='DISK';d.size=size*scale
    o=bpy.data.objects.new(name,d);bpy.context.scene.collection.objects.link(o)
    o.location=Vector(loc)*scale;o.rotation_euler=(Vector(target)*scale-o.location).to_track_quat('-Z','Y').to_euler()
    o.visible_glossy=glossy;o.visible_transmission=False
    return o

def configure(scene,job,variant,shot):
    cfg=job.get('studio',{});scale=cfg.get('scale',1)
    hide_selectors(job.get('hide',{}));hide_selectors(variant.get('hide',{}));hide_selectors(shot.get('hide',{}))
    for name,values in job.get('material_overrides',{}).items():
        mat=bpy.data.materials.get(name)
        if mat is None or not mat.use_nodes:raise ValueError(f'Unknown node material: {name}')
        shader=next((n for n in mat.node_tree.nodes if n.type=='BSDF_PRINCIPLED'),None)
        if shader is None:raise ValueError(f'No Principled shader in {name}')
        for key,value in values.items():shader.inputs[key].default_value=value
    for name,angles in shot.get('object_rotations_degrees',{}).items():
        obj=bpy.data.objects.get(name)
        if obj is None:raise ValueError(f'Unknown animated object: {name}')
        obj.rotation_mode='XYZ';obj.rotation_euler=[math.radians(a) for a in angles]
    if cfg.get('enabled',True):
        mat=bpy.data.materials.new('Workflow | warm grey sweep');mat.use_nodes=True
        p=mat.node_tree.nodes.get('Principled BSDF');color=cfg.get('background_linear_rgb',[.40,.385,.365])
        p.inputs['Base Color'].default_value=(*color,1);p.inputs['Roughness'].default_value=.83
        p.inputs['Emission Color'].default_value=(*color,1);p.inputs['Emission Strength'].default_value=.1
        z=cfg.get('floor_z',-.011);profile=[(-25*scale,z),(2.8*scale,z)]
        for i in range(1,65):
            t=math.pi*.5*i/64;profile.append(((2.8+3*math.sin(t))*scale,z+3*(1-math.cos(t))*scale))
        profile.append((5.8*scale,12*scale));n=len(profile)
        mesh=bpy.data.meshes.new('Workflow sweep');mesh.from_pydata([(x,y,z) for x in [-25*scale,25*scale] for y,z in profile],[],[(i,n+i,n+i+1,i+1) for i in range(n-1)])
        obj=bpy.data.objects.new('Workflow | sweep',mesh);scene.collection.objects.link(obj);mesh.materials.append(mat)
        for face in mesh.polygons:face.use_smooth=True
        interior=shot.get('interior',False);gain=.045 if interior else 1
        area('Workflow | key',(-3.8,-4.6,5.7),(0,0,1),1200*gain,4.8,(1,.965,.92),scale,True)
        area('Workflow | fill',(4.7,-3.4,3.8),(0,0,1),820*gain,4.2,(.94,.97,1),scale)
        area('Workflow | rim',(-1.3,2.2,5.1),(0,0,1),1400*gain,3.8,(1,.96,.89),scale)
        area('Workflow | backdrop',(0,1,6),(0,5.8,2.8),400*gain,7,(1,.98,.95),scale)
        if interior:area('Workflow | cabin fill',(-.2,-1.25,1.65),(0,.55,.8),16,1.6,(1,.93,.87),scale)
        if scene.world is None:scene.world=bpy.data.worlds.new('Workflow world')
        scene.world.use_nodes=True
        background=next((n for n in scene.world.node_tree.nodes if n.type=='BACKGROUND'),None)
        if background is None:raise ValueError('Adapt recipe to the source world node graph')
        background.inputs['Color'].default_value=(.76,.745,.715,1)
        background.inputs['Strength'].default_value=.05 if interior else .48
    scene.view_settings.exposure=shot.get('exposure',job.get('render',{}).get('exposure',0))
