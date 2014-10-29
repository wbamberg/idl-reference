---
layout: default
---

# nsINetworkService #

Provide network services.


## Methods ##

### setWifiTethering ###

Enable or disable Wifi Tethering

@param enabled
       Boolean that indicates whether tethering should be enabled (true) or disabled (false).
@param config
       The Wifi Tethering configuration from settings db.
@param callback
       Callback function used to report status to WifiManager.


### setDhcpServer ###

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


### getNetworkInterfaceStats ###

Retrieve network interface stats.

@param networkName
       Select the Network interface to request estats.

@param callback
       Callback to notify result and provide stats, connectionType
       and the date when stats are retrieved


### setNetworkInterfaceAlarm ###

Set Alarm of usage per interface

@param networkName
       Select the Network interface to set an alarm.

@param threshold
       Amount of data that will trigger the alarm.

@param callback
       Callback to notify the result.

@return false if there is no interface registered for the networkType param.


### setWifiOperationMode ###

Reload Wifi firmware to specific operation mode.

@param interfaceName
       Wifi Network interface name.

@param mode
       AP  - Access pointer mode.
       P2P - Peer to peer connection mode.
       STA - Station mode.

@param callback
       Callback to notify Wifi firmware reload result.


### setNetworkProxy ###

Set http proxy for specific network

@param networkInterface
       The network interface which contains the http proxy host/port
       we want to set.


### setUSBTethering ###

Set USB tethering.

@param enabled
       Boolean to indicate we are going to enable or disable usb tethering.
@param config
       The usb tethering configuration.
@param callback
       Callback function used to report the result enabling/disabling usb tethering.


### resetRoutingTable ###

Reset routing table.

@param networkInterface
       The network interface we want remove from the routing table.


### setDNS ###

Set DNS.

@param networkInterface
       The network interface which contains the DNS we want to set.

@param callback
       Callback to notify the result of setting DNS server.


### setDefaultRoute ###

Set default route.

@param networkInterface
       The network interface we want to set to the default route.
@param oldInterface
       The previous network interface.
@param callback
       Callback to notify the result of setting default route.


### removeDefaultRoute ###

Remove default route.

@param networkInterface
       The network interface we want remove from the default route.


### addHostRoute ###

Add host route.

@param interfaceName
       Network interface name for the output of the host route.
@param gateway
       Gateway ip for the output of the host route.
@param host
       Host ip we want to add route for.

@return A deferred promise that resolves on success or rejects with a
        specified reason otherwise.


### removeHostRoute ###

Remove host route.

@param interfaceName
       Network interface name for the output of the host route.
@param gateway
       Gateway ip for the output of the host route.
@param host
       Host ip we want to remove route for.

@return A deferred promise that resolves on success or rejects with a
        specified reason otherwise.


### removeHostRoutes ###

Remove all host routes.

@param interfaceName
       The interface name we want remove from the routing table.


### addSecondaryRoute ###

Add route to secondary routing table.

@param interfaceName
       The network interface for this route.
@param route
       The route info should have the following fields:
       .ip: destination ip address
       .prefix: destination prefix
       .gateway: gateway ip address


### removeSecondaryRoute ###

Remove route from secondary routing table.

@param interfaceName
       The network interface for the route we want to remove.
@param route
       The route info should have the following fields:
       .ip: destination ip address
       .prefix: destination prefix
       .gateway: gateway ip address


### enableUsbRndis ###

Enable or disable usb rndis.

@param enable
       Boolean to indicate we want enable or disable usb rndis.
@param callback
       Callback function to report the result.


### updateUpStream ###

Update upstream.

@param previous
       The previous internal and external interface.
@param current
       The current internal and external interface.
@param callback
       Callback function to report the result.


### configureInterface ###

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


### dhcpRequest ###

Issue a DHCP client request.

@param networkInterface
       The network interface which we wnat to do the DHCP request on.

@param callback
       Callback to notify the result of the DHCP request.


### enableInterface ###

Enable a network interface.

@param networkInterface
       The network interface name which we want to enable.

@param callback
       Callback to notify the result of disabling network interface.


### disableInterface ###

Disable a network interface.

@param networkInterface
       The network interface name which we want to disable.

@param callback
       Callback to notify the result of disabling network interface.


### resetConnections ###

Reset all connections

@param networkInterface
       The network interface name which we want to reset.

@param callback
       Callback to notify the result of resetting connections.

