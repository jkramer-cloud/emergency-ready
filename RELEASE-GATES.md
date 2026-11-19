## RC7 addendum

See `review-package/RC7-HANDOFF-REVIEW.md` for required new reviewer and physical-device checks. All clinical, device and actual-use approval gates remain pending.

# RC6 addendum — opt-in emergency incident audio

Private release candidate. No medical or district authorization yet. Separate **Start pacing + record incident** action explicitly opts in; ordinary Start never requests microphone access. Pacing starts immediately, independent of permission. Once the mic actually starts, an English or Spanish offline announcement plays once and a visible recording indicator, timer and spoken-notice text appear. The participating helper should announce the recording aloud; the device may not capture its own loudspeaker and this feature is not proof of legal consent. Audio records in the foreground for the selected CPR session until Stop recording, Stop pacing, navigation, hidden tab, intentional telephone dialing, capture interruption or the 60-minute / approximately 64 MiB ceiling (final chunk may exceed limit). Opening/canceling the call confirmation does not stop pacing or an established recording. Automatic log entries reflect recorder/tool activity, not clinical actions. No recording or playback in Training Academy. Questions and recorded-audio playback remain disabled during pacing; manual event entries remain available. The bilingual notice is the sole additional announcement. No call recording, cloud upload, transcription, accounts or background capture. One incident recording stays in tab memory, with explicit local Save audio file, Listen and Delete options. Saved files remain on the device even after in-app Delete; use authorized handling/retention only. A refresh, close, crash or operating-system suspension can lose unsaved audio. If microphone permission fails or is canceled, first aid and pacing continue uninterrupted when the tab remains visible. Do not delay emergency care, and do not use real student data in prototype testing.

Washington RCW 9.73.030(2)(a) permits emergency-nature conversations with consent of one party. Subsection (3) addresses effective announcements where all-party consent is required. This is not a blanket waiver of student privacy, device policy, disclosure or records-retention rules. Obtain district guidance and review prior to real deployment: https://app.leg.wa.gov/RCW/default.aspx?cite=9.73.030. Browser APIs: https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia and https://developer.mozilla.org/en-US/docs/Web/API/MediaRecorder.

# RC5 addendum — helper station and audio notes

Private release candidate only. RC4 features retained. Review the CPR-adjacent manual timeline, automatic pacing-tool start/stop stamps (not clinical actions), question prompts, audio files and bilingual strings. Optional microphone recordings are limited to fictional supervised practice, require explicit permission, stay in tab memory, and are disabled during pacing. No upload, persistent storage, transcription, or recording of calls. Test microphone permission denial, actual device audio routing, deletion, backgrounding, call confirmation, school privacy approval and bilingual clinical review before adoption. Washington RCW 9.73.030 generally requires consent for private conversations, with specific exceptions: https://app.leg.wa.gov/RCW/default.aspx?cite=9.73.030. Browser microphone permission/secure context: https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia.

# Release gates — RC3

All gates below are pending; automated checks are not clinical approval.

- [ ] Qualified clinical review of all reference, guided, audio, tool and practice content; documented resolution of safety findings.
- [ ] Independent approval and tested integration of any visual medical procedures used in emergency mode. Drafts remain excluded.
- [ ] Physical iPhone, Android and Chromebook installation, offline restart, audio, update, storage and telephone-link acceptance (no live test calls).
- [ ] Screen-reader, accessibility and supervised fictional usability testing, including school approval and age-appropriate procedures.
- [ ] Regression tests on exact approved build; re-check runtime digests.
- [ ] Named approving authority, approval date and version/digest recorded; school/district permission for intended use; published limitations and maintenance owner.

No public GitHub or Learning Hub deployment until approvals are documented. The app is not a certified course or substitute for established resources.


## RC4 update — pending review
- Large visible CPR method and rate buttons; default 100/min, unchanged accepted 100–120/min. Five-second breath cue with staged one-second breaths, immediate early resume, and elapsed session timer. Timing is approximate; do not delay care.
- English/Español switch persists locally; Spanish draft written instructions for all 39 card records and 7 chooser paths. English voice, training, inventory and some source/review material remain English; English narration disabled in Spanish. Bilingual medical review is required, including all entries in SPANISH-REVIEW.json.
- Reference: https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support and https://www.redcross.org/take-a-class/cpr/performing-cpr/cpr-steps. Short interruption; each breath about one second. Five seconds is UI design, not a prescribed clinical duration.
