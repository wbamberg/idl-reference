---
layout: default
---

# nsINavHistoryQueryResultNode #
  
Used for places queries and as a base for bookmark folders.  
  
Note that if you request places to *not* be expanded in the options that  
generated this node, this item will report it has no children and never try  
to populate itself.  
  

## Methods ##

### getQueries ###
  
Get the queries which build this node's children.  
Only valid for RESULT_TYPE_QUERY nodes.  
  

## Attributes ##

### queryOptions ###
  
Get the options which group this node's children.  
Only valid for RESULT_TYPE_QUERY nodes.  
  

### folderItemId ###
  
For both simple folder nodes and simple-folder-query nodes, this is set  
to the concrete itemId of the folder. Otherwise, this is set to -1.  
  
