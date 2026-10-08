# Awakepilot 0.14.3

## Responsive VPN detection

- VPN checks run in the background with cached results, a two-second timeout, and bounded output. A stalled VPN query no longer blocks the interface.
- Detection continues to support third-party VPN services registered with macOS.

## Easier automation setup

- Added five ready-made templates for video encoding, builds, file transfers, downloads, and presentations, with two- or four-hour limits.
- Saving a template leaves current rules and sessions unchanged. Apply a saved profile to activate its configuration.
- Automation settings now use separate sections, with expandable USB, Bluetooth, audio, DNS, and IP controls.

## Portable workflow profiles

- Export and import complete automation profiles as versioned JSON files.
- Imports preserve existing profiles, active rules, and running sessions. Conflicting names are renamed, and invalid files are rejected before changes are applied.
- Exported files may include configured device and network names. Review imported Drive Alive settings before applying a profile.

## Language-aware links

- Home, support, pricing, and release-note links follow all ten interface languages, including regional language preferences.

## Updating from 0.14.0 or earlier

If **Installing update** remains visible for more than a minute, close **About and Updates**, then quit Awakepilot from its menu bar menu. The prepared update can then finish and relaunch the app. If it does not, install the latest official DMG. Versions 0.14.1 and later include the installation fix.

## Distribution

Universal application for Apple Silicon and Intel, signed with Developer ID and notarized by Apple. Requires macOS 13 or later. The ZIP is used by the in-app updater; the DMG provides drag-to-install setup. SHA-256 files are included for both versioned packages.
