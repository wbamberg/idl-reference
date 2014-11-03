---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/io/nsIDirectoryService.idl">Source file</a>
</div>

# nsIDirectoryService #
<pre>  
nsIDirectoryService  
  
</pre>
## Methods ##

### init() ###
<pre>  
init  
  
Must be called. Used internally by XPCOM initialization.  
  
  
</pre>
### registerProvider(prov) ###
<pre>  
registerProvider  
  
Register a provider with the service.  
  
@param prov            The service will keep a strong reference  
                       to this object. It will be released when  
                       the service is released.  
  
  
</pre>
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
<pre>  
unregisterProvider  
  
Unregister a provider with the service.  
  
@param prov              
  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>prov</td>
<td></td>
</tr>

</table>
