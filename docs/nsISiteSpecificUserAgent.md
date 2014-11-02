---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/base/nsISiteSpecificUserAgent.idl">Source file</a>
</div>

# nsISiteSpecificUserAgent #
  
nsISiteSpecificUserAgent provides you with site/window-specific User Agent strings.  
  

## Methods ##

### getUserAgentForURIAndWindow(aURI, aWindow) ###
  
Get the User Agent string for a given URI.  
  
@param aURI is the URI of the page the UA string is used for.  
  
@param aWindow is the window this UA is being requested for  
  
@returns the User Agent string for the given URI. If no override applies,  
the default User Agent string is used.  
  

#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>is the URI of the page the UA string is used for.  
</td>
</tr>

<tr>
<td>aWindow</td>
<td>is the window this UA is being requested for  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>the User Agent string for the given URI. If no override applies,  
the default User Agent string is used.  
</td>
</tr>

</table>
