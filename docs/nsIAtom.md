---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/ds/nsIAtom.idl">Source file</a>
</div>

# nsIAtom #

## Methods ##

### toString() ###
<code>  
Get the Unicode or UTF8 value for the string  
  
</code>
### toUTF8String() ###

### equals(aString) ###
<code>  
Compare the atom to a specific string value  
Note that this will NEVER return/throw an error condition.  
  
</code>
### equalsUTF8(aString) ###

### isStaticAtom() ###
<code>  
Returns true if the atom is static and false otherwise.  
  
</code>