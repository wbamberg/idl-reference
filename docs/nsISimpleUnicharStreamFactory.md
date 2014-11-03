---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/io/nsISimpleUnicharStreamFactory.idl">Source file</a>
</div>

# nsISimpleUnicharStreamFactory #
<code>  
Factory to create objects that implement nsIUnicharInputStream,  
converting from a unicode string or a UTF-8 stream.  
  
</code>
## Methods ##

### createInstanceFromString(aString) ###
<code>  
Create a unicode input stream from a unicode string.  
  
</code>
### createInstanceFromUTF8Stream(aStream) ###
<code>  
Create a unicode stream from an input stream in UTF8.  
  
</code>