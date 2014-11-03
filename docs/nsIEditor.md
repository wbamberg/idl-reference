---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/editor/nsIEditor.idl">Source file</a>
</div>

# nsIEditor #

## Methods ##

### finalizeSelection() ###
<code>  
Finalizes selection and caret for the editor.  
  
</code>
### init(doc, aRoot, aSelCon, aFlags, initialValue) ###
<code>  
Init is to tell the implementation of nsIEditor to begin its services  
@param aDoc          The dom document interface being observed  
@param aRoot         This is the root of the editable section of this  
                     document. If it is null then we get root  
                     from document body.  
@param aSelCon       this should be used to get the selection location  
                     (will be null for HTML editors)  
@param aFlags        A bitmask of flags for specifying the behavior  
                     of the editor.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aDoc</td>
<td>The dom document interface being observed  
</td>
</tr>

<tr>
<td>aRoot</td>
<td>This is the root of the editable section of this  
                     document. If it is null then we get root  
                     from document body.  
</td>
</tr>

<tr>
<td>aSelCon</td>
<td>this should be used to get the selection location  
                     (will be null for HTML editors)  
</td>
</tr>

<tr>
<td>aFlags</td>
<td>A bitmask of flags for specifying the behavior  
                     of the editor.  
</td>
</tr>

</table>

### setAttributeOrEquivalent(element, sourceAttrName, sourceAttrValue, aSuppressTransaction) ###

### removeAttributeOrEquivalent(element, sourceAttrName, aSuppressTransaction) ###

### postCreate() ###
<code>  
postCreate should be called after Init, and is the time that the editor  
tells its documentStateObservers that the document has been created.  
  
</code>
### preDestroy(aDestroyingFrames) ###
<code>  
preDestroy is called before the editor goes away, and gives the editor a  
chance to tell its documentStateObservers that the document is going away.  
@param aDestroyingFrames set to true when the frames being edited  
are being destroyed (so there is no need to modify any nsISelections,  
nor is it safe to do so)  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aDestroyingFrames</td>
<td>set to true when the frames being edited  
are being destroyed (so there is no need to modify any nsISelections,  
nor is it safe to do so)  
</td>
</tr>

</table>

### deleteSelection(action, stripWrappers) ###
<code>   
DeleteSelection removes all nodes in the current selection.  
@param aDir  if eNext, delete to the right (for example, the DEL key)  
             if ePrevious, delete to the left (for example, the BACKSPACE key)  
@param stripWrappers If eStrip, strip any empty inline elements left  
                     behind after the deletion; if eNoStrip, don't.  If in  
                     doubt, pass eStrip -- eNoStrip is only for if you're  
                     about to insert text or similar right after.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aDir</td>
<td>if eNext, delete to the right (for example, the DEL key)  
             if ePrevious, delete to the left (for example, the BACKSPACE key)  
</td>
</tr>

<tr>
<td>stripWrappers</td>
<td>If eStrip, strip any empty inline elements left  
                     behind after the deletion; if eNoStrip, don't.  If in  
                     doubt, pass eStrip -- eNoStrip is only for if you're  
                     about to insert text or similar right after.  
</td>
</tr>

</table>

### resetModificationCount() ###
<code> to be used ONLY when we need to override the doc's modification  
state (such as when it's saved).  
  
</code>
### getModificationCount() ###
<code> Gets the modification count of the document we are editing.  
@return the modification count of the document being edited.  
        Zero means unchanged.  
  
</code>
#### Returns ####

<table>

<tr>
<td>the modification count of the document being edited.  
        Zero means unchanged.  
</td>
</tr>

</table>

### incrementModificationCount(aModCount) ###
<code> called each time we modify the document.  
Increments the modification count of the document.  
@param  aModCount  the number of modifications by which  
                   to increase or decrease the count  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aModCount</td>
<td>the number of modifications by which  
                   to increase or decrease the count  
</td>
</tr>

</table>

### doTransaction(txn) ###
<code> doTransaction() fires a transaction.  
It is provided here so clients can create their own transactions.  
If a transaction manager is present, it is used.    
Otherwise, the transaction is just executed directly.  
  
@param aTxn the transaction to execute  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aTxn</td>
<td>the transaction to execute  
</td>
</tr>

</table>

### enableUndo(enable) ###
<code> turn the undo system on or off  
@param aEnable  if PR_TRUE, the undo system is turned on if available  
                if PR_FALSE the undo system is turned off if it  
                was previously on  
@return         if aEnable is PR_TRUE, returns NS_OK if  
                the undo system could be initialized properly  
                if aEnable is PR_FALSE, returns NS_OK.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aEnable</td>
<td>if PR_TRUE, the undo system is turned on if available  
                if PR_FALSE the undo system is turned off if it  
                was previously on  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>if aEnable is PR_TRUE, returns NS_OK if  
                the undo system could be initialized properly  
                if aEnable is PR_FALSE, returns NS_OK.  
</td>
</tr>

</table>

### undo(count) ###
<code> undo reverses the effects of the last Do operation,  
if Undo is enabled in the editor.  
It is provided here so clients need no knowledge of whether  
the editor has a transaction manager or not.  
If a transaction manager is present, it is told to undo,  
and the result of that undo is returned.    
Otherwise, the Undo request is ignored and an  
error NS_ERROR_NOT_AVAILABLE is returned.  
  
  
</code>
### canUndo(isEnabled, canUndo) ###
<code> returns state information about the undo system.  
@param aIsEnabled [OUT] PR_TRUE if undo is enabled  
@param aCanUndo   [OUT] PR_TRUE if at least one transaction is  
                        currently ready to be undone.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aIsEnabled</td>
<td>[OUT] PR_TRUE if undo is enabled  
</td>
</tr>

<tr>
<td>aCanUndo</td>
<td>[OUT] PR_TRUE if at least one transaction is  
                        currently ready to be undone.  
</td>
</tr>

</table>

### redo(count) ###
<code> redo reverses the effects of the last Undo operation  
It is provided here so clients need no knowledge of whether  
the editor has a transaction manager or not.  
If a transaction manager is present, it is told to redo and the  
result of the previously undone transaction is reapplied to the document.  
If no transaction is available for Redo, or if the document  
has no transaction manager, the Redo request is ignored and an  
error NS_ERROR_NOT_AVAILABLE is returned.  
  
  
</code>
### canRedo(isEnabled, canRedo) ###
<code> returns state information about the redo system.  
@param aIsEnabled [OUT] PR_TRUE if redo is enabled  
@param aCanRedo   [OUT] PR_TRUE if at least one transaction is  
currently ready to be redone.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aIsEnabled</td>
<td>[OUT] PR_TRUE if redo is enabled  
</td>
</tr>

<tr>
<td>aCanRedo</td>
<td>[OUT] PR_TRUE if at least one transaction is  
currently ready to be redone.  
</td>
</tr>

</table>

### beginTransaction() ###
<code> beginTransaction is a signal from the caller to the editor that  
the caller will execute multiple updates to the content tree  
that should be treated as a single logical operation,  
in the most efficient way possible.<br>  
All transactions executed between a call to beginTransaction and  
endTransaction will be undoable as an atomic action.<br>  
endTransaction must be called after beginTransaction.<br>  
Calls to beginTransaction can be nested, as long as endTransaction  
is called once per beginUpdate.  
  
</code>
### endTransaction() ###
<code> endTransaction is a signal to the editor that the caller is  
finished updating the content model.<br>  
beginUpdate must be called before endTransaction is called.<br>  
Calls to beginTransaction can be nested, as long as endTransaction  
is called once per beginTransaction.  
  
</code>
### beginPlaceHolderTransaction(name) ###

### endPlaceHolderTransaction() ###

### shouldTxnSetSelection() ###

### setShouldTxnSetSelection(should) ###
<code> Set the flag that prevents insertElementTxn from changing the selection  
@param   should  Set false to suppress changing the selection;  
                 i.e., before using InsertElement() to insert  
                 under <head> element  
WARNING: You must be very careful to reset back to PR_TRUE after  
         setting PR_FALSE, else selection/caret is trashed  
         for further editing.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>should</td>
<td>Set false to suppress changing the selection;  
                 i.e., before using InsertElement() to insert  
                 under <head> element  
WARNING: You must be very careful to reset back to PR_TRUE after  
         setting PR_FALSE, else selection/caret is trashed  
         for further editing.  
</td>
</tr>

</table>

### getInlineSpellChecker(autoCreate) ###
<code> Returns the inline spell checker associated with this object. The spell  
checker is lazily created, so this function may create the object for  
you during this call.  
@param  autoCreate  If true, this will create a spell checker object  
                    if one does not exist yet for this editor. If false  
                    and the object has not been created, this function  
                    WILL RETURN NULL.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>autoCreate</td>
<td>If true, this will create a spell checker object  
                    if one does not exist yet for this editor. If false  
                    and the object has not been created, this function  
                    WILL RETURN NULL.  
</td>
</tr>

</table>

### syncRealTimeSpell() ###
<code> Resyncs spellchecking state (enabled/disabled).  This should be called  
when anything that affects spellchecking state changes, such as the  
spellcheck attribute value.  
  
</code>
### setSpellcheckUserOverride(enable) ###
<code> Called when the user manually overrides the spellchecking state for this  
editor.  
@param  enable  The new state of spellchecking in this editor, as  
                requested by the user.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>enable</td>
<td>The new state of spellchecking in this editor, as  
                requested by the user.  
</td>
</tr>

</table>

### cut() ###
<code> cut the currently selected text, putting it into the OS clipboard  
What if no text is selected?  
What about mixed selections?  
What are the clipboard formats?  
  
</code>
### canCut() ###
<code> Can we cut? True if the doc is modifiable, and we have a non-  
collapsed selection.  
  
</code>
### copy() ###
<code> copy the currently selected text, putting it into the OS clipboard  
What if no text is selected?  
What about mixed selections?  
What are the clipboard formats?  
  
</code>
### canCopy() ###
<code> Can we copy? True if we have a non-collapsed selection.  
  
</code>
### paste(aSelectionType) ###
<code> paste the text in the OS clipboard at the cursor position, replacing  
the selected text (if any)  
  
</code>
### pasteTransferable(aTransferable) ###
<code> Paste the text in |aTransferable| at the cursor position, replacing the  
selected text (if any).  
  
</code>
### canPaste(aSelectionType) ###
<code> Can we paste? True if the doc is modifiable, and we have  
pasteable data in the clipboard.  
  
</code>
### canPasteTransferable(aTransferable) ###
<code> Can we paste |aTransferable| or, if |aTransferable| is null, will a call  
to pasteTransferable later possibly succeed if given an instance of  
nsITransferable then? True if the doc is modifiable, and, if  
|aTransfeable| is non-null, we have pasteable data in |aTransfeable|.  
  
</code>
### selectAll() ###
<code> sets the document selection to the entire contents of the document */  
</code>
### beginningOfDocument() ###
<code> sets the document selection to the beginning of the document */  
</code>
### endOfDocument() ###
<code> sets the document selection to the end of the document */  
</code>
### setAttribute(aElement, attributestr, attvalue) ###
<code>  
setAttribute() sets the attribute of aElement.  
No checking is done to see if aAttribute is a legal attribute of the node,  
or if aValue is a legal value of aAttribute.  
  
@param aElement    the content element to operate on  
@param aAttribute  the string representation of the attribute to set  
@param aValue      the value to set aAttribute to  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aElement</td>
<td>the content element to operate on  
</td>
</tr>

<tr>
<td>aAttribute</td>
<td>the string representation of the attribute to set  
</td>
</tr>

<tr>
<td>aValue</td>
<td>the value to set aAttribute to  
</td>
</tr>

</table>

### getAttributeValue(aElement, attributestr, resultValue) ###
<code>  
getAttributeValue() retrieves the attribute's value for aElement.  
  
@param aElement      the content element to operate on  
@param aAttribute    the string representation of the attribute to get  
@param aResultValue  [OUT] the value of aAttribute.  
                     Only valid if aResultIsSet is PR_TRUE  
@return              PR_TRUE if aAttribute is set on the current node,  
                     PR_FALSE if it is not.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aElement</td>
<td>the content element to operate on  
</td>
</tr>

<tr>
<td>aAttribute</td>
<td>the string representation of the attribute to get  
</td>
</tr>

<tr>
<td>aResultValue</td>
<td>[OUT] the value of aAttribute.  
                     Only valid if aResultIsSet is PR_TRUE  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>PR_TRUE if aAttribute is set on the current node,  
                     PR_FALSE if it is not.  
</td>
</tr>

</table>

### removeAttribute(aElement, aAttribute) ###
<code>  
removeAttribute() deletes aAttribute from the attribute list of aElement.  
If aAttribute is not an attribute of aElement, nothing is done.  
  
@param aElement      the content element to operate on  
@param aAttribute    the string representation of the attribute to get  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aElement</td>
<td>the content element to operate on  
</td>
</tr>

<tr>
<td>aAttribute</td>
<td>the string representation of the attribute to get  
</td>
</tr>

</table>

### cloneAttribute(aAttribute, aDestNode, aSourceNode) ###
<code>  
cloneAttribute() copies the attribute from the source node to  
the destination node and delete those not in the source.  
  
The supplied nodes MUST BE ELEMENTS (most callers are working with nodes)  
@param aAttribute    the name of the attribute to copy  
@param aDestNode     the destination element to operate on  
@param aSourceNode   the source element to copy attributes from  
@exception NS_ERROR_NULL_POINTER at least one of the nodes is null  
@exception NS_ERROR_NO_INTERFACE at least one of the nodes is not an  
                                 element  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aAttribute</td>
<td>the name of the attribute to copy  
</td>
</tr>

<tr>
<td>aDestNode</td>
<td>the destination element to operate on  
</td>
</tr>

<tr>
<td>aSourceNode</td>
<td>the source element to copy attributes from  
@exception NS_ERROR_NULL_POINTER at least one of the nodes is null  
@exception NS_ERROR_NO_INTERFACE at least one of the nodes is not an  
                                 element  
</td>
</tr>

</table>

### cloneAttributes(destNode, sourceNode) ###
<code>  
cloneAttributes() is similar to nsIDOMNode::cloneNode(),  
  it assures the attribute nodes of the destination are identical  
  with the source node by copying all existing attributes from the  
  source and deleting those not in the source.  
  This is used when the destination node (element) already exists  
  
The supplied nodes MUST BE ELEMENTS (most callers are working with nodes)  
@param aDestNode     the destination element to operate on  
@param aSourceNode   the source element to copy attributes from  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aDestNode</td>
<td>the destination element to operate on  
</td>
</tr>

<tr>
<td>aSourceNode</td>
<td>the source element to copy attributes from  
</td>
</tr>

</table>

### createNode(tag, parent, position) ###
<code>   
createNode instantiates a new element of type aTag and inserts it  
into aParent at aPosition.  
@param aTag      The type of object to create  
@param aParent   The node to insert the new object into  
@param aPosition The place in aParent to insert the new node  
@return          The node created.  Caller must release aNewNode.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aTag</td>
<td>The type of object to create  
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
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The node created.  Caller must release aNewNode.  
</td>
</tr>

</table>

### insertNode(node, parent, aPosition) ###
<code>   
insertNode inserts aNode into aParent at aPosition.  
No checking is done to verify the legality of the insertion.  
That is the responsibility of the caller.  
@param aNode     The DOM Node to insert.  
@param aParent   The node to insert the new object into  
@param aPosition The place in aParent to insert the new node  
                 0=first child, 1=second child, etc.  
                 any number > number of current children = last child  
  
</code>
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

### splitNode(existingRightNode, offset, newLeftNode) ###
<code>   
splitNode() creates a new node identical to an existing node,  
and split the contents between the two nodes  
@param aExistingRightNode   the node to split.  
                            It will become the new node's next sibling.  
@param aOffset              the offset of aExistingRightNode's  
                            content|children to do the split at  
@param aNewLeftNode         [OUT] the new node resulting from the split,  
                            becomes aExistingRightNode's previous sibling.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aExistingRightNode</td>
<td>the node to split.  
                            It will become the new node's next sibling.  
</td>
</tr>

<tr>
<td>aOffset</td>
<td>the offset of aExistingRightNode's  
                            content|children to do the split at  
</td>
</tr>

<tr>
<td>aNewLeftNode</td>
<td>[OUT] the new node resulting from the split,  
                            becomes aExistingRightNode's previous sibling.  
</td>
</tr>

</table>

### joinNodes(leftNode, rightNode, parent) ###
<code>   
joinNodes() takes 2 nodes and merge their content|children.  
@param aLeftNode     The left node.  It will be deleted.  
@param aRightNode    The right node. It will remain after the join.  
@param aParent       The parent of aExistingRightNode  
  
                     There is no requirement that the two nodes be  
                     of the same type.  However, a text node can be  
                     merged only with another text node.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aLeftNode</td>
<td>The left node.  It will be deleted.  
</td>
</tr>

<tr>
<td>aRightNode</td>
<td>The right node. It will remain after the join.  
</td>
</tr>

<tr>
<td>aParent</td>
<td>The parent of aExistingRightNode  
</td>
</tr>

</table>

### deleteNode(child) ###
<code>   
deleteNode removes aChild from aParent.  
@param aChild    The node to delete  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aChild</td>
<td>The node to delete  
</td>
</tr>

</table>

### outputsMozDirty() ###
<code>  
Returns true if markNodeDirty() has any effect.  Returns false if  
markNodeDirty() is a no-op.  
  
</code>
### markNodeDirty(node) ###
<code>   
markNodeDirty() sets a special dirty attribute on the node.  
Usually this will be called immediately after creating a new node.  
@param aNode      The node for which to insert formatting.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aNode</td>
<td>The node for which to insert formatting.  
</td>
</tr>

</table>

### switchTextDirection() ###
<code>   
Switches the editor element direction; from "Left-to-Right" to  
"Right-to-Left", and vice versa.  
  
</code>
### outputToString(formatType, flags) ###
<code>  
Output methods:  
aFormatType is a mime type, like text/plain.  
  
</code>
### outputToStream(aStream, formatType, charsetOverride, flags) ###

### addEditorObserver(observer) ###
<code> add an EditorObserver to the editors list of observers. */  
</code>
### removeEditorObserver(observer) ###
<code> Remove an EditorObserver from the editor's list of observers. */  
</code>
### addEditActionListener(listener) ###
<code> add an EditActionListener to the editors list of listeners. */  
</code>
### removeEditActionListener(listener) ###
<code> Remove an EditActionListener from the editor's list of listeners. */  
</code>
### addDocumentStateListener(listener) ###
<code> Add a DocumentStateListener to the editors list of doc state listeners. */  
</code>
### removeDocumentStateListener(listener) ###
<code> Remove a DocumentStateListener to the editors list of doc state listeners. */  
</code>
### dumpContentTree() ###
<code>  
And a debug method -- show us what the tree looks like right now  
  
</code>
### debugDumpContent() ###
<code> Dumps a text representation of the content tree to standard out */  
</code>
### debugUnitTests(outNumTests, outNumTestsFailed) ###

### isModifiableNode(aNode) ###

## Attributes ##

### selection ###

### flags ###
 edit flags for this editor.  May be set at any time. */  

### contentsMIMEType ###
  
the MimeType of the document  
  

### isDocumentEditable ###
 Returns true if we have a document that is not marked read-only */  

### isSelectionEditable ###
 Returns true if the current selection anchor is editable */  

### document ###
  
the DOM Document this editor is associated with, refcounted.  
  

### rootElement ###
 the body element, i.e. the root of the editable document.  
  

### selectionController ###
  
the selection controller for the current presentation, refcounted.  
  

### documentIsEmpty ###
 Returns true if the document has no *meaningful* content */  

### documentModified ###
 Returns true if the document is modifed and needs saving */  

### documentCharacterSet ###
 Sets the current 'Save' document character set */  

### transactionManager ###
 transactionManager Get the transaction manager the editor is using.  
  

### numberOfUndoItems ###
  
The number of items on the undo stack.  
  

### numberOfRedoItems ###
  
The number of items on the redo stack.  
  

### suppressDispatchingInputEvent ###

### isInEditAction ###
  
True if an edit action is being handled (in other words, between calls of  
nsIEditorObserver::BeforeEditAction() and nsIEditorObserver::EditAction()  
or nsIEditorObserver::CancelEditAction().  Otherwise, false.  
  

## Constants ##

### eNone ###

### eNext ###

### ePrevious ###

### eNextWord ###

### ePreviousWord ###

### eToBeginningOfLine ###

### eToEndOfLine ###

### eStrip ###

### eNoStrip ###
