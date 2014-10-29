---
layout: default
---

# nsIChildChannel #

Implemented by content side of IPC protocols.


## connectParent ##

Create the chrome side of the IPC protocol and join an existing 'real'
channel on the parent process.  The id is provided by
nsIRedirectChannelRegistrar on the chrome process and pushed to the child
protocol as an argument to event starting a redirect.

Primarilly used in HttpChannelChild::Redirect1Begin on a newly created
child channel, where the new channel is intended to be created on the
child process.


## completeRedirectSetup ##

As AsyncOpen is called on the chrome process for redirect target channels,
we have to inform the child side of the protocol of that fact by a special
method.

