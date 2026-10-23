const fs=require('fs');
const h=fs.readFileSync('C:/Users/jibra/Desktop/1/KAI/EPISODE.html','utf8');
const blk=h.match(/const SCENES = \[([\s\S]*?)\];/)[1];
const SCENES=[...blk.matchAll(/\{s:\s*([\d.]+),\s*e:\s*([\d.]+)\}/g)].map(m=>({s:+m[1],e:+m[2]}));
const TOTAL=+h.match(/const TOTAL = ([\d.]+);/)[1];
console.log('scenes:',SCENES.map(s=>`${s.s}-${s.e}`).join('  '));

let bad=[], gapTotal=0;
for(let f=0; f<TOTAL*60; f++){
  const t=f/60;
  let idx=SCENES.findIndex(s=>t>=s.s && t<s.e);
  if(idx<0){ bad.push(t); }
}
// group the bad frames into runs
let runs=[],cur=null;
for(const t of bad){
  if(cur && t-cur.end<0.05){ cur.end=t; } else { if(cur) runs.push(cur); cur={start:t,end:t}; }
}
if(cur) runs.push(cur);
console.log(`\nBAD FRAMES (no scene matched): ${bad.length} of ${Math.round(TOTAL*60)}  (${(bad.length/(TOTAL*60)*100).toFixed(1)}%)`);
console.log('these are the gaps between scenes:');
for(const r of runs) console.log(`   ${r.start.toFixed(2)}s -> ${r.end.toFixed(2)}s  (${((r.end-r.start)*1000).toFixed(0)} ms)`);
console.log('\nWith the old fallback `idx = ...? last : 0`, every gap above snapped to SCENE 1 -> flash of the hook.');
