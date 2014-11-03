---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/image/public/imgILoader.idl">Source file</a>
</div>

# imgILoader #
<code>  
imgILoader interface  
  
@author Stuart Parmenter <pavlov@netscape.com>  
@version 0.3  
@see imagelib2  
  
</code>
## Methods ##

### loadImageXPCOM(aURI, aInitialDocumentURL, aReferrerURI, aLoadingPrincipal, aLoadGroup, aObserver, aCX, aLoadFlags, cacheKey, aContentPolicyType) ###
<code>  
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
  
</code>
#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>the URI to load  
</td>
</tr>

<tr>
<td>aInitialDocumentURI</td>
<td>the URI that 'initiated' the load -- used for 3rd party cookie blocking  
</td>
</tr>

<tr>
<td>aReferrerURI</td>
<td>the 'referring' URI  
</td>
</tr>

<tr>
<td>aLoadingPrincipal</td>
<td>the principal of the loading document  
</td>
</tr>

<tr>
<td>aLoadGroup</td>
<td>Loadgroup to put the image load into  
</td>
</tr>

<tr>
<td>aObserver</td>
<td>the observer (may be null)  
</td>
</tr>

<tr>
<td>aCX</td>
<td>some random data  
</td>
</tr>

<tr>
<td>aLoadFlags</td>
<td>Load flags for the request  
</td>
</tr>

<tr>
<td>aCacheKey</td>
<td>cache key to use for a load if the original  
                 image came from a request that had post data  
</td>
</tr>

<tr>
<td>aContentPolicyType</td>
<td>[optional] the nsContentPolicyType to  
                          use for this load. Defaults to  
                          nsIContentPolicy::TYPE_IMAGE  
</td>
</tr>

</table>

### loadImageWithChannelXPCOM(aChannel, aObserver, cx, aListener) ###
<code>  
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
  
</code>
#### Parameters ####

<table>

<tr>
<td>aChannel</td>
<td>the channel to load the image from.  This must  
                already be opened before ths method is called, and there  
                must have been no OnDataAvailable calls for it yet.  
</td>
</tr>

<tr>
<td>aObserver</td>
<td>the observer (may be null)  
</td>
</tr>

<tr>
<td>cx</td>
<td>some random data  
</td>
</tr>

<tr>
<td>aListener</td>
<td>[out]  
       A listener that you must send the channel's notifications and data to.  
       Can be null, in which case imagelib has found a cached image and is  
       not interested in the data. @aChannel will be canceled for you in  
       this case.  
</td>
</tr>

</table>

## Constants ##

### LOAD_CORS_ANONYMOUS ###

### LOAD_CORS_USE_CREDENTIALS ###
