---
layout: default
---

# nsIDOMOfflineResourceList #

## Methods ##

### mozHasItem(uri) ###
  
Check that an entry exists in the list of dynamically-managed entries.  
  
@param uri  
       The resource to check.  
  

### mozItem(index) ###
  
Get the URI of a dynamically-managed entry.  
@status DEPRECATED  
        Clients should use the "items" attribute.  
  

### mozAdd(uri) ###
  
Add an item to the list of dynamically-managed entries.  The resource  
will be fetched into the application cache.  
  
@param uri  
       The resource to add.  
  

### mozRemove(uri) ###
  
Remove an item from the list of dynamically-managed entries.  If this  
was the last reference to a URI in the application cache, the cache  
entry will be removed.  
  
@param uri  
       The resource to remove.  
  

### update() ###
  
Begin the application update process on the associated application cache.  
  

### swapCache() ###
  
Swap in the newest version of the application cache, or disassociate  
from the cache if the cache group is obsolete.  
  

## Attributes ##

### mozItems ###
  
Get the list of dynamically-managed entries.  
  

### mozLength ###
  
Get the number of dynamically-managed entries.  
@status DEPRECATED  
        Clients should use the "items" attribute.  
  

### status ###

### onchecking ###

### onerror ###

### onnoupdate ###

### ondownloading ###

### onprogress ###

### onupdateready ###

### oncached ###

### onobsolete ###

## Constants ##

### UNCACHED ###
  
State of the application cache this object is associated with.  
  

### IDLE ###

### CHECKING ###

### DOWNLOADING ###

### UPDATEREADY ###

### OBSOLETE ###
