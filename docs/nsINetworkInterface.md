---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/system/gonk/nsINetworkManager.idl">Source file</a>
</div>

# nsINetworkInterface #
  
Information about networks that is exposed to network manager API consumers.  
  

## Methods ##

### getAddresses(ips, prefixLengths, count) ###
  
Get the list of ip addresses and prefix lengths, ip address could be IPv4  
or IPv6, typically 1 IPv4 or 1 IPv6 or one of each.  
  
@param ips  
       The list of ip addresses retrieved.  
@param prefixLengths  
       The list of prefix lengths retrieved.  
  
@returns the length of the lists.  
  

#### Parameters ####

<table>

<tr>
<td>ips</td>
<td>       The list of ip addresses retrieved.  
</td>
</tr>

<tr>
<td>prefixLengths</td>
<td>       The list of prefix lengths retrieved.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>the length of the lists.  
</td>
</tr>

</table>

### getGateways(count, gateways) ###
  
Get the list of gateways, could be IPv4 or IPv6, typically 1 IPv4 or 1  
IPv6 or one of each.  
  
@param count  
       The length of the list of gateways  
  
@returns the list of gateways.  
  

#### Parameters ####

<table>

<tr>
<td>count</td>
<td>       The length of the list of gateways  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>the list of gateways.  
</td>
</tr>

</table>

### getDnses(count, dnses) ###
  
Get the list of dnses, could be IPv4 or IPv6.  
  
@param count  
       The length of the list of dnses.  
  
@returns the list of dnses.  
  

#### Parameters ####

<table>

<tr>
<td>count</td>
<td>       The length of the list of dnses.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>the list of dnses.  
</td>
</tr>

</table>

## Attributes ##

### state ###
  
Current network state, one of the NETWORK_STATE_* constants.  
  
When this changes, network interface implementations notify with  
updateNetworkInterface() API.  
  

### type ###
  
Network type. One of the NETWORK_TYPE_* constants.  
  

### name ###
  
Name of the network interface. This identifier is unique.  
  

### httpProxyHost ###
  
The host name of the http proxy server.  
  

### httpProxyPort ###

## Constants ##

### NETWORK_STATE_UNKNOWN ###

### NETWORK_STATE_CONNECTING ###

### NETWORK_STATE_CONNECTED ###

### NETWORK_STATE_DISCONNECTING ###

### NETWORK_STATE_DISCONNECTED ###

### NETWORK_TYPE_UNKNOWN ###

### NETWORK_TYPE_WIFI ###

### NETWORK_TYPE_MOBILE ###

### NETWORK_TYPE_MOBILE_MMS ###

### NETWORK_TYPE_MOBILE_SUPL ###

### NETWORK_TYPE_WIFI_P2P ###

### NETWORK_TYPE_MOBILE_IMS ###

### NETWORK_TYPE_MOBILE_DUN ###
