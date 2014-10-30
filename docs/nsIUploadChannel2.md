---
layout: default
---

# nsIUploadChannel2 #

## Methods ##

### explicitSetUploadStream ###
  
Sets a stream to be uploaded by this channel with the specified  
Content-Type and Content-Length header values.  
  
Most implementations of this interface require that the stream:  
  (1) implement threadsafe addRef and release  
  (2) implement nsIInputStream::readSegments  
  (3) implement nsISeekableStream::seek  
  
@param aStream  
       The stream to be uploaded by this channel.  
@param aContentType  
       This value will replace any existing Content-Type  
       header on the HTTP request, regardless of whether  
       or not its empty.  
@param aContentLength  
       A value of -1 indicates that the length of the stream should be  
       determined by calling the stream's |available| method.  
@param aMethod  
       The HTTP request method to set on the stream.  
@param aStreamHasHeaders  
       True if the stream already contains headers for the HTTP request.  
  

## Attributes ##

### uploadStreamHasHeaders ###
  
Value of aStreamHasHeaders from the last successful call to  
explicitSetUploadStream.  TRUE indicates the attached upload stream  
contians request headers.  
  
