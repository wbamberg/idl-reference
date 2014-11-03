---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/json/nsIJSON.idl">Source file</a>
</div>

# nsIJSON #
<pre>  
Don't use this!  Use JSON.parse and JSON.stringify directly.  
  
</pre>
## Methods ##

### encode(value) ###
<pre>  
New users should use JSON.stringify!  
The encode() method is only present for backward compatibility.  
encode() is not a conforming JSON stringify implementation!  
  
</pre>
### encodeToStream(stream, charset, writeBOM, value) ###
<pre>  
New users should use JSON.stringify.  
You may also want to have a look at nsIConverterOutputStream.  
  
The encodeToStream() method is only present for backward compatibility.  
encodeToStream() is not a conforming JSON stringify implementation!  
  
</pre>
### decode(str) ###
<pre>  
New users should use JSON.parse!  
The decode() method is only present for backward compatibility.  
  
</pre>
### decodeFromStream(stream, contentLength) ###

### encodeFromJSVal(value, cx) ###

### decodeToJSVal(str, cx) ###
