---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/rdf/base/nsIRDFLiteral.idl">Source file</a>
</div>
# nsIRDFLiteral #
  
A literal node in the graph, whose value is a string.  
  

## Methods ##

### GetValueConst(aConstValue) ###
  
An unscriptable version used to avoid a string copy. Meant  
for use as a performance optimization.  
  

## Attributes ##

### Value ###
  
The Unicode string value of the literal.  
  
