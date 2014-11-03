---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsISiteSecurityService.idl">Source file</a>
</div>

# nsISiteSecurityService #

## Methods ##

### processHeader(aType, aSourceURI, aHeader, aSSLStatus, aFlags, aMaxAge, aIncludeSubdomains) ###
<code>  
Parses a given HTTP header and records the results internally.  
Currently two header types are supported: HSTS (aka STS) and HPKP  
The format of the HSTS header is defined by the HSTS specification:  
https://tools.ietf.org/html/rfc6797  
and allows a host to specify that future HTTP requests should be  
upgraded to HTTPS.  
The Format of the HPKP header is currently defined by:  
https://tools.ietf.org/html/draft-ietf-websec-key-pinning-20  
and allows a host to speficy a subset of trusted anchors to be used  
in future HTTPS connections.  
  
@param aType the type of security header in question.  
@param aSourceURI the URI of the resource with the HTTP header.  
@param aSSLStatus the SSLStatus of the current channel  
@param aHeader the HTTP response header specifying security data.  
@param aFlags  options for this request as defined in nsISocketProvider:  
                 NO_PERMANENT_STORAGE  
@param aMaxAge the parsed max-age directive of the header.  
@param aIncludeSubdomains the parsed includeSubdomains directive.  
@return NS_OK            if it succeeds  
        NS_ERROR_FAILURE if it can't be parsed  
        NS_SUCCESS_LOSS_OF_INSIGNIFICANT_DATA  
                         if there are unrecognized tokens in the header.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aType</td>
<td>the type of security header in question.  
</td>
</tr>

<tr>
<td>aSourceURI</td>
<td>the URI of the resource with the HTTP header.  
</td>
</tr>

<tr>
<td>aSSLStatus</td>
<td>the SSLStatus of the current channel  
</td>
</tr>

<tr>
<td>aHeader</td>
<td>the HTTP response header specifying security data.  
</td>
</tr>

<tr>
<td>aFlags</td>
<td>options for this request as defined in nsISocketProvider:  
                 NO_PERMANENT_STORAGE  
</td>
</tr>

<tr>
<td>aMaxAge</td>
<td>the parsed max-age directive of the header.  
</td>
</tr>

<tr>
<td>aIncludeSubdomains</td>
<td>the parsed includeSubdomains directive.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>NS_OK            if it succeeds  
        NS_ERROR_FAILURE if it can't be parsed  
        NS_SUCCESS_LOSS_OF_INSIGNIFICANT_DATA  
                         if there are unrecognized tokens in the header.  
</td>
</tr>

</table>

### unsafeProcessHeader(aType, aSourceURI, aHeader, aFlags, aMaxAge, aIncludeSubdomains) ###
<code>  
Same as processHeader but without checking for the security properties  
of the connection. Use ONLY for testing.  
  
</code>
### removeState(aType, aURI, aFlags) ###
<code>  
Given a header type, removes state relating to that header of a host,  
including the includeSubdomains state that would affect subdomains.  
This essentially removes the state for the domain tree rooted at this  
host.  
@param aType   the type of security state in question  
@param aURI    the URI of the target host  
@param aFlags  options for this request as defined in nsISocketProvider:  
                 NO_PERMANENT_STORAGE  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aType</td>
<td>the type of security state in question  
</td>
</tr>

<tr>
<td>aURI</td>
<td>the URI of the target host  
</td>
</tr>

<tr>
<td>aFlags</td>
<td>options for this request as defined in nsISocketProvider:  
                 NO_PERMANENT_STORAGE  
</td>
</tr>

</table>

### isSecureHost(aType, aHost, aFlags) ###
<code>  
See isSecureURI  
  
@param aType the type of security state in question.  
@param aHost the hostname (punycode) to query for state.  
@param aFlags  options for this request as defined in nsISocketProvider:  
                 NO_PERMANENT_STORAGE  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aType</td>
<td>the type of security state in question.  
</td>
</tr>

<tr>
<td>aHost</td>
<td>the hostname (punycode) to query for state.  
</td>
</tr>

<tr>
<td>aFlags</td>
<td>options for this request as defined in nsISocketProvider:  
                 NO_PERMANENT_STORAGE  
</td>
</tr>

</table>

### shouldIgnoreHeaders(aSecurityInfo) ###
<code>  
Checks if the given security info is for a host with a broken  
transport layer (certificate errors like invalid CN).  
  
</code>
### isSecureURI(aType, aURI, aFlags) ###
<code>  
Checks whether or not the URI's hostname has a given security state set.  
For example, for HSTS:  
The URI is an HSTS URI if either the host has the HSTS state set, or one  
of its super-domains has the HSTS "includeSubdomains" flag set.  
NOTE: this function makes decisions based only on the  
host contained in the URI, and disregards other portions of the URI  
such as path and port.  
  
@param aType the type of security state in question.  
@param aURI the URI to query for STS state.  
@param aFlags  options for this request as defined in nsISocketProvider:  
                 NO_PERMANENT_STORAGE  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aType</td>
<td>the type of security state in question.  
</td>
</tr>

<tr>
<td>aURI</td>
<td>the URI to query for STS state.  
</td>
</tr>

<tr>
<td>aFlags</td>
<td>options for this request as defined in nsISocketProvider:  
                 NO_PERMANENT_STORAGE  
</td>
</tr>

</table>

### clearAll() ###
<code>  
Removes all security state by resetting to factory-original settings.  
  
</code>
### getKeyPinsForHostname(aHostname, evalTime, aPinArray, aIncludeSubdomains) ###
<code>  
Returns an array of sha256-hashed key pins for the given domain, if any.  
If these pins also apply to subdomains of the given domain,  
aIncludeSubdomains will be true. Pins returned are only for non-built-in  
pin entries.  
  
@param aHostname the hosname (punycode) to be queried about  
@param the time at which the pins should be valid. This is in  
mozilla::pkix::Time which uses internally seconds since 0 AD.  
@param aPinArray the set of sha256-hashed key pins for the given domain  
@param aIncludeSubdomains true if the pins apply to subdomains of the  
       given domain  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aHostname</td>
<td>the hosname (punycode) to be queried about  
</td>
</tr>

<tr>
<td>the</td>
<td>time at which the pins should be valid. This is in  
mozilla::pkix::Time which uses internally seconds since 0 AD.  
</td>
</tr>

<tr>
<td>aPinArray</td>
<td>the set of sha256-hashed key pins for the given domain  
</td>
</tr>

<tr>
<td>aIncludeSubdomains</td>
<td>true if the pins apply to subdomains of the  
       given domain  
</td>
</tr>

</table>

### setKeyPins(aHost, aIncludeSubdomains, aMaxAge, aPinCount, aSha256Pins) ###
<code>  
Set public-key pins for a host. The resulting pins will be permanent  
and visible from private and non-private contexts. These pins replace  
any already set by this mechanism or those built-in to Gecko.  
  
@param aHost the hostname (punycode) that pins will apply to  
@param aIncludeSubdomains whether these pins also apply to subdomains  
@param aMaxAge lifetime (in seconds) of this pin set  
@param aPinCount number of keys being pinnned  
@param aSha256Pins array of hashed key fingerprints (SHA-256, base64)  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aHost</td>
<td>the hostname (punycode) that pins will apply to  
</td>
</tr>

<tr>
<td>aIncludeSubdomains</td>
<td>whether these pins also apply to subdomains  
</td>
</tr>

<tr>
<td>aMaxAge</td>
<td>lifetime (in seconds) of this pin set  
</td>
</tr>

<tr>
<td>aPinCount</td>
<td>number of keys being pinnned  
</td>
</tr>

<tr>
<td>aSha256Pins</td>
<td>array of hashed key fingerprints (SHA-256, base64)  
</td>
</tr>

</table>

## Constants ##

### HEADER_HSTS ###

### HEADER_HPKP ###

### HEADER_OMS ###
