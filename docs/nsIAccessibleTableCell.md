---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/accessible/interfaces/nsIAccessibleTable.idl">Source file</a>
</div>
# nsIAccessibleTableCell #

## Methods ##

### isSelected() ###
  
Return a boolean value indicating whether this cell is selected.  
  

## Attributes ##

### table ###
  
Return host table accessible.  
  

### columnIndex ###
  
Return column index of this cell.  
  

### rowIndex ###
  
Return row index of this cell.  
  

### columnExtent ###
  
Return the number of columns occupied by this cell. The result differs  
from 1 if the specified cell spans multiple columns.  
  

### rowExtent ###
  
Return the number of rows occupied by this accessible cell. The result  
differs from 1 if the specified cell spans multiple rows.  
  

### columnHeaderCells ###
  
Return an array of column header cells for this cell.  
  

### rowHeaderCells ###
  
Return an array of row header cells for this cell.  
  
