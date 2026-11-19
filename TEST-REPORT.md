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
