---
layout: default
---

# nsINavHistoryResultObserver #
  
Allows clients to observe what is happening to a result as it updates itself  
according to history and bookmark system events. Register this observer on a  
result using nsINavHistoryResult::addObserver.  
  

## Methods ##

### nodeInserted(aParent, aNode, aNewIndex) ###
  
Called when 'aItem' is inserted into 'aParent' at index 'aNewIndex'.  
The item previously at index (if any) and everything below it will have  
been shifted down by one. The item may be a container or a leaf.  
  

### nodeRemoved(aParent, aItem, aOldIndex) ###
  
Called whan 'aItem' is removed from 'aParent' at 'aOldIndex'. The item  
may be a container or a leaf. This function will be called after the item  
has been removed from its parent list, but before anything else (including  
NULLing out the item's parent) has happened.  
  

### nodeMoved(aNode, aOldParent, aOldIndex, aNewParent, aNewIndex) ###
  
Called whan 'aItem' is moved from 'aOldParent' at 'aOldIndex' to  
aNewParent at aNewIndex. The item may be a container or a leaf.  
  
XXX: at the moment, this method is called only when an item is moved  
within the same container. When an item is moved between containers,  
a new node is created for the item, and the itemRemoved/itemAdded methods  
are used.  
  

### nodeTitleChanged(aNode, aNewTitle) ###
  
Called right after aNode's title has changed.  
  
@param aNode  
       a result node  
@param aNewTitle  
       the new title  
  

### nodeURIChanged(aNode, aNewURI) ###
  
Called right after aNode's uri property has changed.  
  
@param aNode  
       a result node  
@param aNewURI  
       the new uri  
  

### nodeIconChanged(aNode) ###
  
Called right after aNode's icon property has changed.  
  
@param aNode  
       a result node  
  
@note: The new icon is accessible through aNode.icon.  
  

### nodeHistoryDetailsChanged(aNode, aNewVisitDate, aNewAccessCount) ###
  
Called right after aNode's time property or accessCount property, or both,  
have changed.  
  
@param aNode  
       a uri result node  
@param aNewVisitDate  
       the new visit date  
@param aNewAccessCount  
       the new access-count  
  

### nodeTagsChanged(aNode) ###
  
Called when the tags set on the uri represented by aNode have changed.  
  
@param aNode  
       a uri result node  
  
@note: The new tags list is accessible through aNode.tags.  
  

### nodeKeywordChanged(aNode, aNewKeyword) ###
  
Called right after the aNode's keyword property has changed.  
  
@param aNode  
       a uri result node  
@param aNewKeyword  
       the new keyword  
  

### nodeAnnotationChanged(aNode, aAnnoName) ###
  
Called right after an annotation of aNode's has changed (set, altered, or  
unset).  
  
@param aNode  
       a result node  
@param aAnnoName  
       the name of the annotation that changed  
  

### nodeDateAddedChanged(aNode, aNewValue) ###
  
Called right after aNode's dateAdded property has changed.  
  
@param aNode  
       a result node  
@param aNewValue  
       the new value of the dateAdded property  
  

### nodeLastModifiedChanged(aNode, aNewValue) ###
  
Called right after aNode's dateModified property has changed.  
  
@param aNode  
       a result node  
@param aNewValue  
       the new value of the dateModified property  
  

### containerStateChanged(aContainerNode, aOldState, aNewState) ###
  
Called after a container changes state.  
  
@param aContainerNode  
       The container that has changed state.  
@param aOldState  
       The state that aContainerNode has transitioned out of.  
@param aNewState  
       The state that aContainerNode has transitioned into.  
  

### invalidateContainer(aContainerNode) ###
  
Called when something significant has happened within the container. The  
contents of the container should be re-built.  
  
@param aContainerNode  
       the container node to invalidate  
  

### sortingChanged(sortingMode) ###
  
This is called to indicate to the UI that the sort has changed to the  
given mode. For trees, for example, this would update the column headers  
to reflect the sorting. For many other types of views, this won't be  
applicable.  
  
@param sortingMode  One of nsINavHistoryQueryOptions.SORT_BY_* that  
                    indicates the new sorting mode.  
  
This only is expected to update the sorting UI. invalidateAll() will also  
get called if the sorting changes to update everything.  
  

### batching(aToggleMode) ###
  
This is called to indicate that a batch operation is about to start or end.  
The observer could want to disable some events or updates during batches,  
since multiple operations are packed in a short time.  
For example treeviews could temporarily suppress select notifications.  
  
@param aToggleMode  
       true if a batch is starting, false if it's ending.  
  

## Attributes ##

### result ###
  
Called by the result when this observer is added.  
  
