---
layout: default
---

# nsIOutputStreamCallback #

This is a companion interface for nsIAsyncOutputStream::asyncWait.


## onOutputStreamReady ##

Called to indicate that the stream is either writable or closed.

@param aStream
       The stream whose asyncWait method was called.

