---
layout: default
---

# nsITransactionListener #

The nsITransactionListener interface.
<P>
This interface is implemented by an object that tracks transactions.


## willDo ##

Called before a transaction manager calls a transaction's
doTransaction() method.
@param aManager the transaction manager doing the transaction.
@param aTransaction the transaction being executed.
@result boolean value returned by listener which indicates
its desire to interrupt normal control flow. Listeners should
return true if they want to interrupt normal control flow, without
throwing an error.


## didDo ##

Called after a transaction manager calls the doTransaction() method of
a transaction.
@param aManager the transaction manager that did the transaction.
@param aTransaction the transaction that was executed.
@param aDoResult the nsresult returned after executing
the transaction.


## willUndo ##

Called before a transaction manager calls the Undo() method of
a transaction.
@param aManager the transaction manager undoing the transaction.
@param aTransaction the transaction being undone.
@result boolean value returned by listener which indicates
its desire to interrupt normal control flow. Listeners should
return true if they want to interrupt normal control flow, without
throwing an error. Note that listeners can also interrupt normal
control flow by throwing an nsresult that indicates an error.


## didUndo ##

Called after a transaction manager calls the Undo() method of
a transaction.
@param aManager the transaction manager undoing the transaction.
@param aTransaction the transaction being undone.
@param aUndoResult the nsresult returned after undoing the transaction.


## willRedo ##

Called before a transaction manager calls the Redo() method of
a transaction.
@param aManager the transaction manager redoing the transaction.
@param aTransaction the transaction being redone.
@result boolean value returned by listener which indicates
its desire to interrupt normal control flow. Listeners should
return true if they want to interrupt normal control flow, without
throwing an error. Note that listeners can also interrupt normal
control flow by throwing an nsresult that indicates an error.


## didRedo ##

Called after a transaction manager calls the Redo() method of
a transaction.
@param aManager the transaction manager redoing the transaction.
@param aTransaction the transaction being redone.
@param aRedoResult the nsresult returned after redoing the transaction.


## willBeginBatch ##

Called before a transaction manager begins a batch.
@param aManager the transaction manager beginning a batch.
@result boolean value returned by listener which indicates
its desire to interrupt normal control flow. Listeners should
return true if they want to interrupt normal control flow, without
throwing an error. Note that listeners can also interrupt normal
control flow by throwing an nsresult that indicates an error.


## didBeginBatch ##

Called after a transaction manager begins a batch.
@param aManager the transaction manager that began a batch.
@param aResult the nsresult returned after beginning a batch.


## willEndBatch ##

Called before a transaction manager ends a batch.
@param aManager the transaction manager ending a batch.
@result boolean value returned by listener which indicates
its desire to interrupt normal control flow. Listeners should
return true if they want to interrupt normal control flow, without
throwing an error. Note that listeners can also interrupt normal
control flow by throwing an nsresult that indicates an error.


## didEndBatch ##

Called after a transaction manager ends a batch.
@param aManager the transaction manager ending a batch.
@param aResult the nsresult returned after ending a batch.


## willMerge ##

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


## didMerge ##

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

