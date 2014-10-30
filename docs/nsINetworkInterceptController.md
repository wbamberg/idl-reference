---
layout: default
---

# nsINetworkInterceptController #
  
Interface to allow consumers to attach themselves to a channel's  
notification callbacks/loadgroup and determine if a given channel  
request should be intercepted before any network request is initiated.  
  

## Methods ##

### shouldPrepareForIntercept ###
  
Returns true if a channel should avoid initiating any network  
requests until specifically instructed to do so.  
  
@param aURI the URI being requested by a channel  
  

### channelIntercepted ###
  
Notification when a given intercepted channel is prepared to accept a synthesized  
response via the provided stream.  
  
@param aChannel the controlling interface for a channel that has been intercepted  
@param aStream a stream directly into the channel's synthesized response body  
  
