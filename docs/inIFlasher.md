---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/layout/inspector/inIFlasher.idl">Source file</a>
</div>

# inIFlasher #
<pre>  
This class will be removed in gecko v33. See comments below for alternatives.  
  
@status DEPRECATED - see comments below.  
  
</pre>
## Methods ##

### drawElementOutline(aElement) ###
<pre>  
This function now does nothing at all. Use the :-moz-devtools-highlighted  
pseudo-class instead. For example, see the "HIGHLIGHTED_PSEUDO_CLASS" and  
"INVERT" lines in:  
https://hg.mozilla.org/dom-inspector/file/tip/resources/content/Flasher.js  
  
@status DEPRECATED  
  
</pre>
### repaintElement(aElement) ###
<pre>  
This function now does nothing at all.  
  
@status DEPRECATED  
  
</pre>
### scrollElementIntoView(aElement) ###
<pre>  
As of gecko v33 you should use inIDOMUtils::scrollElementIntoView instead  
of this function.  
  
@status DEPRECATED  
  
</pre>
## Attributes ##

### color ###

### invert ###

### thickness ###
