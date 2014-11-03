---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIUploadChannel2.idl">Source file</a>
</div>

# nsIUploadChannel2 #

## Methods ##

### explicitSetUploadStream(aStream, aContentType, aContentLength, aMethod, aStreamHasHeaders) ###
  
Sets a stream to be uploaded by this channel with the specified  
Content-Type and Content-Length header values.  
  
Most implementations of this interface require that the stream:  
  (1) implement threadsafe addRef and release  
  (2) implement nsIInputStream::readSegments  
  (3) implement nsISeekableStream::seek  
  
  

#### Parameters ####

<table>

<tr>
<td>aStream</td>
<td>       The stream to be uploaded by this channel.  
</td>
</tr>

<tr>
<td>aContentType</td>
<td>       This value will replace any existing Content-Type  
       header on the HTTP request, regardless of whether  
       or not its empty.  
</td>
</tr>

<tr>
<td>aContentLength</td>
<td>       A value of -1 indicates that the length of the stream should be  
       determined by calling the stream's |available| method.  
</td>
</tr>

<tr>
<td>aMethod</td>
<td>       The HTTP request method to set on the stream.  
</td>
</tr>

<tr>
<td>aStreamHasHeaders</td>
<td>       True if the stream already contains headers for the HTTP request.  
</td>
</tr>

</table>

## Attributes ##

### uploadStreamHasHeaders ###
  
Value of aStreamHasHeaders from the last successful call to  
explicitSetUploadStream.  TRUE indicates the attached upload stream  
contians request headers.  
  
