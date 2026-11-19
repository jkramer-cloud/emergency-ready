# Emergency Ready v1.0 RC3 — private release candidate

**NOT cleared for real emergency use or publication.** Open the extracted `index.html` to test fictional scenarios only. The current build preserves all v0.9.5 application features, assets and offline framework. No repository deployment. Reviewers: open `review-package/review.html` and read `review-package/START-HERE.md`. The review register covers exact application content and pending illustrations. All device, clinical and institutional release gates remain open.

## RC3 changes
- CPR age selection (teen/adult, child, infant) and age-specific depth and method guidance. Guided screens preselect their corresponding age. The shared rate remains 100–120/min, default 110/min.
- Continuous compression-only pacing or 30:2 cycles; pediatric 15:2 is explicitly limited to two trained healthcare rescuers. A contrasting visual phase and two distinct tones mark a brief approximate 3.5-second breath window; a helper can restart the count/resume early. Follow training, AED and dispatcher rather than the cue. Do not delay care, and never stop CPR just because the tool stops.
- More prominent locally synthesized compression tones, adjustable volume and optional silent visual mode. Sound remains subordinate to phone/dispatcher audio; actual loudness depends on the device.
- 319 review items (one new CPR tool record); review prior decisions against this changed build. Versioned cache and runtime hashes regenerated. All original reference guides, narration, illustrations, kit and training content retained.
- RC1 introduced the reviewer workstation and active-response training safeguard; both remain.


## Prior development documentation
# Emergency Ready v0.9.5 — phone installation & offline readiness

**Private development prototype. Not medically reviewed; do not rely on it during a real emergency.** Use established resources and follow 911 dispatchers instead. No public release or repository needed.

## New in this build
- Phone setup & offline checks, below the emergency interface; never required to access instructions.
- iOS home-screen icon, Android maskable icon, existing manifest identity retained.
- Browser install prompt only when the browser offers one; manual Safari and Chrome instructions.
- Version-pinned cache, SHA-256 verification of 167 runtime files (about 22.8 MB), cache-presence checks, cached audio range responses, and no forced reload or update activation.
- All 139 narration clips and 22 review-only WebP drafts retained unchanged. Training, guides, tools, kits and accessibility settings retained.

## How to try
Extract the entire ZIP. Open `index.html` for local desktop exploration. For installation testing, serve the entire directory from a private HTTPS test site or localhost; a ZIP or file URL is not an installable phone app. Keep the directory structure. See `DEVICE-INSTALL-TEST.md` for the test method and outstanding approval gates. Do not distribute to students for real emergency use until independent clinical and usability review is complete.

## Release management
Upload all files together to the same private test path; never mix files from different versions. Future builds must use a new version/cache key, regenerate the SHA-256 list in `sw.js` and `OFFLINE-ASSET-REGISTER.json`, and preserve the manifest identity and scope. A waiting worker activates when old app clients close. No forced activation, data clearing or automatic navigation. Older unscoped caches are deliberately not deleted to avoid deleting another app's files. Browser storage may be removed automatically; check again and confirm offline reopening. Session-only timers do not survive closing the app. Export kit backups before changing installations. Separate installations may have separate storage.

## Prior build history
# Emergency Ready — v0.9 · Accessibility and panic-use preparation

Private prototype; **not clinically approved for actual emergency use**. Call 911 and follow the dispatcher in a real emergency. No student data, analytics or account needed. Do not publish until clinical review and device/usability testing are complete.

## Open this build
Extract the entire ZIP; keep the asset folders. Open `index.html` in your browser to preview. For install/offline testing, a private HTTPS or localhost host is required.

## v0.9 additions
- Larger-text and high-contrast modes, independently selectable; preferences stored locally when available.
- Compact mobile header; readable, separated action paragraphs; optional tools and narration settings after core directions; quick Read aloud/Stop audio shortcut near the top of guided screens.
- Keyboard skip link, heading focus, visible focus rings, sticky-bar offset and larger controls.
- Home immediately returns to the urgent choices, with a session-only resume/dismiss shortcut for the previous guide. Selecting a new emergency clears the old shortcut. No confirmation for urgent choices or 911.
- Rapid duplicate Next/Previous activations within 350 ms are ignored; confirmation for clearing a stopped elapsed timer. Active timing continues during navigation.
- Existing audio cancellation on backgrounding and telephone-link activation retained.
- 38 guides plus Start here; 139 audio clips; 22 draft WebP illustrations in review-only gallery; 28 academy activities; 38 quiz questions; five emergency tools; seven kit templates all retained.

## Verification
See `TEST-REPORT.md` and `PANIC-USE-TEST-PLAN.md`. WCAG-informed interface improvements do not establish conformance. This build uses the same medical content and audio clips as v0.8.5, except a previously inconsistent active seizure timer alert is aligned to the existing five-minute call warning. No independent clinical review or actual student tests have been performed. Real phone installation and offline behavior remain unverified.

Next: v0.9.5, installability, home-screen access and real-device verification.

## Previous release notes
# Emergency Ready v0.8.5 — Expanded illustration review collection

**Current build:** 22 draft WebP assets (14 new), with topic-grouped review gallery under Sources & info. The previous eight drafts and every previous feature are retained. The following earlier release notes describe development history, not the current asset count. All artwork is excluded from emergency and training workflows until independently approved.

# Emergency Ready v0.8.2 — Training Academy

Private development build; not clinically reviewed or approved for actual emergency use.

## New in v0.8.2
- 18 fictional emergency scenarios and 8 equipment activities (47 decisions). School, home, sports and outdoor scenarios.
- Separate blue practice interface; live telephone links, live emergency tools and normal navigation hidden during practice. Real emergency button returns to the emergency home screen. Active emergency timers prevent launching the academy; narration stops when entering.
- Five-activity mixed practice, prioritizing unfinished activities, randomized answer order, retries, source-linked explanations and eight practice milestones. No countdowns, accounts or personal records.
- Locally saved completion and first-try milestones when browser storage permits; shared devices share practice progress. Reset only clears academy progress. The original 38-question quiz remains available.
- TRAINING-BANK.json is a teacher-review copy of the embedded questions and explanations, not a runtime dependency.
- Existing 38 guides plus Start here, 139 narration clips, kits, tools and eight review-only WebP drafts retained.

## Run
Extract the entire ZIP, then open index.html. Use a private HTTPS server for installation tests. Do not publish yet. Read TEST-REPORT.md and REVIEW-CHECKLIST.md.

## Earlier build notes
# Emergency Ready — v0.8.1 · Spoken guidance and integrated tools

Private U.S. educational development prototype. Not medically approved, not a medical device or certified course. In an emergency call 911 and follow the dispatcher. Do not delay care to operate this app. No GitHub or Learning Hub publication until development and independent clinical review are complete.

## Try the complete build
Extract the ZIP and open `index.html`. Local content and tools use no network or account. For private PWA testing, serve via localhost or private HTTPS, open once online and test offline restart. Telephone calls and external sources require connectivity. Browser storage may be evicted. Actual offline installation has not been verified.

## Features
- All 38 topic guides, Start here, 38 randomized practice questions, category/search filtering, related guides, persistent 911 link and guide printing.
- Tools tab and shortcuts from relevant guides and the emergency dashboard.
- CPR rhythm aid: 100, 110 or 120 BPM; visual beat and optional Web Audio tone. Stops when navigating away or backgrounding the page; never a signal to stop CPR. Does not measure compressions or guide ventilation.
- Independent seizure and general event stopwatches; elapsed time remains visible while navigating. Five-minute seizure escalation message (and other immediate escalation conditions); no clinical thresholds in general event timer.
- Manual timestamps for common events and session-only responder checklist. No patient names, free text, saved records, export or cloud sync. 100-entry limit for the timeline. Refresh clears all tool state.
- Illustration safety revision: earlier diagrams retired; eight WebP drafts in the separate Sources & info review-only gallery. Four conflicting or ambiguous draft drawings removed (infant CPR, infant choking, adult/child choking and severe bleeding). Written infant CPR already used the updated technique; infant choking text now specifies heel-of-hand chest thrusts. Illustration badges removed from emergency tiles pending review.
- Existing source register, medical review checklist, local icon assets and service worker, updated cache v08.

## Safety and testing limits
Time is estimated from the moment Start is pressed, not necessarily symptom onset. Clock changes, browser throttling, backgrounding, audio permissions, device sleep and interruptions can affect timing or playback. No automatic calls, notifications or alarms in a closed app. Clinical review, real-device timing/audio, accessibility, offline installation and printing are required before public use. See TEST-REPORT.md and REVIEW-CHECKLIST.md.

## New in v0.7
- Dedicated Kits tab with six editable starter templates (home, classroom, vehicle, camping/hiking, sports/esports, evacuation bag) and a blank template. Create multiple kits; all initial stock counts are zero.
- Editable targets, usable stock counts, custom supply names/categories on creation, earliest expiry per line, individual inspection dates, and recorded full-kit inspection date. Filters for low stock, expired/expiring items and overdue/missing checks; 30-day alerts are in-app only. Quantities are suggested starting points, not prescribed or regulatory minimums. Split batches into separate lines when dates differ. Do not count unusable items as stock.
- Browser-local storage for generic supplies only, JSON export/restore (replacement confirmation, validated schema), and full printable inventory independent of the active filter. No login, sync, background notices, or personal/patient/student information. Back up before moving browsers or clearing data. Browser storage durability varies, especially for local files. Emergency incident tools remain session-only.
- No default medication inventory or medication dosing. School and event kits must be reviewed for local policies and actual needs. Source examples from Red Cross, CDC and FEMA Ready. No inventory status certifies medical readiness.

Next: v0.8.1 spoken instructions and integrated tools; v0.8.2 interactive training academy.


## v0.7.1 — WebP illustration rebuild
Eight locally bundled original draft visuals in `assets/illustrations/`; inspect them under Sources & info → WebP illustration development. The existing ten inline diagrams are retired. Original editable SVG source and reviewer register are in `illustration-review/`. No artwork is displayed during emergency reference or practice. The service worker includes every WebP in its precache and readiness checks. To revise, replace the corresponding WebP (and source SVG), update review records, and bump the service-worker cache version. No asset is approved; qualified medical review is mandatory. No training features were added in v0.7.1.


## v0.8 — Guided emergency response
- Opens directly to six large symptom-based buttons: not responding, choking, severe bleeding, seizure, trouble breathing and other emergency. Extra buttons for uncertainty and AED access. Persistent 911 link and emergency-home return from other screens. No login or intake form.
- Age-specific CPR and choking paths; no more than 10 seconds checking breathing, no pulse checking required. Critical related actions are grouped together rather than hidden behind a next button. All 38 guides plus Start here can also be read as guided actions via the searchable library.
- Clear escalation, repeated caution, step progress and all-actions view; back/previous navigation and full reference. Navigation is neither diagnosis nor confirmation that care is finished. If unsure, call 911, seek a nearby adult, and follow dispatcher instructions.
- Seizure timer and responder checklist are reachable from a relevant guided path and offer a return to the same action. Timers are advisory, not alarms or medical devices.
- Existing kits, 38 questions, tools and eight review-only WebP drafts retained. No unapproved illustration appears in response mode. The first-pass guided copy reuses the existing unreviewed reference library. Dedicated simulations and additional illustrations are deferred.
- Browser test uses injected HTML rather than a deployed site; no medical review, actual calls, phone/device offline installation or child usability tests have taken place. This is a private preview, not suitable for emergency reliance.


## v0.8.1 audio and tool update
- 139 local English MP3 clips cover the emergency home, every choice screen and every action screen. Generated from the existing priority/action/caution text using eSpeak, with spoken-number and acronym normalization. Synthetic voice, not a human recording; not medically or intelligibility reviewed. See `AUDIO-REGISTER.json` for exact source text and spoken transcript.
- Tap Read aloud or Repeat aloud; optionally enable automatic reading of subsequent guided screens in this session. Audio starts only after user interaction. Stop audio disables automatic reading. Navigation cancels previous narration; dialing a telephone link or hiding the tab cancels audio and disables automatic reading. Keep real dispatcher and AED instructions audible.
- CPR rhythm aid is embedded in adult, child and infant guides; seizure stopwatch embedded in seizure actions; general event stopwatch in severe bleeding, possible stroke, severe allergy, heart attack and heatstroke. Relevant event-marker buttons are available after the instructions. Timers continue across screens; pacing stops on navigation. Starting audible pacing cancels narration; starting narration cancels audible pacing.
- All MP3 files are local and listed in the service-worker pre-cache manifest. Approx. 21 MB of additional audio. No runtime TTS service, microphone access or account. Actual phone playback, intelligibility, OS audio behavior and offline install still require testing.
- Default home screen prioritizes emergency selections before optional audio controls. Training Academy is next; artwork remains review-only. Independent clinical review is still required before using or distributing this for emergencies.


## v0.8.5 illustration expansion
- 14 new source-linked 1100 × 690 WebP concept and recognition graphics; 22 total. Separate editable SVG artwork included.
- Grouped gallery, descriptive alt text, scope and references per image; every asset remains pending independent clinical review.
- Detailed hands-on technique illustrations are still outstanding; the new pictograms do not show complete physical procedures.
- All 22 WebP files are in the updated service worker cache and readiness checks. All 139 audio assets and the Training Academy are unchanged.
- Next: v0.9 accessibility and panic-use testing, then real-device install and medical review. No publication yet.

## RC3 — call safety and offline help
RC2 CPR age profiles, sounds and breath cues retained. A compact 911 entry opens one deliberate confirmation dialog; no automatic dialing, no call prerequisite to open guides. Cancel or Escape returns to the same screen without clearing timers. Actual dialing stops competing narration and pacing, consistent with RC2. A separate no-connection panel offers alternatives; no connection is guaranteed. Minor injury menu opens six existing guides. Two new fictional call practice activities (three decisions) make 28 activities and 47 decisions. The new menus and call dialog are written-only; the 139 earlier audio clips are unchanged. Review version 1.0-rc3 has 319 items; all need review. No public emergency use before approvals.
