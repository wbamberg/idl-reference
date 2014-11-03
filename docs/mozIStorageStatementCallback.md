---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/storage/public/mozIStorageStatementCallback.idl">Source file</a>
</div>

# mozIStorageStatementCallback #

## Methods ##

### handleResult(aResultSet) ###
<code>  
Called when some result is obtained from the database.  This function can  
be called more than once with a different storageIResultSet each time for  
any given asynchronous statement.  
  
@param aResultSet  
       The result set containing the data from the database.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aResultSet</td>
<td>       The result set containing the data from the database.  
</td>
</tr>

</table>

### handleError(aError) ###
<code>  
Called when some error occurs while executing the statement.  This function  
may be called more than once with a different storageIError each time for  
any given asynchronous statement.  
  
@param aError  
       An object containing information about the error.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aError</td>
<td>       An object containing information about the error.  
</td>
</tr>

</table>

### handleCompletion(aReason) ###

## Constants ##

### REASON_FINISHED ###
  
Called when the statement has finished executing.  This function will only  
be called once for any given asynchronous statement.  
  
@param aReason  
       Indicates if the statement is no longer executing because it either  
       finished (REASON_FINISHED), was canceled (REASON_CANCELED), or  
       a fatal error occurred (REASON_ERROR).  
  

### REASON_CANCELED ###

### REASON_ERROR ###
