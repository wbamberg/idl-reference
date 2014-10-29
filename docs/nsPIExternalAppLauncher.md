---
layout: default
---

# nsPIExternalAppLauncher #

This is a private interface shared between external app handlers and the platform specific
external helper app service


## Methods ##

### deleteTemporaryFileOnExit ###

mscott --> eventually I should move this into a new service so other
consumers can add temporary files they want deleted on exit.
@param aTemporaryFile A temporary file we should delete on exit.


### deleteTemporaryPrivateFileWhenPossible ###

Delete a temporary file created inside private browsing mode when
the private browsing mode has ended.

