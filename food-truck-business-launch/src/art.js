/* Original inline SVG illustrations; mathematical values are supplied by code. */
const FTArt=(()=>{
const wrap=(body,label,view='0 0 720 420')=>`<svg xmlns="http://www.w3.org/2000/svg" viewBox="${view}" role="img" aria-label="${label}">${body}</svg>`;
const bowl=()=>`<path d="M35 86Q100 147 165 86" fill="#bd3d2e"/><ellipse cx="100" cy="85" rx="65" ry="18" fill="#f9edd1"/><path d="M48 82l15-22 14 19 20-25 22 25 22-18 12 20" fill="none" stroke="#789277" stroke-width="10"/><path d="M110 32l65 74M126 26l62 76" stroke="#c5a56d" stroke-width="5"/>`;
const wrapFood=()=>`<path d="M55 40L155 80 110 137 44 77Z" fill="#e3b75e"/><path d="M55 40Q102 30 155 80L142 93Q94 48 47 60Z" fill="#7e9369"/><path d="M66 48l30 1 22 17 22 5" fill="none" stroke="#c74b36" stroke-width="12"/><path d="M59 88l59 20-9 27-39-17Z" fill="#fff8e8"/>`;
const noodles=()=>`<path d="M40 81H162L145 126H59Z" fill="#efc260"/><ellipse cx="100" cy="80" rx="60" ry="16" fill="#fff5d4"/><path d="M57 75q22-25 35 0t32 0t28-2M57 83q22-25 35 0t32 0t28-2" fill="none" stroke="#d8a551" stroke-width="6"/><path d="M120 20l51 63M134 16l54 62" stroke="#4a4439" stroke-width="4"/><path d="M71 57l5-11m21 13 3-15" stroke="#688264" stroke-width="6"/>`;
function menu(c='bowl'){return wrap(({bowl,wrap:wrapFood,noodle:noodles})[c](),'Menu illustration: '+({bowl:'rice bowl',wrap:'wrap',noodle:'noodles'})[c],'0 0 200 155')}
function concept(kind){const shapes={ingredients:`<path d="M35 90h130l-20 42H55Z" fill="#b9905a"/><circle cx="72" cy="72" r="24" fill="#799775"/><circle cx="109" cy="81" r="21" fill="#c74b36"/><path d="M137 36l16 60-26-5Z" fill="#e6b95d"/><path d="M58 55l7-20 9 20" fill="#416752"/>`,sauce:`<path d="M64 37h61l10 98H55Z" fill="#bb3f31"/><rect x="69" y="25" width="51" height="22" rx="5" fill="#484738"/><rect x="62" y="71" width="66" height="37" rx="6" fill="#fff1d1"/><path d="M77 89h34" stroke="#ba3e31" stroke-width="5"/>`,packaging:`<path d="M40 66l59-28 60 30-59 30Z" fill="#f2dbac"/><path d="M40 66v52l60 26V98Z" fill="#caaa78"/><path d="M100 98l59-30v52l-59 24Z" fill="#b88c55"/>`,tray:`<rect x="21" y="38" width="156" height="98" rx="17" fill="#b6b9a4"/><rect x="32" y="49" width="66" height="75" rx="10" fill="#eae2c9"/><rect x="106" y="49" width="60" height="34" rx="8" fill="#789477"/><rect x="106" y="91" width="60" height="33" rx="8" fill="#d17b4a"/>`,capacity:`<path d="M54 37h94v107H54Z" fill="#edbd55"/><path d="M68 60h65M68 80h65M68 100h35" stroke="#3f493f" stroke-width="7"/><circle cx="51" cy="52" r="28" fill="#f8f2e4" stroke="#3f493f" stroke-width="5"/><path d="M51 33v20l14 7" fill="none" stroke="#3f493f" stroke-width="5"/>`};return wrap(shapes[kind]||shapes.tray,'Illustration: '+kind,'0 0 200 165')}
function scene(c='bowl',ending='welcome'){const color=ending==='rethink'?'#9c6557':ending==='viable'?'#c79639':'#bd4434';return wrap(`
<rect width="720" height="420" rx="28" fill="#e9e3ce"/><circle cx="590" cy="70" r="40" fill="#e8b64e"/>
<path d="M0 170L0 86 95 116 140 75 208 125 275 94V206H0M516 195V109l91 24 42-32 71 54v61" fill="#c0c9ac"/>
<path d="M0 46Q345 140 720 35" fill="none" stroke="#68725c" stroke-width="3"/>
${[35,100,165,230,295,360,425,490,555,620,685].map((x,i)=>`<path d="M${x} ${60+Math.sin(x/720*Math.PI)*35}l24 3-15 25Z" fill="${i%2?'#c14c3b':'#e0ae4b'}"/>`).join('')}
<path d="M0 350h720v70H0Z" fill="#c9bfa2"/><path d="M80 375h555" stroke="#a79f84" stroke-width="9" stroke-linecap="round"/>
<path d="M100 165q0-20 20-20h366q20 0 27 20l53 102v83H100Z" fill="${color}"/>
<rect x="117" y="168" width="288" height="124" rx="5" fill="#fff0ce"/><rect x="138" y="187" width="244" height="88" rx="3" fill="#344c43"/>
<path d="M419 169h62l47 91H419Z" fill="#bcd3c5"/><path d="M103 160h304l-17 42H119Z" fill="#f2c45b"/>
${[128,188,248,308,368].map(x=>`<path d="M${x} 160h25v41h-25Z" fill="#fff4d8"/>`).join('')}
<rect x="104" y="311" width="441" height="18" fill="#f4c35e"/><rect x="396" y="268" width="56" height="66" fill="${color}" stroke="#9b382d" stroke-width="3"/>
<circle cx="177" cy="345" r="39" fill="#303e38"/><circle cx="177" cy="345" r="18" fill="#f4ebd2"/><circle cx="485" cy="345" r="39" fill="#303e38"/><circle cx="485" cy="345" r="18" fill="#f4ebd2"/>
<g transform="translate(188,185) scale(.75)">${({bowl,wrap:wrapFood,noodle:noodles})[c]()}</g>
<rect x="581" y="275" width="66" height="76" rx="4" fill="#365448"/><path d="M573 357l13-90h59l12 90" fill="none" stroke="#9a7551" stroke-width="7"/>
${ending==='success'?'<path d="M564 223l12-13 14 7 8-14m-12-22 7-16m30 57 21-6" fill="none" stroke="#bd4434" stroke-width="6"/>':ending==='rethink'?'<rect x="595" y="295" width="39" height="30" fill="#eedcbc"/><path d="M600 302h25m-25 9h19" stroke="#9e6658" stroke-width="3"/>':'<path d="M596 303h36m-36 12h29" stroke="#eedcbc" stroke-width="4"/>'}
`,'Illustrated festival food truck — '+ending)}
return {menu,concept,scene};
})();
