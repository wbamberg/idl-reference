---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/docshell/shistory/public/nsISHEntry.idl">Source file</a>
</div>

# nsISHEntryInternal #

## Methods ##

### RemoveFromBFCacheAsync() ###

### RemoveFromBFCacheSync() ###

### getSharedState() ###
<code>  
Some state, particularly that related to the back/forward cache, is  
shared between SHEntries which correspond to the same document.  This  
method gets a pointer to that shared state.  
  
This shared state is the SHEntry's BFCacheEntry.  So  
hasBFCacheEntry(getSharedState()) is guaranteed to return true.  
  
</code>
## Attributes ##

### lastTouched ###
  
A number that is assigned by the sHistory when the entry is activated  
  
