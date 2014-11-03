---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/embedding/components/windowwatcher/nsIDialogParamBlock.idl">Source file</a>
</div>

# nsIDialogParamBlock #
<pre>  
An interface to pass strings, integers and nsISupports to a dialog  
  
</pre>
## Methods ##

### GetInt(inIndex) ###
<pre> Get or set an integer to pass.  
Index must be in the range 0..7  
  
</pre>
### SetInt(inIndex, inInt) ###

### SetNumberStrings(inNumStrings) ###
<pre> Set the maximum number of strings to pass. Default is 16.  
Use before setting any string (If you want to change it from the default).  
  
</pre>
### GetString(inIndex) ###
<pre> Get or set an string to pass.  
Index starts at 0  
  
</pre>
### SetString(inIndex, inString) ###

## Attributes ##

### objects ###
<pre>  
A place where you can store an nsIMutableArray to pass nsISupports   
  
</pre>