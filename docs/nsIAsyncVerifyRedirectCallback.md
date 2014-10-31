---
layout: default
---

# nsIAsyncVerifyRedirectCallback #

## Methods ##

### onRedirectVerifyCallback(result) ###
  
Complement to nsIChannelEventSink asynchronous callback. The result of  
the redirect decision is passed through this callback.  
  
@param result  
   Result of the redirect veto decision. If FAILED the redirect has been  
   vetoed. If SUCCEEDED the redirect has been allowed by all consumers.  
  

#### Parameters ####

<table>

<tr>
<td>result</td>
<td>   Result of the redirect veto decision. If FAILED the redirect has been  
   vetoed. If SUCCEEDED the redirect has been allowed by all consumers.  
</td>
</tr>

</table>
