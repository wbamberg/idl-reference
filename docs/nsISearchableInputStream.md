---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/io/nsIPipe.idl">Source file</a>
</div>

# nsISearchableInputStream #
<code>  
XXX this interface doesn't really belong in here.  It is here because  
currently nsPipeInputStream is the only implementation of this interface.  
  
</code>
## Methods ##

### search(forString, ignoreCase, found, offsetSearchedTo) ###
<code>  
Searches for a string in the input stream. Since the stream has a notion  
of EOF, it is possible that the string may at some time be in the   
buffer, but is is not currently found up to some offset. Consequently,  
both the found and not found cases return an offset:  
   if found, return offset where it was found  
   if not found, return offset of the first byte not searched  
In the case the stream is at EOF and the string is not found, the first  
byte not searched will correspond to the length of the buffer.  
  
</code>