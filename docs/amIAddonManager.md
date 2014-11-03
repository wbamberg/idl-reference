---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/mozapps/extensions/amIAddonManager.idl">Source file</a>
</div>

# amIAddonManager #
<pre>  
A service to make some AddonManager functionality available to C++ callers.  
Javascript callers should still use AddonManager.jsm directly.  
  
</pre>
## Methods ##

### mapURIToAddonID(aURI, aID) ###
<pre>  
Synchronously map a URI to the corresponding Addon ID.  
  
Mappable URIs are limited to in-application resources belonging to the  
add-on, such as Javascript compartments, XUL windows, XBL bindings, etc.  
but do not include URIs from meta data, such as the add-on homepage.  
  
@param  aURI  
        The nsIURI to map  
@return  
        true if the URI has been mapped successfully to an Addon ID  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>        The nsIURI to map  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>        true if the URI has been mapped successfully to an Addon ID  
</td>
</tr>

</table>
