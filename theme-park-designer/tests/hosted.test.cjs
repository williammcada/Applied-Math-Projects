const {chromium}=require('playwright');
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const root=path.resolve(__dirname,'..'),out=path.join(root,'docs/verification');
const url='https://williammcada.github.io/Applied-Math-Projects/theme-park-designer/';
const expected='c3e9dbe937919751c99925a82be16fe2d45c1797d40e4b13ea8e0e03ce4ed6d9';
const checks=[],ok=(value,label)=>{assert.ok(value,label);checks.push({label,passed:true})};
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const proxyUrl=process.env.HTTPS_PROXY||process.env.HTTP_PROXY;let proxy;
if(proxyUrl){const u=new URL(proxyUrl);proxy={server:u.protocol+'//'+u.host};if(u.username)proxy.username=decodeURIComponent(u.username);if(u.password)proxy.password=decodeURIComponent(u.password);}
(async()=>{const browser=await chromium.launch({executablePath:process.env.CHROMIUM_PATH,proxy,args:['--no-sandbox','--disable-dev-shm-usage','--disable-gpu'],headless:true});
try{
 const ctx=await browser.newContext({acceptDownloads:true,ignoreHTTPSErrors:process.env.QA_PROXY_TLS_EXCEPTION==='1',viewport:{width:1440,height:1000}}),p=await ctx.newPage(),exceptions=[],assets=[];
 p.on('pageerror',e=>exceptions.push(e.message));p.on('request',r=>{if(r.resourceType()!=='document')assets.push(r.url())});
 const response=await p.goto(url+'?release=d7f5bba79c0dd104bf80d0ab78ee0a158a31bd02');
 ok(response.status()===200,'public application HTTP 200');ok(sha(await response.body())===expected,'hosted index exactly matches verified HTML');
 const versioned=await ctx.request.get(url+'ThemeParkDesigner_v0.1.0.html');
 ok(versioned.status()===200&&sha(await versioned.body())===expected,'versioned hosted download matches exact candidate');
 ok(/v0\.1\.0/i.test(await p.locator('.brand').innerText()),'visible version 0.1.0');ok(await p.locator('.hero-grid svg').count()>0,'embedded title illustration renders');
 await p.locator('[data-action="new"]').click();await p.locator('#teamAlias').fill('Hosted QA');await p.locator('#parkName').fill('Deployment Test');await p.locator('[data-meta="brief"]').check();await p.locator('[data-action="next"]').click();await p.locator('[data-field="drawW"]').fill('15');await p.locator('[data-action="save"]').click();
 ok((await p.locator('#save-status').innerText()).includes('Saved on this device'),'hosted edits saved');
 let event=p.waitForEvent('download');await p.locator('[data-action="export"]').click();const download=await event;const bytes=fs.readFileSync(await download.path());const saved=JSON.parse(bytes);
 ok(saved.schema==='mcada-project-progress'&&saved.inputs.plan.raw.drawW==='15','hosted export contains real entered response');
 await p.reload();await p.locator('[data-action="sessions"]').first().click();await p.locator('[data-action="resume"]').first().click();ok(await p.locator('[data-field="drawW"]').inputValue()==='15','hosted reload and resume preserve entered response');
 await p.locator('[data-action="sessions"]').click();event=p.waitForEvent('filechooser');await p.locator('[data-action="import"]').click();await(await event).setFiles({name:'hosted-progress.json',mimeType:'application/json',buffer:bytes});await p.getByRole('heading',{name:'Review import',exact:true}).waitFor();await p.locator('[data-action="importCommit"]').click();ok(await p.evaluate(()=>TPApp.store.ids().length)===2,'hosted import creates a separate saved copy');
 await p.locator('[data-action="teacher"]').click();await p.locator('[data-action="diagnostics"]').click();ok(!(await p.locator('.dialog').innerText()).includes('Failed'),'hosted diagnostics pass');
 ok(exceptions.length===0,'zero hosted uncaught exceptions');ok(assets.length===0,'zero separate runtime asset requests');
 fs.writeFileSync(path.join(out,'hosted-results.json'),JSON.stringify({observedAt:new Date().toISOString(),url,releaseCommit:'d7f5bba79c0dd104bf80d0ab78ee0a158a31bd02',htmlSha256:expected,passed:checks.length,failed:0,checks,exceptions,assets,browser:await browser.version(),configuredProxy:!!proxy,proxyCertificateException:process.env.QA_PROXY_TLS_EXCEPTION==='1'},null,2)+'\n');console.log(checks.length+' hosted checks passed');
 await ctx.close();
}finally{await browser.close()}})();
