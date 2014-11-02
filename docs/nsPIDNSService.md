---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/dns/nsPIDNSService.idl">Source file</a>
</div>

# nsPIDNSService #
  
This is a private interface used by the internals of the networking library.  
It will never be frozen.  Do not use it in external code.  
  

## Methods ##

### init() ###
  
called to initialize the DNS service.  
  

### shutdown() ###
  
called to shutdown the DNS service.  any pending asynchronous  
requests will be canceled, and the local cache of DNS records  
will be cleared.  NOTE: the operating system may still have  
its own cache of DNS records, which would be unaffected by  
this method.  
  

## Attributes ##

### prefetchEnabled ###
  
Whether or not DNS prefetching (aka RESOLVE_SPECULATE) is enabled  
  

### offline ###
  
@return whether the DNS service is offline.  
  
