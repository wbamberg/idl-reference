---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/system/gonk/nsINetworkService.idl">Source file</a>
</div>

# nsIDhcpRequestCallback #

## Methods ##

### dhcpRequestResult(success, dhcpInfo) ###
<code>  
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
  
</code>
#### Parameters ####

<table>

<tr>
<td>success</td>
<td>       Boolean to indicate the operation is successful or not.  
</td>
</tr>

<tr>
<td>dhcpInfo</td>
<td>       An object to represent the successful DHCP request:  
</td>
</tr>

</table>
