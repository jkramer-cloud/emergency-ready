# Private device acceptance test — v0.9.5

Run only with fictional scenarios, outside an emergency. Do not dial 911 for testing. Record device, OS, browser, date, release, result and issue. All physical-device checks are pending.

1. Serve the full directory at a private HTTPS URL (not a file share preview or public student site). Confirm emergency home opens immediately and setup is collapsed. Confirm the URL's scope and manifest ID are unchanged across releases.
2. On iPhone/iPad use Safari → Share → Add to Home Screen → Open as Web App if offered → Add. On Android use Chrome menu or Install app if available. Open the icon while connected; the setup screen should report app-window mode if exposed by the OS. Inspect icons, safe areas, navigation and 911 link without activating it.
3. Wait for all 167 runtime files to be reported present. Close the app, turn off Wi-Fi and cellular data, then open from the icon. Check the home screen, an adult CPR guide, simulated audio read/repeat/stop, several library guides, an image in the review gallery, a training scenario, and kit inventory. No real call. Reconnect after testing. Record any failure.
4. Confirm airplane-mode launch after device restart and storage-pressure behavior where safe. Verify the status never reports all files present if the worker is missing, incomplete or a different version. Browser storage is not guaranteed; keep established references available.
5. Validate update behavior with a separate test release, new version and regenerated hashes. Keep a fictional guided response open while downloading the next version. Verify it is not interrupted or reloaded. Check the waiting notice. When safe, close every app tab/window; reopen and confirm new version and full offline check. Repeat with an intentionally incomplete deployment on test infrastructure; the old cached release should remain usable. No real emergency use.
6. Check VoiceOver/TalkBack, large text, contrast, 320px narrow screens, landscape, audio interruptions, and timing controls. Test screen-reader clarity and safe return from training. Verify backups before changing installs.
7. Independently review medical text and narration, and any proposed emergency illustrations. Conduct approved supervised usability drills with fictional situations. This prototype is not a certified first-aid course or medically approved app.

RC3: verify compression tones and breath tones at safe media volumes on each actual test device, including silent mode, interruptions and 911 link cancellation (no real test calls). Compare timing with an independent timer. Verify accessibility and use only a training mannequin in supervised scenarios.

## RC3 call UI (mock only; do not dial 911 for testing)
Open confirmation, cancel, escape/back, choose no-connection help, return while timing a fictional event. Check dialog size, screen-reader focus, and absence of call controls in training. Never tap the final live telephone link during testing; inspect its destination or use a test harness that blocks it.
