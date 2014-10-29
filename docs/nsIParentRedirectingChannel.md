---
layout: default
---

# nsIParentRedirectingChannel #

Implemented by chrome side of IPC protocols that support redirect responses.


## startRedirect ##

Called when the channel got a response that redirects it to a different
URI.  The implementation is responsible for calling the redirect observers
on the child process and provide the decision result to the callback.

@param newChannelId
   id of the redirect channel obtained from nsIRedirectChannelRegistrar.
@param newURI
   the URI we redirect to
@param callback
   redirect result callback, usage is compatible with how
   nsIChannelEventSink defines it


## completeRedirect ##

Called after we are done with redirecting process and we know if to
redirect or not.  Forward the redirect result to the child process.  From
that moment the nsIParentChannel implementation expects it will be
forwarded all notifications from the 'real' channel.

Primarilly used by HttpChannelParentListener::OnRedirectResult and kept
as mActiveChannel and mRedirectChannel in that class.

