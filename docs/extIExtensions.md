---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/exthelper/extIApplication.idl">Source file</a>
</div>

# extIExtensions #
<code>  
Interface representing a list of all installed extensions  
  
</code>
## Methods ##

### has(aId) ###
<code>  
Determines if an extension exists with the given id.  
@param   aId  
         The id of an extension  
@returns true if an extension exists with the given id,  
         false otherwise.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aId</td>
<td>         The id of an extension  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>true if an extension exists with the given id,  
         false otherwise.  
</td>
</tr>

</table>

### get(aId) ###
<code>  
Gets a extIExtension object for an extension.  
@param   aId  
         The id of an extension  
@returns An extension object or null if no extension exists  
         with the given id.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aId</td>
<td>         The id of an extension  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>An extension object or null if no extension exists  
         with the given id.  
</td>
</tr>

</table>

## Attributes ##

### all ###
  
Array of extIExtension listing all extensions in the application.  
  
