from playwright.sync_api import sync_playwright
from pathlib import Path
import json,base64,hashlib
root=Path(__file__).resolve().parent.parent
s=(root/'index.html').read_text(); s=s.replace('src="assets/icon-192.png"','src="data:image/png;base64,'+base64.b64encode((root/'assets/icon-192.png').read_bytes()).decode()+'"')
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']); pg=b.new_page(viewport={'width':390,'height':844},accept_downloads=True); errors=[]; pg.on('pageerror',lambda e:errors.append(str(e))); pg.set_content(s,wait_until='load')
 assert pg.locator('[data-call-open].call').is_visible();assert not pg.locator('#phone-setup').evaluate('(el)=>el.open')
 data=pg.evaluate('''()=>({ids:cards.map(c=>c[0]),groups:Object.keys(chooser),special:Object.keys(specialGuides),audioCount:audioPaths.length,artCount:illustrations.length,academyCount:academyBank.length,quizCount:questions.length,refsOK:cards.every(c=>c[8].every(k=>refs[k]))&&questions.every(q=>refs[q[4]])&&academyBank.every(a=>a.steps.every(q=>refs[q.ref]))})'''); assert data['refsOK'];assert (data['audioCount'],data['artCount'],data['academyCount'],data['quizCount'])==(139,22,28,38)
 assert pg.evaluate('''()=>cards.every(c=>JSON.stringify(currentGuide(c[0]).steps.flatMap(s=>s.slice(1)))===JSON.stringify(c[6]))''')
 screens=0
 for w in (320,390,768):
  pg.set_viewport_size({'width':w,'height':844})
  for mode in (False,True):
   pg.evaluate('(v)=>{displayPrefs={large:v,contrast:v};applyDisplay()}',mode)
   for id in data['ids']+data['groups']+data['special']:
    count=pg.evaluate('(id)=>chooser[id]?1:currentGuide(id).steps.length',id)
    for step in range(count):
     pg.evaluate('([id,step])=>{view="emergency";selected=null;guided={id,step,history:[]};render()}',[id,step]);assert pg.locator('[data-call-open].call').is_visible();assert pg.locator('#guide-heading').is_visible();assert pg.evaluate('document.documentElement.scrollWidth<=innerWidth');assert pg.locator('#screen img').count()==0;screens+=1
 pg.set_viewport_size({'width':390,'height':844});pg.evaluate('()=>{displayPrefs={large:false,contrast:false};applyDisplay();guided=null;interruptedGuide=null;view="emergency";render();startGuide("adult")}')
 pg.once('dialog',lambda d:d.dismiss());pg.locator('nav [data-view="academy"]').click();assert pg.evaluate('()=>guided?.id==="adult" && view==="emergency"')
 pg.once('dialog',lambda d:d.accept());pg.locator('nav [data-view="academy"]').click();assert pg.locator('[data-call-open].call').is_hidden();assert pg.locator('.training-exit').is_visible()
 # every decision, through actual UI buttons in single-item activities
 decisions=0
 for id in pg.evaluate('()=>academyBank.map(x=>x.id)'):
  pg.evaluate('(id)=>{academyStart([academyBank.find(a=>a.id===id)])}',id)
  while not pg.evaluate('()=>academySession.finished'):
   correct=pg.evaluate('()=>{let a=academySession,x=academyBank.find(x=>x.id===a.queue[a.index]);return a.options.findIndex(o=>o.i===x.steps[a.step].correct)}')
   pg.locator(f'[data-academy-answer="{correct}"]').click();assert 'Correct decision' in pg.locator('#academy-feedback').inner_text();pg.locator('[data-academy-next]').click();decisions+=1
 assert decisions==47
 pg.locator('.training-exit [data-guide-home]').click();assert pg.locator('[data-call-open].call').is_visible()
 pg.locator('nav [data-view="library"]').click();pg.locator('#search').fill('tick');assert 'Tick' in pg.locator('#grid').inner_text();pg.locator('#search').fill('');assert pg.locator('#grid .tile').count()==38
 pg.locator('nav [data-view="kits"]').click();pg.locator('#kit-name').fill('Fictional test kit');pg.locator('#kit-create button[type="submit"]').click();assert 'Fictional test kit' in pg.locator('#screen').inner_text()
 pg.locator('nav [data-view="tools"]').click();assert pg.locator('#screen').inner_text();pg.locator('nav [data-view="info"]').click();assert 'review' in pg.locator('#screen').inner_text().lower();pg.locator('nav [data-view="emergency"]').click(); assert pg.locator('[data-call-open].call').is_visible()
 assert not errors,errors
 # separate review workstation: status, notes, search, export/restore
 rv=b.new_page(viewport={'width':1000,'height':900},accept_downloads=True);rv.on('pageerror',lambda e:errors.append(str(e)));rv.set_content((root/'review-package/review.html').read_text(),wait_until='domcontentloaded');assert rv.locator('article').count()==319;rv.locator('#category').select_option('Guides');assert rv.locator('article').count()==39;rv.locator('#search').fill('guide:adult');assert rv.locator('article').count()==1;rv.locator('article select').select_option('changes required');rv.locator('article textarea').fill('Fictional test note');assert '1 of 319' in rv.locator('#counts').inner_text()
 with rv.expect_download() as d:rv.locator('#export').click()
 path=d.value.path();v=json.loads(Path(path).read_text());assert v['decisions']['guide:adult']['notes']=='Fictional test note';rv.reload();rv.set_content((root/'review-package/review.html').read_text(),wait_until='domcontentloaded');rv.locator('#import').set_input_files(path);rv.wait_for_function('document.getElementById("message").textContent==="Review restored."');assert '1 of 319' in rv.locator('#counts').inner_text();assert not errors,errors
 b.close()
print(f'PASS: {screens} guided display states, 47 academy decisions, library, kits, tools, review search and export/restore, training safeguard')
