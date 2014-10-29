---
layout: default
---

# nsIScriptableInputStream #

nsIScriptableInputStream provides scriptable access to an nsIInputStream
instance.


## close ##
 
Closes the stream. 


## init ##

Wrap the given nsIInputStream with this nsIScriptableInputStream. 

@param aInputStream parameter providing the stream to wrap 


## available ##

Return the number of bytes currently available in the stream 

@return the number of bytes 

@throws NS_BASE_STREAM_CLOSED if called after the stream has been closed


## read ##

Read data from the stream.

WARNING: If the data contains a null byte, then this method will return
a truncated string.

@param aCount the maximum number of bytes to read 

@return the data, which will be an empty string if the stream is at EOF.

@throws NS_BASE_STREAM_CLOSED if called after the stream has been closed
@throws NS_ERROR_NOT_INITIALIZED if init was not called


## readBytes ##

Read data from the stream, including NULL bytes.

@param aCount the maximum number of bytes to read.

@return the data from the stream, which will be an empty string if EOF
        has been reached.

@throws NS_BASE_STREAM_WOULD_BLOCK if reading from the input stream
        would block the calling thread (non-blocking mode only).
@throws NS_ERROR_FAILURE if there are not enough bytes available to read
        aCount amount of data.

