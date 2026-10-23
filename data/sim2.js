const fs=require('fs');
const h=fs.readFileSync('C:/Users/jibra/Desktop/1/KAI/EPISODE.html','utf8');
const blk=h.match(/const SCENES = \[([\s\S]*?)\];/)[1];
const SCENES=[...blk.matchAll(/\{s:\s*([\d.]+),\s*e:\s*([\d.]+)\}/g)].map(m=>({s:+m[1],e:+m[2]}));
const TOTAL=+h.match(/const TOTAL = ([\d.]+);/)[1];
let seen={}, bad=0, changes=[], prev=-1;
for(let f=0; f<TOTAL*60; f++){
  const t=f/60;
  let idx=0;
  for(let i=0;i<SCENES.length;i++){ if(t>=SCENES[i].s) idx=i; }
  if(idx<0||idx>=SCENES.length) bad++;
  if(idx!==prev){ changes.push({t:+t.toFixed(2), idx:idx+1}); prev=idx; }
  seen[idx]=(seen[idx]||0)+1;
}
console.log('bad frames      :', bad);
console.log('scene switches  :', changes.length, '(one per scene, no repeats)');
console.log('switch points   :', changes.map(c=>`S${c.idx}@${c.t}s`).join('  '));
const covered=Object.values(seen).reduce((a,b)=>a+b,0);
console.log('frames covered  :', covered, 'of', Math.round(TOTAL*60), '->', covered===Math.round(TOTAL*60));
console.log('frames per scene:', Object.entries(seen).map(([k,v])=>`S${+k+1}:${v}`).join(' '));
