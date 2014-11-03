---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/layout/xul/tree/nsITreeColumns.idl">Source file</a>
</div>

# nsITreeColumns #

## Methods ##

### getFirstColumn() ###
<code>  
Get the first/last column.  
  
</code>
### getLastColumn() ###

### getPrimaryColumn() ###
<code>  
Attribute based column getters.  
  
</code>
### getSortedColumn() ###

### getKeyColumn() ###

### getColumnFor(element) ###
<code>  
Get the column for the given element.  
  
</code>
### getNamedColumn(id) ###
<code>  
Parametric column getters.  
  
</code>
### getColumnAt(index) ###

### invalidateColumns() ###
<code>  
This method is called whenever a treecol is added or removed and  
the column cache needs to be rebuilt.  
  
</code>
### restoreNaturalOrder() ###

## Attributes ##

### tree ###
  
The tree widget for these columns.  
  

### count ###
  
The number of columns.  
  

### length ###
  
An alias for count (for the benefit of scripts which treat this as an  
array).  
  
