---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/io/nsIAsyncOutputStream.idl">Source file</a>
</div>

# nsIOutputStreamCallback #
<code>  
This is a companion interface for nsIAsyncOutputStream::asyncWait.  
  
</code>
## Methods ##

### onOutputStreamReady(aStream) ###
<code>  
Called to indicate that the stream is either writable or closed.  
  
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
