---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/places/nsINavBookmarksService.idl">Source file</a>
</div>

# nsINavBookmarkObserver #
<code>  
Observer for bookmarks changes.  
  
</code>
## Methods ##

### onBeginUpdateBatch() ###
<code>  
Notifies that a batch transaction has started.  
Other notifications will be sent during the batch, but the observer is  
guaranteed that onEndUpdateBatch() will be called at its completion.  
During a batch the observer should do its best to reduce the work done to  
handle notifications, since multiple changes are going to happen in a short  
timeframe.  
  
</code>
### onEndUpdateBatch() ###
<code>  
Notifies that a batch transaction has ended.  
  
</code>
### onItemAdded(aItemId, aParentId, aIndex, aItemType, aURI, aTitle, aDateAdded, aGuid, aParentGuid) ###
<code>  
Notifies that an item (any type) was added.  Called after the actual  
addition took place.  
When a new item is created, all the items following it in the same folder  
will have their index shifted down, but no additional notifications will  
be sent.  
  
@param aItemId  
       The id of the item that was added.  
@param aParentId  
       The id of the folder to which the item was added.  
@param aIndex  
       The item's index in the folder.  
@param aItemType  
       The type of the added item (see TYPE_* constants below).  
@param aURI  
       The URI of the added item if it was TYPE_BOOKMARK, null otherwise.  
@param aTitle  
       The title of the added item.  
@param aDateAdded  
       The stored date added value, in microseconds from the epoch.  
@param aGuid  
       The unique ID associated with the item.  
@param aParentGuid  
       The unique ID associated with the item's parent.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aItemId</td>
<td>       The id of the item that was added.  
</td>
</tr>

<tr>
<td>aParentId</td>
<td>       The id of the folder to which the item was added.  
</td>
</tr>

<tr>
<td>aIndex</td>
<td>       The item's index in the folder.  
</td>
</tr>

<tr>
<td>aItemType</td>
<td>       The type of the added item (see TYPE_* constants below).  
</td>
</tr>

<tr>
<td>aURI</td>
<td>       The URI of the added item if it was TYPE_BOOKMARK, null otherwise.  
</td>
</tr>

<tr>
<td>aTitle</td>
<td>       The title of the added item.  
</td>
</tr>

<tr>
<td>aDateAdded</td>
<td>       The stored date added value, in microseconds from the epoch.  
</td>
</tr>

<tr>
<td>aGuid</td>
<td>       The unique ID associated with the item.  
</td>
</tr>

<tr>
<td>aParentGuid</td>
<td>       The unique ID associated with the item's parent.  
</td>
</tr>

</table>

### onItemRemoved(aItemId, aParentId, aIndex, aItemType, aURI, aGuid, aParentGuid) ###
<code>  
Notifies that an item was removed.  Called after the actual remove took  
place.  
When an item is removed, all the items following it in the same folder  
will have their index shifted down, but no additional notifications will  
be sent.  
  
@param aItemId  
       The id of the item that was removed.  
@param aParentId  
       The id of the folder from which the item was removed.  
@param aIndex  
       The bookmark's index in the folder.  
@param aItemType  
       The type of the item to be removed (see TYPE_* constants below).  
@param aURI  
       The URI of the added item if it was TYPE_BOOKMARK, null otherwise.  
@param aGuid  
       The unique ID associated with the item.  
@param aParentGuid  
       The unique ID associated with the item's parent.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aItemId</td>
<td>       The id of the item that was removed.  
</td>
</tr>

<tr>
<td>aParentId</td>
<td>       The id of the folder from which the item was removed.  
</td>
</tr>

<tr>
<td>aIndex</td>
<td>       The bookmark's index in the folder.  
</td>
</tr>

<tr>
<td>aItemType</td>
<td>       The type of the item to be removed (see TYPE_* constants below).  
</td>
</tr>

<tr>
<td>aURI</td>
<td>       The URI of the added item if it was TYPE_BOOKMARK, null otherwise.  
</td>
</tr>

<tr>
<td>aGuid</td>
<td>       The unique ID associated with the item.  
</td>
</tr>

<tr>
<td>aParentGuid</td>
<td>       The unique ID associated with the item's parent.  
</td>
</tr>

</table>

### onItemChanged(aItemId, aProperty, aIsAnnotationProperty, aNewValue, aLastModified, aItemType, aParentId, aGuid, aParentGuid) ###
<code>  
Notifies that an item's information has changed.  This will be called  
whenever any attributes like "title" are changed.  
  
@param aItemId  
       The id of the item that was changed.  
@param aProperty  
       The property which changed.  Can be null for the removal of all of  
       the annotations, in this case aIsAnnotationProperty is true.  
@param aIsAnnotationProperty  
       Whether or not aProperty is the name of an annotation.  If true  
       aNewValue is always an empty string.  
@param aNewValue  
       For certain properties, this is set to the new value of the  
       property (see the list below).  
@param aLastModified  
       If lastModified changed, this parameter is the new value, otherwise  
       it's set to 0.  
@param aItemType  
       The type of the item to be removed (see TYPE_* constants below).  
@param aParentId  
       The id of the folder containing the item.  
@param aGuid  
       The unique ID associated with the item.  
@param aParentGuid  
       The unique ID associated with the item's parent.  
  
@note List of values that may be associated with properties:  
      aProperty     | aNewValue  
      =====================================================================  
      cleartime      | Empty string (all visits to this item were removed).  
      title         | The new title.  
      favicon       | The "moz-anno" URL of the new favicon.  
      uri           | new URL.  
      tags          | Empty string (tags for this item changed)  
      dateAdded     | PRTime (as string) when the item was first added.  
      lastModified  | PRTime (as string) when the item was last modified.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aItemId</td>
<td>       The id of the item that was changed.  
</td>
</tr>

<tr>
<td>aProperty</td>
<td>       The property which changed.  Can be null for the removal of all of  
       the annotations, in this case aIsAnnotationProperty is true.  
</td>
</tr>

<tr>
<td>aIsAnnotationProperty</td>
<td>       Whether or not aProperty is the name of an annotation.  If true  
       aNewValue is always an empty string.  
</td>
</tr>

<tr>
<td>aNewValue</td>
<td>       For certain properties, this is set to the new value of the  
       property (see the list below).  
</td>
</tr>

<tr>
<td>aLastModified</td>
<td>       If lastModified changed, this parameter is the new value, otherwise  
       it's set to 0.  
</td>
</tr>

<tr>
<td>aItemType</td>
<td>       The type of the item to be removed (see TYPE_* constants below).  
</td>
</tr>

<tr>
<td>aParentId</td>
<td>       The id of the folder containing the item.  
</td>
</tr>

<tr>
<td>aGuid</td>
<td>       The unique ID associated with the item.  
</td>
</tr>

<tr>
<td>aParentGuid</td>
<td>       The unique ID associated with the item's parent.  
</td>
</tr>

</table>

### onItemVisited(aItemId, aVisitId, aTime, aTransitionType, aURI, aParentId, aGuid, aParentGuid) ###
<code>  
Notifies that the item was visited.  Can be invoked only for TYPE_BOOKMARK  
items.  
  
@param aItemId  
       The id of the bookmark that was visited.  
@param aVisitId  
       The id of the visit.  
@param aTime  
       The time of the visit.  
@param aTransitionType  
       The transition for the visit.  See nsINavHistoryService::TRANSITION_*  
       constants for a list of possible values.  
@param aURI  
       The nsIURI for this bookmark.  
@param aParentId  
       The id of the folder containing the item.  
@param aGuid  
       The unique ID associated with the item.  
@param aParentGuid  
       The unique ID associated with the item's parent.  
  
@see onItemChanged with property = "cleartime" for when all visits to an  
     item are removed.  
  
@note The reported time is the time of the visit that was added, which may  
      be well in the past since the visit time can be specified.  This  
      means that the visit the observer is told about may not be the most  
      recent visit for that page.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aItemId</td>
<td>       The id of the bookmark that was visited.  
</td>
</tr>

<tr>
<td>aVisitId</td>
<td>       The id of the visit.  
</td>
</tr>

<tr>
<td>aTime</td>
<td>       The time of the visit.  
</td>
</tr>

<tr>
<td>aTransitionType</td>
<td>       The transition for the visit.  See nsINavHistoryService::TRANSITION_*  
       constants for a list of possible values.  
</td>
</tr>

<tr>
<td>aURI</td>
<td>       The nsIURI for this bookmark.  
</td>
</tr>

<tr>
<td>aParentId</td>
<td>       The id of the folder containing the item.  
</td>
</tr>

<tr>
<td>aGuid</td>
<td>       The unique ID associated with the item.  
</td>
</tr>

<tr>
<td>aParentGuid</td>
<td>       The unique ID associated with the item's parent.  
</td>
</tr>

</table>

### onItemMoved(aItemId, aOldParentId, aOldIndex, aNewParentId, aNewIndex, aItemType, aGuid, aOldParentGuid, aNewParentGuid) ###
<code>  
Notifies that an item has been moved.  
  
@param aItemId  
       The id of the item that was moved.  
@param aOldParentId  
       The id of the old parent.  
@param aOldIndex  
       The old index inside the old parent.  
@param aNewParentId  
       The id of the new parent.  
@param aNewIndex  
       The index inside the new parent.  
@param aItemType  
       The type of the item to be removed (see TYPE_* constants below).  
@param aGuid  
       The unique ID associated with the item.  
@param aOldParentGuid  
       The unique ID associated with the old item's parent.  
@param aNewParentGuid  
       The unique ID associated with the new item's parent.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aItemId</td>
<td>       The id of the item that was moved.  
</td>
</tr>

<tr>
<td>aOldParentId</td>
<td>       The id of the old parent.  
</td>
</tr>

<tr>
<td>aOldIndex</td>
<td>       The old index inside the old parent.  
</td>
</tr>

<tr>
<td>aNewParentId</td>
<td>       The id of the new parent.  
</td>
</tr>

<tr>
<td>aNewIndex</td>
<td>       The index inside the new parent.  
</td>
</tr>

<tr>
<td>aItemType</td>
<td>       The type of the item to be removed (see TYPE_* constants below).  
</td>
</tr>

<tr>
<td>aGuid</td>
<td>       The unique ID associated with the item.  
</td>
</tr>

<tr>
<td>aOldParentGuid</td>
<td>       The unique ID associated with the old item's parent.  
</td>
</tr>

<tr>
<td>aNewParentGuid</td>
<td>       The unique ID associated with the new item's parent.  
</td>
</tr>

</table>
