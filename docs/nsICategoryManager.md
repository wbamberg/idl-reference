---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/components/nsICategoryManager.idl">Source file</a>
</div>

# nsICategoryManager #

## Methods ##

### getCategoryEntry(aCategory, aEntry) ###
  
Get the value for the given category's entry.  
  

#### Parameters ####

<table>

<tr>
<td>aCategory</td>
<td>The name of the category ("protocol")  
</td>
</tr>

<tr>
<td>aEntry</td>
<td>The entry you're looking for ("http")  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The value.  
</td>
</tr>

</table>

### addCategoryEntry(aCategory, aEntry, aValue, aPersist, aReplace) ###
  
Add an entry to a category.  
  

#### Parameters ####

<table>

<tr>
<td>aCategory</td>
<td>The name of the category ("protocol")  
</td>
</tr>

<tr>
<td>aEntry</td>
<td>The entry to be added ("http")  
</td>
</tr>

<tr>
<td>aValue</td>
<td>The value for the entry ("moz.httprulez.1")  
</td>
</tr>

<tr>
<td>aPersist</td>
<td>Should this data persist between invocations?  
</td>
</tr>

<tr>
<td>aReplace</td>
<td>Should we replace an existing entry?  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>Previous entry, if any  
</td>
</tr>

</table>

### deleteCategoryEntry(aCategory, aEntry, aPersist) ###
  
Delete an entry from the category.  
  

#### Parameters ####

<table>

<tr>
<td>aCategory</td>
<td>The name of the category ("protocol")  
</td>
</tr>

<tr>
<td>aEntry</td>
<td>The entry to be added ("http")  
</td>
</tr>

<tr>
<td>aPersist</td>
<td>Delete persistent data from registry, if present?  
</td>
</tr>

</table>

### deleteCategory(aCategory) ###
  
Delete a category and all entries.  
  

#### Parameters ####

<table>

<tr>
<td>aCategory</td>
<td>The category to be deleted.  
</td>
</tr>

</table>

### enumerateCategory(aCategory) ###
  
Enumerate the entries in a category.  
  

#### Parameters ####

<table>

<tr>
<td>aCategory</td>
<td>The category to be enumerated.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>a simple enumerator, each result QIs to  
        nsISupportsCString.  
</td>
</tr>

</table>

### enumerateCategories() ###
  
Enumerate all existing categories  
  

#### Parameters ####

<table>

<tr>
<td>aCategory</td>
<td>The category to be enumerated.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>a simple enumerator, each result QIs to  
        nsISupportsCString.  
</td>
</tr>

</table>
