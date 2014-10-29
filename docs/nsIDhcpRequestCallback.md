---
layout: default
---

# nsIDhcpRequestCallback #

## dhcpRequestResult ##

Callback function used to report the result of DHCP client request.

@param success
       Boolean to indicate the operation is successful or not.

@param dhcpInfo
       An object to represent the successful DHCP request:

         - gateway_str: string
         - dns1_str:    string
         - dns2_str:    string
         - mask_str:    string
         - server_str:  string
         - vendor_str:  string
         - lease:       long
         - mask:        long
         - ipaddr:      long
         - gateway:     long
         - dns1:        long
         - dns2:        long
         - server:      long

