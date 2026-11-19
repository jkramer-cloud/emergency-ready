# RC4 review addendum — required before any approval

The workstation below is the RC3 baseline. Its CPR timing/method UI review entries refer to the previous build and must not be used as RC4 sign-off. Review the actual RC4 pacing screen, five-second cue (one-second breaths, early resume, elapsed session time), and all Spanish draft strings in `../SPANISH-REVIEW.json`. Require a bilingual clinical reviewer and device/usability acceptance. English voice, practice, and kit interfaces remain English.

# RC3 independent review package

**Not approved for emergency use.** Open `review.html` after extracting the entire project. The workstation is separate from the emergency application. Filter, inspect, record decisions and export a review JSON file before closing. Review data stays in the open page; no account or network is needed for review itself. Source links require internet. Keep separate exports for each qualified reviewer and reconcile decisions manually.

The register has 319 entries, including 39 full text/checklist records, seven guided pathways, 139 audio clips, 22 illustration drafts, 11 planned artwork slots, 38 original quiz questions, 47 academy decisions, seven kit templates and nine cross-cutting review gates. The wording is extracted from the actual application and accompanying registers; source references are not approvals. Pathway source coverage and narration correspondence must be checked by the reviewer.

1. Clinical reviewer: validate all guides, thresholds, priority, sequence, age-specific guidance, narration, quizzes and tools against current guidance and local protocols.
2. Illustration reviewer: examine every image; do not move art into emergency mode until separately approved and integrated into a tested release.
3. Device/accessibility reviewers: use DEVICE-INSTALL-TEST.md and PANIC-USE-TEST-PLAN.md in the parent folder.
4. School/district: confirm appropriate use and approval for supervised student testing; never use real student/patient data.
5. Resolve all blocking findings, regenerate assets and hashes after changes, re-test and obtain written authorization for a specific release. The workstation does not grant release approval.

Record date, reviewer qualifications, findings, remediation and re-test evidence. All decisions initially pending.

RC2 added a dedicated CPR pacing and breath-cue review record, retained in RC3. RC3 also adds call-confirmation, no-connection and minor-injury review items plus three call-training decisions. Clinical reviewers should test it with fictional, supervised scenarios and verify the timing and age-specific defaults. Prior RC1 and RC2 review exports are version-specific; do not assume their decisions approve RC3.
