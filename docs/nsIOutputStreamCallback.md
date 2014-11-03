---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/io/nsIAsyncOutputStream.idl">Source file</a>
</div>

# nsIOutputStreamCallback #
<pre>  
This is a companion interface for nsIAsyncOutputStream::asyncWait.  
  
</pre>
## Methods ##

### onOutputStreamReady(aStream) ###
<pre>  
Called to indicate that the stream is either writable or closed.  
  
@param aStream  
       The stream whose asyncWait method was called.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aStream</td>
<td>       The stream whose asyncWait method was called.  
</td>
</tr>

</table>
