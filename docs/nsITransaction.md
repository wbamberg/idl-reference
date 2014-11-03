---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/editor/txmgr/nsITransaction.idl">Source file</a>
</div>

# nsITransaction #

## Methods ##

### doTransaction() ###
  
Executes the transaction.  
  

### undoTransaction() ###
  
Restores the state to what it was before the transaction was executed.  
  

### redoTransaction() ###
  
Executes the transaction again. Can only be called on a transaction that  
was previously undone.  
<P>  
In most cases, the redoTransaction() method will actually call the  
doTransaction() method to execute the transaction again.  
  

### merge(aTransaction) ###
  
Attempts to merge a transaction into "this" transaction. Both transactions  
must be in their undo state, doTransaction() methods already called. The  
transaction manager calls this method to coalesce a new transaction with  
the transaction on the top of the undo stack.  
This method returns a boolean value that indicates the merge result.  
A true value indicates that the transactions were merged successfully,  
a false value if the merge was not possible or failed. If true,  
the transaction manager will Release() the new transacton instead of  
pushing it on the undo stack.  
  

#### Parameters ####

<table>

<tr>
<td>aTransaction</td>
<td>the previously executed transaction to merge.  
</td>
</tr>

</table>

## Attributes ##

### isTransient ###
  
The transaction's transient state. This attribute is checked by  
the transaction manager after the transaction's Execute() method is called.  
If the transient state is false, a reference to the transaction is  
held by the transaction manager so that the transactions' undoTransaction()  
and redoTransaction() methods can be called. If the transient state is  
true, the transaction manager returns immediately after the transaction's  
doTransaction() method is called, no references to the transaction are  
maintained. Transient transactions cannot be undone or redone by the  
transaction manager.  
  
