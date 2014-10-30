---
layout: default
---

# nsIUrlClassifierDBService #
  
This is a proxy class that is instantiated and called from the JS thread.  
It provides async methods for querying and updating the database.  As the  
methods complete, they call the callback function.  
  

## Methods ##

### lookup(principal, tables, c) ###
  
Looks up a URI in the specified tables.  
  
@param principal: The principal containing the URI to search.  
@param c: The callback will be called with a comma-separated list  
       of tables to which the key belongs.  
  

### getTables(c) ###
  
Lists the tables along with which chunks are available in each table.  
This list is in the format of the request body:  
  tablename;chunkdata\n  
  tablename2;chunkdata2\n  
  
For example:  
  goog-phish-regexp;a:10,14,30-40s:56,67  
  goog-white-regexp;a:1-3,5  
  

### setHashCompleter(tableName, completer) ###
  
Set the nsIUrlClassifierCompleter object for a given table.  This  
object will be used to request complete versions of partial  
hashes.  
  

### beginUpdate(updater, tables) ###
  
Begin an update process.  Will throw NS_ERROR_NOT_AVAILABLE if there  
is already an update in progress.  
  
@param updater The update observer tied to this update.  
@param tables A comma-separated list of tables included in this update.  
  

### beginStream(table) ###
  
Begin a stream update.  This should be called once per url being  
fetched.  
  
@param table The table the contents of this stream will be associated  
             with, or empty for the initial stream.  
  

### updateStream(updateChunk) ###
  
Update the table incrementally.  
  

### finishStream() ###
  
Finish an individual stream update.  Must be called for every  
beginStream() call, before the next beginStream() or finishUpdate().  
  
The update observer's streamFinished will be called once the  
stream has been processed.  
  

### finishUpdate() ###
  
Finish an incremental update.  This will attempt to commit any  
pending changes and resets the update interface.  
  
The update observer's updateSucceeded or updateError methods  
will be called when the update has been processed.  
  

### cancelUpdate() ###
  
Cancel an incremental update.  This rolls back any pending changes.  
and resets the update interface.  
  
The update observer's updateError method will be called when the  
update has been rolled back.  
  

### resetDatabase() ###
  
Reset the url-classifier database.  This call will delete the existing  
database, emptying all tables.  Mostly intended for use in unit tests.  
  
