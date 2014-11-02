---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/dns/nsIDNSRecord.idl">Source file</a>
</div>
# nsIDNSRecord #
  
nsIDNSRecord  
  
this interface represents the result of a DNS lookup.  since a DNS  
query may return more than one resolved IP address, the record acts  
like an enumerator, allowing the caller to easily step through the  
list of IP addresses.  
  

## Methods ##

### getNextAddr(aPort) ###
  
this function copies the value of the next IP address into the  
given NetAddr struct and increments the internal address iterator.  
  
@param aPort  
       A port number to initialize the NetAddr with.  
  
@throws NS_ERROR_NOT_AVAILABLE if there is not another IP address in  
the record.  
  

#### Parameters ####

<table>

<tr>
<td>aPort</td>
<td>       A port number to initialize the NetAddr with.  
</td>
</tr>

</table>

### getScriptableNextAddr(aPort) ###
  
this function returns the value of the next IP address as a  
scriptable address and increments the internal address iterator.  
  
@param aPort  
       A port number to initialize the nsINetAddr with.  
  
@throws NS_ERROR_NOT_AVAILABLE if there is not another IP address in  
the record.  
  

#### Parameters ####

<table>

<tr>
<td>aPort</td>
<td>       A port number to initialize the nsINetAddr with.  
</td>
</tr>

</table>

### getNextAddrAsString() ###
  
this function returns the value of the next IP address as a  
string and increments the internal address iterator.  
  
@throws NS_ERROR_NOT_AVAILABLE if there is not another IP address in  
the record.  
  

### hasMore() ###
  
this function returns true if there is another address in the record.  
  

### rewind() ###
  
this function resets the internal address iterator to the first  
address in the record.  
  

### reportUnusable(aPort) ###
  
This function indicates that the last address obtained via getNextAddr*()  
was not usuable and should be skipped in future uses of this  
record if other addresses are available.  
  
@param aPort is the port number associated with the failure, if any.  
       It may be zero if not applicable.  
  

#### Parameters ####

<table>

<tr>
<td>aPort</td>
<td>is the port number associated with the failure, if any.  
       It may be zero if not applicable.  
</td>
</tr>

</table>

## Attributes ##

### canonicalName ###
  
@return the canonical hostname for this record.  this value is empty if  
the record was not fetched with the RESOLVE_CANONICAL_NAME flag.  
  
e.g., www.mozilla.org --> rheet.mozilla.org  
  
