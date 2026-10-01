<div align="center">
  <img src="docs/assets/icon.png" width="128" alt="Awakepilot app icon">
  <h1>Awakepilot</h1>
  <p><strong>Keep your Mac awake only while the work needs it.</strong></p>
  <p>A native macOS menu bar utility for precise wake sessions and explainable automation.</p>
</div>

<p align="center">
  <a href="https://github.com/ninjaBlume/awakepilot/releases/latest/download/Awakepilot.dmg"><strong>Download for macOS</strong></a>
  · <a href="https://ninjablume.github.io/awakepilot/">Website</a>
  · <a href="https://ninjablume.github.io/awakepilot/support.html">Support</a>
  · <a href="https://ninjablume.github.io/awakepilot/privacy.html">Privacy</a>
</p>

## Work-aware wake control

Awakepilot can keep the system awake indefinitely, for a duration, or until an
exact time. Its automation engine follows applications, terminal processes,
schedules, CPU load, network activity, Wi-Fi, VPNs, power state, attached
displays, and external drives. Normal macOS sleep behavior returns as soon as
the active work and safety conditions allow it.

<p align="center">
  <img src="docs/assets/dashboard-en.png" width="720" alt="Awakepilot dashboard with an active wake session and live system metrics">
</p>

## Highlights

- Manual and timed wake sessions with independent display-sleep control
- Ten automation signal types with any/all matching
- Reusable workflow profiles and condition-specific policies
- Live CPU, memory, download, and upload graphs
- Battery, UPS, thermal, and maximum-duration safeguards
- Drive Alive for explicitly selected writable external volumes
- URL scheme, Shortcuts-compatible commands, and `awakepilotctl`
- Local activity history and privacy-filtered diagnostic reports
- English, German, Spanish, and Turkish interfaces
- Signed updates with SHA-256, Developer ID, and Gatekeeper verification

## Installation

Awakepilot supports macOS 13 or later on Apple Silicon and Intel Macs.

1. Download the latest [signed and Apple-notarized DMG](https://github.com/ninjaBlume/awakepilot/releases/latest/download/Awakepilot.dmg).
2. Open the disk image.
3. Drag Awakepilot into **Applications**.
4. Launch Awakepilot and use the clock icon in the menu bar.

## Support and security

- [Installation and troubleshooting](https://ninjablume.github.io/awakepilot/support.html)
- [Privacy details](https://ninjablume.github.io/awakepilot/privacy.html)
- [Release history](https://github.com/ninjaBlume/awakepilot/releases)
- [Report a reproducible problem](https://github.com/ninjaBlume/awakepilot/issues/new/choose)

Review diagnostic files before attaching them to an issue. Never publish license
keys, payment details, private file paths, Wi-Fi names, or other confidential data.

## Repository scope

Awakepilot is proprietary software. This public repository contains the product
website, support material, issue templates, and signed release packages. Application
source code and private signing infrastructure are maintained separately.
