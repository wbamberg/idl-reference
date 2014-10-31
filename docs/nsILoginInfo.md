---
layout: default
---

# nsILoginInfo #
  
An object containing information for a login stored by the  
password manager.  
  

## Methods ##

### init(aHostname, aFormSubmitURL, aHttpRealm, aUsername, aPassword, aUsernameField, aPasswordField) ###
  
Initialize a newly created nsLoginInfo object.  
  
The arguments are the fields for the new object.  
  

### equals(aLoginInfo) ###
  
Test for strict equality with another nsILoginInfo object.  
  
@param aLoginInfo  
       The other object to test.  
  

#### Parameters ####

<table>

<tr>
<td>aLoginInfo</td>
<td>       The other object to test.  
</td>
</tr>

</table>

### matches(aLoginInfo, ignorePassword) ###
  
Test for loose equivalency with another nsILoginInfo object. The  
passwordField and usernameField values are ignored, and the password  
values may be optionally ignored. If one login's formSubmitURL is an  
empty string (but not null), it will be treated as a wildcard. [The  
blank value indicates the login was stored before bug 360493 was fixed.]  
  
@param aLoginInfo  
       The other object to test.  
@param ignorePassword  
       If true, ignore the password when checking for match.  
  

#### Parameters ####

<table>

<tr>
<td>aLoginInfo</td>
<td>       The other object to test.  
</td>
</tr>

<tr>
<td>ignorePassword</td>
<td>       If true, ignore the password when checking for match.  
</td>
</tr>

</table>

### clone() ###
  
Create an identical copy of the login, duplicating all of the login's  
nsILoginInfo and nsILoginMetaInfo properties.  
  
This allows code to be forwards-compatible, when additional properties  
are added to nsILoginMetaInfo (or nsILoginInfo) in the future.  
  

## Attributes ##

### hostname ###
  
The hostname the login applies to.  
  
The hostname should be formatted as an URL. For example,  
"https://site.com", "http://site.com:1234", "ftp://ftp.site.com".  
  

### formSubmitURL ###
  
The URL a form-based login was submitted to.  
  
For logins obtained from HTML forms, this field is the |action|  
attribute from the |form| element, with the path removed. For  
example "http://www.site.com". [Forms with no |action| attribute  
default to submitting to their origin URL, so we store that.]  
  
For logins obtained from a HTTP or FTP protocol authentication,  
this field is NULL.  
  

### httpRealm ###
  
The HTTP Realm a login was requested for.  
  
When an HTTP server sends a 401 result, the WWW-Authenticate  
header includes a realm to identify the "protection space." See  
RFC2617. If the response sent has a missing or blank realm, the  
hostname is used instead.  
  
For logins obtained from HTML forms, this field is NULL.  
  

### username ###
  
The username for the login.  
  

### usernameField ###
  
The |name| attribute for the username input field.  
  
For logins obtained from a HTTP or FTP protocol authentication,  
this field is an empty string.  
  

### password ###
  
The password for the login.  
  

### passwordField ###
  
The |name| attribute for the password input field.  
  
For logins obtained from a HTTP or FTP protocol authentication,  
this field is an empty string.  
  
