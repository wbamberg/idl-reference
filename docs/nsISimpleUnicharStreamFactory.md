---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/io/nsISimpleUnicharStreamFactory.idl">Source file</a>
</div>

# nsISimpleUnicharStreamFactory #
  
Factory to create objects that implement nsIUnicharInputStream,  
converting from a unicode string or a UTF-8 stream.  
  

## Methods ##

### createInstanceFromString(aString) ###
  
Create a unicode input stream from a unicode string.  
  

### createInstanceFromUTF8Stream(aStream) ###
  
Create a unicode stream from an input stream in UTF8.  
  
