---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/browser/fuel/fuelIApplication.idl">Source file</a>
</div>

# fuelIAnnotations #
  
Interface representing a collection of annotations associated  
with a bookmark or bookmark folder.  
  

## Methods ##

### has(aName) ###
  
Determines if an annotation exists with the given name.  
  

#### Parameters ####

<table>

<tr>
<td>aName</td>
<td>         The name of the annotation  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>true if an annotation exists with the given name,  
         false otherwise.  
</td>
</tr>

</table>

### get(aName) ###
  
Gets the value of an annotation with the given name.  
  

#### Parameters ####

<table>

<tr>
<td>aName</td>
<td>         The name of the annotation  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>A variant containing the value of the annotation. Supports  
         string, boolean and number.  
</td>
</tr>

</table>

### set(aName, aValue, aExpiration) ###
  
Sets the value of an annotation with the given name.  
  

#### Parameters ####

<table>

<tr>
<td>aName</td>
<td>         The name of the annotation  
</td>
</tr>

<tr>
<td>aValue</td>
<td>         The new value of the annotation. Supports string, boolean  
         and number  
</td>
</tr>

<tr>
<td>aExpiration</td>
<td>         The expiration policy for the annotation.  
         See nsIAnnotationService.  
</td>
</tr>

</table>

### remove(aName) ###
  
Removes the named annotation from the owner item.  
  

#### Parameters ####

<table>

<tr>
<td>aName</td>
<td>         The name of annotation.  
</td>
</tr>

</table>

## Attributes ##

### names ###
  
Array of the annotation names associated with the owning item  
  
