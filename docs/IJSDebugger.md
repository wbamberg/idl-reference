---
layout: default
---

# IJSDebugger #

Do not use this interface. Instead, write:
    Components.utils.import("resource://gre/modules/jsdebugger.jsm");
    addDebuggerToGlobal(global);


## Methods ##

### addClass ###

Define the global Debugger constructor on a given global.

