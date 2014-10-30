---
layout: default
---

# nsIInterceptedChannel #
  
Interface to allow implementors of nsINetworkInterceptController to control the behaviour  
of intercepted channels without tying implementation details of the interception to  
the actual channel. nsIInterceptedChannel is expected to be implemented by objects  
which do not implement nsIChannel.  
  

## Methods ##

### resetInterception() ###
  
Instruct a channel that has been intercepted to continue with the original  
network request.  
  

### synthesizeHeader(name, value) ###
  
Attach a header name/value pair to the forthcoming synthesized response.  
Overwrites any existing header value.  
  

### finishSynthesizedResponse() ###
  
Instruct a channel that has been intercepted that a response has been  
synthesized and can now be read. No further header modification is allowed  
after this point.  
  
