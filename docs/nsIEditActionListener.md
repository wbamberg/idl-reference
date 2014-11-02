---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/editor/nsIEditActionListener.idl">Source file</a>
</div>

# nsIEditActionListener #
  
A generic editor action listener interface.   
<P>  
nsIEditActionListener is the interface used by applications wishing to be notified  
when the editor modifies the DOM tree.  
  
Note:  this is the wrong class to implement if you are interested in generic  
change notifications.  For generic notifications, you should implement  
nsIDocumentObserver.  
  

## Methods ##

### WillCreateNode(aTag, aParent, aPosition) ###
   
Called before the editor creates a node.  
@param aTag      The tag name of the DOM Node to create.  
@param aParent   The node to insert the new object into  
@param aPosition The place in aParent to insert the new node  
                 0=first child, 1=second child, etc.  
                 any number > number of current children = last child  
  

#### Parameters ####

<table>

<tr>
<td>aTag</td>
<td>The tag name of the DOM Node to create.  
</td>
</tr>

<tr>
<td>aParent</td>
<td>The node to insert the new object into  
</td>
</tr>

<tr>
<td>aPosition</td>
<td>The place in aParent to insert the new node  
                 0=first child, 1=second child, etc.  
                 any number > number of current children = last child  
</td>
</tr>

</table>

### DidCreateNode(aTag, aNode, aParent, aPosition, aResult) ###
   
Called after the editor creates a node.  
@param aTag      The tag name of the DOM Node to create.  
@param aNode     The DOM Node that was created.  
@param aParent   The node to insert the new object into  
@param aPosition The place in aParent to insert the new node  
                 0=first child, 1=second child, etc.  
                 any number > number of current children = last child  
@param aResult   The result of the create node operation.  
  

#### Parameters ####

<table>

<tr>
<td>aTag</td>
<td>The tag name of the DOM Node to create.  
</td>
</tr>

<tr>
<td>aNode</td>
<td>The DOM Node that was created.  
</td>
</tr>

<tr>
<td>aParent</td>
<td>The node to insert the new object into  
</td>
</tr>

<tr>
<td>aPosition</td>
<td>The place in aParent to insert the new node  
                 0=first child, 1=second child, etc.  
                 any number > number of current children = last child  
</td>
</tr>

<tr>
<td>aResult</td>
<td>The result of the create node operation.  
</td>
</tr>

</table>

### WillInsertNode(aNode, aParent, aPosition) ###
   
Called before the editor inserts a node.  
@param aNode     The DOM Node to insert.  
@param aParent   The node to insert the new object into  
@param aPosition The place in aParent to insert the new node  
                 0=first child, 1=second child, etc.  
                 any number > number of current children = last child  
  

#### Parameters ####

<table>

<tr>
<td>aNode</td>
<td>The DOM Node to insert.  
</td>
</tr>

<tr>
<td>aParent</td>
<td>The node to insert the new object into  
</td>
</tr>

<tr>
<td>aPosition</td>
<td>The place in aParent to insert the new node  
                 0=first child, 1=second child, etc.  
                 any number > number of current children = last child  
</td>
</tr>

</table>

### DidInsertNode(aNode, aParent, aPosition, aResult) ###
   
Called after the editor inserts a node.  
@param aNode     The DOM Node to insert.  
@param aParent   The node to insert the new object into  
@param aPosition The place in aParent to insert the new node  
                 0=first child, 1=second child, etc.  
                 any number > number of current children = last child  
@param aResult   The result of the insert node operation.  
  

#### Parameters ####

<table>

<tr>
<td>aNode</td>
<td>The DOM Node to insert.  
</td>
</tr>

<tr>
<td>aParent</td>
<td>The node to insert the new object into  
</td>
</tr>

<tr>
<td>aPosition</td>
<td>The place in aParent to insert the new node  
                 0=first child, 1=second child, etc.  
                 any number > number of current children = last child  
</td>
</tr>

<tr>
<td>aResult</td>
<td>The result of the insert node operation.  
</td>
</tr>

</table>

### WillDeleteNode(aChild) ###
   
Called before the editor deletes a node.  
@param aChild    The node to delete  
  

#### Parameters ####

<table>

<tr>
<td>aChild</td>
<td>The node to delete  
</td>
</tr>

</table>

### DidDeleteNode(aChild, aResult) ###
   
Called after the editor deletes a node.  
@param aChild    The node to delete  
@param aResult   The result of the delete node operation.  
  

#### Parameters ####

<table>

<tr>
<td>aChild</td>
<td>The node to delete  
</td>
</tr>

<tr>
<td>aResult</td>
<td>The result of the delete node operation.  
</td>
</tr>

</table>

### WillSplitNode(aExistingRightNode, aOffset) ###
   
Called before the editor splits a node.  
@param aExistingRightNode   the node to split.  It will become the new node's next sibling.  
@param aOffset              the offset of aExistingRightNode's content|children to do the split at  
@param aNewLeftNode         [OUT] the new node resulting from the split, becomes aExistingRightNode's previous sibling.  
  

#### Parameters ####

<table>

<tr>
<td>aExistingRightNode</td>
<td>the node to split.  It will become the new node's next sibling.  
</td>
</tr>

<tr>
<td>aOffset</td>
<td>the offset of aExistingRightNode's content|children to do the split at  
</td>
</tr>

<tr>
<td>aNewLeftNode</td>
<td>[OUT] the new node resulting from the split, becomes aExistingRightNode's previous sibling.  
</td>
</tr>

</table>

### DidSplitNode(aExistingRightNode, aOffset, aNewLeftNode, aResult) ###
   
Called after the editor splits a node.  
@param aExistingRightNode   the node to split.  It will become the new node's next sibling.  
@param aOffset              the offset of aExistingRightNode's content|children to do the split at  
@param aNewLeftNode         [OUT] the new node resulting from the split, becomes aExistingRightNode's previous sibling.  
  

#### Parameters ####

<table>

<tr>
<td>aExistingRightNode</td>
<td>the node to split.  It will become the new node's next sibling.  
</td>
</tr>

<tr>
<td>aOffset</td>
<td>the offset of aExistingRightNode's content|children to do the split at  
</td>
</tr>

<tr>
<td>aNewLeftNode</td>
<td>[OUT] the new node resulting from the split, becomes aExistingRightNode's previous sibling.  
</td>
</tr>

</table>

### WillJoinNodes(aLeftNode, aRightNode, aParent) ###
   
Called before the editor joins 2 nodes.  
@param aLeftNode   This node will be merged into the right node  
@param aRightNode  The node that will be merged into.  
                   There is no requirement that the two nodes be of  
                   the same type.  
@param aParent     The parent of aRightNode  
  

#### Parameters ####

<table>

<tr>
<td>aLeftNode</td>
<td>This node will be merged into the right node  
</td>
</tr>

<tr>
<td>aRightNode</td>
<td>The node that will be merged into.  
                   There is no requirement that the two nodes be of  
                   the same type.  
</td>
</tr>

<tr>
<td>aParent</td>
<td>The parent of aRightNode  
</td>
</tr>

</table>

### DidJoinNodes(aLeftNode, aRightNode, aParent, aResult) ###
   
Called after the editor joins 2 nodes.  
@param aLeftNode   This node will be merged into the right node  
@param aRightNode  The node that will be merged into.  
                   There is no requirement that the two nodes be of  
                   the same type.  
@param aParent     The parent of aRightNode  
@param aResult     The result of the join operation.  
  

#### Parameters ####

<table>

<tr>
<td>aLeftNode</td>
<td>This node will be merged into the right node  
</td>
</tr>

<tr>
<td>aRightNode</td>
<td>The node that will be merged into.  
                   There is no requirement that the two nodes be of  
                   the same type.  
</td>
</tr>

<tr>
<td>aParent</td>
<td>The parent of aRightNode  
</td>
</tr>

<tr>
<td>aResult</td>
<td>The result of the join operation.  
</td>
</tr>

</table>

### WillInsertText(aTextNode, aOffset, aString) ###
   
Called before the editor inserts text.  
@param aTextNode   This node getting inserted text  
@param aOffset     The offset in aTextNode to insert at.  
@param aString     The string that gets inserted.  
  

#### Parameters ####

<table>

<tr>
<td>aTextNode</td>
<td>This node getting inserted text  
</td>
</tr>

<tr>
<td>aOffset</td>
<td>The offset in aTextNode to insert at.  
</td>
</tr>

<tr>
<td>aString</td>
<td>The string that gets inserted.  
</td>
</tr>

</table>

### DidInsertText(aTextNode, aOffset, aString, aResult) ###
   
Called after the editor inserts text.  
@param aTextNode   This node getting inserted text  
@param aOffset     The offset in aTextNode to insert at.  
@param aString     The string that gets inserted.  
@param aResult     The result of the insert text operation.  
  

#### Parameters ####

<table>

<tr>
<td>aTextNode</td>
<td>This node getting inserted text  
</td>
</tr>

<tr>
<td>aOffset</td>
<td>The offset in aTextNode to insert at.  
</td>
</tr>

<tr>
<td>aString</td>
<td>The string that gets inserted.  
</td>
</tr>

<tr>
<td>aResult</td>
<td>The result of the insert text operation.  
</td>
</tr>

</table>

### WillDeleteText(aTextNode, aOffset, aLength) ###
   
Called before the editor deletes text.  
@param aTextNode   This node getting text deleted  
@param aOffset     The offset in aTextNode to delete at.  
@param aLength     The amount of text to delete.  
  

#### Parameters ####

<table>

<tr>
<td>aTextNode</td>
<td>This node getting text deleted  
</td>
</tr>

<tr>
<td>aOffset</td>
<td>The offset in aTextNode to delete at.  
</td>
</tr>

<tr>
<td>aLength</td>
<td>The amount of text to delete.  
</td>
</tr>

</table>

### DidDeleteText(aTextNode, aOffset, aLength, aResult) ###
   
Called before the editor deletes text.  
@param aTextNode   This node getting text deleted  
@param aOffset     The offset in aTextNode to delete at.  
@param aLength     The amount of text to delete.  
@param aResult     The result of the delete text operation.  
  

#### Parameters ####

<table>

<tr>
<td>aTextNode</td>
<td>This node getting text deleted  
</td>
</tr>

<tr>
<td>aOffset</td>
<td>The offset in aTextNode to delete at.  
</td>
</tr>

<tr>
<td>aLength</td>
<td>The amount of text to delete.  
</td>
</tr>

<tr>
<td>aResult</td>
<td>The result of the delete text operation.  
</td>
</tr>

</table>

### WillDeleteSelection(aSelection) ###
   
Called before the editor deletes the selection.  
@param aSelection   The selection to be deleted  
  

#### Parameters ####

<table>

<tr>
<td>aSelection</td>
<td>The selection to be deleted  
</td>
</tr>

</table>

### DidDeleteSelection(aSelection) ###
   
Called after the editor deletes the selection.  
@param aSelection   The selection, after deletion  
  

#### Parameters ####

<table>

<tr>
<td>aSelection</td>
<td>The selection, after deletion  
</td>
</tr>

</table>
