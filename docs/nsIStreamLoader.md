---
layout: default
---

# nsIStreamLoader #

Asynchronously loads a channel into a memory buffer.

To use this interface, first call init() with a nsIStreamLoaderObserver
that will be notified when the data has been loaded. Then call asyncOpen()
on the channel with the nsIStreamLoader as the listener. The context
argument in the asyncOpen() call will be passed to the onStreamComplete()
callback.

XXX define behaviour for sizes >4 GB


## init ##

Initialize this stream loader, and start loading the data.

@param aObserver
       An observer that will be notified when the data is complete.


## numBytesRead ##

Gets the number of bytes read so far.


## request ##

Gets the request that loaded this file.
null after the request has finished loading.

