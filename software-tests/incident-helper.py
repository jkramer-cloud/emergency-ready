from pathlib import Path
from playwright.sync_api import sync_playwright
p=Path(__file__).resolve().parent.parent
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']); pg=b.new_page(viewport={'width':390,'height':844});errors=[];pg.on('pageerror',lambda e:errors.append(str(e)));pg.set_content((p/'index.html').read_text());pg.wait_for_timeout(100)
 # tools and guided CPR share same helper records
 pg.evaluate('()=>startGuide("adult")');assert pg.locator('#incident-audio').count()==1
 pg.locator('[data-stamp="9"]').click();assert 'CPR begun' in pg.locator('#event-list').inner_text();pg.locator('[data-stamp="11"]').click();assert 'AED turned on' in pg.locator('#event-list').inner_text()
 pg.locator('#pace-sound').uncheck();pg.locator('[data-pace="start"]').click();pg.wait_for_timeout(150);assert pg.evaluate('pace.running');assert 'Pacing tool started' in pg.locator('#event-list').inner_text();pg.locator('[data-stamp="5"]').click();assert pg.evaluate('pace.running');assert 'Shock delivered' in pg.locator('#event-list').inner_text()
 pg.locator('#incident-audio summary').click();assert pg.locator('[data-note-start]').is_disabled();assert pg.locator('[data-incident-question="0"]').is_disabled();pg.locator('[data-pace="stop"]').click();assert 'Pacing tool stopped' in pg.locator('#event-list').inner_text()
 pg.locator('[data-note-start]').click();assert 'permission' in pg.locator('#note-status').inner_text();pg.locator('#note-consent').check();
 # simulate failure and success explicitly; no real microphone access
 pg.evaluate('''()=>{Object.defineProperty(navigator,'mediaDevices',{configurable:true,value:{getUserMedia:async()=>{throw Error('denied')}}})}''');pg.locator('[data-note-start]').click();pg.wait_for_timeout(100);assert 'denied' in pg.locator('#note-status').inner_text()
 pg.evaluate('''()=>{window.trackStops=0;Object.defineProperty(navigator,'mediaDevices',{configurable:true,value:{getUserMedia:async()=>({getTracks:()=>[{stop:()=>window.trackStops++}]})}});window.MediaRecorder=class{constructor(){this.state='inactive';this.mimeType='audio/webm'}start(){this.state='recording'}stop(){this.state='inactive';queueMicrotask(()=>{this.ondataavailable({data:new Blob(['fictional test'],{type:'audio/webm'})});this.onstop()})}}}''');pg.locator('[data-note-start]').click();assert pg.locator('#note-clock').is_visible();pg.locator('[data-note-stop]').click();pg.wait_for_timeout(100);assert pg.locator('[data-note-play]').count()==1;assert pg.evaluate('trackStops')==1;assert 'Voice note captured' in pg.locator('#event-list').inner_text()
 pg.locator('[data-note-delete]').click();assert pg.locator('[data-note-play]').count()==0
 pg.locator('[data-note-start]').click();pg.locator('.callbar [data-call-open]').click();pg.wait_for_timeout(100);assert pg.evaluate('noteRecorder===null && !notePending');assert pg.evaluate('trackStops')==2;pg.locator('#call-safety [data-call-close]').first.click();assert pg.locator('[data-note-play]').count()==0
 pg.locator('[data-note-start]').click();pg.locator('[data-pace="start"]').click();pg.wait_for_timeout(100);assert pg.evaluate('noteRecorder===null && pace.running');assert pg.evaluate('trackStops')==3;pg.locator('[data-pace="stop"]').click();
 pg.locator('.language-strip [data-lang="es"]').click();pg.wait_for_timeout(150);assert 'Panel de ayuda' in pg.locator('.incident-panel h3').inner_text();assert '¿Dónde estamos?' in pg.locator('.incident-questions').inner_text();pg.locator('.language-strip [data-lang="en"]').click();pg.wait_for_timeout(100)
 pg.evaluate('()=>{view="tools";selected=null;render()}');assert pg.locator('#event-list').count()==1;assert pg.locator('#incident-full').count()==1;assert 'AED turned on' in pg.locator('#incident-full').text_content();assert pg.locator('#incident-audio').count()==1
 for w in [320,390,1024]:
  pg.set_viewport_size({'width':w,'height':844});pg.locator('#incident-audio').evaluate('(x)=>x.open=true');assert pg.evaluate('document.documentElement.scrollWidth<=innerWidth'),w
 pg.set_viewport_size({'width':390,'height':844});pg.locator('#incident-audio').evaluate('(x)=>x.open=false');pg.add_style_tag(content='.language-strip,.callbar{position:static!important}');pg.locator('.incident-panel').screenshot(path='/mnt/data/emergency-ready-rc7-helper.png');pg.locator('#incident-audio').evaluate('(x)=>x.open=true');pg.locator('#incident-audio').screenshot(path='/mnt/data/emergency-ready-rc7-audio.png');assert not errors,errors
 b.close()
print('PASS: manual and automatic timestamps, state continuity, microphone refusal and simulated recording, deletion, call cancellation, pacing isolation, bilingual helper UI, no overflow')
