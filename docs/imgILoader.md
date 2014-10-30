---
layout: default
---

# imgILoader #
  
imgILoader interface  
  
@author Stuart Parmenter <pavlov@netscape.com>  
@version 0.3  
@see imagelib2  
  

## Methods ##

### loadImageXPCOM ###
  
Start the load and decode of an image.  
@param aURI the URI to load  
@param aInitialDocumentURI the URI that 'initiated' the load -- used for 3rd party cookie blocking  
@param aReferrerURI the 'referring' URI  
@param aLoadingPrincipal the principal of the loading document  
@param aLoadGroup Loadgroup to put the image load into  
@param aObserver the observer (may be null)  
@param aCX some random data  
@param aLoadFlags Load flags for the request  
@param aCacheKey cache key to use for a load if the original  
                 image came from a request that had post data  
@param aContentPolicyType [optional] the nsContentPolicyType to  
                          use for this load. Defaults to  
                          nsIContentPolicy::TYPE_IMAGE  
  
  
libpr0n does NOT keep a strong ref to the observer; this prevents  
reference cycles.  This means that callers of loadImage should  
make sure to Cancel() the resulting request before the observer  
goes away.  
  

### loadImageWithChannelXPCOM ###
  
Start the load and decode of an image.  
@param aChannel the channel to load the image from.  This must  
                already be opened before ths method is called, and there  
                must have been no OnDataAvailable calls for it yet.  
@param aObserver the observer (may be null)  
@param cx some random data  
@param aListener [out]  
       A listener that you must send the channel's notifications and data to.  
       Can be null, in which case imagelib has found a cached image and is  
       not interested in the data. @aChannel will be canceled for you in  
       this case.  
  
libpr0n does NOT keep a strong ref to the observer; this prevents  
reference cycles.  This means that callers of loadImageWithChannel should  
make sure to Cancel() the resulting request before the observer goes away.  
  

## Constants ##

### LOAD_CORS_ANONYMOUS ###

### LOAD_CORS_USE_CREDENTIALS ###
