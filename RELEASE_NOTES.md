# Awakepilot 0.14.1

## Reliable updates

- Fixed installation getting stuck when the About and Updates sheet prevented the app from quitting. The sheet now closes before installation hands over to the updater.
- If quitting is cancelled, an actionable error appears after five seconds. The installer helper also stops waiting after 30 seconds instead of waiting indefinitely.
- Automatic checks now run every 24 hours while the app remains open, with a due check after wake. Failed automatic checks retry after an hour; manual checks remain available.
- Running jobs continue to block installation, including jobs started while an update is being prepared.

## Clearer controls and help

- Revised interface text in English, German, Spanish, French, Azerbaijani, and Turkish, including explanations of screen behavior, activity thresholds, automation matching, and time limits.
- Improved wrapping for longer settings descriptions.
- Updated the English, German, and Turkish website, support pages, and screenshots.

## Updating from 0.14.0 or earlier

This first update still uses the updater in your installed version. If **Installing update** remains visible for more than a minute, close **About and Updates**, then quit Awakepilot from the menu bar menu. The prepared update can then finish and relaunch the app. If it does not, install the official DMG included below. The installation fix takes effect once 0.14.1 is installed.

## Distribution

Universal application for Apple Silicon and Intel, signed with Developer ID and notarized by Apple. Requires macOS 13 or later. The ZIP is used by the in-app updater; the DMG provides drag-to-install setup. SHA-256 files are included for both versioned packages.
