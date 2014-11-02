---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/layout/xul/tree/nsITreeColumns.idl">Source file</a>
</div>
# nsITreeColumns #

## Methods ##

### getFirstColumn() ###
  
Get the first/last column.  
  

### getLastColumn() ###

### getPrimaryColumn() ###
  
Attribute based column getters.  
  

### getSortedColumn() ###

### getKeyColumn() ###

### getColumnFor(element) ###
  
Get the column for the given element.  
  

### getNamedColumn(id) ###
  
Parametric column getters.  
  

### getColumnAt(index) ###

### invalidateColumns() ###
  
This method is called whenever a treecol is added or removed and  
the column cache needs to be rebuilt.  
  

### restoreNaturalOrder() ###

## Attributes ##

### tree ###
  
The tree widget for these columns.  
  

### count ###
  
The number of columns.  
  

### length ###
  
An alias for count (for the benefit of scripts which treat this as an  
array).  
  
