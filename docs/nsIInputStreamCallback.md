---
layout: default
---

# nsIInputStreamCallback #
  
This is a companion interface for nsIAsyncInputStream::asyncWait.  
  

## Methods ##

### onInputStreamReady ###
  
Called to indicate that the stream is either readable or closed.  
  
@param aStream  
       The stream whose asyncWait method was called.  
  
