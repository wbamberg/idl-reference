---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/rdf/base/nsIRDFLiteral.idl">Source file</a>
</div>

# nsIRDFLiteral #
<pre>  
A literal node in the graph, whose value is a string.  
  
</pre>
## Methods ##

### GetValueConst(aConstValue) ###
<pre>  
An unscriptable version used to avoid a string copy. Meant  
for use as a performance optimization.  
  
</pre>
## Attributes ##

### Value ###
<pre>  
The Unicode string value of the literal.  
  
</pre>