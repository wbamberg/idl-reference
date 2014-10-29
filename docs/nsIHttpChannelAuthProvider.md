---
layout: default
---

# nsIHttpChannelAuthProvider #

nsIHttpChannelAuthProvider

This interface is intended for providing authentication for http-style
channels, like nsIHttpChannel and nsIWebSocket, which implement the
nsIHttpAuthenticableChannel interface.

When requesting pages AddAuthorizationHeaders MUST be called
in order to get the http cached headers credentials. When the request is
unsuccessful because of receiving either a 401 or 407 http response code
ProcessAuthentication MUST be called and the page MUST be requested again
with the new credentials that the user has provided. After a successful
request, checkForSuperfluousAuth MAY be called, and disconnect MUST be
called.


## init ##

Initializes the http authentication support for the channel.
Implementations must hold a weak reference of the channel.


## processAuthentication ##

Upon receipt of a server challenge, this function is called to determine
the credentials to send.

@param httpStatus
       the http status received.
@param sslConnectFailed
       if the last ssl tunnel connection attempt was or not successful.
@param callback
       the callback to be called when it returns NS_ERROR_IN_PROGRESS.
       The implementation must hold a weak reference.

@returns NS_OK if the credentials were got and set successfully.
         NS_ERROR_IN_PROGRESS if the credentials are going to be asked to
                              the user. The channel reference must be
                              alive until the feedback from
                              nsIHttpAuthenticableChannel's methods or
                              until disconnect be called.


## addAuthorizationHeaders ##

Add credentials from the http auth cache.


## checkForSuperfluousAuth ##

Check if an unnecessary(and maybe malicious) url authentication has been
provided.


## disconnect ##

Cancel pending user auth prompts and release the callback and channel
weak references.

