# Awakepilot 0.15.2

## Closed-lid recovery

Fixes closed-lid mode failing to recover after its helper restarts. The dashboard
now keeps a stable recovery message during retries and only shows the authorization
button when the helper needs installation or approval.

On a MacBook Air M5, the corrected helper restarted successfully and the dashboard
returned to active mode. Switching closed-lid mode off restored normal sleep;
switching it on reacquired the override while preserving the active unlimited
session's start time. Earlier operator checks reported working closed-lid sessions
with and without an external display. Battery/adapter transitions, timed-session
and lid-transition preservation, full crash recovery, and Intel runtime checks
remain open.

Install the update in Applications and wait for **Closed-lid mode is active** before
closing the lid. If the old helper is still running after the update, restart your
Mac to load the corrected helper.
