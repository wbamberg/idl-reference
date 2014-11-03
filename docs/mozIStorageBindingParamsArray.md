---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/storage/public/mozIStorageBindingParamsArray.idl">Source file</a>
</div>

# mozIStorageBindingParamsArray #

## Methods ##

### newBindingParams() ###
  
Creates a new mozIStorageBindingParams object that can be added to this  
array.  
  
  

#### Returns ####

<table>

<tr>
<td>a mozIStorageBindingParams object that can be used to specify  
        parameters that need to be bound.  
</td>
</tr>

</table>

### addParams(aParameters) ###
  
Adds the parameters to the end of this array.  
  
  

#### Parameters ####

<table>

<tr>
<td>aParameters</td>
<td>       The parameters to add to this array.  
</td>
</tr>

</table>

## Attributes ##

### length ###
  
The number of mozIStorageBindingParams this object contains.  
  
