---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/io/nsIAsyncInputStream.idl">Source file</a>
</div>

# nsIInputStreamCallback #
  
This is a companion interface for nsIAsyncInputStream::asyncWait.  
  

## Methods ##

### onInputStreamReady(aStream) ###
  
Called to indicate that the stream is either readable or closed.  
  
  

#### Parameters ####

<table>

<tr>
<td>aStream</td>
<td>       The stream whose asyncWait method was called.  
</td>
</tr>

</table>
