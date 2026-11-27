# Awakepilot 0.16.2

This maintenance release improves the reliability of macOS packaging and signing.

App bundles are packaged outside synced folders to prevent Finder and file-provider metadata from disrupting code-signature verification.

Closed-lid sessions now explicitly put the built-in display to sleep when no external display is connected, while keeping the Mac awake.
