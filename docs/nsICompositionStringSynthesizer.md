---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/base/nsICompositionStringSynthesizer.idl">Source file</a>
</div>

# nsICompositionStringSynthesizer #
<pre>  
Stores composition clauses information and caret information for synthesizing  
composition string.  
  
</pre>
## Methods ##

### setString(aString) ###
<pre>  
Set composition string or committed string.  
  
</pre>
### appendClause(aLength, aAttribute) ###
<pre>  
Append a clause.  
  
TODO: Should be able to specify custom clause style.  
  
</pre>
### setCaret(aOffset, aLength) ###
<pre>  
Set caret information.  
  
</pre>
### dispatchEvent() ###
<pre>  
Synthesize composition string with given information by dispatching  
a proper event.  
  
If clauses have never been set, this dispatches a commit event.  
If clauses are not filled all over the composition string, this throw an  
error.  
  
After dispatching event, this clears all the information about the  
composition string. So, you can reuse this instance.  
  
</pre>
## Constants ##

### ATTR_RAWINPUT ###

### ATTR_SELECTEDRAWTEXT ###

### ATTR_CONVERTEDTEXT ###

### ATTR_SELECTEDCONVERTEDTEXT ###
