# Awakepilot 0.14.0

Awakepilot 0.14.0 extends work-aware automation to connected hardware, audio routes,
and the active network configuration.

## Highlights

- Start automation when a selected USB device is connected.
- Follow selected paired Bluetooth devices as they connect and disconnect.
- Keep a session active while a selected macOS audio output is the current route.
- Match selected DNS server addresses from the active resolver configuration.
- Match exact IPv4 or IPv6 addresses and CIDR networks.
- Assign an independent session profile, display policy, and maximum duration to each
  new condition type.
- Save the new hardware and network-context rules inside reusable workflow profiles.
- Add complete English, German, Spanish, French, Azerbaijani, and Turkish interface coverage.
- Open the disk image with large drag-to-install icons, a directional arrow, and a Retina background.

## Privacy and permissions

USB and audio-output detection use local macOS system APIs. Bluetooth rules inspect only
connected paired-device identity and require the standard macOS Bluetooth permission.
Device names, DNS server addresses, and IP rules remain in the current macOS user account.
Diagnostic reports include only rule counts and enabled states; they exclude configured
device names, DNS servers, IP rules, and activity history.
