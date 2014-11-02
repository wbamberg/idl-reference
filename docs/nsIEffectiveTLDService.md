---
layout: default
---

# nsIEffectiveTLDService #

## Methods ##

### getPublicSuffix(aURI) ###
  
Returns the public suffix of a URI. A public suffix is the highest-level domain  
under which individual domains may be registered; it may therefore contain one  
or more dots. For example, the public suffix for "www.bbc.co.uk" is "co.uk",  
because the .uk TLD does not allow the registration of domains at the  
second level ("bbc.uk" is forbidden).  
  
The public suffix will be returned encoded in ASCII/ACE and will be normalized  
according to RFC 3454, i.e. the same encoding returned by nsIURI::GetAsciiHost().  
If consumers wish to compare the result of this method against the host from  
another nsIURI, the host should be obtained using nsIURI::GetAsciiHost().  
In the case of nested URIs, the innermost URI will be used.  
  
@param   aURI   The URI to be analyzed  
  
@returns the public suffix  
  
@throws NS_ERROR_UNEXPECTED   
        or other error returned by nsIIDNService::normalize when   
        the hostname contains characters disallowed in URIs  
@throws NS_ERROR_HOST_IS_IP_ADDRESS  
        if the host is a numeric IPv4 or IPv6 address (as determined by  
        the success of a call to PR_StringToNetAddr()).  
  

#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>The URI to be analyzed  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>the public suffix  
</td>
</tr>

</table>

### getBaseDomain(aURI, aAdditionalParts) ###
  
Returns the base domain of a URI; that is, the public suffix with a given  
number of additional domain name parts. For example, the result of this method  
for "www.bbc.co.uk", depending on the value of aAdditionalParts parameter, will  
be:  
  
   0 (default) -> bbc.co.uk  
   1           -> www.bbc.co.uk  
  
Similarly, the public suffix for "www.developer.mozilla.org" is "org", and the base  
domain will be:  
  
   0 (default) -> mozilla.org  
   1           -> developer.mozilla.org  
   2           -> www.developer.mozilla.org  
  
The base domain will be returned encoded in ASCII/ACE and will be normalized  
according to RFC 3454, i.e. the same encoding returned by nsIURI::GetAsciiHost().  
If consumers wish to compare the result of this method against the host from  
another nsIURI, the host should be obtained using nsIURI::GetAsciiHost().  
In the case of nested URIs, the innermost URI will be used.  
  
@param   aURI               The URI to be analyzed  
@param   aAdditionalParts   Number of domain name parts to be  
                            returned in addition to the public suffix  
  
@returns the base domain (public suffix plus the requested number of additional parts)  
  
@throws NS_ERROR_UNEXPECTED   
        or other error returned by nsIIDNService::normalize when   
        the hostname contains characters disallowed in URIs  
@throws NS_ERROR_INSUFFICIENT_DOMAIN_LEVELS  
        when there are insufficient subdomain levels in the hostname to satisfy the  
        requested aAdditionalParts value.  
@throws NS_ERROR_HOST_IS_IP_ADDRESS  
        if aHost is a numeric IPv4 or IPv6 address (as determined by  
        the success of a call to PR_StringToNetAddr()).  
  
@see    getPublicSuffix()  
  

#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>The URI to be analyzed  
</td>
</tr>

<tr>
<td>aAdditionalParts</td>
<td>Number of domain name parts to be  
                            returned in addition to the public suffix  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>the base domain (public suffix plus the requested number of additional parts)  
</td>
</tr>

</table>

### getPublicSuffixFromHost(aHost) ###
  
NOTE: It is strongly recommended to use getPublicSuffix() above if a suitable  
nsIURI is available. Only use this method if this is not the case.  
  
Returns the public suffix of a host string. Otherwise identical to getPublicSuffix().  
  
@param   aHost   The host to be analyzed. Any additional parts (e.g. scheme,  
                 port, or path) will cause this method to throw. ASCII/ACE and  
                 UTF8 encodings are acceptable as input; normalization will  
                 be performed as specified in getBaseDomain().  
  
@see     getPublicSuffix()  
  

#### Parameters ####

<table>

<tr>
<td>aHost</td>
<td>The host to be analyzed. Any additional parts (e.g. scheme,  
                 port, or path) will cause this method to throw. ASCII/ACE and  
                 UTF8 encodings are acceptable as input; normalization will  
                 be performed as specified in getBaseDomain().  
</td>
</tr>

</table>

### getBaseDomainFromHost(aHost, aAdditionalParts) ###
  
NOTE: It is strongly recommended to use getBaseDomain() above if a suitable  
nsIURI is available. Only use this method if this is not the case.  
  
Returns the base domain of a host string. Otherwise identical to getBaseDomain().  
  
@param   aHost   The host to be analyzed. Any additional parts (e.g. scheme,  
                 port, or path) will cause this method to throw. ASCII/ACE and  
                 UTF8 encodings are acceptable as input; normalization will  
                 be performed as specified in getBaseDomain().  
  
@see     getBaseDomain()  
  

#### Parameters ####

<table>

<tr>
<td>aHost</td>
<td>The host to be analyzed. Any additional parts (e.g. scheme,  
                 port, or path) will cause this method to throw. ASCII/ACE and  
                 UTF8 encodings are acceptable as input; normalization will  
                 be performed as specified in getBaseDomain().  
</td>
</tr>

</table>

### getNextSubDomain(aHost) ###
  
Returns the parent sub-domain of a host string. If the host is a base  
domain, it will throw NS_ERROR_INSUFFICIENT_DOMAIN_LEVELS.  
  
For example: "player.bbc.co.uk" would return "bbc.co.uk" and  
             "bbc.co.uk" would throw NS_ERROR_INSUFFICIENT_DOMAIN_LEVELS.  
  
@param   aHost   The host to be analyzed. Any additional parts (e.g. scheme,  
                 port, or path) will cause this method to throw. ASCII/ACE and  
                 UTF8 encodings are acceptable as input; normalization will  
                 be performed as specified in getBaseDomain().  
  

#### Parameters ####

<table>

<tr>
<td>aHost</td>
<td>The host to be analyzed. Any additional parts (e.g. scheme,  
                 port, or path) will cause this method to throw. ASCII/ACE and  
                 UTF8 encodings are acceptable as input; normalization will  
                 be performed as specified in getBaseDomain().  
</td>
</tr>

</table>
