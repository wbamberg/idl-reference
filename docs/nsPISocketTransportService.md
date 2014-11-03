---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsPISocketTransportService.idl">Source file</a>
</div>

# nsPISocketTransportService #
  
This is a private interface used by the internals of the networking library.  
It will never be frozen.  Do not use it in external code.  
  

## Methods ##

### init() ###
  
init/shutdown routines.  
  

### shutdown() ###

## Attributes ##

### autodialEnabled ###
  
controls whether or not the socket transport service should poke  
the autodialer on connection failure.  
  

### sendBufferSize ###
  
controls the TCP sender window clamp  
  

### offline ###
  
Controls whether the socket transport service is offline.  
Setting it offline will cause non-local socket detachment.  
  

### keepaliveIdleTime ###
  
Controls the default timeout (in seconds) for sending keepalive probes.  
  

### keepaliveRetryInterval ###
  
Controls the default interval (in seconds) between retrying keepalive probes.  
  

### keepaliveProbeCount ###
  
Controls the default retransmission count for keepalive probes.  
  
