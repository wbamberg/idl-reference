---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIAsyncVerifyRedirectCallback.idl">Source file</a>
</div>

# nsIAsyncVerifyRedirectCallback #

## Methods ##

### onRedirectVerifyCallback(result) ###
<pre>  
Complement to nsIChannelEventSink asynchronous callback. The result of  
the redirect decision is passed through this callback.  
  
@param result  
   Result of the redirect veto decision. If FAILED the redirect has been  
   vetoed. If SUCCEEDED the redirect has been allowed by all consumers.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>result</td>
<td>   Result of the redirect veto decision. If FAILED the redirect has been  
   vetoed. If SUCCEEDED the redirect has been allowed by all consumers.  
</td>
</tr>

</table>
