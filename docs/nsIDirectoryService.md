---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/io/nsIDirectoryService.idl">Source file</a>
</div>

# nsIDirectoryService #
  
nsIDirectoryService  
  

## Methods ##

### init() ###
  
init  
  
Must be called. Used internally by XPCOM initialization.  
  
  

### registerProvider(prov) ###
  
registerProvider  
  
Register a provider with the service.  
  
@param prov            The service will keep a strong reference  
                       to this object. It will be released when  
                       the service is released.  
  
  

#### Parameters ####

<table>

<tr>
<td>prov</td>
<td>The service will keep a strong reference  
                       to this object. It will be released when  
                       the service is released.  
</td>
</tr>

</table>

### unregisterProvider(prov) ###
  
unregisterProvider  
  
Unregister a provider with the service.  
  
@param prov              
  
  

#### Parameters ####

<table>

<tr>
<td>prov</td>
<td></td>
</tr>

</table>
