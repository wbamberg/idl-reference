---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/cookie/nsICookieManager.idl">Source file</a>
</div>

# nsICookieManager #
<code>   
An optional interface for accessing or removing the cookies  
that are in the cookie list  
  
</code>
## Methods ##

### removeAll() ###
<code>  
Called to remove all cookies from the cookie list  
  
</code>
### remove(aHost, aName, aPath, aBlocked) ###
<code>  
Called to remove an individual cookie from the cookie list, specified  
by host, name, and path. If the cookie cannot be found, no exception  
is thrown. Typically, the arguments to this method will be obtained  
directly from the desired nsICookie object.  
  
@param aHost The host or domain for which the cookie was set. @see  
             nsICookieManager2::add for a description of acceptable host  
             strings. If the target cookie is a domain cookie, a leading  
             dot must be present.  
@param aName The name specified in the cookie  
@param aPath The path for which the cookie was set  
@param aBlocked Indicates if cookies from this host should be permanently blocked  
  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aHost</td>
<td>The host or domain for which the cookie was set. @see  
             nsICookieManager2::add for a description of acceptable host  
             strings. If the target cookie is a domain cookie, a leading  
             dot must be present.  
</td>
</tr>

<tr>
<td>aName</td>
<td>The name specified in the cookie  
</td>
</tr>

<tr>
<td>aPath</td>
<td>The path for which the cookie was set  
</td>
</tr>

<tr>
<td>aBlocked</td>
<td>Indicates if cookies from this host should be permanently blocked  
</td>
</tr>

</table>

## Attributes ##

### enumerator ###
  
Called to enumerate through each cookie in the cookie list.  
The objects enumerated over are of type nsICookie  
  
