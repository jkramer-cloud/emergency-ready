# Release gate — independent review required

This is a development prototype, not an approved emergency reference. Do not release it as a real-world emergency tool until appropriately qualified clinical and accessibility reviewers approve the content and device behavior. For actual emergencies call 911 and follow the dispatcher; use established, medically reviewed resources and certified training.

## Content review
- [ ] Verify each guide against the cited current guidance and applicable local protocols.
- [ ] Verify all adult, child and infant CPR steps, single-rescuer activation timing, pediatric AED placement and age definitions.
- [ ] Verify choking and drowning protocols against 2025 guidance and current training programs.
- [ ] Verify medication guidance, contraindications, seizure escalation and pediatric diabetes action plans.
- [ ] Review symptoms, emergency thresholds, recovery positioning and instructions not to delay emergency care.
- [ ] Confirm all practice answers and explanations match approved guide wording.
- [ ] Record reviewer, professional qualifications, review date, required changes and retest status; never imply approval merely from citing sources.

## Device and usability review
- [ ] Test install and first load on Android, iOS and school Chromebooks where permitted.
- [ ] Test offline restart in airplane mode, interrupted installation, storage eviction and upgrade from v0.1.
- [ ] Confirm calls require a working phone service and don't accidentally dial during learning-mode testing.
- [ ] Test high zoom, screen readers, touch targets, contrast, keyboard navigation and print layouts.
- [ ] Confirm safety notices are visible and the app does not appear to diagnose conditions or replace dispatchers.
- [ ] Obtain school approval before student-facing use; follow school emergency response plans.

## v0.3 injury review additions
- [ ] Verify burn cooling times and escalation, chemical-specific exceptions and electrical injury scene safety.
- [ ] Verify injury escalation, eye irrigation vs penetrating trauma, tetanus referral, embedded object management and dental reimplantation/aspiration precautions.
- [ ] Verify concussion danger signs, school referral and sports return rules; verify spinal motion precautions and airway priority.
- [ ] Review new quiz wording and all printouts; verify upgrade from v0.2 to v0.3.

## v0.4 environmental review additions
- [ ] Verify heatstroke cooling safety, airway protection, pediatric considerations, and transition from heat exhaustion.
- [ ] Verify hypothermia severity, gentle handling, CPR guidance and frostbite thaw/refreeze precautions.
- [ ] Verify dehydration escalation, fluid advice and pediatric considerations.
- [ ] Verify U.S. snakebite guidance, stinger removal, anaphylaxis linkage and tick follow-up.
- [ ] Verify lightning scene safety, resuscitation, altitude illness descent and rescue guidance.
- [ ] Confirm all ten questions match reviewed guidance; validate outdoors filter and v0.3 to v0.4 cache upgrade on real devices.


## v0.5 illustration review additions
- Confirm CPR hand/finger placement visuals align with approved guidance.
- Confirm AED pad placement visuals and prompts.
- Confirm choking and infant choking sequences.
- Confirm direct pressure/tourniquet emphasis and splinting precautions.
- Confirm environmental response diagrams (heatstroke and hypothermia).

## v0.6 tools review additions
- [ ] Verify CPR pacing rate, accuracy of visual/audio cues, and stop behavior; verify users understand it is not a compression quality monitor or a ventilation cue.
- [ ] Verify seizure warning threshold and escalation conditions, including unknown onset and post-seizure warning.
- [ ] Test multiple concurrent timers, clock adjustments, sleep/wake, backgrounding, lost tab and accessibility of warnings.
- [ ] Test speakerphone interference, volume, audio permissions and hardware audio cadence; do not use pacing to replace the dispatcher.
- [ ] Verify timeline labels and handoff guidance; no identifying fields or persistent records.
- [ ] Replace or independently review all removed and remaining draft illustrations before restoring to emergency guide screens.

## v0.7 preparedness review
- Confirm starter items are appropriate for intended settings and distinguish example counts from regulatory minima; school nurse/district and venue review required.
- Confirm stock/target and date-alert language does not imply medical readiness. Verify manufacturer storage, expiry and inspection rules.
- Test actual browser-local storage across reloads and private browsing, backup restoration on a second device, unavailable/full storage, printed inventory, and no transfer of incident data. No patient/student data in kit names or items.
- No automatic reminder when closed. Verify accessible date fields, alerts and keyboard navigation on devices.

## v0.7.1 artwork checkpoint
- [ ] Review every draft in `illustration-review/REVIEW-STATUS.md`; no approval assumed.
- [ ] Confirm all pending technique assets and age-specific depictions before promotion.
- [ ] Keep review-only art isolated from emergency and learning modes until approved.
- [ ] Confirm all WebP assets decode and are cached for offline review.


## v0.8 guided-response release gates
- Independent clinician: verify wording, routing, safety, age distinctions, escalation, grouping, AED eligibility, action order, contraindications, CPR/choking/bleeding changes and every inherited guide. Verify user never interprets action completion as permission to stop care.
- Supervised simulated usability testing with students (no real calls, no practicing physical techniques on other students); assess recognition, reading comprehension, mis-taps, reaching 911, adult help, task completion without guidance, and recovery from wrong choices.
- Screen reader/keyboard and reduced motion, large-text and phone portrait/landscape; verify persistent call and escape/home access. Test in poor connectivity, standalone installation, cache update and reload, interruption by actual phone interface (use safe test numbers only).
- Verify draft artwork remains isolated, timer continuity and safe notification wording; independent clinical review before enabling public emergency use.


## v0.8.1 narration and inline tools
- Review all `AUDIO-REGISTER.json` transcripts and their corresponding actual recordings against the displayed guide and current clinical sources. Verify pronunciation of acronyms, measurements, ranges, drug names, phone numbers, and distinction between instructions for age groups.
- Test audio intelligibility in realistic noise conditions and on actual phones; test cancellation, replay, phone call interaction, accessibility and cached playback without internet. Confirm no competition with dispatcher or AED prompts.
- Validate timer thresholds, manual event labels, timing under screen sleep, and rhythm aid accuracy. Verify audio and graphical controls never obscure urgent written actions. Assess supervised youth usability without real emergency calls.
- No prompt, visual or timing aid is clinically approved. Do not deploy for real emergency reliance until reviewed.


## v0.8.2 Academy review
- Independently review each of the 47 decisions, explanations and source mappings (TRAINING-BANK.json).
- Test with supervised learners using fictional scenes and training equipment only.
- Confirm simulated actions never trigger phone calls or real treatment instructions via audio or tools; test return to real emergency screen.
- Verify language, developmental appropriateness, assistive technology, storage persistence and shared-device reset.
- Milestones are not clinical competency or certification.


## v0.8.5 visual review gate
- [ ] Review all 22 exact WebP asset versions using ASSET-REGISTER.json and REVIEW-STATUS.md; reviewer, clinical source edition, date, decision and revision recorded.
- [ ] Replace or supplement concept-only cards with qualified, accurate physical demonstrations where required; verify permission for any externally sourced artwork.
- [ ] Confirm pictograms cannot be mistaken for actual anatomy, hand placement, dosing or complete procedures.
- [ ] Test comprehension under simulated stress, narrow screens, and accessibility; do not enable any drawing in emergency/practice until approved.


## v0.9 accessibility and panic-use gate
- [ ] Independent clinical review of guides, alerts, audio and graphics.
- [ ] Staff-led fictional drills per PANIC-USE-TEST-PLAN.md; no actual emergency calls.
- [ ] TalkBack, VoiceOver and ChromeVox, real phone zoom and audio interference tests.
- [ ] Install and offline reload after verifying cache; app update migration and device storage retention.
- [ ] Resolve observed safety-critical usability issues before public use.


## v0.9.5 release gates (pending)
- [ ] Complete DEVICE-INSTALL-TEST.md on actual iOS Safari and Android Chrome, including offline launch/audio and an update while a fictional response is open.
- [ ] Validate actual device accessibility and supervised fictional scenarios.
- [ ] Obtain qualified medical review of all written/spoken guidance and any images before public use. Draft imagery stays review-only until approved.

## RC3 CPR pacing review
- [ ] Validate age definitions and depth reminders, 30:2 and continuous compression modes, and the pediatric 15:2 limitation.
- [ ] Confirm that the 3.5-second automatic cue window does not encourage delay or prolonged interruption; evaluate early resume/restart and actual-device sound intelligibility.
- [ ] Test dispatcher/AED priority, classroom noise, muted devices, audio interruption, navigation and screen sleep. Use training mannequins only under supervision.

## RC3 review additions
- [ ] Call dialog wording, good-faith reassurance, Washington false report and response-cost warning, school policy, accidental-call instruction.
- [ ] Offline communication alternatives, text-to-911 limitations, no guarantee of connectivity.
- [ ] Minor-injury choices and escalation; no delays in life-threatening pathways.
- [ ] Confirm dialing only after deliberate click; no real telephone calls in drills.
- [ ] Verify CPR and response continuity on cancel, including keyboard and device back; check actual call interruption behavior only with a mock test.
- [ ] Review two new call practice scenarios.


## RC4 update — pending review
- Large visible CPR method and rate buttons; default 100/min, unchanged accepted 100–120/min. Five-second breath cue with staged one-second breaths, immediate early resume, and elapsed session timer. Timing is approximate; do not delay care.
- English/Español switch persists locally; Spanish draft written instructions for all 39 card records and 7 chooser paths. English voice, training, inventory and some source/review material remain English; English narration disabled in Spanish. Bilingual medical review is required, including all entries in SPANISH-REVIEW.json.
- Reference: https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support and https://www.redcross.org/take-a-class/cpr/performing-cpr/cpr-steps. Short interruption; each breath about one second. Five seconds is UI design, not a prescribed clinical duration.
