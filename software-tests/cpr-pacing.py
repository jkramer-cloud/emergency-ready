from pathlib import Path
from playwright.sync_api import sync_playwright
import re,json,hashlib
p=Path(__file__).resolve().parent.parent; s=(p/'index.html').read_text()
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']); pg=b.new_page(viewport={'width':390,'height':844}); errors=[];pg.on('pageerror',lambda e:errors.append(str(e)));pg.set_content(s,wait_until='domcontentloaded'); pg.wait_for_timeout(100)
 print('initial errors',errors)
 pg.locator('nav [data-view="tools"]').click(); assert pg.locator('[data-pace-rate="100"]').get_attribute('aria-pressed')=='true'; assert not pg.locator('#pace-rate select,#pace-mode select').count();pg.locator('[data-pace-age="child"]').click();assert pg.locator('[data-pace-mode="30:2"]').get_attribute('aria-pressed')=='true';pg.locator('#pace-sound').uncheck();pg.locator('[data-pace="start"]').click();pg.wait_for_timeout(1200);assert pg.locator('#pace-elapsed').inner_text()=='00:01';
 assert pg.evaluate('''()=>[100,110,120].every(b=>['continuous','30:2','15:2'].every(m=>{let p=60000/b,n=m==='15:2'?15:30;let a=Array.from({length:n},(_,i)=>pacePhase(i*p+1,b,m));return a.every((x,i)=>x.count===i+1&&x.kind==='compression')&&(m==='continuous'||[0,1,2,3,4].every(i=>pacePhase(n*p+i*1000+1,b,m).stage===i)&&pacePhase(n*p+5001,b,m).count===1)}))''')
 pg.evaluate('()=>{pace.start=performance.now()-19300;paceTick();updateTools()}');assert pg.locator('#breath-countdown').is_visible(); assert 'Breath 1' in pg.locator('#pace-phase').inner_text(); pg.locator('.language-strip [data-lang="es"]').click();pg.wait_for_timeout(100);assert pg.evaluate('pace.running');assert 'Respiración 1' in pg.locator('#pace-phase').inner_text();assert pg.locator('#pace-elapsed').inner_text()!='00:00';pg.locator('#tool-cpr').screenshot(path='/mnt/data/emergency-ready-rc7-cpr-spanish.png');pg.locator('[data-pace="resync"]').click();assert pg.evaluate('pace.running');pg.locator('.language-strip [data-lang="en"]').click();pg.wait_for_timeout(100);assert 'Compress chest' in pg.locator('#pace-phase').inner_text();pg.locator('[data-pace="stop"]').click();pg.locator('#tool-cpr').screenshot(path='/mnt/data/emergency-ready-rc7-cpr.png')
 pg.locator('.language-strip [data-lang="es"]').click();pg.evaluate('()=>startGuide("adult")');pg.wait_for_timeout(100);assert 'No respira' in pg.locator('#guide-heading').inner_text();assert 'Llame al 911' in pg.locator('.guide-stage .danger').inner_text();assert pg.locator('[data-quick-voice]').is_hidden();pg.evaluate('()=>goEmergencyHome()');pg.wait_for_timeout(100);pg.screenshot(path='/mnt/data/emergency-ready-rc7-spanish-home.png');pg.locator('.callbar [data-call-open]').click();pg.wait_for_timeout(100);assert pg.locator('#call-dialog-title').inner_text()=='Llamada de emergencia real'; pg.locator('#call-safety [data-lang="en"]').click();assert pg.locator('#call-dialog-title').inner_text()=='Real emergency call';pg.locator('#call-safety [data-call-close]').first.click();
 # all 39 cards in Spanish, check heading and medical paragraphs match dictionary
 pg.locator('.language-strip [data-lang="es"]').click(); count=pg.evaluate('cards.length');
 for i in range(count):
  pg.evaluate('(i)=>{view="library";selected=cards[i][0];render()}',i); pg.wait_for_timeout(5)
  assert pg.evaluate('(i)=>document.querySelector(".detail h2").textContent===DICT[cards[i][1]]',i),i
  assert pg.evaluate('(i)=>[...document.querySelectorAll(".detail .steps li")].every((n,j)=>n.textContent===DICT[cards[i][6][j]])',i),i
 for w in [320,390,768]:
  pg.set_viewport_size({'width':w,'height':844});pg.evaluate('()=>{view="tools";selected=null;render()}');pg.wait_for_timeout(40);assert pg.evaluate('document.documentElement.scrollWidth<=innerWidth'),w
 pg.evaluate('()=>{view="library";selected=null;render()}');pg.locator('#search').fill('garrapata');pg.wait_for_timeout(50);assert pg.locator('[data-card="tickbite"]').count()==1
 print('app errors',errors);assert not errors,errors
 print('PASS: nine timing configs, CPR timer, bilingual toggle, all 39 guide records, search and three widths')
 b.close()
