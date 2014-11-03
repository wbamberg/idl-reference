---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/xulstore/nsIXULStore.idl">Source file</a>
</div>

# nsIXULStore #
  
The XUL store is used to store information related to a XUL document/application.  
Typically it is used to store the persisted state for the document, such as  
window location, toolbars that are open and nodes that are open and closed in a tree.  
  
The data is serialized to [profile directory]/xulstore.json  
  

## Methods ##

### setValue(doc, id, attr, value) ###
  
Sets a value in the store.  
  
  

#### Parameters ####

<table>

<tr>
<td>doc</td>
<td>- document URI  
</td>
</tr>

<tr>
<td>id</td>
<td>- identifier of the node  
</td>
</tr>

<tr>
<td>attr</td>
<td>- attribute to store  
</td>
</tr>

<tr>
<td>value</td>
<td>- value of the attribute  
</td>
</tr>

</table>

### hasValue(doc, id, attr) ###
  
Returns true if the store contains a value for attr.  
  
  

#### Parameters ####

<table>

<tr>
<td>doc</td>
<td>- URI of the document  
</td>
</tr>

<tr>
<td>id</td>
<td>- identifier of the node  
</td>
</tr>

<tr>
<td>attr</td>
<td>- attribute  
</td>
</tr>

</table>

### getValue(doc, id, attr) ###
  
Retrieves a value in the store, or an empty string if it does not exist.  
  
  
  

#### Parameters ####

<table>

<tr>
<td>doc</td>
<td>- document URI  
</td>
</tr>

<tr>
<td>id</td>
<td>- identifier of the node  
</td>
</tr>

<tr>
<td>attr</td>
<td>- attribute to retrieve  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>the value of the attribute  
</td>
</tr>

</table>

### removeValue(doc, id, attr) ###
  
Removes a value in the store.  
  
  

#### Parameters ####

<table>

<tr>
<td>doc</td>
<td>- document URI  
</td>
</tr>

<tr>
<td>id</td>
<td>- identifier of the node  
</td>
</tr>

<tr>
<td>attr</td>
<td>- attribute to remove  
</td>
</tr>

</table>

### getIDsEnumerator(doc) ###
  
Iterates over all of the ids associated with a given document uri that  
have stored data.  
  
  

#### Parameters ####

<table>

<tr>
<td>doc</td>
<td>- document URI  
</td>
</tr>

</table>

### getAttributeEnumerator(doc, id) ###
  
Iterates over all of the attributes associated with a given document uri  
and id that have stored data.  
  
  

#### Parameters ####

<table>

<tr>
<td>doc</td>
<td>- document URI  
</td>
</tr>

<tr>
<td>id</td>
<td>- identifier of the node  
</td>
</tr>

</table>
