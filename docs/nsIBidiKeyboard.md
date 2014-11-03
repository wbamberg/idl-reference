---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsIBidiKeyboard.idl">Source file</a>
</div>

# nsIBidiKeyboard #

## Methods ##

### reset() ###
<pre>  
Inspects the installed keyboards and resets the bidi keyboard state  
  
</pre>
### isLangRTL() ###
<pre>  
Determines if the current keyboard language is right-to-left  
@throws NS_ERROR_FAILURE if no right-to-left keyboards are installed  
  
</pre>
## Attributes ##

### haveBidiKeyboards ###
<pre>  
Determines whether the system has at least one keyboard of each direction  
installed.  
  
@throws NS_ERROR_NOT_IMPLEMENTED if the widget layer does not provide this  
information.  
  
</pre>