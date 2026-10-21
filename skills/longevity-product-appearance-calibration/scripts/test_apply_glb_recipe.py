import importlib.util, json, struct, tempfile, unittest, sys, base64, subprocess
from pathlib import Path

script = Path(__file__).with_name('apply_glb_recipe.py')
spec = importlib.util.spec_from_file_location('recipe_helper', script)
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)

class RecipeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.binary = struct.pack('<9f2f6f', 0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0)
        self.doc = {
            'asset': {'version':'2.0'}, 'scene':0, 'scenes':[{'nodes':[0]}],
            'nodes':[{'name':'Door','mesh':0}], 'buffers':[{'byteLength':len(self.binary)}],
            'bufferViews':[{'buffer':0,'byteOffset':0,'byteLength':36},
                           {'buffer':0,'byteOffset':36,'byteLength':8},
                           {'buffer':0,'byteOffset':44,'byteLength':24}],
            'accessors':[{'bufferView':0,'componentType':5126,'count':3,'type':'VEC3','min':[0,0,0],'max':[1,1,0]},
                         {'bufferView':1,'componentType':5126,'count':2,'type':'SCALAR','min':[0],'max':[1]},
                         {'bufferView':2,'componentType':5126,'count':2,'type':'VEC3'}],
            'meshes':[{'primitives':[{'attributes':{'POSITION':0},'material':0}]}],
            'materials':[{'name':'Coated Panel','pbrMetallicRoughness':{'metallicFactor':0,'roughnessFactor':0.8}}],
            'animations':[{'name':'Door motion','samplers':[{'input':1,'output':2}],
                           'channels':[{'sampler':0,'target':{'node':0,'path':'translation'}}]}]
        }
        self.source = self.root/'source.glb'
        self.source.write_bytes(helper.encode(self.doc,self.binary))
        self.recipe = self.root/'recipe.json'
        self.output = self.root/'output.glb'
    def tearDown(self): self.tmp.cleanup()
    def run_recipe(self, recipe):
        self.recipe.write_text(json.dumps(recipe))
        return helper.apply(self.source,self.recipe,self.output)
    def test_geometry_motion_and_binary_preserved(self):
        png = base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+jY1sAAAAASUVORK5CYII=')
        (self.root/'normal.png').write_bytes(png)
        r = self.run_recipe({'id':'synthetic-r1','textures':{'normal':{'file':'normal.png'}},
             'materials':{'Coated Panel':{'set':{'pbrMetallicRoughness':{'roughnessFactor':0.4},'normalTexture':{'index':'normal','scale':0.2}}}},
             'lights':[{'name':'Demo lamp','type':'point','color':[1,0.1,0.1],'intensity':1,'translation':[0,1,0],'group':'demo','controlMaterial':'Coated Panel'}]})
        after, binary, _ = helper.load(self.output)
        for key in ('meshes','accessors','animations','skins'): self.assertEqual(after.get(key),self.doc.get(key))
        self.assertEqual(after['nodes'][:1],self.doc['nodes'])
        self.assertEqual(binary[:len(self.binary)],self.binary)
        self.assertEqual(binary[after['bufferViews'][3]['byteOffset']:][:len(png)],png)
        self.assertEqual(after['materials'][0]['pbrMetallicRoughness']['roughnessFactor'],0.4)
        self.assertEqual(after['materials'][0]['normalTexture']['index'],0)
        self.assertTrue(r['geometry_and_animation_preserved'])
    def test_unknown_material_refuses_without_writing(self):
        with self.assertRaisesRegex(ValueError,'Unknown material'):
            self.run_recipe({'id':'r1','materials':{'Missing':{'set':{'emissiveFactor':[1,0,0]}}}})
        self.assertFalse(self.output.exists())
    def test_duplicate_material_refuses_without_opt_in(self):
        self.doc['materials'].append(self.doc['materials'][0].copy())
        self.source.write_bytes(helper.encode(self.doc,self.binary))
        with self.assertRaisesRegex(ValueError,'Duplicate material'):
            self.run_recipe({'id':'r1','materials':{'Coated Panel':{'set':{'doubleSided':True}}}})
        self.assertFalse(self.output.exists())
    def test_unresolved_texture_refuses(self):
        with self.assertRaisesRegex(ValueError,'Invalid texture reference'):
            self.run_recipe({'id':'r1','materials':{'Coated Panel':{'set':{'normalTexture':{'index':'missing'}}}}})
        self.assertFalse(self.output.exists())
    def test_source_hash_refuses(self):
        with self.assertRaisesRegex(ValueError,'source hash mismatch'):
            self.run_recipe({'id':'r1','source_sha256':'0'*64})
        self.assertFalse(self.output.exists())
    def test_existing_output_refuses(self):
        self.output.write_bytes(b'keep')
        with self.assertRaisesRegex(ValueError,'Output exists'):self.run_recipe({'id':'r1'})
        self.assertEqual(self.output.read_bytes(),b'keep')
    def test_idempotent_output_and_source_unchanged(self):
        original = self.source.read_bytes()
        self.run_recipe({'id':'r1','source_sha256':helper.digest(original)})
        second = self.root/'second.glb'
        result = helper.apply(self.output,self.recipe,second)
        self.assertTrue(result['already_applied'])
        self.assertEqual(self.output.read_bytes(),second.read_bytes())
        self.assertEqual(self.source.read_bytes(),original)
    def test_external_buffer_refuses_before_writing(self):
        self.doc['buffers'][0]['uri']='external.bin'
        self.source.write_bytes(helper.encode(self.doc,self.binary))
        with self.assertRaisesRegex(ValueError,'embedded buffer'):
            self.run_recipe({'id':'r1'})
        self.assertFalse(self.output.exists())
    def test_report_cannot_overwrite_source(self):
        original = self.source.read_bytes()
        self.recipe.write_text(json.dumps({'id':'r1'}))
        result = subprocess.run([sys.executable,str(script),str(self.source),str(self.recipe),str(self.output),'--report',str(self.source)],capture_output=True,text=True)
        self.assertNotEqual(result.returncode,0)
        self.assertEqual(self.source.read_bytes(),original)
        self.assertFalse(self.output.exists())

if __name__=='__main__': unittest.main()
