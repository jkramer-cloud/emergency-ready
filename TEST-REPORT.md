# v1.0 RC1 — software verification

This is a private, unapproved release candidate. Software checks do not validate clinical correctness or physical-device behavior.

## Passed
- Reproducible injected Chromium test (`software-tests/rc-browser.py`): 828 guided-screen configurations (138 states × three widths × two display settings); visible 911 link, headings, no horizontal overflow, no images in emergency guide screens. Exact guide step grouping retains all original written steps.
- Training entry confirmation: cancel preserves active guide; accept switches to isolated practice with no live call control. All 44 academy decisions tested with correct answers and completion. Return to emergency, library search, kit creation, tools and info navigation tested.
- Reviewer workstation: 313 unique records; guide filtering, ID search, review status and notes, exported JSON and restore; no uncaught page errors in browser checks. Media file paths exist; real playback/visual interpretation in this workstation not tested.
- Node syntax validation for both HTML scripts and service worker. Node VM mocked service worker test passed: corrupted download rollback, successful verified 167-file installation, deferred activation, scope cleanup, offline cached navigation, ranged audio and missing-file repair.
- All 167 runtime file hashes match. All v0.9.5 files retained, and all existing asset bytes unchanged (139 MP3s, 22 WebPs and four icons). No medical text, audio or training-answer changes made in RC1.
- Preview images use injected HTML, not an actual installed phone or hosted worker. The browser test directly initializes guide states and academy activities; this is not a human panic simulation.

## Outstanding / release blocking
Clinical review of all content, narration intelligibility, full technique illustrations and review findings; actual iPhone, Android and Chromebook installation and offline reopen; OS storage persistence, audio, phone handoff, real service-worker update lifecycle; real assistive technology and supervised student usability; school/district authorization. No live 911 tests. No claim of complete WCAG compliance, comprehensive functional regression, or medical approval. See RELEASE-GATES.md, DEVICE-INSTALL-TEST.md, PANIC-USE-TEST-PLAN.md and review-package/START-HERE.md. Prior build details remain in README and earlier packages.
