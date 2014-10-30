---
layout: default
---

# nsIOfflineCacheUpdateObserver #

## Methods ##

### updateStateChanged ###
  
aUpdate has changed its state.  
  
@param aUpdate  
       The nsIOfflineCacheUpdate being processed.  
@param event  
       See enumeration above  
  

### applicationCacheAvailable ###
  
Informs the observer about an application being available to associate.  
  
@param applicationCache  
       The application cache instance that has been created or found by the   
       update to associate with  
  

## Constants ##

### STATE_ERROR ###

### STATE_CHECKING ###

### STATE_NOUPDATE ###

### STATE_OBSOLETE ###

### STATE_DOWNLOADING ###

### STATE_ITEMSTARTED ###

### STATE_ITEMCOMPLETED ###

### STATE_ITEMPROGRESS ###

### STATE_FINISHED ###
