## RC7 addendum

See `review-package/RC7-HANDOFF-REVIEW.md` for required new reviewer and physical-device checks. All clinical, device and actual-use approval gates remain pending.

# RC6 addendum — opt-in emergency incident audio

Private release candidate. No medical or district authorization yet. Separate **Start pacing + record incident** action explicitly opts in; ordinary Start never requests microphone access. Pacing starts immediately, independent of permission. Once the mic actually starts, an English or Spanish offline announcement plays once and a visible recording indicator, timer and spoken-notice text appear. The participating helper should announce the recording aloud; the device may not capture its own loudspeaker and this feature is not proof of legal consent. Audio records in the foreground for the selected CPR session until Stop recording, Stop pacing, navigation, hidden tab, intentional telephone dialing, capture interruption or the 60-minute / approximately 64 MiB ceiling (final chunk may exceed limit). Opening/canceling the call confirmation does not stop pacing or an established recording. Automatic log entries reflect recorder/tool activity, not clinical actions. No recording or playback in Training Academy. Questions and recorded-audio playback remain disabled during pacing; manual event entries remain available. The bilingual notice is the sole additional announcement. No call recording, cloud upload, transcription, accounts or background capture. One incident recording stays in tab memory, with explicit local Save audio file, Listen and Delete options. Saved files remain on the device even after in-app Delete; use authorized handling/retention only. A refresh, close, crash or operating-system suspension can lose unsaved audio. If microphone permission fails or is canceled, first aid and pacing continue uninterrupted when the tab remains visible. Do not delay emergency care, and do not use real student data in prototype testing.

Washington RCW 9.73.030(2)(a) permits emergency-nature conversations with consent of one party. Subsection (3) addresses effective announcements where all-party consent is required. This is not a blanket waiver of student privacy, device policy, disclosure or records-retention rules. Obtain district guidance and review prior to real deployment: https://app.leg.wa.gov/RCW/default.aspx?cite=9.73.030. Browser APIs: https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia and https://developer.mozilla.org/en-US/docs/Web/API/MediaRecorder.

# RC5 addendum — helper station and audio notes

Private release candidate only. RC4 features retained. Review the CPR-adjacent manual timeline, automatic pacing-tool start/stop stamps (not clinical actions), question prompts, audio files and bilingual strings. Optional microphone recordings are limited to fictional supervised practice, require explicit permission, stay in tab memory, and are disabled during pacing. No upload, persistent storage, transcription, or recording of calls. Test microphone permission denial, actual device audio routing, deletion, backgrounding, call confirmation, school privacy approval and bilingual clinical review before adoption. Washington RCW 9.73.030 generally requires consent for private conversations, with specific exceptions: https://app.leg.wa.gov/RCW/default.aspx?cite=9.73.030. Browser microphone permission/secure context: https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia.

# Supervised usability test plan — fictional drills only

Do not use the prototype for actual emergencies or teach unapproved techniques. Obtain school approval; use adult staff first, then supervised volunteers only after appropriate review. Do not induce panic, recreate injuries, or make any real emergency calls. Use training mode or a test harness with all telephone links intercepted by an adult. No identifiable student data should be recorded.

## Test devices and settings
- Android Chrome, iPhone Safari, Chromebook keyboard-only, and screen readers (TalkBack, VoiceOver, ChromeVox).
- Portrait and landscape, narrow 320px-equivalent viewport, 200% zoom and operating-system large text.
- Standard and high-contrast modes, muted audio, and interruptions. Private offline tests after installing and verifying the cache.

## Fictional tasks
1. From the home screen, find emergency-call access without actually activating the dialer. Locate the “I don't know what to do” path.
2. Select the correct response category for a fictional collapse and find the appropriate age-specific guide. Do not perform physical care on a person.
3. Locate choking, severe bleeding, seizure, and breathing difficulty pathways from home. Find the first action without dismissing a modal or navigating through unrelated material.
4. Locate Read aloud and Stop audio; check that instruction text remains visible when audio is silent or interrupted.
5. Go home accidentally, resume the same guide, then return home and choose a different guide; confirm the stale shortcut is gone.
6. In a simulated test, find the seizure timer, switch screens, then return. Check elapsed time and the five-minute warning without making a real call.
7. Enter and exit the academy; ensure no live call button is visible in training. Confirm a real emergency exit remains easy to find.

## Observations (anonymous aggregate only)
Record time to locate the appropriate screen, number of incorrect taps, requests for assistance, readability, audio intelligibility, and whether keyboard/screen-reader focus is visible. Ask which words were unclear. No names, medical history, or individual medical data.

Suggested targets for evaluation (not verified performance claims): locate 911 access immediately; find a primary emergency category in one tap; locate the first instruction without adjusting settings or opening an unrelated section. Investigate hesitation, errors and any safety-critical failures before further release. Do not score speed over correct safe decisions.

Clinical review, accessibility review and real-device validation are release gates. This is a usability protocol, not first-aid certification.

## RC3 additional fictional drills
Find minor care without opening a call. Open and cancel the call confirmation without losing a guided response or timer. Find no-connection assistance. Practice accidental-call instructions in Training Academy. Never actually initiate a 911 call during a drill. Measure time to locate urgent action and the call entry; check reassurance does not deter good-faith requests.
