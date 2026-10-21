const $ = s => document.querySelector(s);
const viewer = $('#viewer');
$('#file').disabled=true; $('#refresh').disabled=true;
let ready = false, selectedFile = null, objectURL = null, homeOrbit = '', homeTarget = '';
const report = message => { $('#status').textContent = message; };
function stopSpin() { viewer.autoRotate = false; $('#spin').textContent = 'Auto-rotate'; }
function disable() {
  ready=false;
  document.querySelectorAll('[data-view],#reset,#spin,#clips,#play,#time').forEach(el=>el.disabled=true);
}
function load() {
  disable(); stopSpin(); viewer.pause();
  if(objectURL) { URL.revokeObjectURL(objectURL); objectURL=null; }
  if(selectedFile) objectURL=URL.createObjectURL(selectedFile);
  viewer.src=objectURL || `model.glb?v=${Date.now()}`;
  report('Loading model…');
}
async function chooseClip() {
  viewer.pause(); viewer.animationName=$('#clips').value;
  await viewer.updateComplete;
  viewer.pause(); viewer.currentTime=0;
  $('#play').textContent='Play'; $('#time').value=0; $('#progress').textContent='0%';
}
viewer.addEventListener('load',async()=>{
  ready=true; stopSpin(); viewer.pause();
  viewer.cameraTarget='auto auto auto'; viewer.cameraOrbit='35deg 78deg auto';
  await viewer.updateComplete; viewer.jumpCameraToGoal();
  const orbit=viewer.getCameraOrbit(), target=viewer.getCameraTarget();
  homeOrbit=`35deg 78deg ${orbit.radius}m`; homeTarget=`${target.x}m ${target.y}m ${target.z}m`;
  document.querySelectorAll('[data-view],#reset,#spin').forEach(el=>el.disabled=false);
  const clips=viewer.availableAnimations || [];
  $('#clips').replaceChildren(...(clips.length?clips:['No animations']).map(name=>new Option(name,name)));
  for(const id of ['clips','play','time']) $('#'+id).disabled=!clips.length;
  if(clips.length) await chooseClip();
  report(`Loaded ${selectedFile?.name || 'model.glb'} · ${clips.length ? clips.length+' animations' : 'No animations in model'} · Rotate and zoom enabled`);
});
viewer.addEventListener('error',()=>{disable();report('Model failed to load: check model.glb in this directory, or choose a local GLB with embedded textures.');});
$('#file').addEventListener('change',e=>{if(e.target.files[0]) {selectedFile=e.target.files[0];load();}});
$('#refresh').addEventListener('click',()=>load());
$('#clips').addEventListener('change',chooseClip);
$('#play').addEventListener('click',()=>{if(viewer.paused){viewer.play();$('#play').textContent='Pause';}else{viewer.pause();$('#play').textContent='Play';}});
$('#time').addEventListener('input',()=>{viewer.pause();$('#play').textContent='Play';viewer.currentTime=Math.max(0,viewer.duration-.00001)*Number($('#time').value)/1000;});
$('#reset').addEventListener('click',()=>{stopSpin();viewer.cameraTarget=homeTarget;viewer.cameraOrbit=homeOrbit;});
$('#spin').addEventListener('click',()=>{viewer.autoRotate=!viewer.autoRotate;$('#spin').textContent=viewer.autoRotate?'Stop rotation':'Auto-rotate';});
document.querySelectorAll('[data-view]').forEach(button=>button.addEventListener('click',()=>{stopSpin();const [theta,phi]=button.dataset.view.split(',');viewer.cameraOrbit=`${theta}deg ${phi}deg ${viewer.getCameraOrbit().radius}m`;}));
function progress() {
  if(ready && viewer.duration>0) {const percent=Math.min(100,Math.round(viewer.currentTime/viewer.duration*100));$('#time').value=percent*10;$('#progress').textContent=percent+'%';}
  requestAnimationFrame(progress);
}
if(location.protocol==='file:') {report('Start an HTTP server with the included serve_viewer.py and open the printed URL.');$('#refresh').disabled=true;$('#file').disabled=true;}
else {
  try {await import('./vendor/model-viewer.min.js');await customElements.whenDefined('model-viewer');$('#file').disabled=false;$('#refresh').disabled=false;load();progress();}
  catch(error){disable();$('#refresh').disabled=true;$('#file').disabled=true;report('3D component failed to load; check that the vendor directory is complete.');console.error(error);}
}
