---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/layout/xul/tree/nsITreeColumns.idl">Source file</a>
</div>

# nsITreeColumns #

## Methods ##

### getFirstColumn() ###
<pre>  
Get the first/last column.  
  
</pre>
### getLastColumn() ###

### getPrimaryColumn() ###
<pre>  
Attribute based column getters.  
  
</pre>
### getSortedColumn() ###

### getKeyColumn() ###

### getColumnFor(element) ###
<pre>  
Get the column for the given element.  
  
</pre>
### getNamedColumn(id) ###
<pre>  
Parametric column getters.  
  
</pre>
### getColumnAt(index) ###

### invalidateColumns() ###
<pre>  
This method is called whenever a treecol is added or removed and  
the column cache needs to be rebuilt.  
  
</pre>
### restoreNaturalOrder() ###

## Attributes ##

### tree ###
<pre>  
The tree widget for these columns.  
  
</pre>
### count ###
<pre>  
The number of columns.  
  
</pre>
### length ###
<pre>  
An alias for count (for the benefit of scripts which treat this as an  
array).  
  
</pre>