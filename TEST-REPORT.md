# RC7 executed software checks

- 834 guided display configurations, 47 academy decisions, library, kits, tools, review workstation search/export/restore and training safeguard: PASS.
- Nine CPR timing configurations, bilingual switch and written content for all 39 guide records, library search and three viewport widths: PASS.
- Call confirmation and cancellation, stopwatch and CPR continuity, mock confirmed dial, 12 dialog layout configurations and training call isolation: PASS. No real calls.
- Incident helper quick/manual timestamps, simulated recording and deletion, language switching, layout and pacing isolation: PASS.
- RC6 opt-in recording: permission denied/late cleanup, bilingual notice selection, foreground session recordings, mock audio save/delete and navigation, call cancellation and simulated dial interruption: PASS.
- RC7 responder handoff: guide opening, manual timestamps, cue and breath-window tracking, nonblocking summary opening/closing, bilingual switching during pacing, multiple-session elapsed time, local text and simulated audio-file downloads, delete, navigation, reset, training isolation and 320/390/768 layouts: PASS (`software-tests/responder-handoff.py`).
- Offline service worker simulation: 181-file integrity install, failed/corrupt download rollback, deferred activation, scoped cache cleanup, offline navigation, audio byte ranges, missing file and verified repair: PASS. Corrected stale index hash found during first test before final verification.

Tests use Chromium with injected HTML, fake microphone/recording objects and simulated service worker lifecycle. They do not establish actual phone installation, mic quality, clinical safety, usability during a genuine emergency, or legal compliance. Audio data and all timestamps used during tests are fictional. See the release gates and RC7 review addendum.

## RC6 executed software checks

- 834 guided display configurations and 47 academy decisions: PASS.
- Nine CPR timing configurations, Spanish switching/39 written records, library search and three viewport widths: PASS.
- Call confirmation, cancellation, simulated confirmed dial, timers and 12 modal configurations: PASS. No real call.
- Incident capture: opt-in only, simulated mic permission and denial, late permission cleanup, bilingual notice selection, language switching, event stamps, recording elapsed timer, cancel call continuation, actual dial action simulated stop, local blob download, delete, navigation and training isolation: PASS. No actual microphone/audio fidelity verification.
- Prior practice voice notes/helper station tests: PASS.
- Simulated service-worker integrity: all 181 runtime files, corrupt file rollback and offline byte ranges: PASS.

Physical microphone, real speaker announcement capture, permissions, backgrounding, browser download handling and school authorization still require review.

# RC6 addendum — opt-in emergency incident audio

Private release candidate. No medical or district authorization yet. Separate **Start pacing + record incident** action explicitly opts in; ordinary Start never requests microphone access. Pacing starts immediately, independent of permission. Once the mic actually starts, an English or Spanish offline announcement plays once and a visible recording indicator, timer and spoken-notice text appear. The participating helper should announce the recording aloud; the device may not capture its own loudspeaker and this feature is not proof of legal consent. Audio records in the foreground for the selected CPR session until Stop recording, Stop pacing, navigation, hidden tab, intentional telephone dialing, capture interruption or the 60-minute / approximately 64 MiB ceiling (final chunk may exceed limit). Opening/canceling the call confirmation does not stop pacing or an established recording. Automatic log entries reflect recorder/tool activity, not clinical actions. No recording or playback in Training Academy. Questions and recorded-audio playback remain disabled during pacing; manual event entries remain available. The bilingual notice is the sole additional announcement. No call recording, cloud upload, transcription, accounts or background capture. One incident recording stays in tab memory, with explicit local Save audio file, Listen and Delete options. Saved files remain on the device even after in-app Delete; use authorized handling/retention only. A refresh, close, crash or operating-system suspension can lose unsaved audio. If microphone permission fails or is canceled, first aid and pacing continue uninterrupted when the tab remains visible. Do not delay emergency care, and do not use real student data in prototype testing.

Washington RCW 9.73.030(2)(a) permits emergency-nature conversations with consent of one party. Subsection (3) addresses effective announcements where all-party consent is required. This is not a blanket waiver of student privacy, device policy, disclosure or records-retention rules. Obtain district guidance and review prior to real deployment: https://app.leg.wa.gov/RCW/default.aspx?cite=9.73.030. Browser APIs: https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia and https://developer.mozilla.org/en-US/docs/Web/API/MediaRecorder.

# RC5 addendum — helper station and audio notes

Private release candidate only. RC4 features retained. Review the CPR-adjacent manual timeline, automatic pacing-tool start/stop stamps (not clinical actions), question prompts, audio files and bilingual strings. Optional microphone recordings are limited to fictional supervised practice, require explicit permission, stay in tab memory, and are disabled during pacing. No upload, persistent storage, transcription, or recording of calls. Test microphone permission denial, actual device audio routing, deletion, backgrounding, call confirmation, school privacy approval and bilingual clinical review before adoption. Washington RCW 9.73.030 generally requires consent for private conversations, with specific exceptions: https://app.leg.wa.gov/RCW/default.aspx?cite=9.73.030. Browser microphone permission/secure context: https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia.

## RC5 software checks passed

- Chromium helper tests: manual and automatic timestamps, state continuity across guided CPR and Tools, simulated microphone denial and recording, stop/delete and track release, call-confirmation and pacing isolation, bilingual helper labels, and layout checks at 320/390/1024 px.
- Re-ran RC4 CPR/Spanish checks: nine timing combinations, automatic elapsed timer, language switch, all 39 guide records, search.
- Regression: 834 guided display states and 47 training decisions.
- Call-safety checks: no real dialing, 12 dialog layouts, timer continuity.
- Service-worker mock: 179-file integrity install, corruption rollback, deferred activation, offline navigation, English and Spanish audio byte ranges, missing-file detection and repair.

Microphone behavior was simulated; no actual physical-device recording, speech quality, or offline installation was verified. No clinical, privacy-policy or bilingual approval is implied.

# RC4 software test results

Passed in Chromium (injected HTML) and simulated service worker: 9 rate/method combinations, 5-second breath phases, elapsed timer, early resume, language switching during active CPR, written translation checks on 39 card records, Spanish keyword search, app and Hub call modal language switch, 3 mobile/desktop widths, 834 guided display configurations, 47 training decisions, library/kits/review baseline behavior, 12 confirmation dialog layouts, no real telephone activation, 167-file cache install/repair/corruption checks. Language translations are drafts, not clinically or professionally verified. No physical-device audio, clinical timing validation, actual offline browser installation or student test performed. The previous RC3 review workstation is historical; see RC4 addendum and SPANISH-REVIEW.json.

## Historical test results
# v1.0 RC2 — software verification

This is a private, unapproved release candidate. Software checks do not validate clinical correctness or physical-device behavior.

## Passed
- Reproducible injected Chromium test (`software-tests/rc-browser.py`): 828 guided-screen configurations (138 states × three widths × two display settings); visible 911 link, headings, no horizontal overflow, no images in emergency guide screens. Exact guide step grouping retains all original written steps.
- Training entry confirmation: cancel preserves active guide; accept switches to isolated practice with no live call control. All 44 academy decisions tested with correct answers and completion. Return to emergency, library search, kit creation, tools and info navigation tested.
- Reviewer workstation: 314 unique records; guide filtering, ID search, review status and notes, exported JSON and restore; no uncaught page errors in browser checks. Media file paths exist; real playback/visual interpretation in this workstation not tested.
- Node syntax validation for both HTML scripts and service worker. Node VM mocked service worker test passed: corrupted download rollback, successful verified 167-file installation, deferred activation, scope cleanup, offline cached navigation, ranged audio and missing-file repair.
- All 167 runtime file hashes match. All v0.9.5 files retained, and all existing asset bytes unchanged (139 MP3s, 22 WebPs and four icons). Original guide text, recordings and training answers preserved; new CPR tool guidance and cue behavior require review.
- Preview images use injected HTML, not an actual installed phone or hosted worker. The browser test directly initializes guide states and academy activities; this is not a human panic simulation.

## Outstanding / release blocking
Clinical review of all content, narration intelligibility, full technique illustrations and review findings; actual iPhone, Android and Chromebook installation and offline reopen; OS storage persistence, audio, phone handoff, real service-worker update lifecycle; real assistive technology and supervised student usability; school/district authorization. No live 911 tests. No claim of complete WCAG compliance, comprehensive functional regression, or medical approval. See RELEASE-GATES.md, DEVICE-INSTALL-TEST.md, PANIC-USE-TEST-PLAN.md and review-package/START-HERE.md. Prior build details remain in README and earlier packages.

## RC2 targeted CPR tests
- `software-tests/cpr-pacing.py`: phase boundary calculations for 9 rate/method combinations, age selection and defaults, restricted pediatric 15:2, visual 30:2 cue, restart-count control, real browser Web Audio context startup and oscillator scheduling, adjustable volume, stop and navigation cancellation, and reflow at 320, 390 and 768 pixels. Browser-run checks use injected HTML; they do not establish actual acoustic loudness or real CPR accuracy.
- `software-tests/service-worker-mock.cjs`: simulated 167-file install, corruption rollback, deferred activation, byte ranges, offline navigation and repair.
- Physical-device acceptance and clinical review still pending.


## RC3 software verification

RC3 includes all RC2 CPR and breath-cue functionality. Automated tests on the cumulative package passed:
- 834 guided display states (139 states across 3 widths and two display modes); 47 training decisions; all library, kits, tools and reviewer navigation checks.
- 9 CPR timing combinations, method selection, simulated audio context, volume and breath cycle controls, navigation and 3 widths.
- Deliberate call confirmation: no callable emergency link until the confirmation opens; cancel and Escape remove the link; offline-help panel does not expose a telephone link; active response, stopwatch and CPR rhythm survive opening/cancel. Simulated confirm suppresses competing audio and preserves stopwatch state. All telephone link activations were blocked by the test harness. No real calls made.
- 12 confirmation/offline dialog layout configurations at 320, 390 and 768 px, standard and large/high-contrast; training mode does not permit opening the call dialog.
- Minor-injury route, Hub first-aid page confirmation and offline help, reviewer register with 319 entries and backup export/restore.
- Mock service worker: 167-file hashed cache installation, corrupt-download rollback, deferred activation, offline requests, audio range requests and verified repair.

Clinical approval, physical-device phone behavior/audio, native installation and offline restart, screen-reader testing and supervised child usability remain outstanding. No real emergency calls should be made for testing. No new narration was added for the minor-injury menu or call dialogs.


## RC4 update — pending review
- Large visible CPR method and rate buttons; default 100/min, unchanged accepted 100–120/min. Five-second breath cue with staged one-second breaths, immediate early resume, and elapsed session timer. Timing is approximate; do not delay care.
- English/Español switch persists locally; Spanish draft written instructions for all 39 card records and 7 chooser paths. English voice, training, inventory and some source/review material remain English; English narration disabled in Spanish. Bilingual medical review is required, including all entries in SPANISH-REVIEW.json.
- Reference: https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support and https://www.redcross.org/take-a-class/cpr/performing-cpr/cpr-steps. Short interruption; each breath about one second. Five seconds is UI design, not a prescribed clinical duration.
