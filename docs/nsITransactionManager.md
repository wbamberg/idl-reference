---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/editor/txmgr/nsITransactionManager.idl">Source file</a>
</div>

# nsITransactionManager #
  
The nsITransactionManager interface.  
<P>  
This interface is implemented by an object that wants to  
manage/track transactions.  
  

## Methods ##

### doTransaction(aTransaction) ###
  
Calls a transaction's doTransaction() method, then pushes it on the  
undo stack.  
<P>  
This method calls the transaction's AddRef() method.  
The transaction's Release() method will be called when the undo or redo  
stack is pruned or when the transaction manager is destroyed.  
@param aTransaction the transaction to do.  
  

#### Parameters ####

<table>

<tr>
<td>aTransaction</td>
<td>the transaction to do.  
</td>
</tr>

</table>

### undoTransaction() ###
  
Pops the topmost transaction on the undo stack, calls its  
undoTransaction() method, then pushes it on the redo stack.  
  

### redoTransaction() ###
  
Pops the topmost transaction on the redo stack, calls its  
redoTransaction() method, then pushes it on the undo stack.  
  

### clear() ###
  
Clears the undo and redo stacks.  
  

### clearUndoStack() ###
  
Clears the undo stack only.  
  

### clearRedoStack() ###
  
Clears the redo stack only.  
  

### beginBatch(aData) ###
  
Turns on the transaction manager's batch mode, forcing all transactions  
executed by the transaction manager's doTransaction() method to be  
aggregated together until EndBatch() is called.  This mode allows an  
application to execute and group together several independent transactions  
so they can be undone with a single call to undoTransaction().  
@param aData An arbitrary nsISupports object that is associated with the  
batch. Can be retrieved from nsITransactionList.  
  

#### Parameters ####

<table>

<tr>
<td>aData</td>
<td>An arbitrary nsISupports object that is associated with the  
batch. Can be retrieved from nsITransactionList.  
</td>
</tr>

</table>

### endBatch(aAllowEmpty) ###
  
Turns off the transaction manager's batch mode.  
@param aAllowEmpty If true, a batch containing no children will be  
pushed onto the undo stack. Otherwise, ending a batch with no  
children will result in no transactions being pushed on the undo stack.  
  

#### Parameters ####

<table>

<tr>
<td>aAllowEmpty</td>
<td>If true, a batch containing no children will be  
pushed onto the undo stack. Otherwise, ending a batch with no  
children will result in no transactions being pushed on the undo stack.  
</td>
</tr>

</table>

### batchTopUndo() ###
  
Combines the transaction at the top of the undo stack (if any) with the  
preceding undo transaction (if any) into a batch transaction. Thus,  
a call to undoTransaction() will undo both transactions.  
  

### removeTopUndo() ###
  
Removes the transaction at the top of the undo stack (if any) without  
transacting.  
  

### peekUndoStack() ###
  
Returns an AddRef'd pointer to the transaction at the top of the  
undo stack. Callers should be aware that this method could return  
return a null in some implementations if there is a batch at the top  
of the undo stack.  
  

### peekRedoStack() ###
  
Returns an AddRef'd pointer to the transaction at the top of the  
redo stack. Callers should be aware that this method could return  
return a null in some implementations if there is a batch at the top  
of the redo stack.  
  

### getUndoList() ###
  
Returns the list of transactions on the undo stack. Note that the  
transaction at the top of the undo stack will actually be at the  
index 'n-1' in the list, where 'n' is the number of items in the list.  
  

### getRedoList() ###
  
Returns the list of transactions on the redo stack. Note that the  
transaction at the top of the redo stack will actually be at the  
index 'n-1' in the list, where 'n' is the number of items in the list.  
  

### AddListener(aListener) ###
  
Adds a listener to the transaction manager's notification list. Listeners  
are notified whenever a transaction is done, undone, or redone.  
<P>  
The listener's AddRef() method is called.  
@param aListener the lister to add.  
  

#### Parameters ####

<table>

<tr>
<td>aListener</td>
<td>the lister to add.  
</td>
</tr>

</table>

### RemoveListener(aListener) ###
  
Removes a listener from the transaction manager's notification list.  
<P>  
The listener's Release() method is called.  
@param aListener the lister to remove.  
  

#### Parameters ####

<table>

<tr>
<td>aListener</td>
<td>the lister to remove.  
</td>
</tr>

</table>

## Attributes ##

### numberOfUndoItems ###
  
The number of items on the undo stack.  
  

### numberOfRedoItems ###
  
The number of items on the redo stack.  
  

### maxTransactionCount ###
  
Sets the maximum number of transaction items the transaction manager will  
maintain at any time. This is commonly referred to as the number of levels  
of undo.  
@param aMaxCount A value of -1 means no limit. A value of zero means the  
transaction manager will execute each transaction, then immediately release  
all references it has to the transaction without pushing it on the undo  
stack. A value greater than zero indicates the max number of transactions  
that can exist at any time on both the undo and redo stacks. This method  
will prune the necessary number of transactions on the undo and redo  
stacks if the value specified is less than the number of items that exist  
on both the undo and redo stacks.  
  
