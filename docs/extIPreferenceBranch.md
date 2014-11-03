---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/exthelper/extIApplication.idl">Source file</a>
</div>

# extIPreferenceBranch #
  
Interface for simplified access to preferences. The interface has a  
predefined root preference branch. The root branch is set based on the  
context of the owner. For example, an extension's preferences have a root  
of "extensions.<extensionid>.", while the application level preferences  
have an empty root. All preference "aName" parameters used in this interface  
are relative to the root branch.  
  

## Methods ##

### has(aName) ###
  
Check to see if a preference exists.  
  

#### Parameters ####

<table>

<tr>
<td>aName</td>
<td>         The name of preference  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>true if the preference exists, false if not  
</td>
</tr>

</table>

### get(aName) ###
  
Gets an object representing a preference  
  

#### Parameters ####

<table>

<tr>
<td>aName</td>
<td>         The name of preference  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>a preference object, or null if the preference does not exist  
</td>
</tr>

</table>

### getValue(aName, aDefaultValue) ###
  
Gets the value of a preference. Returns a default value if  
the preference does not exist.  
  

#### Parameters ####

<table>

<tr>
<td>aName</td>
<td>         The name of preference  
</td>
</tr>

<tr>
<td>aDefaultValue</td>
<td>         The value to return if preference does not exist  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>value of the preference or the given default value if preference  
         does not exists.  
</td>
</tr>

</table>

### setValue(aName, aValue) ###
  
Sets the value of a storage item with the given name.  
  

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

### reset() ###
  
Resets all preferences in a branch back to their default values.  
  

## Attributes ##

### root ###
  
The name of the branch root.  
  

### all ###
  
Array of extIPreference listing all preferences in this branch.  
  

### events ###
  
The events object for the preferences  
supports: "change"  
  
