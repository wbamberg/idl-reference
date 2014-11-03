---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/storage/public/mozIStorageAsyncConnection.idl">Source file</a>
</div>

# mozIStorageAsyncConnection #
  
mozIStorageAsyncConnection represents an asynchronous database  
connection attached to a specific file or to an in-memory data  
storage.  It is the primary interface for interacting with a  
database from the main thread, including creating prepared  
statements, executing SQL, and examining database errors.  
  

## Methods ##

### asyncClose(aCallback) ###
  
Close this database connection, allowing all pending statements  
to complete first.  
  
  
@throws NS_ERROR_NOT_SAME_THREAD  
        If is called on a thread other than the one that opened it.  
  

#### Parameters ####

<table>

<tr>
<td>aCallback</td>
<td>[optional]  
       A callback that will be notified when the close is completed,  
       with the following arguments:  
       - status: the status of the call  
       - value: |null|  
</td>
</tr>

</table>

### asyncClone(aReadOnly, aCallback) ###
  
Clone a database and make the clone read only if needed.  
  
  
  
@throws NS_ERROR_NOT_SAME_THREAD  
        If is called on a thread other than the one that opened it.  
@throws NS_ERROR_UNEXPECTED  
        If this connection is a memory database.  
  
@note If your connection is already read-only, you will get a read-only  
      clone.  
@note Due to a bug in SQLite, if you use the shared cache  
      (see mozIStorageService), you end up with the same privileges as the  
      first connection opened regardless of what is specified in aReadOnly.  
@note The following pragmas are copied over to a read-only clone:  
       - cache_size  
       - temp_store  
      The following pragmas are copied over to a writeable clone:  
       - cache_size  
       - temp_store  
       - foreign_keys  
       - journal_size_limit  
       - synchronous  
       - wal_autocheckpoint  
  

#### Parameters ####

<table>

<tr>
<td>aReadOnly</td>
<td>       If true, the returned database should be put into read-only mode.  
</td>
</tr>

<tr>
<td>aCallback</td>
<td>       A callback that will be notified when the operation is complete,  
       with the following arguments:  
       - status: the status of the operation  
       - value: in case of success, an intance of  
            mozIStorageAsyncConnection cloned from this one.  
</td>
</tr>

</table>

### createAsyncStatement(aSQLStatement) ###
  
Create an asynchronous statement for the given SQL. An  
asynchronous statement can only be used to dispatch asynchronous  
requests to the asynchronous execution thread and cannot be used  
to take any synchronous actions on the database.  
  
The expression may use ? to indicate sequential numbered arguments,  
?1, ?2 etc. to indicate specific numbered arguments or :name and  
$var to indicate named arguments.  
  
  

#### Parameters ####

<table>

<tr>
<td>aSQLStatement</td>
<td>       The SQL statement to execute.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>a new mozIStorageAsyncStatement  
@note The statement is created lazily on first execution.  
</td>
</tr>

</table>

### executeAsync(aStatements, aNumStatements, aCallback) ###
  
Execute an array of statements created with this connection using  
any currently bound parameters. When the array contains multiple  
statements, the execution is wrapped in a single  
transaction. These statements can be reused immediately, and  
reset does not need to be called.  
  
  
@note If you have any custom defined functions, they must be  
       re-entrant since they can be called on multiple threads.  
  

#### Parameters ####

<table>

<tr>
<td>aStatements</td>
<td>       The array of statements to execute asynchronously, in the order they  
       are given in the array.  
</td>
</tr>

<tr>
<td>aNumStatements</td>
<td>       The number of statements in aStatements.  
</td>
</tr>

<tr>
<td>aCallback</td>
<td>[optional]  
       The callback object that will be notified of progress, errors, and  
       completion.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>an object that can be used to cancel the statements execution.  
</td>
</tr>

</table>

### executeSimpleSQLAsync(aSQLStatement, aCallback) ###
  
Execute asynchronously an SQL expression, expecting no arguments.  
  
  

#### Parameters ####

<table>

<tr>
<td>aSQLStatement</td>
<td>       The SQL statement to execute  
</td>
</tr>

<tr>
<td>aCallback</td>
<td>[optional]  
       The callback object that will be notified of progress, errors, and  
       completion.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>an object that can be used to cancel the statement execution.  
</td>
</tr>

</table>

### createFunction(aFunctionName, aNumArguments, aFunction) ###
  
Create a new SQL function.  If you use your connection on multiple threads,  
your function needs to be threadsafe, or it should only be called on one  
thread.  
  
  

#### Parameters ####

<table>

<tr>
<td>aFunctionName</td>
<td>       The name of function to create, as seen in SQL.  
</td>
</tr>

<tr>
<td>aNumArguments</td>
<td>       The number of arguments the function takes. Pass -1 for  
       variable-argument functions.  
</td>
</tr>

<tr>
<td>aFunction</td>
<td>       The instance of mozIStorageFunction, which implements the function  
       in question.  
</td>
</tr>

</table>

### createAggregateFunction(aFunctionName, aNumArguments, aFunction) ###
  
Create a new SQL aggregate function.  If you use your connection on  
multiple threads, your function needs to be threadsafe, or it should only  
be called on one thread.  
  
  

#### Parameters ####

<table>

<tr>
<td>aFunctionName</td>
<td>       The name of aggregate function to create, as seen in SQL.  
</td>
</tr>

<tr>
<td>aNumArguments</td>
<td>       The number of arguments the function takes. Pass -1 for  
       variable-argument functions.  
</td>
</tr>

<tr>
<td>aFunction</td>
<td>       The instance of mozIStorageAggreagteFunction, which implements the  
       function in question.  
</td>
</tr>

</table>

### removeFunction(aFunctionName) ###
  
Delete custom SQL function (simple or aggregate one).  
  
  

#### Parameters ####

<table>

<tr>
<td>aFunctionName</td>
<td>       The name of function to remove.  
</td>
</tr>

</table>

### setProgressHandler(aGranularity, aHandler) ###
  
Sets a progress handler. Only one handler can be registered at a time.  
If you need more than one, you need to chain them yourself.  This progress  
handler should be threadsafe if you use this connection object on more than  
one thread.  
  
  

#### Parameters ####

<table>

<tr>
<td>aGranularity</td>
<td>       The number of SQL virtual machine steps between progress handler  
       callbacks.  
</td>
</tr>

<tr>
<td>aHandler</td>
<td>       The instance of mozIStorageProgressHandler.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>previous registered handler.  
</td>
</tr>

</table>

### removeProgressHandler() ###
  
Remove a progress handler.  
  
  

#### Returns ####

<table>

<tr>
<td>previous registered handler.  
</td>
</tr>

</table>

## Attributes ##

### databaseFile ###
  
The current database nsIFile.  Null if the database  
connection refers to an in-memory database.  
  
