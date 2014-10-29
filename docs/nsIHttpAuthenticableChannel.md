---
layout: default
---

# nsIHttpAuthenticableChannel #

## Methods ##

### cancel ###

Cancels the current request. See nsIRequest.


### setProxyCredentials ###

Sets the Proxy-Authorization request header. An empty string
will clear it.


### setWWWCredentials ###

Sets the Authorization request header. An empty string
will clear it.


### onAuthAvailable ###

Called when authentication information is ready and has been set on this
object using setWWWCredentials/setProxyCredentials. Implementations can
continue with the request and send the given information to the server.

It is called asynchronously from
nsIHttpChannelAuthProvider::processAuthentication if that method returns
NS_ERROR_IN_PROGRESS.

@note  Any exceptions thrown from this method should be ignored.


### onAuthCancelled ###

Notifies that the prompt was cancelled. It is called asynchronously
from nsIHttpChannelAuthProvider::processAuthentication if that method
returns NS_ERROR_IN_PROGRESS.

@param userCancel
       If the user was cancelled has cancelled the authentication prompt.


## Attributes ##

### isSSL ###

If the channel being authenticated is using SSL.


### proxyMethodIsConnect ###

Returns if the proxy HTTP method used is CONNECT. If no proxy is being
used it must return PR_FALSE.


### loadFlags ###

The load flags of this request. See nsIRequest.


### URI ###

The URI corresponding to the channel. See nsIChannel.


### loadGroup ###

The load group of this request. It is here for querying its
notificationCallbacks. See nsIRequest.


### notificationCallbacks ###

The notification callbacks for the channel. See nsIChannel.


### requestMethod ###

The HTTP request method. See nsIHttpChannel.


### serverResponseHeader ###

The "Server" response header.
Return NS_ERROR_NOT_AVAILABLE if not available.


### proxyChallenges ###

The Proxy-Authenticate response header.


### WWWChallenges ###

The WWW-Authenticate response header.

