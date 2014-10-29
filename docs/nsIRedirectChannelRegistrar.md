---
layout: default
---

# nsIRedirectChannelRegistrar #

Used on the chrome process as a service to join channel implementation
and parent IPC protocol side under a unique id.  Provides this way a generic
communication while redirecting to various protocols.

See also nsIChildChannel and nsIParentChannel.


## registerChannel ##

Register the redirect target channel and obtain a unique ID for that
channel.

Primarily used in HttpChannelParentListener::AsyncOnChannelRedirect to get
a channel id sent to the HttpChannelChild being redirected.


## linkChannels ##

First, search for the channel registered under the id.  If found return
it.  Then, register under the same id the parent side of IPC protocol
to let it be later grabbed back by the originator of the redirect and
notifications from the real channel could be forwarded to this parent
channel.

Primarily used in parent side of an IPC protocol implementation
in reaction to nsIChildChannel.connectParent(id) called from the child
process.


## getRegisteredChannel ##

Returns back the channel previously registered under the ID with
registerChannel method.

Primarilly used in chrome IPC side of protocols when attaching a redirect
target channel to an existing 'real' channel implementation.


## getParentChannel ##

Returns the stream listener that shall be attached to the redirect target
channel, all notification from the redirect target channel will be
forwarded to this stream listener.

Primarilly used in HttpChannelParentListener::OnRedirectResult callback
to grab the created parent side of the channel and forward notifications
to it.


## deregisterChannels ##

To not force all channel implementations to support weak reference
consumers of this service must ensure release of registered channels them
self.  This releases both the real and parent channel registered under
the id.

Primarilly used in HttpChannelParentListener::OnRedirectResult callback.

