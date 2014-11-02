---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/base/nsICompositionStringSynthesizer.idl">Source file</a>
</div>
# nsICompositionStringSynthesizer #
  
Stores composition clauses information and caret information for synthesizing  
composition string.  
  

## Methods ##

### setString(aString) ###
  
Set composition string or committed string.  
  

### appendClause(aLength, aAttribute) ###
  
Append a clause.  
  
TODO: Should be able to specify custom clause style.  
  

### setCaret(aOffset, aLength) ###
  
Set caret information.  
  

### dispatchEvent() ###
  
Synthesize composition string with given information by dispatching  
a proper event.  
  
If clauses have never been set, this dispatches a commit event.  
If clauses are not filled all over the composition string, this throw an  
error.  
  
After dispatching event, this clears all the information about the  
composition string. So, you can reuse this instance.  
  

## Constants ##

### ATTR_RAWINPUT ###

### ATTR_SELECTEDRAWTEXT ###

### ATTR_CONVERTEDTEXT ###

### ATTR_SELECTEDCONVERTEDTEXT ###
