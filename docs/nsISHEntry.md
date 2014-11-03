---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/docshell/shistory/public/nsISHEntry.idl">Source file</a>
</div>

# nsISHEntry #

## Methods ##

### setURI(aURI) ###
<pre> URI for the document */  
</pre>
### getViewerBounds(bounds) ###
<pre>  
Saved position and dimensions of the content viewer; we must adjust the  
root view's widget accordingly if this has changed when the presentation  
is restored.  
  
</pre>
### setViewerBounds(bounds) ###

### addChildShell(shell) ###
<pre>  
Saved child docshells corresponding to contentViewer.  The child shells  
are restored as children of the parent docshell, in this order, when the  
parent docshell restores a saved presentation.  
  
</pre><pre> Append a child shell to the end of our list. */  
</pre>
### childShellAt(index) ###
<pre>  
Get the child shell at |index|; returns null if |index| is out of bounds.  
  
</pre>
### clearChildShells() ###
<pre>  
Clear the child shell list.  
  
</pre>
### syncPresentationState() ###
<pre>  
Ensure that the cached presentation members are self-consistent.  
If either |contentViewer| or |windowState| are null, then all of the  
following members are cleared/reset:  
 contentViewer, sticky, windowState, viewerBounds, childShells,  
 refreshURIList.  
  
</pre>
### setTitle(aTitle) ###
<pre> Title for the document */  
</pre>
### setScrollPosition(x, y) ###
<pre> Set/Get scrollers' positon in anchored pages */  
</pre>
### getScrollPosition(x, y) ###

### create(URI, title, inputStream, layoutHistoryState, cacheKey, contentType, owner, docshellID, dynamicCreation) ###
<pre> Additional ways to create an entry */  
</pre>
### clone() ###

### setIsSubFrame(aFlag) ###
<pre> Attribute that indicates if this entry is for a subframe navigation */  
</pre>
### getAnyContentViewer(ownerEntry) ###
<pre> Return any content viewer present in or below this node in the  
nsSHEntry tree.  This will differ from contentViewer in the case  
where a child nsSHEntry has the content viewer for this tree. */  
</pre>
### forgetEditorData() ###
<pre>  
Gets the owning pointer to the editor data assosicated with  
this shistory entry. This forgets its pointer, so free it when  
you're done.  
  
</pre>
### setEditorData(aData) ###
<pre>  
Sets the owning pointer to the editor data assosicated with  
this shistory entry. Unless forgetEditorData() is called, this  
shentry will destroy the editor data when it's destroyed.  
  
</pre>
### hasDetachedEditor() ###
<pre> Returns true if this shistory entry is storing a detached editor. */  
</pre>
### isDynamicallyAdded() ###
<pre>  
Returns true if the related docshell was added because of  
dynamic addition of an iframe/frame.  
  
</pre>
### hasDynamicallyAddedChild() ###
<pre>  
Returns true if any of the child entries returns true  
when isDynamicallyAdded is called on it.  
  
</pre>
### hasBFCacheEntry(aEntry) ###
<pre>  
Does this SHEntry point to the given BFCache entry?  If so, evicting  
the BFCache entry will evict the SHEntry, since the two entries  
correspond to the same document.  
  
</pre>
### adoptBFCacheEntry(aEntry) ###
<pre>  
Adopt aEntry's BFCacheEntry, so now both this and aEntry point to  
aEntry's BFCacheEntry.  
  
</pre>
### abandonBFCacheEntry() ###
<pre>  
Create a new BFCache entry and drop our reference to our old one.  This  
call unlinks this SHEntry from any other SHEntries for its document.  
  
</pre>
### sharesDocumentWith(aEntry) ###
<pre>  
Does this SHEntry correspond to the same document as aEntry?  This is  
true iff the two SHEntries have the same BFCacheEntry.  So in  
particular, sharesDocumentWith(aEntry) is guaranteed to return true if  
it's preceeded by a call to adoptBFCacheEntry(aEntry).  
  
</pre>
## Attributes ##

### URI ###
<pre>  
A readonly property that returns the URI  
of the current entry. The object returned is  
of type nsIURI  
  
</pre>
### title ###
<pre>  
A readonly property that returns the title  
of the current entry.  The object returned  
is a encoded string  
  
</pre>
### isSubFrame ###
<pre>  
A readonly property that returns a boolean  
flag which indicates if the entry was created as a  
result of a subframe navigation. This flag will be  
'false' when a frameset page is visited for  
the first time. This flag will be 'true' for all  
history entries created as a result of a subframe  
navigation.  
  
</pre>
### referrerURI ###
<pre> Referrer URI */  
</pre>
### contentViewer ###
<pre> Content viewer, for fast restoration of presentation */  
</pre>
### sticky ###
<pre> Whether the content viewer is marked "sticky" */  
</pre>
### windowState ###
<pre> Saved state of the global window object */  
</pre>
### refreshURIList ###
<pre> Saved refresh URI list for the content viewer */  
</pre>
### postData ###
<pre> Post Data for the document */  
</pre>
### layoutHistoryState ###
<pre> LayoutHistoryState for scroll position and form values */  
</pre>
### parent ###
<pre> parent of this entry */  
</pre>
### loadType ###
<pre>  
The loadType for this entry. This is typically loadHistory except  
when reload is pressed, it has the appropriate reload flag  
  
</pre>
### ID ###
<pre>  
An ID to help identify this entry from others during  
subframe navigation  
  
</pre>
### cacheKey ###
<pre> attribute to set and get the cache key for the entry */  
</pre>
### saveLayoutStateFlag ###
<pre> attribute to indicate whether layoutHistoryState should be saved */  
</pre>
### expirationStatus ###
<pre> attribute to indicate whether the page is already expired in cache */  
</pre>
### contentType ###
<pre>  
attribute to indicate the content-type of the document that this  
is a session history entry for  
  
</pre>
### URIWasModified ###
<pre>  
If we created this SHEntry via history.pushState or modified it via  
history.replaceState, and if we changed the SHEntry's URI via the  
push/replaceState call, and if the SHEntry's new URI differs from its  
old URI by more than just the hash, then we set this field to true.  
  
Additionally, if this SHEntry was created by calling pushState from a  
SHEntry whose URI was modified, this SHEntry's URIWasModified field is  
true.  
  
  
</pre>
### owner ###
<pre>  
Get the owner, if any, that was associated with the channel  
that the document that was loaded to create this history entry  
came from.  
  
</pre>
### stateData ###
<pre>  
Get/set data associated with this history state via a pushState() call,  
serialized using structured clone.  
/  
</pre>
### docshellID ###
<pre>  
The history ID of the docshell.  
  
</pre>
### BFCacheEntry ###

### isSrcdocEntry ###
<pre>  
True if this SHEntry corresponds to a document created by a srcdoc iframe.  
Set when a value is assigned to  srcdocData.  
  
</pre>
### srcdocData ###
<pre>  
Contents of the srcdoc attribute in a srcdoc iframe to be loaded instead  
of the URI.  Similar to a Data URI, this information is needed to  
recreate the document at a later stage.  
Setting this sets isSrcdocEntry to true  
  
</pre>
### baseURI ###
<pre>  
When isSrcdocEntry is true, this contains the baseURI of the srcdoc  
document for use in situations where it cannot otherwise be determined,  
for example with view-source.  
  
</pre>