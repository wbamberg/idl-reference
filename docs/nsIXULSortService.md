---
layout: default
---

# nsIXULSortService #
  
A service used to sort the contents of a XUL widget.  
  

## Methods ##

### sort ###
  
Sort the contents of the widget containing <code>aNode</code>  
using <code>aSortKey</code> as the comparison key, and  
<code>aSortDirection</code> as the direction.  
  
@param aNode A node in the XUL widget whose children are to be sorted.  
@param aSortKey The value to be used as the comparison key.  
@param aSortHints One or more hints as to how to sort:  
  
  ascending: to sort the contents in ascending order  
  descending: to sort the contents in descending order  
  comparecase: perform case sensitive comparisons  
  integer: treat values as integers, non-integers are compared as strings  
  twostate: don't allow the natural (unordered state)  
  

## Constants ##

### SORT_COMPARECASE ###

### SORT_INTEGER ###
