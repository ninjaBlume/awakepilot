# Awakepilot 0.15.1

## Optional closed-lid sessions for MacBook

Keep an active session working with the lid closed, including without an external
display. The built-in display turns off when the lid closes. This setting is separate
from **Keep display on** and is off by default.

Install Awakepilot in Applications, enable **Keep working with the lid closed**, and
approve its bundled helper in System Settings. Wait until the mode is active before
closing the lid. Enabling it preserves the current session and its deadline.

## Sleep restoration and power protection

The helper uses a renewable, bounded authorization and restores normal sleep when
the session stops, protection pauses it, or the authorization expires. Recovery
records allow restoration after a helper restart. Existing sleep overrides are left
unchanged. Battery rules and independent critical-temperature protection still apply.

While this mode is active, manual Sleep is also blocked. Stop the session before
putting your Mac to sleep or transporting it.

## Distribution and languages

The controls and status messages support all ten app languages. Apple Silicon and
Intel packages are signed with Developer ID and notarized by Apple. Automated policy,
lifecycle, menu, localization, and update-package checks passed. Physical MacBook
validation of helper approval, lid transitions, and work continuity is still pending.
