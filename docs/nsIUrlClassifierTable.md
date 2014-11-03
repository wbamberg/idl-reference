---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/url-classifier/nsIUrlClassifierTable.idl">Source file</a>
</div>

# nsIUrlClassifierTable #

## Methods ##

### exists(key, cb) ###
<code>  
In the simple case, exists just looks up the string in the  
table and call the callback after the query returns with true or  
false.  It's possible that something more complex happens  
(e.g., canonicalize the url).  
  
</code>
## Attributes ##

### name ###
  
The name used to identify this table  
  

### needsUpdate ###
  
Set to false if we don't want to update this table.  
  
