---
layout: default
---

# imgIRequest #
  
imgIRequest interface  
  
@author Stuart Parmenter <stuart@mozilla.com>  
@version 0.1  
@see imagelib2  
  

## Methods ##

### clone ###
  
Clone this request; the returned request will have aObserver as the  
observer.  aObserver will be notified synchronously (before the clone()  
call returns) with all the notifications that have already been dispatched  
for this image load.  
  

### cancelAndForgetObserver ###
  
Cancels this request as in nsIRequest::Cancel(); further, also nulls out  
decoderObserver so it gets no further notifications from us.  
  
NOTE: You should not use this in any new code; instead, use cancel(). Note  
that cancel() is asynchronous, which means that some time after you call  
it, the listener/observer will get an OnStopRequest(). This means that, if  
you're the observer, you can't call cancel() from your destructor.  
  

### requestDecode ###
  
Requests a decode for the image.  
  
imgIContainer has a requestDecode() method, but callers may want to request  
a decode before the container has necessarily been instantiated. Calling  
requestDecode() on the imgIRequest simply forwards along the request if the  
container already exists, or calls it once it gets OnStartContainer if the  
container does not yet exist.  
  

### startDecoding ###

### lockImage ###
  
Locks an image. If the image does not exist yet, locks it once it becomes  
available. The lock persists for the lifetime of the imgIRequest (until  
unlockImage is called) even if the underlying image changes.  
  
If you don't call unlockImage() by the time this imgIRequest goes away, it  
will be called for you automatically.  
  
@see imgIContainer::lockImage for documentation of the underlying call.  
  

### unlockImage ###
  
Unlocks an image.  
  
@see imgIContainer::unlockImage for documentation of the underlying call.  
  

### requestDiscard ###
  
If this image is unlocked, discard the image's decoded data.  If the image  
is locked or is already discarded, do nothing.  
  

### getStaticRequest ###
  
If this request is for an animated image, the method creates a new  
request which contains the current frame of the image.  
Otherwise returns the same request.  
  

### incrementAnimationConsumers ###
  
Requests that the image animate (if it has an animation).  
  
@see Image::IncrementAnimationConsumers for documentation of the underlying call.  
  

### decrementAnimationConsumers ###
  
Tell the image it can forget about a request that the image animate.  
  
@see Image::DecrementAnimationConsumers for documentation of the underlying call.  
  

## Attributes ##

### image ###
  
the image container...  
@return the image object associated with the request.  
@attention NEED DOCS  
  

### imageStatus ###
  
Status flags of the STATUS_* variety.  
  

### imageErrorCode ###

### URI ###
  
The URI the image load was started with.  Note that this might not be the  
actual URI for the image (e.g. if HTTP redirects happened during the  
load).  
  

### notificationObserver ###

### mimeType ###

### imagePrincipal ###
  
The principal gotten from the channel the image was loaded from.  
  

### multipart ###
  
Whether the request is multipart (ie, multipart/x-mixed-replace)  
  

### CORSMode ###
  
The CORS mode that this image was loaded with.   
  

## Constants ##

### STATUS_NONE ###
  
Bits set in the return value from imageStatus  
@name statusflags  
  
Meanings:  
  
STATUS_NONE: Nothing to report.  
  
STATUS_SIZE_AVAILABLE: We received enough image data  
from the network or filesystem that we know the width  
and height of the image, and have thus called SetSize()  
on the container.  
  
STATUS_LOAD_PARTIAL: Used internally by imgRequest to  
flag that a request is being cancelled as a result of  
a failure of a proxy holder and not an internal failure.  
At least I think that's what it does. Regardless, there's  
no reason for this flag to be public, and it should either  
go away or become a private state flag within imgRequest.  
Don't rely on it.  
  
STATUS_LOAD_COMPLETE: The data has been fully loaded  
to memory, but not necessarily fully decoded.  
  
STATUS_ERROR: An error occurred loading the image.  
  
STATUS_DECODE_STARTED: The decoding process has begun, but not yet  
finished.  
  
STATUS_FRAME_COMPLETE: The first frame has been  
completely decoded.  
  
STATUS_DECODE_COMPLETE: The whole image has been decoded.  
  

### STATUS_SIZE_AVAILABLE ###

### STATUS_LOAD_PARTIAL ###

### STATUS_LOAD_COMPLETE ###

### STATUS_ERROR ###

### STATUS_DECODE_STARTED ###

### STATUS_FRAME_COMPLETE ###

### STATUS_DECODE_COMPLETE ###

### CORS_NONE ###
  
CORS modes images can be loaded with.  
  
By default, all images are loaded with CORS_NONE and cannot be used  
cross-origin in context like WebGL.  
  
If an HTML img element has the crossorigin attribute set, the imgIRequest  
will be validated for cross-origin usage with CORS, and, if successful,  
will have its CORS mode set to the relevant type.  
  

### CORS_ANONYMOUS ###

### CORS_USE_CREDENTIALS ###
