---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/embedding/components/windowwatcher/nsIDialogParamBlock.idl">Source file</a>
</div>

# nsIDialogParamBlock #
<code>  
An interface to pass strings, integers and nsISupports to a dialog  
  
</code>
## Methods ##

### GetInt(inIndex) ###
<code> Get or set an integer to pass.  
Index must be in the range 0..7  
  
</code>
### SetInt(inIndex, inInt) ###

### SetNumberStrings(inNumStrings) ###
<code> Set the maximum number of strings to pass. Default is 16.  
Use before setting any string (If you want to change it from the default).  
  
</code>
### GetString(inIndex) ###
<code> Get or set an string to pass.  
Index starts at 0  
  
</code>
### SetString(inIndex, inString) ###

## Attributes ##

### objects ###
  
A place where you can store an nsIMutableArray to pass nsISupports   
  
