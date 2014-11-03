---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsPISocketTransportService.idl">Source file</a>
</div>

# nsPISocketTransportService #
<pre>  
This is a private interface used by the internals of the networking library.  
It will never be frozen.  Do not use it in external code.  
  
</pre>
## Methods ##

### init() ###
<pre>  
init/shutdown routines.  
  
</pre>
### shutdown() ###

## Attributes ##

### autodialEnabled ###
<pre>  
controls whether or not the socket transport service should poke  
the autodialer on connection failure.  
  
</pre>
### sendBufferSize ###
<pre>  
controls the TCP sender window clamp  
  
</pre>
### offline ###
<pre>  
Controls whether the socket transport service is offline.  
Setting it offline will cause non-local socket detachment.  
  
</pre>
### keepaliveIdleTime ###
<pre>  
Controls the default timeout (in seconds) for sending keepalive probes.  
  
</pre>
### keepaliveRetryInterval ###
<pre>  
Controls the default interval (in seconds) between retrying keepalive probes.  
  
</pre>
### keepaliveProbeCount ###
<pre>  
Controls the default retransmission count for keepalive probes.  
  
</pre>