---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/storage/public/mozIStorageBindingParams.idl">Source file</a>
</div>

# mozIStorageBindingParams #

## Methods ##

### bindByName(aName, aValue) ###
  
Binds aValue to the parameter with the name aName.  
  
@param aName  
       The name of the parameter to bind aValue to.  
@param aValue  
       The value to bind.  
  

#### Parameters ####

<table>

<tr>
<td>aName</td>
<td>       The name of the parameter to bind aValue to.  
</td>
</tr>

<tr>
<td>aValue</td>
<td>       The value to bind.  
</td>
</tr>

</table>

### bindUTF8StringByName(aName, aValue) ###

### bindStringByName(aName, aValue) ###

### bindDoubleByName(aName, aValue) ###

### bindInt32ByName(aName, aValue) ###

### bindInt64ByName(aName, aValue) ###

### bindNullByName(aName) ###

### bindBlobByName(aName, aValue, aValueSize) ###

### bindAdoptedBlobByName(aName, aValue, aValueSize) ###

### bindByIndex(aIndex, aValue) ###
  
Binds aValue to the parameter with the index aIndex.  
  
@param aIndex  
       The zero-based index of the parameter to bind aValue to.  
@param aValue  
       The value to bind.  
  

#### Parameters ####

<table>

<tr>
<td>aIndex</td>
<td>       The zero-based index of the parameter to bind aValue to.  
</td>
</tr>

<tr>
<td>aValue</td>
<td>       The value to bind.  
</td>
</tr>

</table>

### bindUTF8StringByIndex(aIndex, aValue) ###

### bindStringByIndex(aIndex, aValue) ###

### bindDoubleByIndex(aIndex, aValue) ###

### bindInt32ByIndex(aIndex, aValue) ###

### bindInt64ByIndex(aIndex, aValue) ###

### bindNullByIndex(aIndex) ###

### bindBlobByIndex(aIndex, aValue, aValueSize) ###

### bindAdoptedBlobByIndex(aIndex, aValue, aValueSize) ###
