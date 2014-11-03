---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/exthelper/extIApplication.idl">Source file</a>
</div>

# extISessionStorage #
<pre>  
Interface representing a simple storage system  
  
</pre>
## Methods ##

### has(aName) ###
<pre>  
Determines if a storage item exists with the given name.  
@param   aName  
         The name of an item  
@returns true if an item exists with the given name,  
         false otherwise.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aName</td>
<td>         The name of an item  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>true if an item exists with the given name,  
         false otherwise.  
</td>
</tr>

</table>

### set(aName, aValue) ###
<pre>  
Sets the value of a storage item with the given name.  
@param   aName  
         The name of an item  
@param   aValue  
         The value to assign to the item  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aName</td>
<td>         The name of an item  
</td>
</tr>

<tr>
<td>aValue</td>
<td>         The value to assign to the item  
</td>
</tr>

</table>

### get(aName, aDefaultValue) ###
<pre>  
Gets the value of a storage item with the given name. Returns a  
default value if the item does not exist.  
@param   aName  
         The name of an item  
@param   aDefaultValue  
         The value to return if no item exists with the given name  
@returns value of the item or the given default value if no item  
         exists with the given name.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aName</td>
<td>         The name of an item  
</td>
</tr>

<tr>
<td>aDefaultValue</td>
<td>         The value to return if no item exists with the given name  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>value of the item or the given default value if no item  
         exists with the given name.  
</td>
</tr>

</table>

## Attributes ##

### events ###
<pre>  
The events object for the storage  
supports: "change"  
  
</pre>