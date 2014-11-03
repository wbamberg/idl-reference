---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsITransferable.idl">Source file</a>
</div>

# nsIFlavorDataProvider #

## Methods ##

### getFlavorData(aTransferable, aFlavor, aData, aDataLen) ###
  
Retrieve the data from this data provider.  
  
  

#### Parameters ####

<table>

<tr>
<td>aTransferable</td>
<td>(in parameter) the transferable we're being called for.  
</td>
</tr>

<tr>
<td>aFlavor</td>
<td>(in parameter) the flavor of data to retrieve  
</td>
</tr>

<tr>
<td>aData</td>
<td>the data. Some variant of class in nsISupportsPrimitives.idl  
</td>
</tr>

<tr>
<td>aDataLen</td>
<td>the length of the data  
</td>
</tr>

</table>
