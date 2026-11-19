from pathlib import Path
from playwright.sync_api import sync_playwright
import base64,sys
root=Path(__file__).resolve().parent.parent
html=(root/'index.html').read_text().replace('src="assets/icon-192.png"','src="data:image/png;base64,'+base64.b64encode((root/'assets/icon-192.png').read_bytes()).decode()+'"')
hub=Path(sys.argv[1]).read_text() if len(sys.argv)>1 else None
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']); page=b.new_page(viewport={'width':390,'height':844});errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.set_content(html,wait_until='load')
 # Absolutely no live calls: suppress all telephone actions at browser's window capture phase.
 page.evaluate('''()=>{window.mockCalls=0;window.addEventListener('click',e=>{if(e.target.closest('a[href^="tel:"]')){window.mockCalls++;e.preventDefault()}},true)}''')
 assert page.locator('a[href="tel:911"]').count()==0
 page.locator('[data-guide-start="minor"]').click();assert page.locator('#guide-heading').inner_text()=='Minor injury / first aid';page.locator('[data-guide-start="nosebleed"]').click();assert page.evaluate('guided.id==="nosebleed"');assert page.locator('a[href="tel:911"]').count()==0
 page.evaluate('()=>{startGuide("adult");timerAction("event","start")}');page.locator('#pace-sound').uncheck();page.locator('[data-pace="start"]').click();assert page.evaluate('pace.running');before=page.evaluate('timerState.event.start');step=page.evaluate('guided.step')
 page.locator('.callbar [data-call-open]').click();assert page.locator('#call-safety').evaluate('el=>el.open');assert page.locator('a[href="tel:911"]').count()==1;assert page.evaluate('mockCalls===0 && pace.running');assert page.locator('#call-dialog-title').evaluate('el=>document.activeElement===el');page.screenshot(path='/mnt/data/emergency-ready-rc3-confirm.png')
 page.locator('#call-confirm-view [data-call-close]').click();assert page.locator('a[href="tel:911"]').count()==0;assert page.evaluate('pace.running && guided.id==="adult"');assert page.evaluate('timerState.event.start')==before;assert page.evaluate('guided.step')==step
 page.locator('.callbar [data-no-connection]').click();assert page.locator('#call-offline-view').is_visible();assert page.locator('a[href="tel:911"]').count()==0;assert page.evaluate('pace.running');page.screenshot(path='/mnt/data/emergency-ready-rc3-offline.png');page.keyboard.press('Escape');assert not page.locator('#call-safety').evaluate('el=>el.open');assert page.evaluate('pace.running')
 page.locator('.callbar [data-call-open]').click();page.locator('#dial-confirm').click();page.wait_for_timeout(100);assert page.evaluate('mockCalls===1 && !pace.running');assert page.evaluate('timerState.event.start')==before;assert page.locator('a[href="tel:911"]').count()==0
 # Reflow and large contrast combinations; confirm and cancel without link activation.
 for width in (320,390,768):
  page.set_viewport_size({'width':width,'height':844})
  for mode in (False,True):
   page.evaluate('(v)=>{displayPrefs={large:v,contrast:v};applyDisplay()}',mode)
   for selector in ('.callbar [data-call-open]','.callbar [data-no-connection]'):
    page.locator(selector).click();assert page.locator('#call-safety').evaluate('el=>el.scrollWidth<=el.clientWidth+1');page.keyboard.press('Escape');assert page.locator('a[href="tel:911"]').count()==0
 page.evaluate('timerAction("event","stop")');page.once('dialog',lambda d:d.accept());page.locator('nav [data-view="academy"]').click();assert page.locator('.callbar [data-call-open]').is_hidden();page.evaluate('document.querySelector(".callbar [data-call-open]").click()');assert not page.locator('#call-safety').evaluate('el=>el.open');assert page.locator('a[href="tel:911"]').count()==0
 assert not errors,errors
 if hub:
  q=b.new_page(viewport={'width':320,'height':844});q.on('pageerror',lambda e:errors.append(str(e)));q.set_content(hub);assert q.locator('a[href="tel:911"]').count()==0;q.locator('.emergency [data-call-open]').click();assert q.locator('#call-safety').evaluate('el=>el.open && el.scrollWidth<=el.clientWidth+1');assert q.locator('a[href="tel:911"]').count()==1;q.locator('#call-confirm-view [data-no-connection]').click();assert q.locator('a[href="tel:911"]').count()==0;q.keyboard.press('Escape');assert not q.locator('#call-safety').evaluate('el=>el.open');q.screenshot(path='/mnt/data/playforge-rc3-first-aid.png');assert not errors,errors
 b.close()
print('PASS: call confirmation, no actual dialing, cancel and Escape, guided/CPR and stopwatch continuity, mock confirmed call, 12 dialog layout configurations, training call isolation, Hub page')
