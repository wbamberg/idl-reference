---
layout: default
---

# nsIProxiedChannel #

An interface for accessing the proxy info that a channel was
constructed with.

@see nsIProxiedProtocolHandler


## proxyInfo ##

Gets the proxy info the channel was constructed with. null or a
proxyInfo with type "direct" mean no proxy.

The returned proxy info must not be modified.

