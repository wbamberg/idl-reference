---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/accessible/interfaces/nsIAccessiblePivot.idl">Source file</a>
</div>

# nsIAccessibleTraversalRule #

## Methods ##

### getMatchRoles(aRoles, aCount) ###
  
Retrieve a list of roles that the traversal rule should test for. Any node  
with a role not in this list will automatically be ignored. An empty list  
will match all roles. It should be assumed that this method is called once  
at the start of a traversal, so changing the method's return result after  
that would have no affect.  
  
@param aRoles [out] an array of the roles to match.  
@param aCount [out] the length of the array.  
  

#### Parameters ####

<table>

<tr>
<td>aRoles</td>
<td>[out] an array of the roles to match.  
</td>
</tr>

<tr>
<td>aCount</td>
<td>[out] the length of the array.  
</td>
</tr>

</table>

### match(aAccessible) ###
  
Determines if a given accessible is to be accepted in our traversal rule  
  
@param aAccessible [in] accessible to examine.  
@return a bitfield of FILTER_MATCH and FILTER_IGNORE_SUBTREE.  
  

#### Parameters ####

<table>

<tr>
<td>aAccessible</td>
<td>[in] accessible to examine.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>a bitfield of FILTER_MATCH and FILTER_IGNORE_SUBTREE.  
</td>
</tr>

</table>

## Attributes ##

### preFilter ###
  
Pre-filter bitfield to filter out obviously ignorable nodes and lighten  
the load on match().  
  

## Constants ##

### FILTER_IGNORE ###

### FILTER_MATCH ###

### FILTER_IGNORE_SUBTREE ###

### PREFILTER_INVISIBLE ###

### PREFILTER_OFFSCREEN ###

### PREFILTER_NOT_FOCUSABLE ###

### PREFILTER_ARIA_HIDDEN ###

### PREFILTER_TRANSPARENT ###
