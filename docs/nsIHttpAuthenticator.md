---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/protocol/http/nsIHttpAuthenticator.idl">Source file</a>
</div>

# nsIHttpAuthenticator #
  
nsIHttpAuthenticator  
  
Interface designed to allow for pluggable HTTP authentication modules.  
Implementations are registered under the ContractID:  
  
  "@mozilla.org/network/http-authenticator;1?scheme=<auth-scheme>"  
  
where <auth-scheme> is the lower-cased value of the authentication scheme  
found in the server challenge per the rules of RFC 2617.  
  

## Methods ##

### challengeReceived(aChannel, aChallenge, aProxyAuth, aSessionState, aContinuationState, aInvalidatesIdentity) ###
  
Upon receipt of a server challenge, this function is called to determine  
whether or not the current user identity has been rejected.  If true,  
then the user will be prompted by the channel to enter (or revise) their  
identity.  Following this, generateCredentials will be called.  
  
If the IDENTITY_IGNORED auth flag is set, then the aInvalidateIdentity  
return value will be ignored, and user prompting will be suppressed.  
  
@param aChannel  
       the http channel that received the challenge.  
@param aChallenge  
       the challenge from the WWW-Authenticate/Proxy-Authenticate  
       server response header.  (possibly from the auth cache.)  
@param aProxyAuth  
       flag indicating whether or not aChallenge is from a proxy.  
@param aSessionState  
       see description below for generateCredentials.  
@param aContinuationState  
       see description below for generateCredentials.  
@param aInvalidateIdentity  
       return value indicating whether or not to prompt the user for a  
       revised identity.  
  

#### Parameters ####

<table>

<tr>
<td>aChannel</td>
<td>       the http channel that received the challenge.  
</td>
</tr>

<tr>
<td>aChallenge</td>
<td>       the challenge from the WWW-Authenticate/Proxy-Authenticate  
       server response header.  (possibly from the auth cache.)  
</td>
</tr>

<tr>
<td>aProxyAuth</td>
<td>       flag indicating whether or not aChallenge is from a proxy.  
</td>
</tr>

<tr>
<td>aSessionState</td>
<td>       see description below for generateCredentials.  
</td>
</tr>

<tr>
<td>aContinuationState</td>
<td>       see description below for generateCredentials.  
</td>
</tr>

<tr>
<td>aInvalidateIdentity</td>
<td>       return value indicating whether or not to prompt the user for a  
       revised identity.  
</td>
</tr>

</table>

### generateCredentials(aChannel, aChallenge, aProxyAuth, aDomain, aUser, aPassword, aSessionState, aContinuationState, aFlags) ###
  
Called to generate the authentication credentials for a particular  
server/proxy challenge.  This is the value that will be sent back  
to the server via an Authorization/Proxy-Authorization header.  
  
This function may be called using a cached challenge provided the  
authenticator sets the REUSABLE_CHALLENGE flag.  
  
@param aChannel  
       the http channel requesting credentials  
@param aChallenge  
       the challenge from the WWW-Authenticate/Proxy-Authenticate  
       server response header.  (possibly from the auth cache.)  
@param aProxyAuth  
       flag indicating whether or not aChallenge is from a proxy.  
@param aDomain  
       string containing the domain name (if appropriate)  
@param aUser  
       string containing the user name  
@param aPassword  
       string containing the password  
@param aSessionState  
       state stored along side the user's identity in the auth cache  
       for the lifetime of the browser session.  if a new auth cache  
       entry is created for this challenge, then this parameter will  
       be null.  on return, the result will be stored in the new auth  
       cache entry.  this parameter is non-null when an auth cache entry  
       is being reused.  
@param aContinuationState  
       state held by the channel between consecutive calls to  
       generateCredentials, assuming multiple calls are required  
       to authenticate.  this state is held for at most the lifetime of  
       the channel.  
@param aFlags  
       authenticator may return one of the generate flags bellow.  
  

#### Parameters ####

<table>

<tr>
<td>aChannel</td>
<td>       the http channel requesting credentials  
</td>
</tr>

<tr>
<td>aChallenge</td>
<td>       the challenge from the WWW-Authenticate/Proxy-Authenticate  
       server response header.  (possibly from the auth cache.)  
</td>
</tr>

<tr>
<td>aProxyAuth</td>
<td>       flag indicating whether or not aChallenge is from a proxy.  
</td>
</tr>

<tr>
<td>aDomain</td>
<td>       string containing the domain name (if appropriate)  
</td>
</tr>

<tr>
<td>aUser</td>
<td>       string containing the user name  
</td>
</tr>

<tr>
<td>aPassword</td>
<td>       string containing the password  
</td>
</tr>

<tr>
<td>aSessionState</td>
<td>       state stored along side the user's identity in the auth cache  
       for the lifetime of the browser session.  if a new auth cache  
       entry is created for this challenge, then this parameter will  
       be null.  on return, the result will be stored in the new auth  
       cache entry.  this parameter is non-null when an auth cache entry  
       is being reused.  
</td>
</tr>

<tr>
<td>aContinuationState</td>
<td>       state held by the channel between consecutive calls to  
       generateCredentials, assuming multiple calls are required  
       to authenticate.  this state is held for at most the lifetime of  
       the channel.  
</td>
</tr>

<tr>
<td>aFlags</td>
<td>       authenticator may return one of the generate flags bellow.  
</td>
</tr>

</table>

## Attributes ##

### authFlags ###
  
Flags defining various properties of the authenticator.  
  

## Constants ##

### USING_INTERNAL_IDENTITY ###
  
Generate flags  
  
  
Indicates that the authenticator has used an out-of-band or internal  
source of identity and tells the consumer that it must not cache  
the returned identity because it might not be valid and would overwrite  
the cached identity.  See bug 542318 comment 32.  
  

### REQUEST_BASED ###
  
A request based authentication scheme only authenticates an individual  
request (or a set of requests under the same authentication domain as  
defined by RFC 2617).  BASIC and DIGEST are request based authentication  
schemes.  
  

### CONNECTION_BASED ###
  
A connection based authentication scheme authenticates an individual  
connection.  Multiple requests may be issued over the connection without  
repeating the authentication steps.  Connection based authentication  
schemes can associate state with the connection being authenticated via  
the aContinuationState parameter (see generateCredentials).  
  

### REUSABLE_CREDENTIALS ###
  
The credentials returned from generateCredentials may be reused with any  
other URLs within "the protection space" as defined by RFC 2617 section  
1.2.  If this flag is not set, then generateCredentials must be called  
for each request within the protection space.  REUSABLE_CREDENTIALS  
implies REUSABLE_CHALLENGE.  
  

### REUSABLE_CHALLENGE ###
  
A challenge may be reused to later generate credentials in anticipation  
of a duplicate server challenge for URLs within "the protection space"  
as defined by RFC 2617 section 1.2.  
  

### IDENTITY_IGNORED ###
  
This flag indicates that the identity of the user is not required by  
this authentication scheme.  
  

### IDENTITY_INCLUDES_DOMAIN ###
  
This flag indicates that the identity of the user includes a domain  
attribute that the user must supply.  
  

### IDENTITY_ENCRYPTED ###
  
This flag indicates that the identity will be sent encrypted. It does  
not make sense to combine this flag with IDENTITY_IGNORED.  
  
