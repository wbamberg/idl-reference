---
layout: default
---

# nsIDebug2 #

## Attributes ##

### isDebugBuild ###

Whether XPCOM was compiled with DEBUG defined.  This often
correlates to whether other code (e.g., Firefox, XULRunner) was
compiled with DEBUG defined.


### assertionCount ###

The number of assertions since process start.


### isDebuggerAttached ###

Whether a debugger is currently attached.
Supports Windows + Mac

