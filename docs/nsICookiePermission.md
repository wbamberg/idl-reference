---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/cookie/nsICookiePermission.idl">Source file</a>
</div>

# nsICookiePermission #
  
An interface to test for cookie permissions  
  

## Methods ##

### setAccess(aURI, aAccess) ###
  
setAccess  
  
this method is called to block cookie access for the given URI.  this  
may result in other URIs being blocked as well (e.g., URIs which share  
the same host name).  
  
@param aURI  
       the URI to block  
@param aAccess  
       the new cookie access for the URI.  
  

#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>       the URI to block  
</td>
</tr>

<tr>
<td>aAccess</td>
<td>       the new cookie access for the URI.  
</td>
</tr>

</table>

### canAccess(aURI, aChannel) ###
  
canAccess  
  
this method is called to test whether or not the given URI/channel may  
access the cookie database, either to set or get cookies.  
  
@param aURI  
       the URI trying to access cookies  
@param aChannel  
       the channel corresponding to aURI  
  
@return one of the following nsCookieAccess values:  
        ACCESS_DEFAULT, ACCESS_ALLOW, ACCESS_DENY, or  
        ACCESS_ALLOW_FIRST_PARTY_ONLY  
  

#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>       the URI trying to access cookies  
</td>
</tr>

<tr>
<td>aChannel</td>
<td>       the channel corresponding to aURI  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>one of the following nsCookieAccess values:  
        ACCESS_DEFAULT, ACCESS_ALLOW, ACCESS_DENY, or  
        ACCESS_ALLOW_FIRST_PARTY_ONLY  
</td>
</tr>

</table>

### canSetCookie(aURI, aChannel, aCookie, aIsSession, aExpiry) ###
  
canSetCookie  
  
this method is called to test whether or not the given URI/channel may  
set a specific cookie.  this method is always preceded by a call to  
canAccess. it may modify the isSession and expiry attributes of the  
cookie via the aIsSession and aExpiry parameters, in order to limit  
or extend the lifetime of the cookie. this is useful, for instance, to  
downgrade a cookie to session-only if it fails to meet certain criteria.  
  
@param aURI  
       the URI trying to set the cookie  
@param aChannel  
       the channel corresponding to aURI  
@param aCookie  
       the cookie being added to the cookie database  
@param aIsSession  
       when canSetCookie is invoked, this is the current isSession attribute  
       of the cookie. canSetCookie may leave this value unchanged to  
       preserve this attribute of the cookie.  
@param aExpiry  
       when canSetCookie is invoked, this is the current expiry time of  
       the cookie. canSetCookie may leave this value unchanged to  
       preserve this attribute of the cookie.  
  
@return true if the cookie can be set.  
  

#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>       the URI trying to set the cookie  
</td>
</tr>

<tr>
<td>aChannel</td>
<td>       the channel corresponding to aURI  
</td>
</tr>

<tr>
<td>aCookie</td>
<td>       the cookie being added to the cookie database  
</td>
</tr>

<tr>
<td>aIsSession</td>
<td>       when canSetCookie is invoked, this is the current isSession attribute  
       of the cookie. canSetCookie may leave this value unchanged to  
       preserve this attribute of the cookie.  
</td>
</tr>

<tr>
<td>aExpiry</td>
<td>       when canSetCookie is invoked, this is the current expiry time of  
       the cookie. canSetCookie may leave this value unchanged to  
       preserve this attribute of the cookie.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>true if the cookie can be set.  
</td>
</tr>

</table>

## Constants ##

### ACCESS_DEFAULT ###
  
nsCookieAccess values  
  

### ACCESS_ALLOW ###

### ACCESS_DENY ###

### ACCESS_SESSION ###
  
additional values for nsCookieAccess which may not match  
nsIPermissionManager. Keep 3-7 available to allow nsIPermissionManager to  
add values without colliding. ACCESS_SESSION is not directly returned by  
any methods on this interface.  
  

### ACCESS_ALLOW_FIRST_PARTY_ONLY ###

### ACCESS_LIMIT_THIRD_PARTY ###
