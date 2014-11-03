---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/io/nsISimpleUnicharStreamFactory.idl">Source file</a>
</div>

# nsISimpleUnicharStreamFactory #
<pre>  
Factory to create objects that implement nsIUnicharInputStream,  
converting from a unicode string or a UTF-8 stream.  
  
</pre>
## Methods ##

### createInstanceFromString(aString) ###
<pre>  
Create a unicode input stream from a unicode string.  
  
</pre>
### createInstanceFromUTF8Stream(aStream) ###
<pre>  
Create a unicode stream from an input stream in UTF8.  
  
</pre>