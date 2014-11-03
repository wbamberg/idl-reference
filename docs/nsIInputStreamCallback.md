---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/io/nsIAsyncInputStream.idl">Source file</a>
</div>

# nsIInputStreamCallback #
<code>  
This is a companion interface for nsIAsyncInputStream::asyncWait.  
  
</code>
## Methods ##

### onInputStreamReady(aStream) ###
<code>  
Called to indicate that the stream is either readable or closed.  
  
@param aStream  
       The stream whose asyncWait method was called.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aStream</td>
<td>       The stream whose asyncWait method was called.  
</td>
</tr>

</table>
