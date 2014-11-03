---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/passwordmgr/nsILoginManagerStorage.idl">Source file</a>
</div>

# nsILoginManagerStorage #

## Methods ##

### initialize() ###
<pre>  
Initialize the component.  
  
At present, other methods of this interface may be called before the  
returned promise is resolved or rejected.  
  
@return {Promise}  
@resolves When initialization is complete.  
@rejects JavaScript exception.  
  
</pre>
#### Returns ####

<table>

<tr>
<td>{Promise}  
@resolves When initialization is complete.  
@rejects JavaScript exception.  
</td>
</tr>

</table>

### terminate() ###
<pre>  
Ensures that all data has been written to disk and all files are closed.  
  
At present, this method is called by regression tests only.  Finalization  
on shutdown is done by observers within the component.  
  
@return {Promise}  
@resolves When finalization is complete.  
@rejects JavaScript exception.  
  
</pre>
#### Returns ####

<table>

<tr>
<td>{Promise}  
@resolves When finalization is complete.  
@rejects JavaScript exception.  
</td>
</tr>

</table>

### addLogin(aLogin) ###
<pre>  
Store a new login in the storage module.  
  
@param aLogin  
       The login to be added.  
  
Default values for the login's nsILoginMetaInfo properties will be  
created. However, if the caller specifies non-default values, they will  
be used instead.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aLogin</td>
<td>       The login to be added.  
</td>
</tr>

</table>

### removeLogin(aLogin) ###
<pre>  
Remove a login from the storage module.  
  
@param aLogin  
       The login to be removed.  
  
The specified login must exactly match a stored login. However, the  
values of any nsILoginMetaInfo properties are ignored.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aLogin</td>
<td>       The login to be removed.  
</td>
</tr>

</table>

### modifyLogin(oldLogin, newLoginData) ###
<pre>  
Modify an existing login in the storage module.  
  
@param oldLogin  
       The login to be modified.  
@param newLoginData  
       The new login values (either a nsILoginInfo or nsIProperyBag)  
  
If newLoginData is a nsILoginInfo, all of the old login's nsILoginInfo  
properties are changed to the values from newLoginData (but the old  
login's nsILoginMetaInfo properties are unmodified).  
  
If newLoginData is a nsIPropertyBag, only the specified properties  
will be changed. The nsILoginMetaInfo properties of oldLogin can be  
changed in this manner.  
  
If the propertybag contains an item named "timesUsedIncrement", the  
login's timesUsed property will be incremented by the item's value.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>oldLogin</td>
<td>       The login to be modified.  
</td>
</tr>

<tr>
<td>newLoginData</td>
<td>       The new login values (either a nsILoginInfo or nsIProperyBag)  
</td>
</tr>

</table>

### removeAllLogins() ###
<pre>  
Remove all stored logins.  
  
The browser sanitization feature allows the user to clear any stored  
passwords. This interface allows that to be done without getting each  
login first (which might require knowing the master password).  
  
  
</pre>
### getAllLogins(count, logins) ###
<pre>  
Fetch all logins in the login manager. An array is always returned;  
if there are no logins the array is empty.  
  
@param count  
       The number of elements in the array. JS callers can simply use  
       the array's .length property and omit this param.  
@param logins  
       An array of nsILoginInfo objects.  
  
NOTE: This can be called from JS as:  
      var logins = pwmgr.getAllLogins();  
      (|logins| is an array).  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>count</td>
<td>       The number of elements in the array. JS callers can simply use  
       the array's .length property and omit this param.  
</td>
</tr>

<tr>
<td>logins</td>
<td>       An array of nsILoginInfo objects.  
</td>
</tr>

</table>

### searchLogins(count, matchData, logins) ###
<pre>  
Search for logins in the login manager. An array is always returned;  
if there are no logins the array is empty.  
  
@param count  
       The number of elements in the array. JS callers can simply use  
       the array's .length property, and supply an dummy object for  
       this out param. For example: |searchLogins({}, matchData)|  
@param matchData  
       The data used to search. This does not follow the same  
       requirements as findLogins for those fields. Wildcard matches are  
       simply not specified.  
@param logins  
       An array of nsILoginInfo objects.  
  
NOTE: This can be called from JS as:  
      var logins = pwmgr.searchLogins({}, matchData);  
      (|logins| is an array).  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>count</td>
<td>       The number of elements in the array. JS callers can simply use  
       the array's .length property, and supply an dummy object for  
       this out param. For example: |searchLogins({}, matchData)|  
</td>
</tr>

<tr>
<td>matchData</td>
<td>       The data used to search. This does not follow the same  
       requirements as findLogins for those fields. Wildcard matches are  
       simply not specified.  
</td>
</tr>

<tr>
<td>logins</td>
<td>       An array of nsILoginInfo objects.  
</td>
</tr>

</table>

### getAllDisabledHosts(count, hostnames) ###
<pre>  
Obtain a list of all hosts for which password saving is disabled.  
  
@param count  
       The number of elements in the array. JS callers can simply use  
       the array's .length property and omit this param.  
@param hostnames  
       An array of hostname strings, in origin URL format without a  
       pathname. For example: "https://www.site.com".  
  
NOTE: This can be called from JS as:  
      var logins = pwmgr.getAllDisabledHosts();  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>count</td>
<td>       The number of elements in the array. JS callers can simply use  
       the array's .length property and omit this param.  
</td>
</tr>

<tr>
<td>hostnames</td>
<td>       An array of hostname strings, in origin URL format without a  
       pathname. For example: "https://www.site.com".  
</td>
</tr>

</table>

### getLoginSavingEnabled(aHost) ###
<pre>  
Check to see if saving logins has been disabled for a host.  
  
@param aHost  
       The hostname to check. This argument should be in the origin  
       URL format, without a pathname. For example: "http://foo.com".  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aHost</td>
<td>       The hostname to check. This argument should be in the origin  
       URL format, without a pathname. For example: "http://foo.com".  
</td>
</tr>

</table>

### setLoginSavingEnabled(aHost, isEnabled) ###
<pre>  
Disable (or enable) storing logins for the specified host. When  
disabled, the login manager will not prompt to store logins for  
that host. Existing logins are not affected.  
  
@param aHost  
       The hostname to set. This argument should be in the origin  
       URL format, without a pathname. For example: "http://foo.com".  
@param isEnabled  
       Specify if saving logins should be enabled (true) or  
       disabled (false)  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aHost</td>
<td>       The hostname to set. This argument should be in the origin  
       URL format, without a pathname. For example: "http://foo.com".  
</td>
</tr>

<tr>
<td>isEnabled</td>
<td>       Specify if saving logins should be enabled (true) or  
       disabled (false)  
</td>
</tr>

</table>

### findLogins(count, aHostname, aActionURL, aHttpRealm, logins) ###
<pre>  
Search for logins matching the specified criteria. Called when looking  
for logins that might be applicable to a form or authentication request.  
  
@param count  
       The number of elements in the array. JS callers can simply use  
       the array's .length property, and supply an dummy object for  
       this out param. For example: |findLogins({}, hostname, ...)|  
@param aHostname  
       The hostname to restrict searches to, in URL format. For  
       example: "http://www.site.com".  
@param aActionURL  
       For form logins, this argument should be the URL to which the  
       form will be submitted. For protocol logins, specify null.  
@param aHttpRealm  
       For protocol logins, this argument should be the HTTP Realm  
       for which the login applies. This is obtained from the  
       WWW-Authenticate header. See RFC2617. For form logins,  
       specify null.  
@param logins  
       An array of nsILoginInfo objects.  
  
NOTE: This can be called from JS as:  
      var logins = pwmgr.findLogins({}, hostname, ...);  
  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>count</td>
<td>       The number of elements in the array. JS callers can simply use  
       the array's .length property, and supply an dummy object for  
       this out param. For example: |findLogins({}, hostname, ...)|  
</td>
</tr>

<tr>
<td>aHostname</td>
<td>       The hostname to restrict searches to, in URL format. For  
       example: "http://www.site.com".  
</td>
</tr>

<tr>
<td>aActionURL</td>
<td>       For form logins, this argument should be the URL to which the  
       form will be submitted. For protocol logins, specify null.  
</td>
</tr>

<tr>
<td>aHttpRealm</td>
<td>       For protocol logins, this argument should be the HTTP Realm  
       for which the login applies. This is obtained from the  
       WWW-Authenticate header. See RFC2617. For form logins,  
       specify null.  
</td>
</tr>

<tr>
<td>logins</td>
<td>       An array of nsILoginInfo objects.  
</td>
</tr>

</table>

### countLogins(aHostname, aActionURL, aHttpRealm) ###
<pre>  
Search for logins matching the specified criteria, as with  
findLogins(). This interface only returns the number of matching  
logins (and not the logins themselves), which allows a caller to  
check for logins without causing the user to be prompted for a master  
password to decrypt the logins.  
  
@param aHostname  
       The hostname to restrict searches to. Specify an empty string  
       to match all hosts. A null value will not match any logins, and  
       will thus always return a count of 0.  
@param aActionURL  
       The URL to which a form login will be submitted. To match any  
       form login, specify an empty string. To not match any form  
       login, specify null.  
@param aHttpRealm  
       The HTTP Realm for which the login applies. To match logins for  
       any realm, specify an empty string. To not match logins for any  
       realm, specify null.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aHostname</td>
<td>       The hostname to restrict searches to. Specify an empty string  
       to match all hosts. A null value will not match any logins, and  
       will thus always return a count of 0.  
</td>
</tr>

<tr>
<td>aActionURL</td>
<td>       The URL to which a form login will be submitted. To match any  
       form login, specify an empty string. To not match any form  
       login, specify null.  
</td>
</tr>

<tr>
<td>aHttpRealm</td>
<td>       The HTTP Realm for which the login applies. To match logins for  
       any realm, specify an empty string. To not match logins for any  
       realm, specify null.  
</td>
</tr>

</table>

## Attributes ##

### uiBusy ###
<pre>  
True when a master password prompt is being shown.  
  
</pre>
### isLoggedIn ###
<pre>  
True when the master password has already been entered, and so a caller  
can ask for decrypted logins without triggering a prompt.  
  
</pre>