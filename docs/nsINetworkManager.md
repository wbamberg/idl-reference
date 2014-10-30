---
layout: default
---

# nsINetworkManager #
  
Manage network interfaces.  
  

## Methods ##

### registerNetworkInterface ###
  
Register the given network interface with the network manager.  
  
Consumers will be notified with the 'network-interface-registered'  
observer notification.  
  
Throws if there's already an interface registered with the same network id.  
  
@param network  
       Network interface to register.  
  

### updateNetworkInterface ###
  
Update the routes and DNSes according the state of the given network.  
  
Consumers will be notified with the 'network-connection-state-changed'  
observer notification.  
  
Throws an exception if the specified network interface object isn't  
registered.  
  
@param network  
       Network interface to update.  
  

### unregisterNetworkInterface ###
  
Unregister the given network interface from the network manager.  
  
Consumers will be notified with the 'network-interface-unregistered'  
observer notification.  
  
Throws an exception if the specified network interface object isn't  
registered.  
  
@param network  
       Network interface to unregister.  
  

### overrideActive ###
  
Override the default behaviour for preferredNetworkType and route  
all network traffic through the the specified interface.  
  
Consumers can observe changes to the active network by subscribing to  
the 'network-active-changed' observer notification.  
  
@param network  
       Network to route all network traffic to. If this is null,  
       a previous override is canceled.  
  

### setWifiTethering ###
  
Enable or disable Wifi Tethering  
  
@param enabled  
       Boolean that indicates whether tethering should be enabled (true) or disabled (false).  
@param network  
       The Wifi network interface with at least name of network interface.  
@param config  
       The Wifi Tethering configuration from settings db.  
@param callback  
       Callback function used to report status to WifiManager.  
  

### addHostRoute ###
  
Add host route to the specified network into routing table.  
  
@param network  
       The network interface where the host to be routed to.  
@param host  
       The host to be added.  
       The host will be resolved in advance if it's not an ip-address.  
  
@return a Promise  
        resolved if added; rejected, otherwise.  
  

### removeHostRoute ###
  
Remove host route to the specified network from routing table.  
  
@param network  
       The network interface where the routing to be removed from.  
@param host  
       The host routed to the network.  
       The host will be resolved in advance if it's not an ip-address.  
  
@return a Promise  
        resolved if removed; rejected, otherwise.  
  

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
  
