---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/mozIThirdPartyUtil.idl">Source file</a>
</div>

# mozIThirdPartyUtil #
  
Utility functions for determining whether a given URI, channel, or window  
hierarchy is third party with respect to a known URI.  
  

## Methods ##

### isThirdPartyURI(aFirstURI, aSecondURI) ###
  
isThirdPartyURI  
  
Determine whether two URIs are third party with respect to each other.  
This is determined by computing the base domain for both URIs. If they can  
be determined, and the base domains match, the request is defined as first  
party. If it cannot be determined because one or both URIs do not have a  
base domain (for instance, in the case of IP addresses, host aliases such  
as 'localhost', or a file:// URI), an exact string comparison on host is  
performed.  
  
For example, the URI "http://mail.google.com/" is not third party with  
respect to "http://images.google.com/", but "http://mail.yahoo.com/" and  
"http://192.168.1.1/" are.  
  
  
@throws if either URI is null, has a malformed host, or has an empty host  
        and is not a file:// URI.  
  

#### Returns ####

<table>

<tr>
<td>true if aFirstURI is third party with respect to aSecondURI.  
</td>
</tr>

</table>

### isThirdPartyWindow(aWindow, aURI) ###
  
isThirdPartyWindow  
  
Determine whether the given window hierarchy is third party. This is done  
as follows:  
  
1) Obtain the URI of the principal associated with 'aWindow'. Call this the  
   'bottom URI'.  
2) If 'aURI' is provided, determine if it is third party with respect to  
   the bottom URI. If so, return.  
3) Find the same-type parent window, if there is one, and its URI.  
   Determine whether it is third party with respect to the bottom URI. If  
   so, return.  
  
Therefore, each level in the window hierarchy is tested. (This means that  
nested iframes with different base domains, even though the bottommost and  
topmost URIs might be equal, will be considered third party.)  
  
  
For example, if 'aURI' is "http://mail.google.com/", 'aWindow' has a URI  
of "http://google.com/", and its parent is the topmost content window with  
a URI of "http://mozilla.com", the result will be true.  
  
  
@throws if aWindow is null; the same-type parent of any window in the  
        hierarchy cannot be determined; or the URI associated with any  
        window in the hierarchy is null, has a malformed host, or has an  
        empty host and is not a file:// URI.  
  
@see isThirdPartyURI  
  

#### Parameters ####

<table>

<tr>
<td>aWindow</td>
<td>       The bottommost window in the hierarchy.  
</td>
</tr>

<tr>
<td>aURI</td>
<td>       A URI to test against. If null, the URI of the principal  
       associated with 'aWindow' will be used.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>true if 'aURI' is third party with respect to any of the URIs  
        associated with aWindow and its same-type parents.  
</td>
</tr>

</table>

### isThirdPartyChannel(aChannel, aURI) ###
  
isThirdPartyChannel  
  
Determine whether the given channel and its content window hierarchy is  
third party. This is done as follows:  
  
1) If 'aChannel' is an nsIHttpChannel and has the  
   'forceAllowThirdPartyCookie' property set, then:  
   a) If 'aURI' is null, return false.  
   b) Otherwise, find the URI of the channel, determine whether it is  
      foreign with respect to 'aURI', and return.  
2) Find the URI of the channel and determine whether it is third party with  
   respect to the URI of the channel. If so, return.  
3) Obtain the bottommost nsIDOMWindow, and its same-type parent if it  
   exists, from the channel's notification callbacks. Then:  
   a) If the parent is the same as the bottommost window, and the channel  
      has the LOAD_DOCUMENT_URI flag set, return false. This represents the  
      case where a toplevel load is occurring and the window's URI has not  
      yet been updated. (We have already checked that 'aURI' is not foreign  
      with respect to the channel URI.)  
   b) Otherwise, return the result of isThirdPartyWindow with arguments  
      of the channel's bottommost window and the channel URI, respectively.  
  
Therefore, both the channel's URI and each level in the window hierarchy  
associated with the channel is tested.  
  
  
For example, if 'aURI' is "http://mail.google.com/", 'aChannel' has a URI  
of "http://google.com/", and its parent is the topmost content window with  
a URI of "http://mozilla.com", the result will be true.  
  
  
@throws if 'aChannel' is null; the channel has no notification callbacks or  
        an associated window; or isThirdPartyWindow throws.  
  
@see isThirdPartyWindow  
  

#### Parameters ####

<table>

<tr>
<td>aChannel</td>
<td>       The channel associated with the load.  
</td>
</tr>

<tr>
<td>aURI</td>
<td>       A URI to test against. If null, the URI of the channel will be used.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>true if aURI is third party with respect to the channel URI or any  
        of the URIs associated with the same-type window hierarchy of the  
        channel.  
</td>
</tr>

</table>

### getBaseDomain(aHostURI) ###
  
getBaseDomain  
  
Get the base domain for aHostURI; e.g. for "www.bbc.co.uk", this would be  
"bbc.co.uk". Only properly-formed URI's are tolerated, though a trailing  
dot may be present. If aHostURI is an IP address, an alias such as  
'localhost', an eTLD such as 'co.uk', or the empty string, aBaseDomain will  
be the exact host. The result of this function should only be used in exact  
string comparisons, since substring comparisons will not be valid for the  
special cases elided above.  
  
  
  

#### Parameters ####

<table>

<tr>
<td>aHostURI</td>
<td>       The URI to analyze.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>the base domain.  
</td>
</tr>

</table>

### getURIFromWindow(aWindow) ###
  
getURIFromWindow  
  
Returns the URI associated with the script object principal for the  
window.  
  

### getTopWindowForChannel(aChannel) ###
  
getTopWindowForChannel  
  
Returns the top-level window associated with the given channel.  
  
