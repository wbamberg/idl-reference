---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/uriloader/base/nsIWebProgressListener2.idl">Source file</a>
</div>

# nsIWebProgressListener2 #
<code>  
An extended version of nsIWebProgressListener.  
  
</code>
## Methods ##

### onProgressChange64(aWebProgress, aRequest, aCurSelfProgress, aMaxSelfProgress, aCurTotalProgress, aMaxTotalProgress) ###
<code>  
Notification that the progress has changed for one of the requests  
associated with aWebProgress.  Progress totals are reset to zero when all  
requests in aWebProgress complete (corresponding to onStateChange being  
called with aStateFlags including the STATE_STOP and STATE_IS_WINDOW  
flags).  
  
This function is identical to nsIWebProgressListener::onProgressChange,  
except that this function supports 64-bit values.  
  
@param aWebProgress  
       The nsIWebProgress instance that fired the notification.  
@param aRequest  
       The nsIRequest that has new progress.  
@param aCurSelfProgress  
       The current progress for aRequest.  
@param aMaxSelfProgress  
       The maximum progress for aRequest.  
@param aCurTotalProgress  
       The current progress for all requests associated with aWebProgress.  
@param aMaxTotalProgress  
       The total progress for all requests associated with aWebProgress.  
  
NOTE: If any progress value is unknown, then its value is replaced with -1.  
  
@see nsIWebProgressListener2::onProgressChange64  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aWebProgress</td>
<td>       The nsIWebProgress instance that fired the notification.  
</td>
</tr>

<tr>
<td>aRequest</td>
<td>       The nsIRequest that has new progress.  
</td>
</tr>

<tr>
<td>aCurSelfProgress</td>
<td>       The current progress for aRequest.  
</td>
</tr>

<tr>
<td>aMaxSelfProgress</td>
<td>       The maximum progress for aRequest.  
</td>
</tr>

<tr>
<td>aCurTotalProgress</td>
<td>       The current progress for all requests associated with aWebProgress.  
</td>
</tr>

<tr>
<td>aMaxTotalProgress</td>
<td>       The total progress for all requests associated with aWebProgress.  
</td>
</tr>

</table>

### onRefreshAttempted(aWebProgress, aRefreshURI, aMillis, aSameURI) ###
<code>  
Notification that a refresh or redirect has been requested in aWebProgress  
For example, via a <meta http-equiv="refresh"> or an HTTP Refresh: header  
  
@param aWebProgress  
       The nsIWebProgress instance that fired the notification.  
@param aRefreshURI  
       The new URI that aWebProgress has requested redirecting to.  
@param aMillis  
       The delay (in milliseconds) before refresh.  
@param aSameURI  
       True if aWebProgress is requesting a refresh of the  
       current URI.  
       False if aWebProgress is requesting a redirection to  
       a different URI.  
  
@return True if the refresh may proceed.  
        False if the refresh should be aborted.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aWebProgress</td>
<td>       The nsIWebProgress instance that fired the notification.  
</td>
</tr>

<tr>
<td>aRefreshURI</td>
<td>       The new URI that aWebProgress has requested redirecting to.  
</td>
</tr>

<tr>
<td>aMillis</td>
<td>       The delay (in milliseconds) before refresh.  
</td>
</tr>

<tr>
<td>aSameURI</td>
<td>       True if aWebProgress is requesting a refresh of the  
       current URI.  
       False if aWebProgress is requesting a redirection to  
       a different URI.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>True if the refresh may proceed.  
        False if the refresh should be aborted.  
</td>
</tr>

</table>
