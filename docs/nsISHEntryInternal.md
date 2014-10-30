---
layout: default
---

# nsISHEntryInternal #

## Methods ##

### RemoveFromBFCacheAsync ###

### RemoveFromBFCacheSync ###

### getSharedState ###
  
Some state, particularly that related to the back/forward cache, is  
shared between SHEntries which correspond to the same document.  This  
method gets a pointer to that shared state.  
  
This shared state is the SHEntry's BFCacheEntry.  So  
hasBFCacheEntry(getSharedState()) is guaranteed to return true.  
  

## Attributes ##

### lastTouched ###
  
A number that is assigned by the sHistory when the entry is activated  
  
