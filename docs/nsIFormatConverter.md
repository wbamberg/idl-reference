---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsIFormatConverter.idl">Source file</a>
</div>

# nsIFormatConverter #

## Methods ##

### getInputDataFlavors() ###
<code>  
Get the list of the "input" data flavors (mime types as nsISupportsCString),  
in otherwords, the flavors that this converter can convert "from" (the   
incoming data to the converter).  
  
</code>
### getOutputDataFlavors() ###
<code>  
Get the list of the "output" data flavors (mime types as nsISupportsCString),  
in otherwords, the flavors that this converter can convert "to" (the   
outgoing data to the converter).  
  
@param  aDataFlavorList fills list with supported flavors  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aDataFlavorList</td>
<td>fills list with supported flavors  
</td>
</tr>

</table>

### canConvert(aFromDataFlavor, aToDataFlavor) ###
<code>  
Determines whether a conversion from one flavor to another is supported  
  
@param  aFromFormatConverter flavor to convert from  
@param  aFromFormatConverter flavor to convert to  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aFromFormatConverter</td>
<td>flavor to convert from  
</td>
</tr>

<tr>
<td>aFromFormatConverter</td>
<td>flavor to convert to  
</td>
</tr>

</table>

### convert(aFromDataFlavor, aFromData, aDataLen, aToDataFlavor, aToData, aDataToLen) ###
<code>  
Converts from one flavor to another.  
  
@param  aFromFormatConverter flavor to convert from  
@param  aFromFormatConverter flavor to convert to (destination own the memory)  
@returns returns NS_OK if it was converted  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aFromFormatConverter</td>
<td>flavor to convert from  
</td>
</tr>

<tr>
<td>aFromFormatConverter</td>
<td>flavor to convert to (destination own the memory)  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>returns NS_OK if it was converted  
</td>
</tr>

</table>
