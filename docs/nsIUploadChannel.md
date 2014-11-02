---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIUploadChannel.idl">Source file</a>
</div>

# nsIUploadChannel #
  
nsIUploadChannel  
  
A channel may optionally implement this interface if it supports the  
notion of uploading a data stream.  The upload stream may only be set  
prior to the invocation of asyncOpen on the channel.  
  

## Methods ##

### setUploadStream(aStream, aContentType, aContentLength) ###
  
Sets a stream to be uploaded by this channel.  
  
Most implementations of this interface require that the stream:  
  (1) implement threadsafe addRef and release  
  (2) implement nsIInputStream::readSegments  
  (3) implement nsISeekableStream::seek  
  
History here is that we need to support both streams that already have  
headers (e.g., Content-Type and Content-Length) information prepended to  
the stream (by plugins) as well as clients (composer, uploading  
application) that want to upload data streams without any knowledge of  
protocol specifications.  For this reason, we have a special meaning  
for the aContentType parameter (see below).  
  
@param aStream  
       The stream to be uploaded by this channel.  
@param aContentType  
       If aContentType is empty, the protocol will assume that no  
       content headers are to be added to the uploaded stream and that  
       any required headers are already encoded in the stream.  In the  
       case of HTTP, if this parameter is non-empty, then its value will  
       replace any existing Content-Type header on the HTTP request.  
       In the case of FTP and FILE, this parameter is ignored.  
@param aContentLength  
       A value of -1 indicates that the length of the stream should be  
       determined by calling the stream's |available| method.  
  

#### Parameters ####

<table>

<tr>
<td>aStream</td>
<td>       The stream to be uploaded by this channel.  
</td>
</tr>

<tr>
<td>aContentType</td>
<td>       If aContentType is empty, the protocol will assume that no  
       content headers are to be added to the uploaded stream and that  
       any required headers are already encoded in the stream.  In the  
       case of HTTP, if this parameter is non-empty, then its value will  
       replace any existing Content-Type header on the HTTP request.  
       In the case of FTP and FILE, this parameter is ignored.  
</td>
</tr>

<tr>
<td>aContentLength</td>
<td>       A value of -1 indicates that the length of the stream should be  
       determined by calling the stream's |available| method.  
</td>
</tr>

</table>

## Attributes ##

### uploadStream ###
  
Get the stream (to be) uploaded by this channel.  
  
