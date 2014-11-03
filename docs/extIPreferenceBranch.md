---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/exthelper/extIApplication.idl">Source file</a>
</div>

# extIPreferenceBranch #
<pre>  
Interface for simplified access to preferences. The interface has a  
predefined root preference branch. The root branch is set based on the  
context of the owner. For example, an extension's preferences have a root  
of "extensions.<extensionid>.", while the application level preferences  
have an empty root. All preference "aName" parameters used in this interface  
are relative to the root branch.  
  
</pre>
## Methods ##

### has(aName) ###
<pre>  
Check to see if a preference exists.  
@param   aName  
         The name of preference  
@returns true if the preference exists, false if not  
  
</pre>
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
<pre>  
Gets an object representing a preference  
@param   aName  
         The name of preference  
@returns a preference object, or null if the preference does not exist  
  
</pre>
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
<pre>  
Gets the value of a preference. Returns a default value if  
the preference does not exist.  
@param   aName  
         The name of preference  
@param   aDefaultValue  
         The value to return if preference does not exist  
@returns value of the preference or the given default value if preference  
         does not exists.  
  
</pre>
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

### reset() ###
<pre>  
Resets all preferences in a branch back to their default values.  
  
</pre>
## Attributes ##

### root ###
<pre>  
The name of the branch root.  
  
</pre>
### all ###
<pre>  
Array of extIPreference listing all preferences in this branch.  
  
</pre>
### events ###
<pre>  
The events object for the preferences  
supports: "change"  
  
</pre>