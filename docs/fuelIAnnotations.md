---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/browser/fuel/fuelIApplication.idl">Source file</a>
</div>

# fuelIAnnotations #
<pre>  
Interface representing a collection of annotations associated  
with a bookmark or bookmark folder.  
  
</pre>
## Methods ##

### has(aName) ###
<pre>  
Determines if an annotation exists with the given name.  
@param   aName  
         The name of the annotation  
@returns true if an annotation exists with the given name,  
         false otherwise.  
  
</pre>
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
<pre>  
Gets the value of an annotation with the given name.  
@param   aName  
         The name of the annotation  
@returns A variant containing the value of the annotation. Supports  
         string, boolean and number.  
  
</pre>
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
<pre>  
Sets the value of an annotation with the given name.  
@param   aName  
         The name of the annotation  
@param   aValue  
         The new value of the annotation. Supports string, boolean  
         and number  
@param   aExpiration  
         The expiration policy for the annotation.  
         See nsIAnnotationService.  
  
</pre>
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
<pre>  
Removes the named annotation from the owner item.  
@param   aName  
         The name of annotation.  
  
</pre>
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
<pre>  
Array of the annotation names associated with the owning item  
  
</pre>