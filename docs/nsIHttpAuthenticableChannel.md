---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/protocol/http/nsIHttpAuthenticableChannel.idl">Source file</a>
</div>

# nsIHttpAuthenticableChannel #

## Methods ##

### cancel(aStatus) ###
<pre>  
Cancels the current request. See nsIRequest.  
  
</pre>
### setProxyCredentials(credentials) ###
<pre>  
Sets the Proxy-Authorization request header. An empty string  
will clear it.  
  
</pre>
### setWWWCredentials(credentials) ###
<pre>  
Sets the Authorization request header. An empty string  
will clear it.  
  
</pre>
### onAuthAvailable() ###
<pre>  
Called when authentication information is ready and has been set on this  
object using setWWWCredentials/setProxyCredentials. Implementations can  
continue with the request and send the given information to the server.  
  
It is called asynchronously from  
nsIHttpChannelAuthProvider::processAuthentication if that method returns  
NS_ERROR_IN_PROGRESS.  
  
@note  Any exceptions thrown from this method should be ignored.  
  
</pre>
### onAuthCancelled(userCancel) ###
<pre>  
Notifies that the prompt was cancelled. It is called asynchronously  
from nsIHttpChannelAuthProvider::processAuthentication if that method  
returns NS_ERROR_IN_PROGRESS.  
  
@param userCancel  
       If the user was cancelled has cancelled the authentication prompt.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>userCancel</td>
<td>       If the user was cancelled has cancelled the authentication prompt.  
</td>
</tr>

</table>

## Attributes ##

### isSSL ###
<pre>  
If the channel being authenticated is using SSL.  
  
</pre>
### proxyMethodIsConnect ###
<pre>  
Returns if the proxy HTTP method used is CONNECT. If no proxy is being  
used it must return PR_FALSE.  
  
</pre>
### loadFlags ###
<pre>  
The load flags of this request. See nsIRequest.  
  
</pre>
### URI ###
<pre>  
The URI corresponding to the channel. See nsIChannel.  
  
</pre>
### loadGroup ###
<pre>  
The load group of this request. It is here for querying its  
notificationCallbacks. See nsIRequest.  
  
</pre>
### notificationCallbacks ###
<pre>  
The notification callbacks for the channel. See nsIChannel.  
  
</pre>
### requestMethod ###
<pre>  
The HTTP request method. See nsIHttpChannel.  
  
</pre>
### serverResponseHeader ###
<pre>  
The "Server" response header.  
Return NS_ERROR_NOT_AVAILABLE if not available.  
  
</pre>
### proxyChallenges ###
<pre>  
The Proxy-Authenticate response header.  
  
</pre>
### WWWChallenges ###
<pre>  
The WWW-Authenticate response header.  
  
</pre>