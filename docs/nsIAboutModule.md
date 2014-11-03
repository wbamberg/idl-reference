---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/protocol/about/nsIAboutModule.idl">Source file</a>
</div>

# nsIAboutModule #

## Methods ##

### newChannel(aURI, aLoadInfo) ###
  
Constructs a new channel for the about protocol module.   
  
  

#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>the uri of the new channel  
</td>
</tr>

<tr>
<td>aLoadInfo</td>
<td>the loadinfo of the new channel  
</td>
</tr>

</table>

### getURIFlags(aURI) ###
  
A method to get the flags that apply to a given about: URI.  The URI  
passed in is guaranteed to be one of the URIs that this module  
registered to deal with.  
  

### getIndexedDBOriginPostfix(aURI) ###
  
Returns the Indexed DB origin's postfix used for the given about: URI.  
If the postfix returned is null then the URI's path (e.g. "home" for  
about:home) will be used to construct the origin.  
  

## Constants ##

### URI_SAFE_FOR_UNTRUSTED_CONTENT ###
  
A flag that indicates whether a URI is safe for untrusted  
content.  If it is, web pages and so forth will be allowed to  
link to this about: URI, and the about: protocol handler will  
enforce that the principal of channels created for it be based  
on their originalURI or URI (depending on the channel flags),  
by setting their "owner" to null.  
Otherwise, only chrome will be able to link to it.  
  

### ALLOW_SCRIPT ###
  
A flag that indicates whether script should be enabled for the  
given about: URI even if it's disabled in general.  
  

### HIDE_FROM_ABOUTABOUT ###
  
A flag that indicates whether this about: URI doesn't want to be listed  
in about:about, especially if it's not useful without a query string.  
  

### ENABLE_INDEXED_DB ###
  
A flag that indicates whether this about: URI wants Indexed DB enabled.  
  
