---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsINetAddr.idl">Source file</a>
</div>

# nsINetAddr #
<pre>  
nsINetAddr  
  
This interface represents a native NetAddr struct in a readonly  
interface.  
  
</pre>
## Methods ##

### getNetAddr() ###
<pre>  
@return the underlying NetAddr struct.  
  
</pre>
#### Returns ####

<table>

<tr>
<td>the underlying NetAddr struct.  
</td>
</tr>

</table>

## Attributes ##

### family ###
<pre>  
@return the address family of the network address, which corresponds to  
one of the FAMILY_ constants.  
  
</pre>
### address ###
<pre>  
@return Either the IP address (FAMILY_INET, FAMILY_INET6) or the path  
(FAMILY_LOCAL) in string form. IP addresses are in the format produced by  
mozilla::net::NetAddrToString.  
  
Note: Paths for FAMILY_LOCAL may have length limitations which are  
implementation dependent and not documented as part of this interface.  
  
</pre>
### port ###
<pre>  
@return the port number for a FAMILY_INET or FAMILY_INET6 address.  
  
@throws NS_ERROR_NOT_AVAILABLE if the address family is not FAMILY_INET or  
FAMILY_INET6.  
  
</pre>
### flow ###
<pre>  
@return the flow label for a FAMILY_INET6 address.   
  
@see http://www.ietf.org/rfc/rfc3697.txt  
  
@throws NS_ERROR_NOT_AVAILABLE if the address family is not FAMILY_INET6  
  
</pre>
### scope ###
<pre>  
@return the address scope of a FAMILY_INET6 address.    
  
@see http://tools.ietf.org/html/rfc4007  
  
@throws NS_ERROR_NOT_AVAILABLE if the address family is not FAMILY_INET6  
  
</pre>
### isV4Mapped ###
<pre>  
@return whether a FAMILY_INET6 address is mapped from FAMILY_INET.  
  
@throws NS_ERROR_NOT_AVAILABLE if the address family is not FAMILY_INET6  
  
</pre>
## Constants ##

### FAMILY_INET ###
<pre>  
Network address families. These correspond to all the network address  
families supported by the NetAddr struct.  
  
</pre>
### FAMILY_INET6 ###

### FAMILY_LOCAL ###
