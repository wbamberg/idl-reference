---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/passwordmgr/nsILoginInfo.idl">Source file</a>
</div>

# nsILoginInfo #
<pre>  
An object containing information for a login stored by the  
password manager.  
  
</pre>
## Methods ##

### init(aHostname, aFormSubmitURL, aHttpRealm, aUsername, aPassword, aUsernameField, aPasswordField) ###
<pre>  
Initialize a newly created nsLoginInfo object.  
  
The arguments are the fields for the new object.  
  
</pre>
### equals(aLoginInfo) ###
<pre>  
Test for strict equality with another nsILoginInfo object.  
  
@param aLoginInfo  
       The other object to test.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aLoginInfo</td>
<td>       The other object to test.  
</td>
</tr>

</table>

### matches(aLoginInfo, ignorePassword) ###
<pre>  
Test for loose equivalency with another nsILoginInfo object. The  
passwordField and usernameField values are ignored, and the password  
values may be optionally ignored. If one login's formSubmitURL is an  
empty string (but not null), it will be treated as a wildcard. [The  
blank value indicates the login was stored before bug 360493 was fixed.]  
  
@param aLoginInfo  
       The other object to test.  
@param ignorePassword  
       If true, ignore the password when checking for match.  
  
</pre>
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
<pre>  
Create an identical copy of the login, duplicating all of the login's  
nsILoginInfo and nsILoginMetaInfo properties.  
  
This allows code to be forwards-compatible, when additional properties  
are added to nsILoginMetaInfo (or nsILoginInfo) in the future.  
  
</pre>
## Attributes ##

### hostname ###
<pre>  
The hostname the login applies to.  
  
The hostname should be formatted as an URL. For example,  
"https://site.com", "http://site.com:1234", "ftp://ftp.site.com".  
  
</pre>
### formSubmitURL ###
<pre>  
The URL a form-based login was submitted to.  
  
For logins obtained from HTML forms, this field is the |action|  
attribute from the |form| element, with the path removed. For  
example "http://www.site.com". [Forms with no |action| attribute  
default to submitting to their origin URL, so we store that.]  
  
For logins obtained from a HTTP or FTP protocol authentication,  
this field is NULL.  
  
</pre>
### httpRealm ###
<pre>  
The HTTP Realm a login was requested for.  
  
When an HTTP server sends a 401 result, the WWW-Authenticate  
header includes a realm to identify the "protection space." See  
RFC2617. If the response sent has a missing or blank realm, the  
hostname is used instead.  
  
For logins obtained from HTML forms, this field is NULL.  
  
</pre>
### username ###
<pre>  
The username for the login.  
  
</pre>
### usernameField ###
<pre>  
The |name| attribute for the username input field.  
  
For logins obtained from a HTTP or FTP protocol authentication,  
this field is an empty string.  
  
</pre>
### password ###
<pre>  
The password for the login.  
  
</pre>
### passwordField ###
<pre>  
The |name| attribute for the password input field.  
  
For logins obtained from a HTTP or FTP protocol authentication,  
this field is an empty string.  
  
</pre>