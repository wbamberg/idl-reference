---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/embedding/components/windowwatcher/nsIDialogParamBlock.idl">Source file</a>
</div>
# nsIDialogParamBlock #
  
An interface to pass strings, integers and nsISupports to a dialog  
  

## Methods ##

### GetInt(inIndex) ###
 Get or set an integer to pass.  
Index must be in the range 0..7  
  

### SetInt(inIndex, inInt) ###

### SetNumberStrings(inNumStrings) ###
 Set the maximum number of strings to pass. Default is 16.  
Use before setting any string (If you want to change it from the default).  
  

### GetString(inIndex) ###
 Get or set an string to pass.  
Index starts at 0  
  

### SetString(inIndex, inString) ###

## Attributes ##

### objects ###
  
A place where you can store an nsIMutableArray to pass nsISupports   
  
