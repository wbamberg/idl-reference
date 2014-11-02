---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/system/gonk/nsINetworkService.idl">Source file</a>
</div>

# nsINetworkService #
  
Provide network services.  
  

## Methods ##

### setWifiTethering(enabled, config, callback) ###
  
Enable or disable Wifi Tethering  
  
@param enabled  
       Boolean that indicates whether tethering should be enabled (true) or disabled (false).  
@param config  
       The Wifi Tethering configuration from settings db.  
@param callback  
       Callback function used to report status to WifiManager.  
  

#### Parameters ####

<table>

<tr>
<td>enabled</td>
<td>       Boolean that indicates whether tethering should be enabled (true) or disabled (false).  
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

### setDhcpServer(enabled, config, callback) ###
  
Enable or disable DHCP server  
  
@param enabled  
       Boolean that indicates enabling or disabling DHCP server.  
  
@param config  
       Config used to enable the DHCP server. It contains  
       .startIp    start of the ip lease range (string)  
       .endIp      end of the ip lease range (string)  
       .serverIp   ip of the DHCP server (string)  
       .maskLength the length of the subnet mask  
       .ifname     the interface name  
  
       As for disabling the DHCP server, put this value |null|.  
  
@param callback  
       Callback function used to report status.  
  

#### Parameters ####

<table>

<tr>
<td>enabled</td>
<td>       Boolean that indicates enabling or disabling DHCP server.  
</td>
</tr>

<tr>
<td>config</td>
<td>       Config used to enable the DHCP server. It contains  
       .startIp    start of the ip lease range (string)  
       .endIp      end of the ip lease range (string)  
       .serverIp   ip of the DHCP server (string)  
       .maskLength the length of the subnet mask  
       .ifname     the interface name  
</td>
</tr>

<tr>
<td>callback</td>
<td>       Callback function used to report status.  
</td>
</tr>

</table>

### getNetworkInterfaceStats(networkName, callback) ###
  
Retrieve network interface stats.  
  
@param networkName  
       Select the Network interface to request estats.  
  
@param callback  
       Callback to notify result and provide stats, connectionType  
       and the date when stats are retrieved  
  

#### Parameters ####

<table>

<tr>
<td>networkName</td>
<td>       Select the Network interface to request estats.  
</td>
</tr>

<tr>
<td>callback</td>
<td>       Callback to notify result and provide stats, connectionType  
       and the date when stats are retrieved  
</td>
</tr>

</table>

### setNetworkInterfaceAlarm(networkName, threshold, callback) ###
  
Set Alarm of usage per interface  
  
@param networkName  
       Select the Network interface to set an alarm.  
  
@param threshold  
       Amount of data that will trigger the alarm.  
  
@param callback  
       Callback to notify the result.  
  
@return false if there is no interface registered for the networkType param.  
  

#### Parameters ####

<table>

<tr>
<td>networkName</td>
<td>       Select the Network interface to set an alarm.  
</td>
</tr>

<tr>
<td>threshold</td>
<td>       Amount of data that will trigger the alarm.  
</td>
</tr>

<tr>
<td>callback</td>
<td>       Callback to notify the result.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>false if there is no interface registered for the networkType param.  
</td>
</tr>

</table>

### setWifiOperationMode(interfaceName, mode, callback) ###
  
Reload Wifi firmware to specific operation mode.  
  
@param interfaceName  
       Wifi Network interface name.  
  
@param mode  
       AP  - Access pointer mode.  
       P2P - Peer to peer connection mode.  
       STA - Station mode.  
  
@param callback  
       Callback to notify Wifi firmware reload result.  
  

#### Parameters ####

<table>

<tr>
<td>interfaceName</td>
<td>       Wifi Network interface name.  
</td>
</tr>

<tr>
<td>mode</td>
<td>       AP  - Access pointer mode.  
       P2P - Peer to peer connection mode.  
       STA - Station mode.  
</td>
</tr>

<tr>
<td>callback</td>
<td>       Callback to notify Wifi firmware reload result.  
</td>
</tr>

</table>

### setNetworkProxy(networkInterface) ###
  
Set http proxy for specific network  
  
@param networkInterface  
       The network interface which contains the http proxy host/port  
       we want to set.  
  

#### Parameters ####

<table>

<tr>
<td>networkInterface</td>
<td>       The network interface which contains the http proxy host/port  
       we want to set.  
</td>
</tr>

</table>

### setUSBTethering(enabled, config, callback) ###
  
Set USB tethering.  
  
@param enabled  
       Boolean to indicate we are going to enable or disable usb tethering.  
@param config  
       The usb tethering configuration.  
@param callback  
       Callback function used to report the result enabling/disabling usb tethering.  
  

#### Parameters ####

<table>

<tr>
<td>enabled</td>
<td>       Boolean to indicate we are going to enable or disable usb tethering.  
</td>
</tr>

<tr>
<td>config</td>
<td>       The usb tethering configuration.  
</td>
</tr>

<tr>
<td>callback</td>
<td>       Callback function used to report the result enabling/disabling usb tethering.  
</td>
</tr>

</table>

### resetRoutingTable(networkInterface) ###
  
Reset routing table.  
  
@param networkInterface  
       The network interface we want remove from the routing table.  
  

#### Parameters ####

<table>

<tr>
<td>networkInterface</td>
<td>       The network interface we want remove from the routing table.  
</td>
</tr>

</table>

### setDNS(networkInterface, callback) ###
  
Set DNS.  
  
@param networkInterface  
       The network interface which contains the DNS we want to set.  
  
@param callback  
       Callback to notify the result of setting DNS server.  
  

#### Parameters ####

<table>

<tr>
<td>networkInterface</td>
<td>       The network interface which contains the DNS we want to set.  
</td>
</tr>

<tr>
<td>callback</td>
<td>       Callback to notify the result of setting DNS server.  
</td>
</tr>

</table>

### setDefaultRoute(networkInterface, oldInterface, callback) ###
  
Set default route.  
  
@param networkInterface  
       The network interface we want to set to the default route.  
@param oldInterface  
       The previous network interface.  
@param callback  
       Callback to notify the result of setting default route.  
  

#### Parameters ####

<table>

<tr>
<td>networkInterface</td>
<td>       The network interface we want to set to the default route.  
</td>
</tr>

<tr>
<td>oldInterface</td>
<td>       The previous network interface.  
</td>
</tr>

<tr>
<td>callback</td>
<td>       Callback to notify the result of setting default route.  
</td>
</tr>

</table>

### removeDefaultRoute(networkInterface) ###
  
Remove default route.  
  
@param networkInterface  
       The network interface we want remove from the default route.  
  

#### Parameters ####

<table>

<tr>
<td>networkInterface</td>
<td>       The network interface we want remove from the default route.  
</td>
</tr>

</table>

### addHostRoute(interfaceName, gateway, host) ###
  
Add host route.  
  
@param interfaceName  
       Network interface name for the output of the host route.  
@param gateway  
       Gateway ip for the output of the host route.  
@param host  
       Host ip we want to add route for.  
  
@return A deferred promise that resolves on success or rejects with a  
        specified reason otherwise.  
  

#### Parameters ####

<table>

<tr>
<td>interfaceName</td>
<td>       Network interface name for the output of the host route.  
</td>
</tr>

<tr>
<td>gateway</td>
<td>       Gateway ip for the output of the host route.  
</td>
</tr>

<tr>
<td>host</td>
<td>       Host ip we want to add route for.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>A deferred promise that resolves on success or rejects with a  
        specified reason otherwise.  
</td>
</tr>

</table>

### removeHostRoute(interfaceName, gateway, host) ###
  
Remove host route.  
  
@param interfaceName  
       Network interface name for the output of the host route.  
@param gateway  
       Gateway ip for the output of the host route.  
@param host  
       Host ip we want to remove route for.  
  
@return A deferred promise that resolves on success or rejects with a  
        specified reason otherwise.  
  

#### Parameters ####

<table>

<tr>
<td>interfaceName</td>
<td>       Network interface name for the output of the host route.  
</td>
</tr>

<tr>
<td>gateway</td>
<td>       Gateway ip for the output of the host route.  
</td>
</tr>

<tr>
<td>host</td>
<td>       Host ip we want to remove route for.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>A deferred promise that resolves on success or rejects with a  
        specified reason otherwise.  
</td>
</tr>

</table>

### removeHostRoutes(interfaceName) ###
  
Remove all host routes.  
  
@param interfaceName  
       The interface name we want remove from the routing table.  
  

#### Parameters ####

<table>

<tr>
<td>interfaceName</td>
<td>       The interface name we want remove from the routing table.  
</td>
</tr>

</table>

### addSecondaryRoute(interfaceName, route) ###
  
Add route to secondary routing table.  
  
@param interfaceName  
       The network interface for this route.  
@param route  
       The route info should have the following fields:  
       .ip: destination ip address  
       .prefix: destination prefix  
       .gateway: gateway ip address  
  

#### Parameters ####

<table>

<tr>
<td>interfaceName</td>
<td>       The network interface for this route.  
</td>
</tr>

<tr>
<td>route</td>
<td>       The route info should have the following fields:  
       .ip: destination ip address  
       .prefix: destination prefix  
       .gateway: gateway ip address  
</td>
</tr>

</table>

### removeSecondaryRoute(interfaceName, route) ###
  
Remove route from secondary routing table.  
  
@param interfaceName  
       The network interface for the route we want to remove.  
@param route  
       The route info should have the following fields:  
       .ip: destination ip address  
       .prefix: destination prefix  
       .gateway: gateway ip address  
  

#### Parameters ####

<table>

<tr>
<td>interfaceName</td>
<td>       The network interface for the route we want to remove.  
</td>
</tr>

<tr>
<td>route</td>
<td>       The route info should have the following fields:  
       .ip: destination ip address  
       .prefix: destination prefix  
       .gateway: gateway ip address  
</td>
</tr>

</table>

### enableUsbRndis(enable, callback) ###
  
Enable or disable usb rndis.  
  
@param enable  
       Boolean to indicate we want enable or disable usb rndis.  
@param callback  
       Callback function to report the result.  
  

#### Parameters ####

<table>

<tr>
<td>enable</td>
<td>       Boolean to indicate we want enable or disable usb rndis.  
</td>
</tr>

<tr>
<td>callback</td>
<td>       Callback function to report the result.  
</td>
</tr>

</table>

### updateUpStream(previous, current, callback) ###
  
Update upstream.  
  
@param previous  
       The previous internal and external interface.  
@param current  
       The current internal and external interface.  
@param callback  
       Callback function to report the result.  
  

#### Parameters ####

<table>

<tr>
<td>previous</td>
<td>       The previous internal and external interface.  
</td>
</tr>

<tr>
<td>current</td>
<td>       The current internal and external interface.  
</td>
</tr>

<tr>
<td>callback</td>
<td>       Callback function to report the result.  
</td>
</tr>

</table>

### configureInterface(config, callback) ###
  
Configure a network interface.  
  
@param config  
       An object containing the detail that we want to configure the interface:  
  
         - ifname:  string  
         - ipaddr:  long  
         - mask:    long  
         - gateway: long  
         - dns1:    long  
         - dns2:    long  
  
@param callback  
       Callback to notify the result of configurating network interface.  
  

#### Parameters ####

<table>

<tr>
<td>config</td>
<td>       An object containing the detail that we want to configure the interface:  
</td>
</tr>

<tr>
<td>callback</td>
<td>       Callback to notify the result of configurating network interface.  
</td>
</tr>

</table>

### dhcpRequest(interfaceName, callback) ###
  
Issue a DHCP client request.  
  
@param networkInterface  
       The network interface which we wnat to do the DHCP request on.  
  
@param callback  
       Callback to notify the result of the DHCP request.  
  

#### Parameters ####

<table>

<tr>
<td>networkInterface</td>
<td>       The network interface which we wnat to do the DHCP request on.  
</td>
</tr>

<tr>
<td>callback</td>
<td>       Callback to notify the result of the DHCP request.  
</td>
</tr>

</table>

### enableInterface(interfaceName, callback) ###
  
Enable a network interface.  
  
@param networkInterface  
       The network interface name which we want to enable.  
  
@param callback  
       Callback to notify the result of disabling network interface.  
  

#### Parameters ####

<table>

<tr>
<td>networkInterface</td>
<td>       The network interface name which we want to enable.  
</td>
</tr>

<tr>
<td>callback</td>
<td>       Callback to notify the result of disabling network interface.  
</td>
</tr>

</table>

### disableInterface(interfaceName, callback) ###
  
Disable a network interface.  
  
@param networkInterface  
       The network interface name which we want to disable.  
  
@param callback  
       Callback to notify the result of disabling network interface.  
  

#### Parameters ####

<table>

<tr>
<td>networkInterface</td>
<td>       The network interface name which we want to disable.  
</td>
</tr>

<tr>
<td>callback</td>
<td>       Callback to notify the result of disabling network interface.  
</td>
</tr>

</table>

### resetConnections(interfaceName, callback) ###
  
Reset all connections  
  
@param networkInterface  
       The network interface name which we want to reset.  
  
@param callback  
       Callback to notify the result of resetting connections.  
  

#### Parameters ####

<table>

<tr>
<td>networkInterface</td>
<td>       The network interface name which we want to reset.  
</td>
</tr>

<tr>
<td>callback</td>
<td>       Callback to notify the result of resetting connections.  
</td>
</tr>

</table>
