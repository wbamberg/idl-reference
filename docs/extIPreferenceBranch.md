---
layout: default
---

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
@param   aName  
         The name of preference  
@returns true if the preference exists, false if not  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>aName  
         The name of preference  
</td>
</tr>

</table>

### get(aName) ###
  
Gets an object representing a preference  
@param   aName  
         The name of preference  
@returns a preference object, or null if the preference does not exist  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>aName  
         The name of preference  
</td>
</tr>

</table>

### getValue(aName, aDefaultValue) ###
  
Gets the value of a preference. Returns a default value if  
the preference does not exist.  
@param   aName  
         The name of preference  
@param   aDefaultValue  
         The value to return if preference does not exist  
@returns value of the preference or the given default value if preference  
         does not exists.  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>aName  
         The name of preference  
</td>
</tr>

<tr>
<td></td>
<td>aDefaultValue  
         The value to return if preference does not exist  
</td>
</tr>

</table>

### setValue(aName, aValue) ###
  
Sets the value of a storage item with the given name.  
@param   aName  
         The name of an item  
@param   aValue  
         The value to assign to the item  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>aName  
         The name of an item  
</td>
</tr>

<tr>
<td></td>
<td>aValue  
         The value to assign to the item  
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
  
