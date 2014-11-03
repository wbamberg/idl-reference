---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/rdf/base/nsIRDFInferDataSource.idl">Source file</a>
</div>

# nsIRDFInferDataSource #
<pre>  
An nsIRDFInferDataSource is implemented by a infer engine. This  
engine mimics assertions in addition to those in the baseDataSource  
according to a particular vocabulary.  
Infer engines have contract IDs in the form of  
"@mozilla.org/rdf/infer-datasource;1?engine="  
  
</pre>
## Attributes ##

### baseDataSource ###
<pre>  
  
The wrapped datasource.  
  
The InferDataSource contains all arcs from the wrapped  
datasource plus those infered by the vocabulary implemented  
by the InferDataSource.  
  
</pre>