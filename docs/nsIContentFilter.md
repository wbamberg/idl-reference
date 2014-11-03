---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/editor/nsIContentFilter.idl">Source file</a>
</div>

# nsIContentFilter #

## Methods ##

### notifyOfInsertion(mimeType, contentSourceURL, sourceDocument, willDeleteSelection, docFragment, contentStartNode, contentStartOffset, contentEndNode, contentEndOffset, insertionPointNode, insertionPointOffset, continueWithInsertion) ###
<code>  
This notification occurs in an editor during these events:  
   * open of document (once rendered in window but before editable)  
   * paste from clipboard  
   * drop from mouse  
   * insertion of html (such as with "cmd_insertHTML")  
It provides a hook so the above actions can be canceled or the data  
can be modified (using standard DOM APIs) or left untouched.  The data  
that results (if any) from all filter callbacks is what will be used  
for transaction purposes (undo/redo) except for the open event.  
  
The willDeleteSelection parameter is offered for filters who want to  
handle the insertion themselves and need to handle drag/drop correctly.  
The flag is true when the editor intends to delete the selection.  
  
Callers who want to cancel all insertion can simply set  
continueWithInsertion to PR_FALSE and return.  
Note: If cancellation occurs during the "open" event, the editor will  
still be available but will be empty.  
  
Callers who want to allow insertion of the data with no changes  
can simply set continueWithInsertion to PR_TRUE and return.  
  
Callers who want to modify the content (docFragment) being inserted are   
responsible for updating contentStartNode, contentStartOffset,   
contentEndNode, and contentEndOffset (if necessary).    
Callers are responsible for freeing and addref'ing if they want to   
completely replace any of the DOM nodes passed in.  
  
The location where insertion will occur should be considered an  
approximation since the editor may need to adjust it if it deletes  
the selection as part of the event and later determines that insertion  
point is an empty container which should also be removed (or in other  
scenarios such as -moz-user-select:none).  
  
In some scenarios the selection will be deleted.  If callers choose  
to adjust the insertion point, they should be careful that the insertion  
point is not in the current selection.  
  
The contentStartNode and contentEndNode are not necessarily  
immediate children of the docFragment.  Any nodes outside of the range  
set by contentStartNode and contentEndNode are for context from the  
source document.  
  
@param mimeType          the mimetype used for retrieving data  
@param contentSourceURL  location where docFragment came from  
@param sourceDocument      document where content came from (can be null)  
@param willDeleteSelection tells hook if selection will/should be deleted  
@param docFragment         fragment of node to be inserted  
@param contentStartNode    node under which content to be inserted begins  
@param contentStartOffset  start offset within contentStartNode  
@param contentEndNode      node under which content to be inserted ends  
@param contentEndOffset    ending offset withing contentEndNode  
@param insertionPointNode     location where insertion will occur  
@param insertionPointOffset   offset within node where insertion occurs  
@param continueWithInsertion  flag to cancel insertion (if desired)  
  
</code>
#### Parameters ####

<table>

<tr>
<td>mimeType</td>
<td>the mimetype used for retrieving data  
</td>
</tr>

<tr>
<td>contentSourceURL</td>
<td>location where docFragment came from  
</td>
</tr>

<tr>
<td>sourceDocument</td>
<td>document where content came from (can be null)  
</td>
</tr>

<tr>
<td>willDeleteSelection</td>
<td>tells hook if selection will/should be deleted  
</td>
</tr>

<tr>
<td>docFragment</td>
<td>fragment of node to be inserted  
</td>
</tr>

<tr>
<td>contentStartNode</td>
<td>node under which content to be inserted begins  
</td>
</tr>

<tr>
<td>contentStartOffset</td>
<td>start offset within contentStartNode  
</td>
</tr>

<tr>
<td>contentEndNode</td>
<td>node under which content to be inserted ends  
</td>
</tr>

<tr>
<td>contentEndOffset</td>
<td>ending offset withing contentEndNode  
</td>
</tr>

<tr>
<td>insertionPointNode</td>
<td>location where insertion will occur  
</td>
</tr>

<tr>
<td>insertionPointOffset</td>
<td>offset within node where insertion occurs  
</td>
</tr>

<tr>
<td>continueWithInsertion</td>
<td>flag to cancel insertion (if desired)  
</td>
</tr>

</table>
