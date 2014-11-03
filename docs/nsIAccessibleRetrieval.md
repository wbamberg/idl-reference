---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/accessible/interfaces/nsIAccessibleRetrieval.idl">Source file</a>
</div>

# nsIAccessibleRetrieval #
  
An interface for in-process accessibility clients wishing to get an  
nsIAccessible for a given DOM node.  More documentation at:  
  http://www.mozilla.org/projects/ui/accessibility  
  

## Methods ##

### getApplicationAccessible() ###
  
Return application accessible.  
  

### getAccessibleFor(aNode) ###
  
Return an nsIAccessible for a DOM node in pres shell 0.  
Create a new accessible of the appropriate type if necessary,  
or use one from the accessibility cache if it already exists.  
  

#### Parameters ####

<table>

<tr>
<td>aNode</td>
<td>The DOM node to get an accessible for.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The nsIAccessible for the given DOM node.  
</td>
</tr>

</table>

### getStringRole(aRole) ###
  
Returns accessible role as a string.  
  
  

#### Parameters ####

<table>

<tr>
<td>aRole</td>
<td>- the accessible role constants.  
</td>
</tr>

</table>

### getStringStates(aStates, aExtraStates) ###
  
Returns list which contains accessible states as a strings.  
  
  

#### Parameters ####

<table>

<tr>
<td>aStates</td>
<td>- accessible states.  
</td>
</tr>

<tr>
<td>aExtraStates</td>
<td>- accessible extra states.  
</td>
</tr>

</table>

### getStringEventType(aEventType) ###
  
Get the type of accessible event as a string.  
  
  

#### Parameters ####

<table>

<tr>
<td>aEventType</td>
<td>- the accessible event type constant  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>- accessible event type presented as human readable string  
</td>
</tr>

</table>

### getStringRelationType(aRelationType) ###
  
Get the type of accessible relation as a string.  
  
  

#### Parameters ####

<table>

<tr>
<td>aRelationType</td>
<td>- the accessible relation type constant  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>- accessible relation type presented as human readable string  
</td>
</tr>

</table>

### getAccessibleFromCache(aNode) ###
  
Return an accessible for the given DOM node from the cache.  
@note  the method is intended for testing purposes  
  
  
  

#### Parameters ####

<table>

<tr>
<td>aNode</td>
<td>[in] the DOM node to get an accessible for  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>cached accessible for the given DOM node if any  
</td>
</tr>

</table>

### createAccessiblePivot(aRoot) ###
  
Create a new pivot for tracking a position and traversing a subtree.  
  
  

#### Parameters ####

<table>

<tr>
<td>aRoot</td>
<td>[in] the accessible root for the pivot  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>a new pivot  
</td>
</tr>

</table>

### setLogging(aModules) ###
  
Enable logging for the given modules, all other modules aren't logged.  
  
  

#### Parameters ####

<table>

<tr>
<td>aModules</td>
<td>[in] list of modules, format is comma separated list  
                     like 'docload,doccreate'.  
@note Works on debug build only.  
@see Logging.cpp for list of possible values.  
</td>
</tr>

</table>

### isLogged(aModule) ###
  
Return true if the given module is logged.  
  
