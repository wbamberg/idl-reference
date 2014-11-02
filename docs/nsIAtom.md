---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/ds/nsIAtom.idl">Source file</a>
</div>

# nsIAtom #

## Methods ##

### toString() ###
  
Get the Unicode or UTF8 value for the string  
  

### toUTF8String() ###

### equals(aString) ###
  
Compare the atom to a specific string value  
Note that this will NEVER return/throw an error condition.  
  

### equalsUTF8(aString) ###

### isStaticAtom() ###
  
Returns true if the atom is static and false otherwise.  
  
