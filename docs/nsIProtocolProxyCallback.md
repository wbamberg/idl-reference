---
layout: default
---

# nsIProtocolProxyCallback #
  
This interface serves as a closure for nsIProtocolProxyService's  
asyncResolve method.  
  

## Methods ##

### onProxyAvailable(aRequest, aURI, aProxyInfo, aStatus) ###
  
This method is called when proxy info is available or when an error  
in the proxy resolution occurs.  
  
@param aRequest  
       The value returned from asyncResolve.  
@param aURI  
       The URI passed to asyncResolve.  
@param aProxyInfo  
       The resulting proxy info or null if there is no associated proxy  
       info for aURI.  As with the result of nsIProtocolProxyService's  
       resolve method, a null result implies that a direct connection  
       should be used.  
@param aStatus  
       The status of the callback.  This is a failure code if the request  
       could not be satisfied, in which case the value of aStatus  
       indicates the reason for the failure and aProxyInfo will be null.  
  

#### Parameters ####

<table>

<tr>
<td>aRequest</td>
<td>       The value returned from asyncResolve.  
</td>
</tr>

<tr>
<td>aURI</td>
<td>       The URI passed to asyncResolve.  
</td>
</tr>

<tr>
<td>aProxyInfo</td>
<td>       The resulting proxy info or null if there is no associated proxy  
       info for aURI.  As with the result of nsIProtocolProxyService's  
       resolve method, a null result implies that a direct connection  
       should be used.  
</td>
</tr>

<tr>
<td>aStatus</td>
<td>       The status of the callback.  This is a failure code if the request  
       could not be satisfied, in which case the value of aStatus  
       indicates the reason for the failure and aProxyInfo will be null.  
</td>
</tr>

</table>
