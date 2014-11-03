---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/xslt/nsIXSLTProcessorPrivate.idl">Source file</a>
</div>

# nsIXSLTProcessorPrivate #

## Attributes ##

### flags ###
<pre>  
Flags for this processor. Defaults to 0. See individual flags above  
for documentation for effect of reset()  
  
</pre>
## Constants ##

### DISABLE_ALL_LOADS ###
<pre>  
Disables all loading of external documents, such as from  
<xsl:import> and document()  
Defaults to off and is *not* reset by calls to reset()  
  
</pre>