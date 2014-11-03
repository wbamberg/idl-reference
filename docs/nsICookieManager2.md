---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/cookie/nsICookieManager2.idl">Source file</a>
</div>

# nsICookieManager2 #
   
Additions to the frozen nsICookieManager  
  

## Methods ##

### add(aHost, aPath, aName, aValue, aIsSecure, aIsHttpOnly, aIsSession, aExpiry) ###
  
Add a cookie. nsICookieService is the normal way to do this. This  
method is something of a backdoor.  
  
  

#### Parameters ####

<table>

<tr>
<td>aHost</td>
<td>       the host or domain for which the cookie is set. presence of a  
       leading dot indicates a domain cookie; otherwise, the cookie  
       is treated as a non-domain cookie (see RFC2109). The host string  
       will be normalized to ASCII or ACE; any trailing dot will be  
       stripped. To be a domain cookie, the host must have at least two  
       subdomain parts (e.g. '.foo.com', not '.com'), otherwise an  
       exception will be thrown. An empty string is acceptable  
       (e.g. file:// URI's).  
</td>
</tr>

<tr>
<td>aPath</td>
<td>       path within the domain for which the cookie is valid  
</td>
</tr>

<tr>
<td>aName</td>
<td>       cookie name  
</td>
</tr>

<tr>
<td>aValue</td>
<td>       cookie data  
</td>
</tr>

<tr>
<td>aIsSecure</td>
<td>       true if the cookie should only be sent over a secure connection.  
</td>
</tr>

<tr>
<td>aIsHttpOnly</td>
<td>       true if the cookie should only be sent to, and can only be  
       modified by, an http connection.  
</td>
</tr>

<tr>
<td>aIsSession</td>
<td>       true if the cookie should exist for the current session only.  
       see aExpiry.  
</td>
</tr>

<tr>
<td>aExpiry</td>
<td>       expiration date, in seconds since midnight (00:00:00), January 1,  
       1970 UTC. note that expiry time will also be honored for session cookies;  
       in this way, the more restrictive of the two will take effect.  
</td>
</tr>

</table>

### cookieExists(aCookie) ###
  
Find whether a given cookie already exists.  
  
  
  

#### Parameters ####

<table>

<tr>
<td>aCookie</td>
<td>       the cookie to look for  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>true if a cookie was found which matches the host, path, and name  
        fields of aCookie  
</td>
</tr>

</table>

### countCookiesFromHost(aHost) ###
  
Count how many cookies exist within the base domain of 'aHost'.  
Thus, for a host "weather.yahoo.com", the base domain would be "yahoo.com",  
and any host or domain cookies for "yahoo.com" and its subdomains would be  
counted.  
  
  
  

#### Parameters ####

<table>

<tr>
<td>aHost</td>
<td>       the host string to search for, e.g. "google.com". this should consist  
       of only the host portion of a URI. see @add for a description of  
       acceptable host strings.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>the number of cookies found.  
</td>
</tr>

</table>

### getCookiesFromHost(aHost) ###
  
Returns an enumerator of cookies that exist within the base domain of  
'aHost'. Thus, for a host "weather.yahoo.com", the base domain would be  
"yahoo.com", and any host or domain cookies for "yahoo.com" and its  
subdomains would be returned.  
  
  
  
@see countCookiesFromHost  
  

#### Parameters ####

<table>

<tr>
<td>aHost</td>
<td>       the host string to search for, e.g. "google.com". this should consist  
       of only the host portion of a URI. see @add for a description of  
       acceptable host strings.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>an nsISimpleEnumerator of nsICookie2 objects.  
</td>
</tr>

</table>

### importCookies(aCookieFile) ###
  
Import an old-style cookie file. Imported cookies will be added to the  
existing database. If the database contains any cookies the same as those  
being imported (i.e. domain, name, and path match), they will be replaced.  
  
  

#### Parameters ####

<table>

<tr>
<td>aCookieFile</td>
<td>the file to import, usually cookies.txt  
</td>
</tr>

</table>

### getCookiesForApp(appId, onlyBrowserElement) ###
  
Returns an enumerator of all cookies that are related to a specific app.  
  
If the onlyBrowserELement parameter is set to true, only cookies part of  
a browser element inside the app will be returned. If set to false, all  
cookies will be returned, regardless of their browserElement flag.  
  
This method assumes that appId is a valid app id. It should not be a  
special value like UNKNOWN_APP_ID or NO_APP_ID.  
  

### removeCookiesForApp(appId, onlyBrowserElement) ###
  
Remove all the cookies associated with the app with the id aAppId.  
  
If onlyBrowserElement is set to true, the method will only remove the  
cookies marked as part of a browser element inside the app.  
  
Special app id values are not allowed (NO_APP_ID or UNKNOWN_APP_ID for example).  
  
