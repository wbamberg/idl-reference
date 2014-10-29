---
layout: default
---

# nsISHEntry #

## URI ##

A readonly property that returns the URI
of the current entry. The object returned is
of type nsIURI


## title ##

A readonly property that returns the title
of the current entry.  The object returned
is a encoded string


## isSubFrame ##

A readonly property that returns a boolean
flag which indicates if the entry was created as a
result of a subframe navigation. This flag will be
'false' when a frameset page is visited for
the first time. This flag will be 'true' for all
history entries created as a result of a subframe
navigation.


## setURI ##
 URI for the document */

## referrerURI ##
 Referrer URI */

## contentViewer ##
 Content viewer, for fast restoration of presentation */

## sticky ##
 Whether the content viewer is marked "sticky" */

## windowState ##
 Saved state of the global window object */

## getViewerBounds ##

Saved position and dimensions of the content viewer; we must adjust the
root view's widget accordingly if this has changed when the presentation
is restored.


## setViewerBounds ##

## addChildShell ##

Saved child docshells corresponding to contentViewer.  The child shells
are restored as children of the parent docshell, in this order, when the
parent docshell restores a saved presentation.

 Append a child shell to the end of our list. */

## childShellAt ##

Get the child shell at |index|; returns null if |index| is out of bounds.


## clearChildShells ##

Clear the child shell list.


## refreshURIList ##
 Saved refresh URI list for the content viewer */

## syncPresentationState ##

Ensure that the cached presentation members are self-consistent.
If either |contentViewer| or |windowState| are null, then all of the
following members are cleared/reset:
 contentViewer, sticky, windowState, viewerBounds, childShells,
 refreshURIList.


## setTitle ##
 Title for the document */

## postData ##
 Post Data for the document */

## layoutHistoryState ##
 LayoutHistoryState for scroll position and form values */

## parent ##
 parent of this entry */

## loadType ##

The loadType for this entry. This is typically loadHistory except
when reload is pressed, it has the appropriate reload flag


## ID ##

An ID to help identify this entry from others during
subframe navigation


## cacheKey ##
 attribute to set and get the cache key for the entry */

## saveLayoutStateFlag ##
 attribute to indicate whether layoutHistoryState should be saved */

## expirationStatus ##
 attribute to indicate whether the page is already expired in cache */

## contentType ##

attribute to indicate the content-type of the document that this
is a session history entry for


## URIWasModified ##

If we created this SHEntry via history.pushState or modified it via
history.replaceState, and if we changed the SHEntry's URI via the
push/replaceState call, and if the SHEntry's new URI differs from its
old URI by more than just the hash, then we set this field to true.

Additionally, if this SHEntry was created by calling pushState from a
SHEntry whose URI was modified, this SHEntry's URIWasModified field is
true.



## setScrollPosition ##
 Set/Get scrollers' positon in anchored pages */

## getScrollPosition ##

## create ##
 Additional ways to create an entry */

## clone ##

## setIsSubFrame ##
 Attribute that indicates if this entry is for a subframe navigation */

## getAnyContentViewer ##
 Return any content viewer present in or below this node in the
nsSHEntry tree.  This will differ from contentViewer in the case
where a child nsSHEntry has the content viewer for this tree. */

## owner ##

Get the owner, if any, that was associated with the channel
that the document that was loaded to create this history entry
came from.


## stateData ##

Get/set data associated with this history state via a pushState() call,
serialized using structured clone.
/

## forgetEditorData ##

Gets the owning pointer to the editor data assosicated with
this shistory entry. This forgets its pointer, so free it when
you're done.


## setEditorData ##

Sets the owning pointer to the editor data assosicated with
this shistory entry. Unless forgetEditorData() is called, this
shentry will destroy the editor data when it's destroyed.


## hasDetachedEditor ##
 Returns true if this shistory entry is storing a detached editor. */

## isDynamicallyAdded ##

Returns true if the related docshell was added because of
dynamic addition of an iframe/frame.


## hasDynamicallyAddedChild ##

Returns true if any of the child entries returns true
when isDynamicallyAdded is called on it.


## docshellID ##

The history ID of the docshell.


## BFCacheEntry ##

## hasBFCacheEntry ##

Does this SHEntry point to the given BFCache entry?  If so, evicting
the BFCache entry will evict the SHEntry, since the two entries
correspond to the same document.


## adoptBFCacheEntry ##

Adopt aEntry's BFCacheEntry, so now both this and aEntry point to
aEntry's BFCacheEntry.


## abandonBFCacheEntry ##

Create a new BFCache entry and drop our reference to our old one.  This
call unlinks this SHEntry from any other SHEntries for its document.


## sharesDocumentWith ##

Does this SHEntry correspond to the same document as aEntry?  This is
true iff the two SHEntries have the same BFCacheEntry.  So in
particular, sharesDocumentWith(aEntry) is guaranteed to return true if
it's preceeded by a call to adoptBFCacheEntry(aEntry).


## isSrcdocEntry ##

True if this SHEntry corresponds to a document created by a srcdoc iframe.
Set when a value is assigned to  srcdocData.


## srcdocData ##

Contents of the srcdoc attribute in a srcdoc iframe to be loaded instead
of the URI.  Similar to a Data URI, this information is needed to
recreate the document at a later stage.
Setting this sets isSrcdocEntry to true


## baseURI ##

When isSrcdocEntry is true, this contains the baseURI of the srcdoc
document for use in situations where it cannot otherwise be determined,
for example with view-source.

