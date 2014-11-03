---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/events/nsIDOMDataContainerEvent.idl">Source file</a>
</div>

# nsIDOMDataContainerEvent #

## Methods ##

### getData(key) ###
  
Return the data associated with the given key.  
  
  

#### Parameters ####

<table>

<tr>
<td>key</td>
<td>the key  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>the data associated with the key  
</td>
</tr>

</table>

### setData(key, data) ###
  
Set the data for the given key.  
  
  

#### Parameters ####

<table>

<tr>
<td>key</td>
<td>the data key  
</td>
</tr>

<tr>
<td>data</td>
<td>the data  
@throws       NS_ERROR_UNEXPECTED if the method is called during event  
              dispatch  
</td>
</tr>

</table>
