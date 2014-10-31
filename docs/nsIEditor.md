---
layout: default
---

# nsIEditor #

## Methods ##

### finalizeSelection() ###
  
Finalizes selection and caret for the editor.  
  

### init(doc, aRoot, aSelCon, aFlags, initialValue) ###
  
Init is to tell the implementation of nsIEditor to begin its services  
@param aDoc          The dom document interface being observed  
@param aRoot         This is the root of the editable section of this  
                     document. If it is null then we get root  
                     from document body.  
@param aSelCon       this should be used to get the selection location  
                     (will be null for HTML editors)  
@param aFlags        A bitmask of flags for specifying the behavior  
                     of the editor.  
  

#### Parameters ####

<table>

<tr>
<td>aDoc</td>
<td>The dom document interface being observed  
</td>
</tr>

<tr>
<td>aDoc</td>
<td>The dom document interface being observed  
</td>
</tr>

<tr>
<td>aDoc</td>
<td>The dom document interface being observed  
</td>
</tr>

<tr>
<td>aDoc</td>
<td>The dom document interface being observed  
</td>
</tr>

</table>

### setAttributeOrEquivalent(element, sourceAttrName, sourceAttrValue, aSuppressTransaction) ###

### removeAttributeOrEquivalent(element, sourceAttrName, aSuppressTransaction) ###

### postCreate() ###
  
postCreate should be called after Init, and is the time that the editor  
tells its documentStateObservers that the document has been created.  
  

### preDestroy(aDestroyingFrames) ###
  
preDestroy is called before the editor goes away, and gives the editor a  
chance to tell its documentStateObservers that the document is going away.  
@param aDestroyingFrames set to true when the frames being edited  
are being destroyed (so there is no need to modify any nsISelections,  
nor is it safe to do so)  
  

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
   
DeleteSelection removes all nodes in the current selection.  
@param aDir  if eNext, delete to the right (for example, the DEL key)  
             if ePrevious, delete to the left (for example, the BACKSPACE key)  
@param stripWrappers If eStrip, strip any empty inline elements left  
                     behind after the deletion; if eNoStrip, don't.  If in  
                     doubt, pass eStrip -- eNoStrip is only for if you're  
                     about to insert text or similar right after.  
  

#### Parameters ####

<table>

<tr>
<td>aDir</td>
<td>if eNext, delete to the right (for example, the DEL key)  
             if ePrevious, delete to the left (for example, the BACKSPACE key)  
</td>
</tr>

<tr>
<td>aDir</td>
<td>if eNext, delete to the right (for example, the DEL key)  
             if ePrevious, delete to the left (for example, the BACKSPACE key)  
</td>
</tr>

</table>

### resetModificationCount() ###
 to be used ONLY when we need to override the doc's modification  
state (such as when it's saved).  
  

### getModificationCount() ###
 Gets the modification count of the document we are editing.  
@return the modification count of the document being edited.  
        Zero means unchanged.  
  

### incrementModificationCount(aModCount) ###
 called each time we modify the document.  
Increments the modification count of the document.  
@param  aModCount  the number of modifications by which  
                   to increase or decrease the count  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>aModCount  the number of modifications by which  
                   to increase or decrease the count  
</td>
</tr>

</table>

### doTransaction(txn) ###
 doTransaction() fires a transaction.  
It is provided here so clients can create their own transactions.  
If a transaction manager is present, it is used.    
Otherwise, the transaction is just executed directly.  
  
@param aTxn the transaction to execute  
  

#### Parameters ####

<table>

<tr>
<td>aTxn</td>
<td>the transaction to execute  
</td>
</tr>

</table>

### enableUndo(enable) ###
 turn the undo system on or off  
@param aEnable  if PR_TRUE, the undo system is turned on if available  
                if PR_FALSE the undo system is turned off if it  
                was previously on  
@return         if aEnable is PR_TRUE, returns NS_OK if  
                the undo system could be initialized properly  
                if aEnable is PR_FALSE, returns NS_OK.  
  

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

### undo(count) ###
 undo reverses the effects of the last Do operation,  
if Undo is enabled in the editor.  
It is provided here so clients need no knowledge of whether  
the editor has a transaction manager or not.  
If a transaction manager is present, it is told to undo,  
and the result of that undo is returned.    
Otherwise, the Undo request is ignored and an  
error NS_ERROR_NOT_AVAILABLE is returned.  
  
  

### canUndo(isEnabled, canUndo) ###
 returns state information about the undo system.  
@param aIsEnabled [OUT] PR_TRUE if undo is enabled  
@param aCanUndo   [OUT] PR_TRUE if at least one transaction is  
                        currently ready to be undone.  
  

#### Parameters ####

<table>

<tr>
<td>aIsEnabled</td>
<td>[OUT] PR_TRUE if undo is enabled  
</td>
</tr>

<tr>
<td>aIsEnabled</td>
<td>[OUT] PR_TRUE if undo is enabled  
</td>
</tr>

</table>

### redo(count) ###
 redo reverses the effects of the last Undo operation  
It is provided here so clients need no knowledge of whether  
the editor has a transaction manager or not.  
If a transaction manager is present, it is told to redo and the  
result of the previously undone transaction is reapplied to the document.  
If no transaction is available for Redo, or if the document  
has no transaction manager, the Redo request is ignored and an  
error NS_ERROR_NOT_AVAILABLE is returned.  
  
  

### canRedo(isEnabled, canRedo) ###
 returns state information about the redo system.  
@param aIsEnabled [OUT] PR_TRUE if redo is enabled  
@param aCanRedo   [OUT] PR_TRUE if at least one transaction is  
currently ready to be redone.  
  

#### Parameters ####

<table>

<tr>
<td>aIsEnabled</td>
<td>[OUT] PR_TRUE if redo is enabled  
</td>
</tr>

<tr>
<td>aIsEnabled</td>
<td>[OUT] PR_TRUE if redo is enabled  
</td>
</tr>

</table>

### beginTransaction() ###
 beginTransaction is a signal from the caller to the editor that  
the caller will execute multiple updates to the content tree  
that should be treated as a single logical operation,  
in the most efficient way possible.<br>  
All transactions executed between a call to beginTransaction and  
endTransaction will be undoable as an atomic action.<br>  
endTransaction must be called after beginTransaction.<br>  
Calls to beginTransaction can be nested, as long as endTransaction  
is called once per beginUpdate.  
  

### endTransaction() ###
 endTransaction is a signal to the editor that the caller is  
finished updating the content model.<br>  
beginUpdate must be called before endTransaction is called.<br>  
Calls to beginTransaction can be nested, as long as endTransaction  
is called once per beginTransaction.  
  

### beginPlaceHolderTransaction(name) ###

### endPlaceHolderTransaction() ###

### shouldTxnSetSelection() ###

### setShouldTxnSetSelection(should) ###
 Set the flag that prevents insertElementTxn from changing the selection  
@param   should  Set false to suppress changing the selection;  
                 i.e., before using InsertElement() to insert  
                 under <head> element  
WARNING: You must be very careful to reset back to PR_TRUE after  
         setting PR_FALSE, else selection/caret is trashed  
         for further editing.  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>should  Set false to suppress changing the selection;  
                 i.e., before using InsertElement() to insert  
                 under <head> element  
WARNING: You must be very careful to reset back to PR_TRUE after  
         setting PR_FALSE, else selection/caret is trashed  
         for further editing.  
</td>
</tr>

</table>

### getInlineSpellChecker(autoCreate) ###
 Returns the inline spell checker associated with this object. The spell  
checker is lazily created, so this function may create the object for  
you during this call.  
@param  autoCreate  If true, this will create a spell checker object  
                    if one does not exist yet for this editor. If false  
                    and the object has not been created, this function  
                    WILL RETURN NULL.  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>autoCreate  If true, this will create a spell checker object  
                    if one does not exist yet for this editor. If false  
                    and the object has not been created, this function  
                    WILL RETURN NULL.  
</td>
</tr>

</table>

### syncRealTimeSpell() ###
 Resyncs spellchecking state (enabled/disabled).  This should be called  
when anything that affects spellchecking state changes, such as the  
spellcheck attribute value.  
  

### setSpellcheckUserOverride(enable) ###
 Called when the user manually overrides the spellchecking state for this  
editor.  
@param  enable  The new state of spellchecking in this editor, as  
                requested by the user.  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>enable  The new state of spellchecking in this editor, as  
                requested by the user.  
</td>
</tr>

</table>

### cut() ###
 cut the currently selected text, putting it into the OS clipboard  
What if no text is selected?  
What about mixed selections?  
What are the clipboard formats?  
  

### canCut() ###
 Can we cut? True if the doc is modifiable, and we have a non-  
collapsed selection.  
  

### copy() ###
 copy the currently selected text, putting it into the OS clipboard  
What if no text is selected?  
What about mixed selections?  
What are the clipboard formats?  
  

### canCopy() ###
 Can we copy? True if we have a non-collapsed selection.  
  

### paste(aSelectionType) ###
 paste the text in the OS clipboard at the cursor position, replacing  
the selected text (if any)  
  

### pasteTransferable(aTransferable) ###
 Paste the text in |aTransferable| at the cursor position, replacing the  
selected text (if any).  
  

### canPaste(aSelectionType) ###
 Can we paste? True if the doc is modifiable, and we have  
pasteable data in the clipboard.  
  

### canPasteTransferable(aTransferable) ###
 Can we paste |aTransferable| or, if |aTransferable| is null, will a call  
to pasteTransferable later possibly succeed if given an instance of  
nsITransferable then? True if the doc is modifiable, and, if  
|aTransfeable| is non-null, we have pasteable data in |aTransfeable|.  
  

### selectAll() ###
 sets the document selection to the entire contents of the document */  

### beginningOfDocument() ###
 sets the document selection to the beginning of the document */  

### endOfDocument() ###
 sets the document selection to the end of the document */  

### setAttribute(aElement, attributestr, attvalue) ###
  
setAttribute() sets the attribute of aElement.  
No checking is done to see if aAttribute is a legal attribute of the node,  
or if aValue is a legal value of aAttribute.  
  
@param aElement    the content element to operate on  
@param aAttribute  the string representation of the attribute to set  
@param aValue      the value to set aAttribute to  
  

#### Parameters ####

<table>

<tr>
<td>aElement</td>
<td>the content element to operate on  
</td>
</tr>

<tr>
<td>aElement</td>
<td>the content element to operate on  
</td>
</tr>

<tr>
<td>aElement</td>
<td>the content element to operate on  
</td>
</tr>

</table>

### getAttributeValue(aElement, attributestr, resultValue) ###
  
getAttributeValue() retrieves the attribute's value for aElement.  
  
@param aElement      the content element to operate on  
@param aAttribute    the string representation of the attribute to get  
@param aResultValue  [OUT] the value of aAttribute.  
                     Only valid if aResultIsSet is PR_TRUE  
@return              PR_TRUE if aAttribute is set on the current node,  
                     PR_FALSE if it is not.  
  

#### Parameters ####

<table>

<tr>
<td>aElement</td>
<td>the content element to operate on  
</td>
</tr>

<tr>
<td>aElement</td>
<td>the content element to operate on  
</td>
</tr>

<tr>
<td>aElement</td>
<td>the content element to operate on  
</td>
</tr>

</table>

### removeAttribute(aElement, aAttribute) ###
  
removeAttribute() deletes aAttribute from the attribute list of aElement.  
If aAttribute is not an attribute of aElement, nothing is done.  
  
@param aElement      the content element to operate on  
@param aAttribute    the string representation of the attribute to get  
  

#### Parameters ####

<table>

<tr>
<td>aElement</td>
<td>the content element to operate on  
</td>
</tr>

<tr>
<td>aElement</td>
<td>the content element to operate on  
</td>
</tr>

</table>

### cloneAttribute(aAttribute, aDestNode, aSourceNode) ###
  
cloneAttribute() copies the attribute from the source node to  
the destination node and delete those not in the source.  
  
The supplied nodes MUST BE ELEMENTS (most callers are working with nodes)  
@param aAttribute    the name of the attribute to copy  
@param aDestNode     the destination element to operate on  
@param aSourceNode   the source element to copy attributes from  
@exception NS_ERROR_NULL_POINTER at least one of the nodes is null  
@exception NS_ERROR_NO_INTERFACE at least one of the nodes is not an  
                                 element  
  

#### Parameters ####

<table>

<tr>
<td>aAttribute</td>
<td>the name of the attribute to copy  
</td>
</tr>

<tr>
<td>aAttribute</td>
<td>the name of the attribute to copy  
</td>
</tr>

<tr>
<td>aAttribute</td>
<td>the name of the attribute to copy  
</td>
</tr>

</table>

### cloneAttributes(destNode, sourceNode) ###
  
cloneAttributes() is similar to nsIDOMNode::cloneNode(),  
  it assures the attribute nodes of the destination are identical  
  with the source node by copying all existing attributes from the  
  source and deleting those not in the source.  
  This is used when the destination node (element) already exists  
  
The supplied nodes MUST BE ELEMENTS (most callers are working with nodes)  
@param aDestNode     the destination element to operate on  
@param aSourceNode   the source element to copy attributes from  
  

#### Parameters ####

<table>

<tr>
<td>aDestNode</td>
<td>the destination element to operate on  
</td>
</tr>

<tr>
<td>aDestNode</td>
<td>the destination element to operate on  
</td>
</tr>

</table>

### createNode(tag, parent, position) ###
   
createNode instantiates a new element of type aTag and inserts it  
into aParent at aPosition.  
@param aTag      The type of object to create  
@param aParent   The node to insert the new object into  
@param aPosition The place in aParent to insert the new node  
@return          The node created.  Caller must release aNewNode.  
  

#### Parameters ####

<table>

<tr>
<td>aTag</td>
<td>The type of object to create  
</td>
</tr>

<tr>
<td>aTag</td>
<td>The type of object to create  
</td>
</tr>

<tr>
<td>aTag</td>
<td>The type of object to create  
</td>
</tr>

</table>

### insertNode(node, parent, aPosition) ###
   
insertNode inserts aNode into aParent at aPosition.  
No checking is done to verify the legality of the insertion.  
That is the responsibility of the caller.  
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
<td>aNode</td>
<td>The DOM Node to insert.  
</td>
</tr>

<tr>
<td>aNode</td>
<td>The DOM Node to insert.  
</td>
</tr>

</table>

### splitNode(existingRightNode, offset, newLeftNode) ###
   
splitNode() creates a new node identical to an existing node,  
and split the contents between the two nodes  
@param aExistingRightNode   the node to split.  
                            It will become the new node's next sibling.  
@param aOffset              the offset of aExistingRightNode's  
                            content|children to do the split at  
@param aNewLeftNode         [OUT] the new node resulting from the split,  
                            becomes aExistingRightNode's previous sibling.  
  

#### Parameters ####

<table>

<tr>
<td>aExistingRightNode</td>
<td>the node to split.  
                            It will become the new node's next sibling.  
</td>
</tr>

<tr>
<td>aExistingRightNode</td>
<td>the node to split.  
                            It will become the new node's next sibling.  
</td>
</tr>

<tr>
<td>aExistingRightNode</td>
<td>the node to split.  
                            It will become the new node's next sibling.  
</td>
</tr>

</table>

### joinNodes(leftNode, rightNode, parent) ###
   
joinNodes() takes 2 nodes and merge their content|children.  
@param aLeftNode     The left node.  It will be deleted.  
@param aRightNode    The right node. It will remain after the join.  
@param aParent       The parent of aExistingRightNode  
  
                     There is no requirement that the two nodes be  
                     of the same type.  However, a text node can be  
                     merged only with another text node.  
  

#### Parameters ####

<table>

<tr>
<td>aLeftNode</td>
<td>The left node.  It will be deleted.  
</td>
</tr>

<tr>
<td>aLeftNode</td>
<td>The left node.  It will be deleted.  
</td>
</tr>

<tr>
<td>aLeftNode</td>
<td>The left node.  It will be deleted.  
</td>
</tr>

</table>

### deleteNode(child) ###
   
deleteNode removes aChild from aParent.  
@param aChild    The node to delete  
  

#### Parameters ####

<table>

<tr>
<td>aChild</td>
<td>The node to delete  
</td>
</tr>

</table>

### outputsMozDirty() ###
  
Returns true if markNodeDirty() has any effect.  Returns false if  
markNodeDirty() is a no-op.  
  

### markNodeDirty(node) ###
   
markNodeDirty() sets a special dirty attribute on the node.  
Usually this will be called immediately after creating a new node.  
@param aNode      The node for which to insert formatting.  
  

#### Parameters ####

<table>

<tr>
<td>aNode</td>
<td>The node for which to insert formatting.  
</td>
</tr>

</table>

### switchTextDirection() ###
   
Switches the editor element direction; from "Left-to-Right" to  
"Right-to-Left", and vice versa.  
  

### outputToString(formatType, flags) ###
  
Output methods:  
aFormatType is a mime type, like text/plain.  
  

### outputToStream(aStream, formatType, charsetOverride, flags) ###

### addEditorObserver(observer) ###
 add an EditorObserver to the editors list of observers. */  

### removeEditorObserver(observer) ###
 Remove an EditorObserver from the editor's list of observers. */  

### addEditActionListener(listener) ###
 add an EditActionListener to the editors list of listeners. */  

### removeEditActionListener(listener) ###
 Remove an EditActionListener from the editor's list of listeners. */  

### addDocumentStateListener(listener) ###
 Add a DocumentStateListener to the editors list of doc state listeners. */  

### removeDocumentStateListener(listener) ###
 Remove a DocumentStateListener to the editors list of doc state listeners. */  

### dumpContentTree() ###
  
And a debug method -- show us what the tree looks like right now  
  

### debugDumpContent() ###
 Dumps a text representation of the content tree to standard out */  

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
