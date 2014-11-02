---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsINetAddr.idl">Source file</a>
</div>

# nsINetAddr #
  
nsINetAddr  
  
This interface represents a native NetAddr struct in a readonly  
interface.  
  

## Methods ##

### getNetAddr() ###
  
@return the underlying NetAddr struct.  
  

#### Returns ####

<table>

<tr>
<td>the underlying NetAddr struct.  
</td>
</tr>

</table>

## Attributes ##

### family ###
  
@return the address family of the network address, which corresponds to  
one of the FAMILY_ constants.  
  

### address ###
  
@return Either the IP address (FAMILY_INET, FAMILY_INET6) or the path  
(FAMILY_LOCAL) in string form. IP addresses are in the format produced by  
mozilla::net::NetAddrToString.  
  
Note: Paths for FAMILY_LOCAL may have length limitations which are  
implementation dependent and not documented as part of this interface.  
  

### port ###
  
@return the port number for a FAMILY_INET or FAMILY_INET6 address.  
  
@throws NS_ERROR_NOT_AVAILABLE if the address family is not FAMILY_INET or  
FAMILY_INET6.  
  

### flow ###
  
@return the flow label for a FAMILY_INET6 address.   
  
@see http://www.ietf.org/rfc/rfc3697.txt  
  
@throws NS_ERROR_NOT_AVAILABLE if the address family is not FAMILY_INET6  
  

### scope ###
  
@return the address scope of a FAMILY_INET6 address.    
  
@see http://tools.ietf.org/html/rfc4007  
  
@throws NS_ERROR_NOT_AVAILABLE if the address family is not FAMILY_INET6  
  

### isV4Mapped ###
  
@return whether a FAMILY_INET6 address is mapped from FAMILY_INET.  
  
@throws NS_ERROR_NOT_AVAILABLE if the address family is not FAMILY_INET6  
  

## Constants ##

### FAMILY_INET ###
  
Network address families. These correspond to all the network address  
families supported by the NetAddr struct.  
  

### FAMILY_INET6 ###

### FAMILY_LOCAL ###
