---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsINetworkLinkService.idl">Source file</a>
</div>

# nsINetworkLinkService #
  
Network link status monitoring service.  
  

## Attributes ##

### isLinkUp ###
  
This is set to true when the system is believed to have a usable  
network connection.  
  
The link is only up when network connections can be established. For  
example, the link is down during DHCP configuration (unless there  
is another usable interface already configured).  
  
If the link status is not currently known, we generally assume that  
it is up.  
  

### linkStatusKnown ###
  
This is set to true when we believe that isLinkUp is accurate.  
  

### linkType ###
  
The type of network connection.  
  

## Constants ##

### LINK_TYPE_UNKNOWN ###

### LINK_TYPE_ETHERNET ###

### LINK_TYPE_USB ###

### LINK_TYPE_WIFI ###

### LINK_TYPE_WIMAX ###

### LINK_TYPE_2G ###

### LINK_TYPE_3G ###

### LINK_TYPE_4G ###
