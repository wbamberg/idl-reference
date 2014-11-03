---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/io/nsIAsyncOutputStream.idl">Source file</a>
</div>

# nsIAsyncOutputStream #
  
If an output stream is non-blocking, it may return NS_BASE_STREAM_WOULD_BLOCK  
when written to.  The caller must then wait for the stream to become  
writable.  If the stream implements nsIAsyncOutputStream, then the caller can  
use this interface to request an asynchronous notification when the stream  
becomes writable or closed (via the AsyncWait method).  
  
While this interface is almost exclusively used with non-blocking streams, it  
is not necessary that nsIOutputStream::isNonBlocking return true.  Nor is it  
necessary that a non-blocking nsIOutputStream implementation also implement  
nsIAsyncOutputStream.  
  

## Methods ##

### closeWithStatus(reason) ###
  
This method closes the stream and sets its internal status.  If the   
stream is already closed, then this method is ignored.  Once the stream  
is closed, the stream's status cannot be changed.  Any successful status  
code passed to this method is treated as NS_BASE_STREAM_CLOSED, which  
is equivalent to nsIInputStream::close.   
  
NOTE: this method exists in part to support pipes, which have both an   
input end and an output end.  If the output end of a pipe is closed, then  
reads from the input end of the pipe will fail.  The error code returned   
when an attempt is made to read from a "closed" pipe corresponds to the  
status code passed in when the output end of the pipe is closed, which  
greatly simplifies working with pipes in some cases.  
  
  

#### Parameters ####

<table>

<tr>
<td>aStatus</td>
<td>       The error that will be reported if this stream is accessed after  
       it has been closed.  
</td>
</tr>

</table>

### asyncWait(aCallback, aFlags, aRequestedCount, aEventTarget) ###
  
Asynchronously wait for the stream to be writable or closed.  The  
notification is one-shot, meaning that each asyncWait call will result  
in exactly one notification callback.  After the OnOutputStreamReady event  
is dispatched, the stream releases its reference to the   
nsIOutputStreamCallback object.  It is safe to call asyncWait again from the  
notification handler.  
  
This method may be called at any time (even if write has not been called).  
In other words, this method may be called when the stream already has  
room for more data.  It may also be called when the stream is closed.  If  
the stream is already writable or closed when AsyncWait is called, then the  
OnOutputStreamReady event will be dispatched immediately.  Otherwise, the  
event will be dispatched when the stream becomes writable or closed.  
  
  

#### Parameters ####

<table>

<tr>
<td>aCallback</td>
<td>       This object is notified when the stream becomes ready.  This  
       parameter may be null to clear an existing callback.  
</td>
</tr>

<tr>
<td>aFlags</td>
<td>       This parameter specifies optional flags passed in to configure  
       the behavior of this method.  Pass zero to specify no flags.  
</td>
</tr>

<tr>
<td>aRequestedCount</td>
<td>       Wait until at least this many bytes can be written.  This is only  
       a suggestion to the underlying stream; it may be ignored.  The  
       caller may pass zero to indicate no preference.  
</td>
</tr>

<tr>
<td>aEventTarget</td>
<td>       Specify NULL to receive notification on ANY thread (possibly even  
       recursively on the calling thread -- i.e., synchronously), or  
       specify that the notification be delivered to a specific event  
       target.  
</td>
</tr>

</table>

## Constants ##

### WAIT_CLOSURE_ONLY ###
  
If passed to asyncWait, this flag overrides the default behavior,  
causing the OnOutputStreamReady notification to be suppressed until the  
stream becomes closed (either as a result of closeWithStatus/close being  
called on the stream or possibly due to some error in the underlying  
stream).  
  
