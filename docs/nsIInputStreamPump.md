---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIInputStreamPump.idl">Source file</a>
</div>

# nsIInputStreamPump #
  
nsIInputStreamPump  
  
This interface provides a means to configure and use a input stream pump  
instance.  The input stream pump will asynchronously read from an input  
stream, and push data to an nsIStreamListener instance.  It utilizes the  
current thread's nsIEventTarget in order to make reading from the stream  
asynchronous. A different thread can be used if the pump also implements  
nsIThreadRetargetableRequest.  
  
If the given stream supports nsIAsyncInputStream, then the stream pump will  
call the stream's AsyncWait method to drive the stream listener.  Otherwise,  
the stream will be read on a background thread utilizing the stream  
transport service.  More details are provided below.  
  

## Methods ##

### init(aStream, aStreamPos, aStreamLen, aSegmentSize, aSegmentCount, aCloseWhenDone) ###
  
Initialize the input stream pump.  
  
  

#### Parameters ####

<table>

<tr>
<td>aStream</td>
<td>       contains the data to be read.  if the input stream is non-blocking,  
       then it will be QI'd to nsIAsyncInputStream.  if the QI succeeds  
       then the stream will be read directly.  otherwise, it will be read  
       on a background thread using the stream transport service.  
</td>
</tr>

<tr>
<td>aStreamPos</td>
<td>       specifies the stream offset from which to start reading.  the  
       offset value is absolute.  pass -1 to specify the current offset.  
       NOTE: this parameter is ignored if the underlying stream does not  
       implement nsISeekableStream.  
</td>
</tr>

<tr>
<td>aStreamLen</td>
<td>       specifies how much data to read from the stream.  pass -1 to read  
       all data available in the stream.  
</td>
</tr>

<tr>
<td>aSegmentSize</td>
<td>       if the stream transport service is used, then this parameter  
       specifies the segment size for the stream transport's buffer.  
       pass 0 to specify the default value.  
</td>
</tr>

<tr>
<td>aSegmentCount</td>
<td>       if the stream transport service is used, then this parameter  
       specifies the segment count for the stream transport's buffer.  
       pass 0 to specify the default value.  
</td>
</tr>

<tr>
<td>aCloseWhenDone</td>
<td>       if true, the input stream will be closed after it has been read.  
</td>
</tr>

</table>

### asyncRead(aListener, aListenerContext) ###
  
asyncRead causes the input stream to be read in chunks and delivered  
asynchronously to the listener via OnDataAvailable.  
  
  

#### Parameters ####

<table>

<tr>
<td>aListener</td>
<td>       receives notifications.  
</td>
</tr>

<tr>
<td>aListenerContext</td>
<td>       passed to listener methods.  
</td>
</tr>

</table>
