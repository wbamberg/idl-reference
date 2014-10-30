---
layout: default
---

# nsINavBookmarksService #
  
The BookmarksService interface provides methods for managing bookmarked  
history items.  Bookmarks consist of a set of user-customizable  
folders.  A URI in history can be contained in one or more such folders.  
  

## Methods ##

### insertBookmark ###
  
Inserts a child bookmark into the given folder.  
  
 @param aParentId  
        The id of the parent folder  
 @param aURI  
        The URI to insert  
 @param aIndex  
        The index to insert at, or DEFAULT_INDEX to append  
 @param aTitle  
        The title for the new bookmark  
 @param [optional] aGuid  
        The GUID to be set for the new item.  If not set, a new GUID is  
        generated.  Unless you've a very sound reason, such as an undo  
        manager implementation, do not pass this argument.  
 @return The ID of the newly-created bookmark.  
  
 @note aTitle will be truncated to TITLE_LENGTH_MAX and  
       aURI will be truncated to URI_LENGTH_MAX.  
 @throws if aGuid is malformed.  
  

### removeItem ###
  
Removes a child item. Used to delete a bookmark or separator.  
 @param aItemId  
        The child item to remove  
  

### createFolder ###
  
Creates a new child folder and inserts it under the given parent.  
 @param aParentFolder  
        The id of the parent folder  
 @param aName  
        The name of the new folder  
 @param aIndex  
        The index to insert at, or DEFAULT_INDEX to append  
 @param [optional] aGuid  
        The GUID to be set for the new item.  If not set, a new GUID is  
        generated.  Unless you've a very sound reason, such as an undo  
        manager implementation, do not pass this argument.  
 @return The ID of the newly-inserted folder.  
 @throws if aGuid is malformed.  
  

### getRemoveFolderTransaction ###
  
Gets an undo-able transaction for removing a folder from the bookmarks  
tree.  
 @param aItemId  
        The id of the folder to remove.  
 @return An object implementing nsITransaction that can be used to undo  
         or redo the action.  
  
This method exists because complex delete->undo operations rely on  
recreated folders to have the same ID they had before they were deleted,  
so that any other items deleted in different transactions can be  
re-inserted correctly. This provides a safe encapsulation of this  
functionality without exposing the ability to recreate folders with  
specific IDs (potentially dangerous if abused by other code!) in the  
public API.  
  

### removeFolderChildren ###
  
Convenience function for container services.  Removes  
all children of the given folder.  
 @param aItemId  
        The id of the folder to remove children from.  
  

### moveItem ###
  
Moves an item to a different container, preserving its contents.  
 @param aItemId  
        The id of the item to move  
 @param aNewParentId  
        The id of the new parent  
 @param aIndex  
        The index under aNewParent, or DEFAULT_INDEX to append  
  
NOTE: When moving down in the same container we take into account the  
removal of the original item. If you want to move from index X to  
index Y > X you must use moveItem(id, folder, Y + 1)  
  

### insertSeparator ###
  
Inserts a bookmark separator into the given folder at the given index.  
The separator can be removed using removeChildAt().  
 @param aParentId  
        The id of the parent folder  
 @param aIndex  
        The separator's index under folder, or DEFAULT_INDEX to append  
 @param [optional] aGuid  
        The GUID to be set for the new item.  If not set, a new GUID is  
        generated.  Unless you've a very sound reason, such as an undo  
        manager implementation, do not pass this argument.  
 @return The ID of the new separator.  
 @throws if aGuid is malformed.  
  

### getIdForItemAt ###
  
Get the itemId given the containing folder and the index.  
 @param aParentId  
        The id of the diret parent folder of the item  
 @param aIndex  
        The index of the item within the parent folder.  
        Pass DEFAULT_INDEX for the last item.  
 @return The ID of the found item, -1 if the item does not exists.  
  

### setItemTitle ###
  
Set the title for an item.  
 @param aItemId  
        The id of the item whose title should be updated.  
 @param aTitle  
        The new title for the bookmark.  
  
 @note  aTitle will be truncated to TITLE_LENGTH_MAX.  
  

### getItemTitle ###
  
Get the title for an item.  
  
If no item title is available it will return a void string (null in JS).  
  
 @param aItemId  
        The id of the item whose title should be retrieved  
 @return The title of the item.  
  

### setItemDateAdded ###
  
Set the date added time for an item.  
  

### getItemDateAdded ###
  
Get the date added time for an item.  
  

### setItemLastModified ###
  
Set the last modified time for an item.  
  
 @note This is the only method that will send an itemChanged notification  
       for the property.  lastModified will still be updated in  
       any other method that changes an item property, but we will send  
       the corresponding itemChanged notification instead.  
  

### getItemLastModified ###
  
Get the last modified time for an item.  
  
 @note When an item is added lastModified is set to the same value as  
       dateAdded.  
  

### getBookmarkURI ###
  
Get the URI for a bookmark item.  
  

### getItemIndex ###
  
Get the index for an item.  
  

### setItemIndex ###
  
Changes the index for a item. This method does not change the indices of  
any other items in the same folder, so ensure that the new index does not  
already exist, or change the index of other items accordingly, otherwise  
the indices will become corrupted.  
  
WARNING: This is API is intended for scenarios such as folder sorting,  
         where the caller manages the indices of *all* items in the folder.  
         You must always ensure each index is unique after a reordering.  
  
 @param aItemId    The id of the item to modify  
 @param aNewIndex  The new index  
  
 @throws If aNewIndex is out of bounds.  
  

### getItemType ###
  
Get an item's type (bookmark, separator, folder).  
The type is one of the TYPE_* constants defined above.  
  

### isBookmarked ###
  
Returns true if the given URI is in any bookmark folder. If you want the  
results to be redirect-aware, use getBookmarkedURIFor()  
  

### getBookmarkedURIFor ###
  
Used to see if the given URI is bookmarked, or any page that redirected to  
it is bookmarked. For example, if I bookmark "mozilla.org" by manually  
typing it in, and follow the bookmark, I will get redirected to  
"www.mozilla.org". Logically, this new page is also bookmarked. This  
function, if given "www.mozilla.org", will return the URI of the bookmark,  
in this case "mozilla.org".  
  
If there is no bookmarked page found, it will return NULL.  
  
@note The function will only return bookmarks in the first 2 levels of  
      redirection (1 -> 2 -> aURI).  
  

### changeBookmarkURI ###
  
Change the bookmarked URI for a bookmark.  
This changes which "place" the bookmark points at,  
which means all annotations, etc are carried along.  
  

### getFolderIdForItem ###
  
Get the parent folder's id for an item.  
  

### getBookmarkIdsForURI ###
  
Returns the list of bookmark ids that contain the given URI.  
  

### setKeywordForBookmark ###
  
Associates the given keyword with the given bookmark.  
  
Use an empty keyword to clear the keyword associated with the URI.  
In both of these cases, succeeds but does nothing if the URL/keyword is not found.  
  

### getKeywordForURI ###
  
Retrieves the keyword for the given URI. Will be void string  
(null in JS) if no such keyword is found.  
  

### getKeywordForBookmark ###
  
Retrieves the keyword for the given bookmark. Will be void string  
(null in JS) if no such keyword is found.  
  

### getURIForKeyword ###
  
Returns the URI associated with the given keyword. Empty if no such  
keyword is found.  
  

### addObserver ###
  
Adds a bookmark observer. If ownsWeak is false, the bookmark service will  
keep an owning reference to the observer.  If ownsWeak is true, then  
aObserver must implement nsISupportsWeakReference, and the bookmark  
service will keep a weak reference to the observer.  
  

### removeObserver ###
  
Removes a bookmark observer.  
  

### getObservers ###
  
Gets an array of registered nsINavBookmarkObserver objects.  
  

### runInBatchMode ###
  
Runs the passed callback inside of a database transaction.  
Use this when a lot of things are about to change, for example  
adding or deleting a large number of bookmark items. Calls can  
be nested. Observers are notified when batches begin and end, via  
nsINavBookmarkObserver.onBeginUpdateBatch/onEndUpdateBatch.  
  
@param aCallback  
       nsINavHistoryBatchCallback interface to call.  
@param aUserData  
       Opaque parameter passed to nsINavBookmarksBatchCallback  
  

## Attributes ##

### placesRoot ###
  
The item ID of the Places root.  
  

### bookmarksMenuFolder ###
  
The item ID of the bookmarks menu folder.  
  

### tagsFolder ###
  
The item ID of the top-level folder that contain the tag "folders".  
  

### unfiledBookmarksFolder ###
  
The item ID of the unfiled-bookmarks folder.  
  

### toolbarFolder ###
  
The item ID of the personal toolbar folder.  
  

## Constants ##

### DEFAULT_INDEX ###
  
This value should be used for APIs that allow passing in an index  
where an index is not known, or not required to be specified.  
e.g.: When appending an item to a folder.  
  

### TYPE_BOOKMARK ###

### TYPE_FOLDER ###

### TYPE_SEPARATOR ###

### TYPE_DYNAMIC_CONTAINER ###
