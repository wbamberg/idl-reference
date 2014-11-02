---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/base/nsIMacUtils.idl">Source file</a>
</div>
# nsIMacUtils #
  
nsIMacUtils: Generic globally-available Mac-specific utilities.  
  

## Attributes ##

### isUniversalBinary ###
  
True when the main executable is a fat file supporting at least  
ppc and x86 (universal binary).  
  

### architecturesInBinary ###
  
Returns a string containing a list of architectures delimited  
by "-". Architecture sets are always in the same order:  
ppc > i386 > ppc64 > x86_64 > (future additions)  
  

### isTranslated ###
  
True when running under binary translation (Rosetta).  
  
