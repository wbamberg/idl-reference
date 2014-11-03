---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/system/gonk/nsINetworkManager.idl">Source file</a>
</div>

# nsINetworkManager #
<code>  
Manage network interfaces.  
  
</code>
## Methods ##

### registerNetworkInterface(network) ###
<code>  
Register the given network interface with the network manager.  
  
Consumers will be notified with the 'network-interface-registered'  
observer notification.  
  
Throws if there's already an interface registered with the same network id.  
  
@param network  
       Network interface to register.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>network</td>
<td>       Network interface to register.  
</td>
</tr>

</table>

### updateNetworkInterface(network) ###
<code>  
Update the routes and DNSes according the state of the given network.  
  
Consumers will be notified with the 'network-connection-state-changed'  
observer notification.  
  
Throws an exception if the specified network interface object isn't  
registered.  
  
@param network  
       Network interface to update.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>network</td>
<td>       Network interface to update.  
</td>
</tr>

</table>

### unregisterNetworkInterface(network) ###
<code>  
Unregister the given network interface from the network manager.  
  
Consumers will be notified with the 'network-interface-unregistered'  
observer notification.  
  
Throws an exception if the specified network interface object isn't  
registered.  
  
@param network  
       Network interface to unregister.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>network</td>
<td>       Network interface to unregister.  
</td>
</tr>

</table>

### overrideActive(network) ###
<code>  
Override the default behaviour for preferredNetworkType and route  
all network traffic through the the specified interface.  
  
Consumers can observe changes to the active network by subscribing to  
the 'network-active-changed' observer notification.  
  
@param network  
       Network to route all network traffic to. If this is null,  
       a previous override is canceled.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>network</td>
<td>       Network to route all network traffic to. If this is null,  
       a previous override is canceled.  
</td>
</tr>

</table>

### setWifiTethering(enabled, networkInterface, config, callback) ###
<code>  
Enable or disable Wifi Tethering  
  
@param enabled  
       Boolean that indicates whether tethering should be enabled (true) or disabled (false).  
@param network  
       The Wifi network interface with at least name of network interface.  
@param config  
       The Wifi Tethering configuration from settings db.  
@param callback  
       Callback function used to report status to WifiManager.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>enabled</td>
<td>       Boolean that indicates whether tethering should be enabled (true) or disabled (false).  
</td>
</tr>

<tr>
<td>network</td>
<td>       The Wifi network interface with at least name of network interface.  
</td>
</tr>

<tr>
<td>config</td>
<td>       The Wifi Tethering configuration from settings db.  
</td>
</tr>

<tr>
<td>callback</td>
<td>       Callback function used to report status to WifiManager.  
</td>
</tr>

</table>

### addHostRoute(network, host) ###
<code>  
Add host route to the specified network into routing table.  
  
@param network  
       The network interface where the host to be routed to.  
@param host  
       The host to be added.  
       The host will be resolved in advance if it's not an ip-address.  
  
@return a Promise  
        resolved if added; rejected, otherwise.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>network</td>
<td>       The network interface where the host to be routed to.  
</td>
</tr>

<tr>
<td>host</td>
<td>       The host to be added.  
       The host will be resolved in advance if it's not an ip-address.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>a Promise  
        resolved if added; rejected, otherwise.  
</td>
</tr>

</table>

### removeHostRoute(network, host) ###
<code>  
Remove host route to the specified network from routing table.  
  
@param network  
       The network interface where the routing to be removed from.  
@param host  
       The host routed to the network.  
       The host will be resolved in advance if it's not an ip-address.  
  
@return a Promise  
        resolved if removed; rejected, otherwise.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>network</td>
<td>       The network interface where the routing to be removed from.  
</td>
</tr>

<tr>
<td>host</td>
<td>       The host routed to the network.  
       The host will be resolved in advance if it's not an ip-address.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>a Promise  
        resolved if removed; rejected, otherwise.  
</td>
</tr>

</table>

## Attributes ##

### networkInterfaces ###
  
Object containing all known network connections, keyed by their  
network id. Network id is composed of a sub-id + '-' + network  
type. For mobile network types, sub-id is 'ril' + service id; for  
non-mobile network types, sub-id is always 'device'.  
  

### preferredNetworkType ###
  
The preferred network type. One of the  
nsINetworkInterface::NETWORK_TYPE_* constants.  
  
This attribute is used for setting default route to favor  
interfaces with given type.  This can be overriden by calling  
overrideDefaultRoute().  
  

### active ###
  
The network interface handling all data traffic.  
  
When this changes, the 'network-active-changed' observer  
notification is dispatched.  
  
