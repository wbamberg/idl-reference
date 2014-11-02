---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/protocol/http/nsIHttpAuthManager.idl">Source file</a>
</div>

# nsIHttpAuthManager #
  
nsIHttpAuthManager  
  
This service provides access to cached HTTP authentication  
user credentials (domain, username, password) for sites  
visited during the current browser session.  
  
This interface exists to provide other HTTP stacks with the  
ability to share HTTP authentication credentials with Necko.  
This is currently used by the Java plugin (version 1.5 and  
higher) to avoid duplicate authentication prompts when the  
Java client fetches content from a HTTP site that the user  
has already logged into.  
  

## Methods ##

### getAuthIdentity(aScheme, aHost, aPort, aAuthType, aRealm, aPath, aUserDomain, aUserName, aUserPassword, aIsPrivate, aPrincipal) ###
  
Lookup auth identity.  
  
@param aScheme  
       the URL scheme (e.g., "http").  NOTE: for proxy authentication,  
       this should be "http" (this includes authentication for CONNECT  
       tunneling).  
@param aHost  
       the host of the server issuing a challenge (ASCII only).  
@param aPort  
       the port of the server issuing a challenge.  
@param aAuthType  
       optional string identifying auth type used (e.g., "basic")  
@param aRealm  
       optional string identifying auth realm.  
@param aPath  
       optional string identifying auth path. empty for proxy auth.  
@param aUserDomain  
       return value containing user domain.  
@param aUserName  
       return value containing user name.  
@param aUserPassword  
       return value containing user password.  
@param aIsPrivate  
       whether to look up a private or public identity (they are  
       stored separately, for use by private browsing)  
@param aPrincipal  
       the principal from which to derive information about which  
       app/mozbrowser is in use for this request  
  

#### Parameters ####

<table>

<tr>
<td>aScheme</td>
<td>       the URL scheme (e.g., "http").  NOTE: for proxy authentication,  
       this should be "http" (this includes authentication for CONNECT  
       tunneling).  
</td>
</tr>

<tr>
<td>aHost</td>
<td>       the host of the server issuing a challenge (ASCII only).  
</td>
</tr>

<tr>
<td>aPort</td>
<td>       the port of the server issuing a challenge.  
</td>
</tr>

<tr>
<td>aAuthType</td>
<td>       optional string identifying auth type used (e.g., "basic")  
</td>
</tr>

<tr>
<td>aRealm</td>
<td>       optional string identifying auth realm.  
</td>
</tr>

<tr>
<td>aPath</td>
<td>       optional string identifying auth path. empty for proxy auth.  
</td>
</tr>

<tr>
<td>aUserDomain</td>
<td>       return value containing user domain.  
</td>
</tr>

<tr>
<td>aUserName</td>
<td>       return value containing user name.  
</td>
</tr>

<tr>
<td>aUserPassword</td>
<td>       return value containing user password.  
</td>
</tr>

<tr>
<td>aIsPrivate</td>
<td>       whether to look up a private or public identity (they are  
       stored separately, for use by private browsing)  
</td>
</tr>

<tr>
<td>aPrincipal</td>
<td>       the principal from which to derive information about which  
       app/mozbrowser is in use for this request  
</td>
</tr>

</table>

### setAuthIdentity(aScheme, aHost, aPort, aAuthType, aRealm, aPath, aUserDomain, aUserName, aUserPassword, aIsPrivate, aPrincipal) ###
  
Store auth identity.  
  
@param aScheme  
       the URL scheme (e.g., "http").  NOTE: for proxy authentication,  
       this should be "http" (this includes authentication for CONNECT  
       tunneling).  
@param aHost  
       the host of the server issuing a challenge (ASCII only).  
@param aPort  
       the port of the server issuing a challenge.  
@param aAuthType  
       optional string identifying auth type used (e.g., "basic")  
@param aRealm  
       optional string identifying auth realm.  
@param aPath  
       optional string identifying auth path. empty for proxy auth.  
@param aUserDomain  
       optional string containing user domain.  
@param aUserName  
       optional string containing user name.  
@param aUserPassword  
       optional string containing user password.  
@param aIsPrivate  
       whether to store a private or public identity (they are  
       stored separately, for use by private browsing)  
@param aPrincipal  
       the principal from which to derive information about which  
       app/mozbrowser is in use for this request  
  

#### Parameters ####

<table>

<tr>
<td>aScheme</td>
<td>       the URL scheme (e.g., "http").  NOTE: for proxy authentication,  
       this should be "http" (this includes authentication for CONNECT  
       tunneling).  
</td>
</tr>

<tr>
<td>aHost</td>
<td>       the host of the server issuing a challenge (ASCII only).  
</td>
</tr>

<tr>
<td>aPort</td>
<td>       the port of the server issuing a challenge.  
</td>
</tr>

<tr>
<td>aAuthType</td>
<td>       optional string identifying auth type used (e.g., "basic")  
</td>
</tr>

<tr>
<td>aRealm</td>
<td>       optional string identifying auth realm.  
</td>
</tr>

<tr>
<td>aPath</td>
<td>       optional string identifying auth path. empty for proxy auth.  
</td>
</tr>

<tr>
<td>aUserDomain</td>
<td>       optional string containing user domain.  
</td>
</tr>

<tr>
<td>aUserName</td>
<td>       optional string containing user name.  
</td>
</tr>

<tr>
<td>aUserPassword</td>
<td>       optional string containing user password.  
</td>
</tr>

<tr>
<td>aIsPrivate</td>
<td>       whether to store a private or public identity (they are  
       stored separately, for use by private browsing)  
</td>
</tr>

<tr>
<td>aPrincipal</td>
<td>       the principal from which to derive information about which  
       app/mozbrowser is in use for this request  
</td>
</tr>

</table>

### clearAll() ###
  
Clear all auth cache.  
  
