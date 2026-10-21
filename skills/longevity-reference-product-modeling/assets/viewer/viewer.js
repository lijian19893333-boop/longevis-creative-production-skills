const $ = s => document.querySelector(s);
const viewer = $('#viewer');
$('#file').disabled=true; $('#refresh').disabled=true;
let ready = false, selectedFile = null, objectURL = null, homeOrbit = '', homeTarget = '';
const report = message => { $('#status').textContent = message; };
function stopSpin() { viewer.autoRotate = false; $('#spin').textContent = '自动旋转'; }
function disable() {
  ready=false;
  document.querySelectorAll('[data-view],#reset,#spin,#clips,#play,#time').forEach(el=>el.disabled=true);
}
function load() {
  disable(); stopSpin(); viewer.pause();
  if(objectURL) { URL.revokeObjectURL(objectURL); objectURL=null; }
  if(selectedFile) objectURL=URL.createObjectURL(selectedFile);
  viewer.src=objectURL || `model.glb?v=${Date.now()}`;
  report('正在载入模型…');
}
async function chooseClip() {
  viewer.pause(); viewer.animationName=$('#clips').value;
  await viewer.updateComplete;
  viewer.pause(); viewer.currentTime=0;
  $('#play').textContent='播放'; $('#time').value=0; $('#progress').textContent='0%';
}
viewer.addEventListener('load',async()=>{
  ready=true; stopSpin(); viewer.pause();
  viewer.cameraTarget='auto auto auto'; viewer.cameraOrbit='35deg 78deg auto';
  await viewer.updateComplete; viewer.jumpCameraToGoal();
  const orbit=viewer.getCameraOrbit(), target=viewer.getCameraTarget();
  homeOrbit=`35deg 78deg ${orbit.radius}m`; homeTarget=`${target.x}m ${target.y}m ${target.z}m`;
  document.querySelectorAll('[data-view],#reset,#spin').forEach(el=>el.disabled=false);
  const clips=viewer.availableAnimations || [];
  $('#clips').replaceChildren(...(clips.length?clips:['无动画']).map(name=>new Option(name,name)));
  for(const id of ['clips','play','time']) $('#'+id).disabled=!clips.length;
  if(clips.length) await chooseClip();
  report(`已载入 ${selectedFile?.name || 'model.glb'} · ${clips.length ? clips.length+' 个动画' : '模型没有动画'} · 可旋转缩放`);
});
viewer.addEventListener('error',()=>{disable();report('模型加载失败：检查同目录 model.glb，或通过上方按钮选择自带贴图的 GLB。');});
$('#file').addEventListener('change',e=>{if(e.target.files[0]) {selectedFile=e.target.files[0];load();}});
$('#refresh').addEventListener('click',()=>load());
$('#clips').addEventListener('change',chooseClip);
$('#play').addEventListener('click',()=>{if(viewer.paused){viewer.play();$('#play').textContent='暂停';}else{viewer.pause();$('#play').textContent='播放';}});
$('#time').addEventListener('input',()=>{viewer.pause();$('#play').textContent='播放';viewer.currentTime=Math.max(0,viewer.duration-.00001)*Number($('#time').value)/1000;});
$('#reset').addEventListener('click',()=>{stopSpin();viewer.cameraTarget=homeTarget;viewer.cameraOrbit=homeOrbit;});
$('#spin').addEventListener('click',()=>{viewer.autoRotate=!viewer.autoRotate;$('#spin').textContent=viewer.autoRotate?'停止旋转':'自动旋转';});
document.querySelectorAll('[data-view]').forEach(button=>button.addEventListener('click',()=>{stopSpin();const [theta,phi]=button.dataset.view.split(',');viewer.cameraOrbit=`${theta}deg ${phi}deg ${viewer.getCameraOrbit().radius}m`;}));
function progress() {
  if(ready && viewer.duration>0) {const percent=Math.min(100,Math.round(viewer.currentTime/viewer.duration*100));$('#time').value=percent*10;$('#progress').textContent=percent+'%';}
  requestAnimationFrame(progress);
}
if(location.protocol==='file:') {report('请使用随包 serve_viewer.py 启动 HTTP 服务，再打开它打印的链接。');$('#refresh').disabled=true;$('#file').disabled=true;}
else {
  try {await import('./vendor/model-viewer.min.js');await customElements.whenDefined('model-viewer');$('#file').disabled=false;$('#refresh').disabled=false;load();progress();}
  catch(error){disable();$('#refresh').disabled=true;$('#file').disabled=true;report('三维组件未加载，请检查 vendor 文件夹是否完整。');console.error(error);}
}
