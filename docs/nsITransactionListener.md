---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/editor/txmgr/nsITransactionListener.idl">Source file</a>
</div>

# nsITransactionListener #
<code>  
The nsITransactionListener interface.  
<P>  
This interface is implemented by an object that tracks transactions.  
  
</code>
## Methods ##

### willDo(aManager, aTransaction) ###
<code>  
Called before a transaction manager calls a transaction's  
doTransaction() method.  
@param aManager the transaction manager doing the transaction.  
@param aTransaction the transaction being executed.  
@result boolean value returned by listener which indicates  
its desire to interrupt normal control flow. Listeners should  
return true if they want to interrupt normal control flow, without  
throwing an error.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aManager</td>
<td>the transaction manager doing the transaction.  
</td>
</tr>

<tr>
<td>aTransaction</td>
<td>the transaction being executed.  
@result boolean value returned by listener which indicates  
its desire to interrupt normal control flow. Listeners should  
return true if they want to interrupt normal control flow, without  
throwing an error.  
</td>
</tr>

</table>

### didDo(aManager, aTransaction, aDoResult) ###
<code>  
Called after a transaction manager calls the doTransaction() method of  
a transaction.  
@param aManager the transaction manager that did the transaction.  
@param aTransaction the transaction that was executed.  
@param aDoResult the nsresult returned after executing  
the transaction.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aManager</td>
<td>the transaction manager that did the transaction.  
</td>
</tr>

<tr>
<td>aTransaction</td>
<td>the transaction that was executed.  
</td>
</tr>

<tr>
<td>aDoResult</td>
<td>the nsresult returned after executing  
the transaction.  
</td>
</tr>

</table>

### willUndo(aManager, aTransaction) ###
<code>  
Called before a transaction manager calls the Undo() method of  
a transaction.  
@param aManager the transaction manager undoing the transaction.  
@param aTransaction the transaction being undone.  
@result boolean value returned by listener which indicates  
its desire to interrupt normal control flow. Listeners should  
return true if they want to interrupt normal control flow, without  
throwing an error. Note that listeners can also interrupt normal  
control flow by throwing an nsresult that indicates an error.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aManager</td>
<td>the transaction manager undoing the transaction.  
</td>
</tr>

<tr>
<td>aTransaction</td>
<td>the transaction being undone.  
@result boolean value returned by listener which indicates  
its desire to interrupt normal control flow. Listeners should  
return true if they want to interrupt normal control flow, without  
throwing an error. Note that listeners can also interrupt normal  
control flow by throwing an nsresult that indicates an error.  
</td>
</tr>

</table>

### didUndo(aManager, aTransaction, aUndoResult) ###
<code>  
Called after a transaction manager calls the Undo() method of  
a transaction.  
@param aManager the transaction manager undoing the transaction.  
@param aTransaction the transaction being undone.  
@param aUndoResult the nsresult returned after undoing the transaction.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aManager</td>
<td>the transaction manager undoing the transaction.  
</td>
</tr>

<tr>
<td>aTransaction</td>
<td>the transaction being undone.  
</td>
</tr>

<tr>
<td>aUndoResult</td>
<td>the nsresult returned after undoing the transaction.  
</td>
</tr>

</table>

### willRedo(aManager, aTransaction) ###
<code>  
Called before a transaction manager calls the Redo() method of  
a transaction.  
@param aManager the transaction manager redoing the transaction.  
@param aTransaction the transaction being redone.  
@result boolean value returned by listener which indicates  
its desire to interrupt normal control flow. Listeners should  
return true if they want to interrupt normal control flow, without  
throwing an error. Note that listeners can also interrupt normal  
control flow by throwing an nsresult that indicates an error.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aManager</td>
<td>the transaction manager redoing the transaction.  
</td>
</tr>

<tr>
<td>aTransaction</td>
<td>the transaction being redone.  
@result boolean value returned by listener which indicates  
its desire to interrupt normal control flow. Listeners should  
return true if they want to interrupt normal control flow, without  
throwing an error. Note that listeners can also interrupt normal  
control flow by throwing an nsresult that indicates an error.  
</td>
</tr>

</table>

### didRedo(aManager, aTransaction, aRedoResult) ###
<code>  
Called after a transaction manager calls the Redo() method of  
a transaction.  
@param aManager the transaction manager redoing the transaction.  
@param aTransaction the transaction being redone.  
@param aRedoResult the nsresult returned after redoing the transaction.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aManager</td>
<td>the transaction manager redoing the transaction.  
</td>
</tr>

<tr>
<td>aTransaction</td>
<td>the transaction being redone.  
</td>
</tr>

<tr>
<td>aRedoResult</td>
<td>the nsresult returned after redoing the transaction.  
</td>
</tr>

</table>

### willBeginBatch(aManager) ###
<code>  
Called before a transaction manager begins a batch.  
@param aManager the transaction manager beginning a batch.  
@result boolean value returned by listener which indicates  
its desire to interrupt normal control flow. Listeners should  
return true if they want to interrupt normal control flow, without  
throwing an error. Note that listeners can also interrupt normal  
control flow by throwing an nsresult that indicates an error.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aManager</td>
<td>the transaction manager beginning a batch.  
@result boolean value returned by listener which indicates  
its desire to interrupt normal control flow. Listeners should  
return true if they want to interrupt normal control flow, without  
throwing an error. Note that listeners can also interrupt normal  
control flow by throwing an nsresult that indicates an error.  
</td>
</tr>

</table>

### didBeginBatch(aManager, aResult) ###
<code>  
Called after a transaction manager begins a batch.  
@param aManager the transaction manager that began a batch.  
@param aResult the nsresult returned after beginning a batch.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aManager</td>
<td>the transaction manager that began a batch.  
</td>
</tr>

<tr>
<td>aResult</td>
<td>the nsresult returned after beginning a batch.  
</td>
</tr>

</table>

### willEndBatch(aManager) ###
<code>  
Called before a transaction manager ends a batch.  
@param aManager the transaction manager ending a batch.  
@result boolean value returned by listener which indicates  
its desire to interrupt normal control flow. Listeners should  
return true if they want to interrupt normal control flow, without  
throwing an error. Note that listeners can also interrupt normal  
control flow by throwing an nsresult that indicates an error.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aManager</td>
<td>the transaction manager ending a batch.  
@result boolean value returned by listener which indicates  
its desire to interrupt normal control flow. Listeners should  
return true if they want to interrupt normal control flow, without  
throwing an error. Note that listeners can also interrupt normal  
control flow by throwing an nsresult that indicates an error.  
</td>
</tr>

</table>

### didEndBatch(aManager, aResult) ###
<code>  
Called after a transaction manager ends a batch.  
@param aManager the transaction manager ending a batch.  
@param aResult the nsresult returned after ending a batch.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aManager</td>
<td>the transaction manager ending a batch.  
</td>
</tr>

<tr>
<td>aResult</td>
<td>the nsresult returned after ending a batch.  
</td>
</tr>

</table>

### willMerge(aManager, aTopTransaction, aTransactionToMerge) ###
<code>  
Called before a transaction manager tries to merge  
a transaction, that was just executed, with the  
transaction at the top of the undo stack.  
@param aManager the transaction manager ending a batch.  
@param aTopTransaction the transaction at the top of the undo stack.  
@param aTransactionToMerge the transaction to merge.  
@result boolean value returned by listener which indicates  
its desire to interrupt normal control flow. Listeners should  
return true if they want to interrupt normal control flow, without  
throwing an error. Note that listeners can also interrupt normal  
control flow by throwing an nsresult that indicates an error.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aManager</td>
<td>the transaction manager ending a batch.  
</td>
</tr>

<tr>
<td>aTopTransaction</td>
<td>the transaction at the top of the undo stack.  
</td>
</tr>

<tr>
<td>aTransactionToMerge</td>
<td>the transaction to merge.  
@result boolean value returned by listener which indicates  
its desire to interrupt normal control flow. Listeners should  
return true if they want to interrupt normal control flow, without  
throwing an error. Note that listeners can also interrupt normal  
control flow by throwing an nsresult that indicates an error.  
</td>
</tr>

</table>

### didMerge(aManager, aTopTransaction, aTransactionToMerge, aDidMerge, aMergeResult) ###
<code>  
Called after a transaction manager tries to merge  
a transaction, that was just executed, with the  
transaction at the top of the undo stack.  
@param aManager the transaction manager ending a batch.  
@param aTopTransaction the transaction at the top of the undo stack.  
@param aTransactionToMerge the transaction to merge.  
@param aDidMerge true if transaction was merged, else false.  
@param aMergeResult the nsresult returned after the merge attempt.  
@param aInterrupt listeners should set this to PR_TRUE if they  
want to interrupt normal control flow, without throwing an error.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aManager</td>
<td>the transaction manager ending a batch.  
</td>
</tr>

<tr>
<td>aTopTransaction</td>
<td>the transaction at the top of the undo stack.  
</td>
</tr>

<tr>
<td>aTransactionToMerge</td>
<td>the transaction to merge.  
</td>
</tr>

<tr>
<td>aDidMerge</td>
<td>true if transaction was merged, else false.  
</td>
</tr>

<tr>
<td>aMergeResult</td>
<td>the nsresult returned after the merge attempt.  
</td>
</tr>

<tr>
<td>aInterrupt</td>
<td>listeners should set this to PR_TRUE if they  
want to interrupt normal control flow, without throwing an error.  
</td>
</tr>

</table>
