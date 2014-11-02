---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/io/nsIDirectoryService.idl">Source file</a>
</div>
# nsIDirectoryServiceProvider #
  
nsIDirectoryServiceProvider  
  
Used by Directory Service to get file locations.  
  

## Methods ##

### getFile(prop, persistent) ###
  
getFile  
  
Directory Service calls this when it gets the first request for  
a prop or on every request if the prop is not persistent.  
  
@param prop         The symbolic name of the file.  
@param persistent   TRUE - The returned file will be cached by Directory  
                    Service. Subsequent requests for this prop will  
                    bypass the provider and use the cache.  
                    FALSE - The provider will be asked for this prop  
                    each time it is requested.  
  
@return             The file represented by the property.  
  
  

#### Parameters ####

<table>

<tr>
<td>prop</td>
<td>The symbolic name of the file.  
</td>
</tr>

<tr>
<td>persistent</td>
<td>TRUE - The returned file will be cached by Directory  
                    Service. Subsequent requests for this prop will  
                    bypass the provider and use the cache.  
                    FALSE - The provider will be asked for this prop  
                    each time it is requested.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The file represented by the property.  
</td>
</tr>

</table>
