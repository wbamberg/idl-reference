---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/js/ductwork/debugger/IJSDebugger.idl">Source file</a>
</div>

# IJSDebugger #
  
Do not use this interface. Instead, write:  
    Components.utils.import("resource://gre/modules/jsdebugger.jsm");  
    addDebuggerToGlobal(global);  
  

## Methods ##

### addClass(global) ###
  
Define the global Debugger constructor on a given global.  
  
