---
layout: default
---

# nsIGlobalHistory2 #

## Methods ##

### addURI(aURI, aRedirect, aToplevel, aReferrer) ###
  
Add a URI to global history  
  
@param aURI      the URI of the page  
@param aRedirect whether the URI was redirected to another location;  
                 this is 'true' for the original URI which is  
                 redirected.  
@param aToplevel whether the URI is loaded in a top-level window  
@param aReferrer the URI of the referring page  
  
@note  Docshell will not filter out URI schemes like chrome: data:  
       about: and view-source:.  Embedders should consider filtering out  
       these schemes and others, e.g. mailbox: for the main URI and the  
       referrer.  
  

#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>the URI of the page  
</td>
</tr>

<tr>
<td>aRedirect</td>
<td>whether the URI was redirected to another location;  
                 this is 'true' for the original URI which is  
                 redirected.  
</td>
</tr>

<tr>
<td>aToplevel</td>
<td>whether the URI is loaded in a top-level window  
</td>
</tr>

<tr>
<td>aReferrer</td>
<td>the URI of the referring page  
</td>
</tr>

</table>

### isVisited(aURI) ###
  
Checks to see whether the given URI is in history.  
  
@param aURI the uri to the page  
@return true if a URI has been visited  
  

#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>the uri to the page  
</td>
</tr>

</table>

### setPageTitle(aURI, aTitle) ###
  
Set the page title for the given uri. URIs that are not already in  
global history will not be added.  
  
@param aURI    the URI for which to set to the title  
@param aTitle  the page title  
  

#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>the URI for which to set to the title  
</td>
</tr>

<tr>
<td>aTitle</td>
<td>the page title  
</td>
</tr>

</table>
