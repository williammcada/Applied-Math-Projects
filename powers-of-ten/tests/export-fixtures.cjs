/* Reproducible synthetic saved sessions; never classroom observations. */
const C=require('../src/core.js'),{filled}=require('./fixtures.cjs'),fs=require('fs'),path=require('path');const cases=[];
function add(name,t,mutate=()=>{}){const s=filled(C,t);s.teamAlias='Synthetic: '+name;mutate(s);C.parseImport(JSON.stringify(s));cases.push(s)}
add('Featured cell','A');add('Featured cosmic','B');
add('Pending physical review','A',s=>s.reviews=s.reviews.filter(r=>r.type!=='inspection'));
add('Pending interpretation','B',s=>s.reviews=s.reviews.filter(r=>r.type!=='interpretation'));
for(const t of ['A','B'])add('Outside tolerance '+t,t,s=>{const k=t==='A'?'cell':'centers';C.setInput(s,'C09'+t+'.'+k,t==='A'?'163':'610');C.setInput(s,'C09'+t+'.'+k+'Deviation',t==='A'?'3':'10');C.check(s,'C09'+t)});
add('Missing source label','A',s=>C.setInput(s,'placardA.source',''));
add('Incorrect property label','B',s=>C.setInput(s,'placardB.property','diameter'));
add('Stale upstream plan','A',s=>C.setInput(s,'C08A.model','0.17'));
add('Active bypass','B',s=>C.bypass(s,'C04a','Fixture','Synthetic inaccessible checkpoint case'));
add('Pending paper transfer','A',s=>{C.setInput(s,'C121.mode','paper');C.setInput(s,'C121.submission','Synthetic receipt, not a learner response');C.check(s,'C121')});
add('Wrong tiny answer','A',s=>{C.setInput(s,'C01a.a','0');C.check(s,'C01a')});
const target=path.join(__dirname,'saved-fixtures');fs.mkdirSync(target,{recursive:true});
for(const s of cases){const name=s.teamAlias.replace('Synthetic: ','').toLowerCase().replaceAll(' ','-');fs.writeFileSync(path.join(target,name+'.json'),JSON.stringify(s,null,2)+'\n')}
fs.writeFileSync(path.join(target,'malformed-import.json'),'{broken');
fs.writeFileSync(path.join(target,'README.md'),'# Synthetic saved fixtures\n\nThese 12 valid sessions and one intentionally malformed file are test evidence, not student observations. Generate with `node powers-of-ten/tests/export-fixtures.cjs`. Import through Sessions as copies. Alias states describe the expected scenario; test reviewer notes explicitly identify synthetic evidence.\n\n'+cases.map(s=>'- '+s.teamAlias+': **'+C.outcome(s)+'**').join('\n')+'\n');
console.log('Saved '+cases.length+' valid synthetic cases and one malformed-import case.');
