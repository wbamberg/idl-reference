---
layout: default
---

# mozIStorageStatementCallback #

## Methods ##

### handleResult ###
  
Called when some result is obtained from the database.  This function can  
be called more than once with a different storageIResultSet each time for  
any given asynchronous statement.  
  
@param aResultSet  
       The result set containing the data from the database.  
  

### handleError ###
  
Called when some error occurs while executing the statement.  This function  
may be called more than once with a different storageIError each time for  
any given asynchronous statement.  
  
@param aError  
       An object containing information about the error.  
  

### handleCompletion ###

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
