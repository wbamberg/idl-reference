---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/accessible/interfaces/nsIAccessibleTable.idl">Source file</a>
</div>

# nsIAccessibleTableCell #

## Methods ##

### isSelected() ###
<pre>  
Return a boolean value indicating whether this cell is selected.  
  
</pre>
## Attributes ##

### table ###
<pre>  
Return host table accessible.  
  
</pre>
### columnIndex ###
<pre>  
Return column index of this cell.  
  
</pre>
### rowIndex ###
<pre>  
Return row index of this cell.  
  
</pre>
### columnExtent ###
<pre>  
Return the number of columns occupied by this cell. The result differs  
from 1 if the specified cell spans multiple columns.  
  
</pre>
### rowExtent ###
<pre>  
Return the number of rows occupied by this accessible cell. The result  
differs from 1 if the specified cell spans multiple rows.  
  
</pre>
### columnHeaderCells ###
<pre>  
Return an array of column header cells for this cell.  
  
</pre>
### rowHeaderCells ###
<pre>  
Return an array of row header cells for this cell.  
  
</pre>