# Awakepilot 0.15.3

## Closed-lid recovery after updating the app

Fixes closed-lid mode becoming unavailable after an application update leaves the
previous helper running from a removed bundle. Awakepilot now waits for the
approved helper to stop, registers its current executable, and verifies its
connection before confirming the mode.

Helper registration retries are bounded. An interrupted replacement is resumed
on the next launch, and reinstalling the same build can repair a stale connection.
A normal relaunch keeps a confirmed helper running. New installations and revoked
approval continue to require the normal macOS authorization.

Recovery diagnostics record operation names and error codes without personal
session or job details. Closed-lid recovery and power protection from 0.15.2 remain
included.

MacBook Air M5 checks verified replacement through the production installer,
same-build reinstallation, normal relaunch, and sleep restoration. The dashboard
was confirmed active. Battery/adapter transitions and Intel runtime checks remain
pending.
