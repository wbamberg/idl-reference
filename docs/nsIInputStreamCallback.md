---
layout: default
---

# nsIInputStreamCallback #
  
This is a companion interface for nsIAsyncInputStream::asyncWait.  
  

## Methods ##

### onInputStreamReady(aStream) ###
  
Called to indicate that the stream is either readable or closed.  
  
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
