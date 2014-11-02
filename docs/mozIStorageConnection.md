---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/storage/public/mozIStorageConnection.idl">Source file</a>
</div>

# mozIStorageConnection #
  
mozIStorageConnection represents a database connection attached to  
a specific file or to the in-memory data storage.  It is the  
primary interface for interacting with a database, including  
creating prepared statements, executing SQL, and examining database  
errors.  
  
@note From the main thread, you should rather use mozIStorageAsyncConnection.  
  
@threadsafe  
  

## Methods ##

### close() ###
  
Closes a database connection.  Callers must finalize all statements created  
for this connection prior to calling this method.  It is illegal to use  
call this method if any asynchronous statements have been executed on this  
connection.  
  
@throws NS_ERROR_UNEXPECTED  
        If any statement has been executed asynchronously on this object.  
@throws NS_ERROR_UNEXPECTED  
        If is called on a thread other than the one that opened it.  
  

### clone(aReadOnly) ###
  
Clones a database connection and makes the clone read only if needed.  
  
@param aReadOnly  
       If true, the returned database should be put into read-only mode.  
       Defaults to false.  
@return the cloned database connection.  
  
@throws NS_ERROR_UNEXPECTED  
        If this connection is a memory database.  
@note If your connection is already read-only, you will get a read-only  
      clone.  
@note Due to a bug in SQLite, if you use the shared cache (openDatabase),  
      you end up with the same privileges as the first connection opened  
      regardless of what is specified in aReadOnly.  
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
       Defaults to false.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>the cloned database connection.  
</td>
</tr>

</table>

### createStatement(aSQLStatement) ###
  
Create a mozIStorageStatement for the given SQL expression.  The  
expression may use ? to indicate sequential numbered arguments,  
?1, ?2 etc. to indicate specific numbered arguments or :name and   
$var to indicate named arguments.  
  
@param aSQLStatement  
       The SQL statement to execute.  
@return a new mozIStorageStatement  
  

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
<td>a new mozIStorageStatement  
</td>
</tr>

</table>

### executeSimpleSQL(aSQLStatement) ###
  
Execute a SQL expression, expecting no arguments.  
  
@param aSQLStatement  The SQL statement to execute  
  

#### Parameters ####

<table>

<tr>
<td>aSQLStatement</td>
<td>The SQL statement to execute  
</td>
</tr>

</table>

### tableExists(aTableName) ###
  
Check if the given table exists.  
  
@param aTableName  
       The table to check  
@return TRUE if table exists, FALSE otherwise.  
  

#### Parameters ####

<table>

<tr>
<td>aTableName</td>
<td>       The table to check  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>TRUE if table exists, FALSE otherwise.  
</td>
</tr>

</table>

### indexExists(aIndexName) ###
  
Check if the given index exists.  
  
@param aIndexName   The index to check  
@return TRUE if the index exists, FALSE otherwise.  
  

#### Parameters ####

<table>

<tr>
<td>aIndexName</td>
<td>The index to check  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>TRUE if the index exists, FALSE otherwise.  
</td>
</tr>

</table>

### beginTransaction() ###
  
Begin a new transaction.  sqlite default transactions are deferred.  
If a transaction is active, throws an error.  
  

### beginTransactionAs(transactionType) ###

### commitTransaction() ###
  
Commits the current transaction.  If no transaction is active,  
@throws NS_ERROR_UNEXPECTED.  
@throws NS_ERROR_NOT_INITIALIZED.  
  

### rollbackTransaction() ###
  
Rolls back the current transaction.  If no transaction is active,  
@throws NS_ERROR_UNEXPECTED.  
@throws NS_ERROR_NOT_INITIALIZED.  
  

### createTable(aTableName, aTableSchema) ###
  
Create the table with the given name and schema.  
  
If the table already exists, NS_ERROR_FAILURE is thrown.  
(XXX at some point in the future it will check if the schema is  
the same as what is specified, but that doesn't happen currently.)  
  
@param aTableName  
       The table name to be created, consisting of [A-Za-z0-9_], and  
       beginning with a letter.  
@param aTableSchema  
       The schema of the table; what would normally go between the parens  
       in a CREATE TABLE statement: e.g., "foo  INTEGER, bar STRING".  
  
@throws NS_ERROR_FAILURE  
        If the table already exists or could not be created for any other  
        reason.  
  

#### Parameters ####

<table>

<tr>
<td>aTableName</td>
<td>       The table name to be created, consisting of [A-Za-z0-9_], and  
       beginning with a letter.  
</td>
</tr>

<tr>
<td>aTableSchema</td>
<td>       The schema of the table; what would normally go between the parens  
       in a CREATE TABLE statement: e.g., "foo  INTEGER, bar STRING".  
</td>
</tr>

</table>

### setGrowthIncrement(aIncrement, aDatabaseName) ###
  
Controls SQLITE_FCNTL_CHUNK_SIZE setting in sqlite. This helps avoid fragmentation  
by growing/shrinking the database file in SQLITE_FCNTL_CHUNK_SIZE increments. To  
conserve memory on systems short on storage space, this function will have no effect  
on mobile devices or if less than 500MiB of space is left available.  
  
@param aIncrement  
       The database file will grow in multiples of chunkSize.  
@param aDatabaseName  
       Sqlite database name. "" means pass NULL for zDbName to sqlite3_file_control.  
       See http://sqlite.org/c3ref/file_control.html for more details.  
@throws NS_ERROR_FILE_TOO_BIG  
        If the system is short on storage space.  
  

#### Parameters ####

<table>

<tr>
<td>aIncrement</td>
<td>       The database file will grow in multiples of chunkSize.  
</td>
</tr>

<tr>
<td>aDatabaseName</td>
<td>       Sqlite database name. "" means pass NULL for zDbName to sqlite3_file_control.  
       See http://sqlite.org/c3ref/file_control.html for more details.  
@throws NS_ERROR_FILE_TOO_BIG  
        If the system is short on storage space.  
</td>
</tr>

</table>

### enableModule(aModuleName) ###
  
Enable a predefined virtual table implementation.  
  
@param aModuleName  
       The module to enable. Only "filesystem" is currently supported.  
  
@throws NS_ERROR_FAILURE  
        For unknown module names.  
  

#### Parameters ####

<table>

<tr>
<td>aModuleName</td>
<td>       The module to enable. Only "filesystem" is currently supported.  
</td>
</tr>

</table>

## Attributes ##

### defaultPageSize ###
  
The default size for SQLite database pages used by mozStorage for new  
databases.  
  

### connectionReady ###
  
Indicates if the connection is open and ready to use.  This will be false  
if the connection failed to open, or it has been closed.  
  

### lastInsertRowID ###
  
lastInsertRowID returns the row ID from the last INSERT  
operation.  
  

### affectedRows ###
  
affectedRows returns the number of database rows that were changed or  
inserted or deleted by last operation.  
  

### lastError ###
  
The last error SQLite error code.  
  

### lastErrorString ###
  
The last SQLite error as a string (in english, straight from the  
sqlite library).  
  

### schemaVersion ###
  
The schema version of the database.  This should not be used until the   
database is ready.  The schema will be reported as zero if it is not set.  
  

### transactionInProgress ###
  
Returns true if a transaction is active on this connection.  
  

## Constants ##

### TRANSACTION_DEFERRED ###
  
Begins a new transaction with the given type.  
  

### TRANSACTION_IMMEDIATE ###

### TRANSACTION_EXCLUSIVE ###
