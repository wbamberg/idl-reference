---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/json/nsIJSON.idl">Source file</a>
</div>

# nsIJSON #
<code>  
Don't use this!  Use JSON.parse and JSON.stringify directly.  
  
</code>
## Methods ##

### encode(value) ###
<code>  
New users should use JSON.stringify!  
The encode() method is only present for backward compatibility.  
encode() is not a conforming JSON stringify implementation!  
  
</code>
### encodeToStream(stream, charset, writeBOM, value) ###
<code>  
New users should use JSON.stringify.  
You may also want to have a look at nsIConverterOutputStream.  
  
The encodeToStream() method is only present for backward compatibility.  
encodeToStream() is not a conforming JSON stringify implementation!  
  
</code>
### decode(str) ###
<code>  
New users should use JSON.parse!  
The decode() method is only present for backward compatibility.  
  
</code>
### decodeFromStream(stream, contentLength) ###

### encodeFromJSVal(value, cx) ###

### decodeToJSVal(str, cx) ###
