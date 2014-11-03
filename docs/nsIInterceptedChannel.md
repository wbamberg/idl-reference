---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsINetworkInterceptController.idl">Source file</a>
</div>

# nsIInterceptedChannel #
<pre>  
Interface to allow implementors of nsINetworkInterceptController to control the behaviour  
of intercepted channels without tying implementation details of the interception to  
the actual channel. nsIInterceptedChannel is expected to be implemented by objects  
which do not implement nsIChannel.  
  
</pre>
## Methods ##

### resetInterception() ###
<pre>  
Instruct a channel that has been intercepted to continue with the original  
network request.  
  
</pre>
### synthesizeHeader(name, value) ###
<pre>  
Attach a header name/value pair to the forthcoming synthesized response.  
Overwrites any existing header value.  
  
</pre>
### finishSynthesizedResponse() ###
<pre>  
Instruct a channel that has been intercepted that a response has been  
synthesized and can now be read. No further header modification is allowed  
after this point.  
  
</pre>