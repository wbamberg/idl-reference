---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/storage/public/mozIStorageRow.idl">Source file</a>
</div>

# mozIStorageRow #

## Methods ##

### getResultByIndex(aIndex) ###
  
Obtains the result of a given column specified by aIndex.  
  
@param aIndex  
       Zero-based index of the result to get from the tuple.  
@returns the result of the specified column.  
  

#### Parameters ####

<table>

<tr>
<td>aIndex</td>
<td>       Zero-based index of the result to get from the tuple.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>the result of the specified column.  
</td>
</tr>

</table>

### getResultByName(aName) ###
  
Obtains the result of a given column specified by aName.  
  
@param aName  
       Name of the result to get from the tuple.  
@returns the result of the specified column.  
@note The name of a result column is the value of the "AS" clause for that  
      column.  If there is no AS clause then the name of the column is  
      unspecified and may change from one release to the next.  
  

#### Parameters ####

<table>

<tr>
<td>aName</td>
<td>       Name of the result to get from the tuple.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>the result of the specified column.  
@note The name of a result column is the value of the "AS" clause for that  
      column.  If there is no AS clause then the name of the column is  
      unspecified and may change from one release to the next.  
</td>
</tr>

</table>
