---
layout: default
---

# nsIUrlClassifierTable #

## Methods ##

### exists(key, cb) ###
  
In the simple case, exists just looks up the string in the  
table and call the callback after the query returns with true or  
false.  It's possible that something more complex happens  
(e.g., canonicalize the url).  
  

## Attributes ##

### name ###
  
The name used to identify this table  
  

### needsUpdate ###
  
Set to false if we don't want to update this table.  
  
