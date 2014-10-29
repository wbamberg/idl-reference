---
layout: default
---

# nsIShellService #

## switchTask ##

This method displays a UI to switch to (or launch) a different task


## createShortcut ##

This method creates a shortcut on a desktop or homescreen that opens in
the our application.

@param aTitle     the user-friendly name of the shortcut.
@param aURI       the URI to open.
@param aIconData  a base64-encoded data: URI representation of the shortcut's icon, as accepted by the favicon decoder.
@param aIntent    obsolete and ignored, but remains for backward compatibility; pass an empty string

