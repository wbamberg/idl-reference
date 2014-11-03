---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsINetworkPredictor.idl">Source file</a>
</div>

# nsINetworkPredictor #
  
nsINetworkPredictor - learn about pages users visit, and allow us to take  
                      predictive actions upon future visits.  
                      NOTE: nsINetworkPredictor should only  
                      be used on the main thread.  
  

## Methods ##

### predict(targetURI, sourceURI, reason, loadContext, verifier) ###
  
Start taking predictive actions  
  
Calling this will cause the predictor to (possibly) start  
taking actions such as DNS prefetch and/or TCP preconnect based on  
(1) the host name that we are given, and (2) the reason we are being  
asked to take actions.  
  
@param targetURI - The URI we are being asked to take actions based on.  
@param sourceURI - The URI that is currently loaded. This is so we can  
  avoid doing predictive actions for link hover on an HTTPS page (for  
  example).  
@param reason - The reason we are being asked to take actions. Can be  
  any of the PREDICT_* values above.  
  In the case of PREDICT_LINK, targetURI should be the URI of the link  
  that is being hovered over, and sourceURI should be the URI of the page  
  on which the link appears.  
  In the case of PREDICT_LOAD, targetURI should be the URI of the page that  
  is being loaded and sourceURI should be null.  
  In the case of PREDICT_STARTUP, both targetURI and sourceURI should be  
  null.  
@param loadContext - The nsILoadContext of the page load we are predicting  
  about.  
@param verifier - An nsINetworkPredictorVerifier used in testing to ensure  
  we're predicting the way we expect to. Not necessary (or desired) for  
  normal operation.  
  

#### Parameters ####

<table>

<tr>
<td>targetURI</td>
<td>- The URI we are being asked to take actions based on.  
</td>
</tr>

<tr>
<td>sourceURI</td>
<td>- The URI that is currently loaded. This is so we can  
  avoid doing predictive actions for link hover on an HTTPS page (for  
  example).  
</td>
</tr>

<tr>
<td>reason</td>
<td>- The reason we are being asked to take actions. Can be  
  any of the PREDICT_* values above.  
  In the case of PREDICT_LINK, targetURI should be the URI of the link  
  that is being hovered over, and sourceURI should be the URI of the page  
  on which the link appears.  
  In the case of PREDICT_LOAD, targetURI should be the URI of the page that  
  is being loaded and sourceURI should be null.  
  In the case of PREDICT_STARTUP, both targetURI and sourceURI should be  
  null.  
</td>
</tr>

<tr>
<td>loadContext</td>
<td>- The nsILoadContext of the page load we are predicting  
  about.  
</td>
</tr>

<tr>
<td>verifier</td>
<td>- An nsINetworkPredictorVerifier used in testing to ensure  
  we're predicting the way we expect to. Not necessary (or desired) for  
  normal operation.  
</td>
</tr>

</table>

### learn(targetURI, sourceURI, reason, loadContext) ###
  
Add to our compendium of knowledge  
  
This adds to our prediction database to make things (hopefully)  
smarter next time we predict something.  
  
@param targetURI - The URI that was loaded that we are keeping track of.  
@param sourceURI - The URI that caused targetURI to be loaded (for page  
  loads). This means the DOCUMENT URI.  
@param reason - The reason we are learning this bit of knowledge.  
  Reason can be any of the LEARN_* values.  
  In the case of LEARN_LOAD_SUBRESOURCE, targetURI should be the URI of a  
  subresource of a page, and sourceURI should be the top-level URI.  
  In the case of LEARN_LOAD_REDIRECT, targetURI is the NEW URI of a  
  top-level resource that was redirected to, and sourceURI is the  
  ORIGINAL URI of said top-level resource.  
  In the case of LEARN_STARTUP, targetURI should be the URI of a page  
  that was loaded immediately after browser startup, and sourceURI should  
  be null.  
@param loadContext - The nsILoadContext for the page load that we are  
  learning about.  
  

#### Parameters ####

<table>

<tr>
<td>targetURI</td>
<td>- The URI that was loaded that we are keeping track of.  
</td>
</tr>

<tr>
<td>sourceURI</td>
<td>- The URI that caused targetURI to be loaded (for page  
  loads). This means the DOCUMENT URI.  
</td>
</tr>

<tr>
<td>reason</td>
<td>- The reason we are learning this bit of knowledge.  
  Reason can be any of the LEARN_* values.  
  In the case of LEARN_LOAD_SUBRESOURCE, targetURI should be the URI of a  
  subresource of a page, and sourceURI should be the top-level URI.  
  In the case of LEARN_LOAD_REDIRECT, targetURI is the NEW URI of a  
  top-level resource that was redirected to, and sourceURI is the  
  ORIGINAL URI of said top-level resource.  
  In the case of LEARN_STARTUP, targetURI should be the URI of a page  
  that was loaded immediately after browser startup, and sourceURI should  
  be null.  
</td>
</tr>

<tr>
<td>loadContext</td>
<td>- The nsILoadContext for the page load that we are  
  learning about.  
</td>
</tr>

</table>

### reset() ###
  
Clear out all our learned knowledge  
  
This removes everything from our database so that any predictions begun  
after this completes will start from a blank slate.  
  

### prepareForDnsTest(timestamp, uri) ###
  
@deprecated THIS API IS FOR TESTING ONLY. IF YOU DON'T KNOW WHAT IT DOES,  
DON'T USE IT  
  

## Constants ##

### PREDICT_LINK ###
  
Prediction reasons  
  
PREDICT_LINK - we are being asked to take predictive action because  
the user is hovering over a link.  
  
PREDICT_LOAD - we are being asked to take predictive action because  
the user has initiated a pageload.  
  
PREDICT_STARTUP - we are being asked to take predictive action  
because the browser is starting up.  
  

### PREDICT_LOAD ###

### PREDICT_STARTUP ###

### LEARN_LOAD_TOPLEVEL ###

### LEARN_LOAD_SUBRESOURCE ###

### LEARN_LOAD_REDIRECT ###

### LEARN_STARTUP ###
