---
layout: default
---

# nsIStreamLoaderObserver #

## Methods ##

### onStreamComplete(loader, ctxt, status, resultLength, result) ###
  
Called when the entire stream has been loaded.  
  
@param loader the stream loader that loaded the stream.  
@param ctxt the context parameter of the underlying channel  
@param status the status of the underlying channel  
@param resultLength the length of the data loaded  
@param result the data  
  
This method will always be called asynchronously by the  
nsIStreamLoader involved, on the thread that called the  
loader's init() method.  
  
If the observer wants to take over responsibility for the  
data buffer (result), it returns NS_SUCCESS_ADOPTED_DATA  
in place of NS_OK as its success code. The loader will then  
"forget" about the data and not moz_free() it after  
onStreamComplete() returns; observer must call moz_free()  
when the data is no longer required.  
  
