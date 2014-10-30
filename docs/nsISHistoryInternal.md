---
layout: default
---

# nsISHistoryInternal #

## Methods ##

### addEntry ###
  
Add a new Entry to the History List  
@param aEntry - The entry to add  
@param aPersist - If true this specifies that the entry should persist  
in the list.  If false, this means that when new entries are added  
this element will not appear in the session history list.  
  

### updateIndex ###
   
Update the index maintained by sessionHistory  
  

### replaceEntry ###
  
Replace the nsISHEntry at a particular index  
@param aIndex - The index at which the entry should be replaced  
@param aReplaceEntry - The replacement entry for the index.  
  

### notifyOnHistoryReload ###
  
Notifies all registered session history listeners about an impending  
reload.  
  
@param aReloadURI    The URI of the document to be reloaded.  
@param aReloadFlags  Flags that indicate how the document is to be  
                     refreshed. See constants on the nsIWebNavigation  
                     interface.  
@return              Whether the operation can proceed.  
  

### evictOutOfRangeContentViewers ###
  
Evict content viewers which don't lie in the "safe" range around aIndex.  
In practice, this should leave us with no more than gHistoryMaxViewers  
viewers associated with this SHistory object.  
  
Also make sure that the total number of content viewers in all windows is  
not greater than our global max; if it is, evict viewers as appropriate.  
  
@param aIndex - The index around which the "safe" range is centered.  In  
  general, if you just navigated the history, aIndex should be the index  
  history was navigated to.  
  

### evictExpiredContentViewerForEntry ###
  
Evict the content viewer associated with a bfcache entry  
that has timed out.  
  

### evictAllContentViewers ###
  
Evict all the content viewers in this session history  
  

### RemoveEntries ###
  
Removes entries from the history if their docshellID is in  
aIDs array.  
  

## Attributes ##

### rootTransaction ###
  
Get the root transaction  
  

### rootDocShell ###
  
The toplevel docshell object to which this SHistory object belongs to.  
  
