---
layout: default
---

# nsIRDFInferDataSource #

An nsIRDFInferDataSource is implemented by a infer engine. This
engine mimics assertions in addition to those in the baseDataSource
according to a particular vocabulary.
Infer engines have contract IDs in the form of
"@mozilla.org/rdf/infer-datasource;1?engine="


## baseDataSource ##


The wrapped datasource.

The InferDataSource contains all arcs from the wrapped
datasource plus those infered by the vocabulary implemented
by the InferDataSource.

