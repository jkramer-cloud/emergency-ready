from playwright.sync_api import sync_playwright
from pathlib import Path
import base64
root=Path(__file__).resolve().parent.parent
s=(root/'index.html').read_text().replace('src="assets/icon-192.png"','src="data:image/png;base64,'+base64.b64encode((root/'assets/icon-192.png').read_bytes()).decode()+'"')
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']); pg=b.new_page(viewport={'width':390,'height':844});errors=[];pg.on('pageerror',lambda e:errors.append(str(e)));pg.set_content(s,wait_until='load')
 # Check all rates, compression counts, breath boundaries, repeat and continuous
 assert pg.evaluate('''()=>[100,110,120].every(bpm=>['30:2','15:2','continuous'].every(mode=>{let period=60000/bpm,n=mode==='15:2'?15:30;let samples=Array.from({length:n},(_,i)=>pacePhase(i*period+2,bpm,mode));if(!samples.every((a,i)=>a.kind==='compression'&&a.count===i+1))return false;if(mode==='continuous')return pacePhase(100000,bpm,mode).kind==='compression';let x=pacePhase(n*period+2,bpm,mode),y=pacePhase(n*period+1600,bpm,mode),z=pacePhase(n*period+3502,bpm,mode);return x.kind==='breath'&&y.kind==='breath'&&x.slot!==y.slot&&z.kind==='compression'&&z.count===1}))''')
 pg.locator('nav [data-view="tools"]').click(); assert pg.locator('#pace-mode').input_value()=='continuous'
 pg.locator('[data-pace-age="child"]').click(); assert pg.locator('#pace-mode').input_value()=='30:2';assert pg.locator('#pace-profile').inner_text().find('one-third')>=0
 pg.locator('[data-pace-age="infant"]').click();assert '1.5 inches' in pg.locator('#pace-profile').inner_text();assert pg.locator('#pace-mode option[value="15:2"]').count()==1
 pg.locator('[data-pace-age="adult"]').click();assert pg.locator('#pace-mode option[value="15:2"]').count()==0
 pg.locator('[data-pace-age="child"]').click();pg.locator('#pace-rate').select_option('120');pg.locator('#pace-sound').uncheck();pg.locator('[data-pace="start"]').click();assert pg.locator('#pace-mode').is_disabled();assert pg.locator('#pace-beat').inner_text().endswith('/ 30')
 # advance internal clock deliberately without sleeping 15 seconds; real pause isn't simulated clinical performance
 pg.evaluate('()=>{pace.start=performance.now()-15300;paceTick();updateTools()}');assert pg.locator('#pace-beat').inner_text()=='2 BREATHS';assert pg.locator('#pace-phase').inner_text().startswith('Give 2 breaths')
 pg.locator('#tool-cpr').screenshot(path='/mnt/data/emergency-ready-rc3-cpr-breaths.png')
 pg.locator('[data-pace="resync"]').click();assert pg.locator('#pace-beat').inner_text()=='1 / 30';pg.locator('[data-pace="stop"]').click();assert not pg.locator('#pace-mode').is_disabled()
 pg.locator('[data-pace-age="adult"]').click();pg.locator('#pace-sound').check();pg.locator('[data-pace="start"]').click();pg.wait_for_timeout(800);assert pg.evaluate('()=>pace.running && pace.ctx?.state==="running" && pace.lastToneSlot!==""');pg.locator('#pace-volume').fill('100');assert pg.evaluate('()=>pace.volume===1');pg.locator('[data-pace="stop"]').click();assert pg.evaluate('()=>!pace.running&&pace.ctx===null')
 # guided defaults and navigation cancellation
 pg.evaluate('()=>startGuide("infant")');assert pg.locator('[data-pace-age="infant"]').get_attribute('aria-pressed')=='true';assert pg.locator('#pace-mode').input_value()=='30:2';pg.locator('#pace-sound').uncheck();pg.locator('[data-pace="start"]').click();pg.locator('nav [data-view="library"]').click();assert pg.evaluate('()=>!pace.running')
 for w in (320,390,768):
  pg.set_viewport_size({'width':w,'height':844});pg.locator('nav [data-view="tools"]').click();assert pg.evaluate('document.documentElement.scrollWidth<=innerWidth');assert pg.locator('[data-call-open].call').is_visible()
 pg.set_viewport_size({'width':390,'height':844});pg.locator('[data-pace-age="infant"]').click();pg.locator('#tool-cpr').screenshot(path='/mnt/data/emergency-ready-rc3-cpr-profile.png');assert not errors,errors;b.close()
print('PASS: 9 timing configurations, profile/method selection, live audio context, volume, breath cue, resync, stop, guided auto-selection, navigation and 3 widths')
