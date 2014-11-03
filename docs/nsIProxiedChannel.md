---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIProxiedChannel.idl">Source file</a>
</div>

# nsIProxiedChannel #
<code>  
An interface for accessing the proxy info that a channel was  
constructed with.  
  
@see nsIProxiedProtocolHandler  
  
</code>
## Attributes ##

### proxyInfo ###
  
Gets the proxy info the channel was constructed with. null or a  
proxyInfo with type "direct" mean no proxy.  
  
The returned proxy info must not be modified.  
  
