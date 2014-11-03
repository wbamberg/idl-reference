---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/ds/nsIPersistentProperties2.idl">Source file</a>
</div>

# nsIPersistentProperties #

## Methods ##

### load(input) ###
  
load a set of name/value pairs from the input stream  
names and values should be in UTF8  
  

### save(output, header) ###
  
output the values to the stream - results will be in UTF8  
  

### subclass(superclass) ###
  
call subclass() to make future calls to load() set the properties  
in this "superclass" instead  
  

### enumerate() ###
  
get an enumeration of nsIPropertyElement objects,  
which are read-only (i.e. setting properties on the element will  
not make changes back into the source nsIPersistentProperties  
  

### getStringProperty(key) ###
  
shortcut to nsIProperty's get() which retrieves a string value  
directly (and thus faster)  
  

### setStringProperty(key, value) ###
  
shortcut to nsIProperty's set() which sets a string value  
directly (and thus faster). If the given property already exists,  
then the old value will be returned  
  
