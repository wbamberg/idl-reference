---
layout: default
---

# fuelIAnnotations #
  
Interface representing a collection of annotations associated  
with a bookmark or bookmark folder.  
  

## Methods ##

### has(aName) ###
  
Determines if an annotation exists with the given name.  
@param   aName  
         The name of the annotation  
@returns true if an annotation exists with the given name,  
         false otherwise.  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>aName  
         The name of the annotation  
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
@param   aName  
         The name of the annotation  
@returns A variant containing the value of the annotation. Supports  
         string, boolean and number.  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>aName  
         The name of the annotation  
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
@param   aName  
         The name of the annotation  
@param   aValue  
         The new value of the annotation. Supports string, boolean  
         and number  
@param   aExpiration  
         The expiration policy for the annotation.  
         See nsIAnnotationService.  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>aName  
         The name of the annotation  
</td>
</tr>

<tr>
<td></td>
<td>aValue  
         The new value of the annotation. Supports string, boolean  
         and number  
</td>
</tr>

<tr>
<td></td>
<td>aExpiration  
         The expiration policy for the annotation.  
         See nsIAnnotationService.  
</td>
</tr>

</table>

### remove(aName) ###
  
Removes the named annotation from the owner item.  
@param   aName  
         The name of annotation.  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>aName  
         The name of annotation.  
</td>
</tr>

</table>

## Attributes ##

### names ###
  
Array of the annotation names associated with the owning item  
  
