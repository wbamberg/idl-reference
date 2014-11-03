---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/js/ductwork/debugger/IJSDebugger.idl">Source file</a>
</div>

# IJSDebugger #
<pre>  
Do not use this interface. Instead, write:  
    Components.utils.import("resource://gre/modules/jsdebugger.jsm");  
    addDebuggerToGlobal(global);  
  
</pre>
## Methods ##

### addClass(global) ###
<pre>  
Define the global Debugger constructor on a given global.  
  
</pre>