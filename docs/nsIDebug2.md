---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/base/nsIDebug2.idl">Source file</a>
</div>

# nsIDebug2 #

## Attributes ##

### isDebugBuild ###
<pre>  
Whether XPCOM was compiled with DEBUG defined.  This often  
correlates to whether other code (e.g., Firefox, XULRunner) was  
compiled with DEBUG defined.  
  
</pre>
### assertionCount ###
<pre>  
The number of assertions since process start.  
  
</pre>
### isDebuggerAttached ###
<pre>  
Whether a debugger is currently attached.  
Supports Windows + Mac  
  
</pre>