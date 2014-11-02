---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsINetworkInterceptController.idl">Source file</a>
</div>

# nsINetworkInterceptController #
  
Interface to allow consumers to attach themselves to a channel's  
notification callbacks/loadgroup and determine if a given channel  
request should be intercepted before any network request is initiated.  
  

## Methods ##

### shouldPrepareForIntercept(aURI) ###
  
Returns true if a channel should avoid initiating any network  
requests until specifically instructed to do so.  
  
@param aURI the URI being requested by a channel  
  

#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>the URI being requested by a channel  
</td>
</tr>

</table>

### channelIntercepted(aChannel, aStream) ###
  
Notification when a given intercepted channel is prepared to accept a synthesized  
response via the provided stream.  
  
@param aChannel the controlling interface for a channel that has been intercepted  
@param aStream a stream directly into the channel's synthesized response body  
  

#### Parameters ####

<table>

<tr>
<td>aChannel</td>
<td>the controlling interface for a channel that has been intercepted  
</td>
</tr>

<tr>
<td>aStream</td>
<td>a stream directly into the channel's synthesized response body  
</td>
</tr>

</table>
