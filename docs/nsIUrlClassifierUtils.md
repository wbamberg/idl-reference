---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/url-classifier/nsIUrlClassifierUtils.idl">Source file</a>
</div>

# nsIUrlClassifierUtils #

## Methods ##

### getKeyForURI(uri) ###
  
Get the lookup string for a given URI.  This normalizes the hostname,  
url-decodes the string, and strips off the protocol.  
  
@param uri URI to get the lookup key for.  
  
@returns String containing the canonicalized URI.  
  

#### Parameters ####

<table>

<tr>
<td>uri</td>
<td>URI to get the lookup key for.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>String containing the canonicalized URI.  
</td>
</tr>

</table>
