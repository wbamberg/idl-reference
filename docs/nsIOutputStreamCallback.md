---
layout: default
---

# nsIOutputStreamCallback #
  
This is a companion interface for nsIAsyncOutputStream::asyncWait.  
  

## Methods ##

### onOutputStreamReady(aStream) ###
  
Called to indicate that the stream is either writable or closed.  
  
@param aStream  
       The stream whose asyncWait method was called.  
  

#### Parameters ####

<table>

<tr>
<td>aStream</td>
<td>       The stream whose asyncWait method was called.  
</td>
</tr>

</table>
