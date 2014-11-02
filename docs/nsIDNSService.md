---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/dns/nsIDNSService.idl">Source file</a>
</div>

# nsIDNSService #
  
nsIDNSService  
  

## Methods ##

### asyncResolve(aHostName, aFlags, aListener, aListenerTarget) ###
  
kicks off an asynchronous host lookup.  
  
@param aHostName  
       the hostname or IP-address-literal to resolve.  
@param aFlags  
       a bitwise OR of the RESOLVE_ prefixed constants defined below.  
@param aListener  
       the listener to be notified when the result is available.  
@param aListenerTarget  
       optional parameter (may be null).  if non-null, this parameter  
       specifies the nsIEventTarget of the thread on which the  
       listener's onLookupComplete should be called.  however, if this  
       parameter is null, then onLookupComplete will be called on an  
       unspecified thread (possibly recursively).  
  
@return An object that can be used to cancel the host lookup.  
  

#### Parameters ####

<table>

<tr>
<td>aHostName</td>
<td>       the hostname or IP-address-literal to resolve.  
</td>
</tr>

<tr>
<td>aFlags</td>
<td>       a bitwise OR of the RESOLVE_ prefixed constants defined below.  
</td>
</tr>

<tr>
<td>aListener</td>
<td>       the listener to be notified when the result is available.  
</td>
</tr>

<tr>
<td>aListenerTarget</td>
<td>       optional parameter (may be null).  if non-null, this parameter  
       specifies the nsIEventTarget of the thread on which the  
       listener's onLookupComplete should be called.  however, if this  
       parameter is null, then onLookupComplete will be called on an  
       unspecified thread (possibly recursively).  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>An object that can be used to cancel the host lookup.  
</td>
</tr>

</table>

### cancelAsyncResolve(aHostName, aFlags, aListener, aReason) ###
  
Attempts to cancel a previously requested async DNS lookup  
  
@param aHostName  
       the hostname or IP-address-literal to resolve.  
@param aFlags  
       a bitwise OR of the RESOLVE_ prefixed constants defined below.  
@param aListener  
       the original listener which was to be notified about the host lookup  
       result - used to match request information to requestor.  
@param aReason  
       nsresult reason for the cancellation  
  
@return An object that can be used to cancel the host lookup.  
  

#### Parameters ####

<table>

<tr>
<td>aHostName</td>
<td>       the hostname or IP-address-literal to resolve.  
</td>
</tr>

<tr>
<td>aFlags</td>
<td>       a bitwise OR of the RESOLVE_ prefixed constants defined below.  
</td>
</tr>

<tr>
<td>aListener</td>
<td>       the original listener which was to be notified about the host lookup  
       result - used to match request information to requestor.  
</td>
</tr>

<tr>
<td>aReason</td>
<td>       nsresult reason for the cancellation  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>An object that can be used to cancel the host lookup.  
</td>
</tr>

</table>

### resolve(aHostName, aFlags) ###
  
called to synchronously resolve a hostname.  warning this method may  
block the calling thread for a long period of time.  it is extremely  
unwise to call this function on the UI thread of an application.  
  
@param aHostName  
       the hostname or IP-address-literal to resolve.  
@param aFlags  
       a bitwise OR of the RESOLVE_ prefixed constants defined below.  
  
@return DNS record corresponding to the given hostname.  
@throws NS_ERROR_UNKNOWN_HOST if host could not be resolved.  
  

#### Parameters ####

<table>

<tr>
<td>aHostName</td>
<td>       the hostname or IP-address-literal to resolve.  
</td>
</tr>

<tr>
<td>aFlags</td>
<td>       a bitwise OR of the RESOLVE_ prefixed constants defined below.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>DNS record corresponding to the given hostname.  
@throws NS_ERROR_UNKNOWN_HOST if host could not be resolved.  
</td>
</tr>

</table>

### getDNSCacheEntries(args) ###
  
The method takes a pointer to an nsTArray  
and fills it with cache entry data  
Called by the networking dashboard  
  

## Attributes ##

### myHostName ###
  
@return the hostname of the operating system.  
  

## Constants ##

### RESOLVE_BYPASS_CACHE ###
*********************************************************************  
Listed below are the various flags that may be OR'd together to form  
the aFlags parameter passed to asyncResolve() and resolve().  
  
  
if set, this flag suppresses the internal DNS lookup cache.  
  

### RESOLVE_CANONICAL_NAME ###
  
if set, the canonical name of the specified host will be queried.  
  

### RESOLVE_PRIORITY_MEDIUM ###
  
if set, the query is given lower priority. Medium takes precedence  
if both are used.  
  

### RESOLVE_PRIORITY_LOW ###

### RESOLVE_SPECULATE ###
  
if set, indicates request is speculative. Speculative requests   
return errors if prefetching is disabled by configuration.  
  

### RESOLVE_DISABLE_IPV6 ###
  
If set, only IPv4 addresses will be returned from resolve/asyncResolve.  
  

### RESOLVE_OFFLINE ###
  
If set, only literals and cached entries will be returned from resolve/  
asyncResolve.  
  

### RESOLVE_DISABLE_IPV4 ###
  
If set, only IPv6 addresses will be returned from resolve/asyncResolve.  
  
