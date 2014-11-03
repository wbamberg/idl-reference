---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/xul/templates/nsIXULSortService.idl">Source file</a>
</div>

# nsIXULSortService #
  
A service used to sort the contents of a XUL widget.  
  

## Methods ##

### sort(aNode, aSortKey, aSortHints) ###
  
Sort the contents of the widget containing <code>aNode</code>  
using <code>aSortKey</code> as the comparison key, and  
<code>aSortDirection</code> as the direction.  
  
  
  ascending: to sort the contents in ascending order  
  descending: to sort the contents in descending order  
  comparecase: perform case sensitive comparisons  
  integer: treat values as integers, non-integers are compared as strings  
  twostate: don't allow the natural (unordered state)  
  

#### Parameters ####

<table>

<tr>
<td>aNode</td>
<td>A node in the XUL widget whose children are to be sorted.  
</td>
</tr>

<tr>
<td>aSortKey</td>
<td>The value to be used as the comparison key.  
</td>
</tr>

<tr>
<td>aSortHints</td>
<td>One or more hints as to how to sort:  
</td>
</tr>

</table>

## Constants ##

### SORT_COMPARECASE ###

### SORT_INTEGER ###
