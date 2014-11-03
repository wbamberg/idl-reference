---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/storage/public/mozIStorageService.idl">Source file</a>
</div>

# mozIStorageService #
<code>  
The mozIStorageService interface is intended to be implemented by  
a service that can create storage connections (mozIStorageConnection)  
to either a well-known profile database or to a specific database file.  
  
This is the only way to open a database connection.  
  
@note The first reference to mozIStorageService must be made on the main  
thread.  
  
</code>
## Methods ##

### openAsyncDatabase(aDatabaseStore, aOptions, aCallback) ###
<code>  
Open an asynchronous connection to a database.  
  
This method MUST be called from the main thread. The connection object  
returned by this function is not threadsafe. You MUST use it only from  
the main thread.  
  
If you have more than one connection to a file, you MUST use the EXACT  
SAME NAME for the file each time, including case. The sqlite code uses  
a simple string compare to see if there is already a connection. Opening  
a connection to "Foo.sqlite" and "foo.sqlite" will CORRUPT YOUR DATABASE.  
  
@param aDatabaseStore Either a nsIFile representing the file that contains  
the database or a special string to open a special database. The special  
string may be:  
- "memory" to open an in-memory database.  
  
@param aOptions A set of options (may be null). Options may contain:  
- bool shared (defaults to |false|).  
  -- If |true|, opens the database with a shared-cache. The  
    shared-cache mode is more memory-efficient when many  
    connections to the same database are expected, though, the  
    connections will contend the cache resource. In any cases  
    where performance matter, working without a shared-cache will  
    improve concurrency.  @see openUnsharedDatabase  
  
- int growthIncrement (defaults to none).  
  -- Set the growth increment for the main database.  This hints SQLite to  
     grow the database file by a given chunk size and may reduce  
     filesystem fragmentation on large databases.  
     @see mozIStorageConnection::setGrowthIncrement  
  
@param aCallback A callback that will receive the result of the operation.  
 In case of error, it may receive as status:  
 - NS_ERROR_OUT_OF_MEMORY if allocating a new storage object fails.  
 - NS_ERROR_FILE_CORRUPTED if the database file is corrupted.  
 In case of success, it receives as argument the new database  
 connection, as an instance of |mozIStorageAsyncConnection|.  
  
@throws NS_ERROR_INVALID_ARG if |aDatabaseStore| is neither a file nor  
        one of the special strings understood by this method, or if one of  
        the options passed through |aOptions| does not have the right type.  
@throws NS_ERROR_NOT_SAME_THREAD if called from a thread other than the  
        main thread.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aDatabaseStore</td>
<td>Either a nsIFile representing the file that contains  
the database or a special string to open a special database. The special  
string may be:  
- "memory" to open an in-memory database.  
</td>
</tr>

<tr>
<td>aOptions</td>
<td>A set of options (may be null). Options may contain:  
- bool shared (defaults to |false|).  
  -- If |true|, opens the database with a shared-cache. The  
    shared-cache mode is more memory-efficient when many  
    connections to the same database are expected, though, the  
    connections will contend the cache resource. In any cases  
    where performance matter, working without a shared-cache will  
    improve concurrency.  @see openUnsharedDatabase  
</td>
</tr>

<tr>
<td>aCallback</td>
<td>A callback that will receive the result of the operation.  
 In case of error, it may receive as status:  
 - NS_ERROR_OUT_OF_MEMORY if allocating a new storage object fails.  
 - NS_ERROR_FILE_CORRUPTED if the database file is corrupted.  
 In case of success, it receives as argument the new database  
 connection, as an instance of |mozIStorageAsyncConnection|.  
</td>
</tr>

</table>

### openSpecialDatabase(aStorageKey) ###
<code>  
Get a connection to a named special database storage.  
  
@param aStorageKey a string key identifying the type of storage  
requested.  Valid values include: "memory".  
  
@see openDatabase for restrictions on how database connections may be  
used. For the profile database, you should only access it from the main  
thread since other callers may also have connections.  
  
@returns a new mozIStorageConnection for the requested  
storage database.  
  
@throws NS_ERROR_INVALID_ARG if aStorageKey is invalid.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aStorageKey</td>
<td>a string key identifying the type of storage  
requested.  Valid values include: "memory".  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>a new mozIStorageConnection for the requested  
storage database.  
</td>
</tr>

</table>

### openDatabase(aDatabaseFile) ###
<code>  
Open a connection to the specified file.  
  
Consumers should check mozIStorageConnection::connectionReady to ensure  
that they can use the database.  If this value is false, it is strongly  
recommended that the database be backed up with  
mozIStorageConnection::backupDB so user data is not lost.  
  
==========  
  DANGER  
==========  
  
If you have more than one connection to a file, you MUST use the EXACT  
SAME NAME for the file each time, including case. The sqlite code uses  
a simple string compare to see if there is already a connection. Opening  
a connection to "Foo.sqlite" and "foo.sqlite" will CORRUPT YOUR DATABASE.  
  
The connection object returned by this function is not threadsafe. You must  
use it only from the thread you created it from.  
  
@param aDatabaseFile  
       A nsIFile that represents the database that is to be opened..  
  
@returns a mozIStorageConnection for the requested database file.  
  
@throws NS_ERROR_OUT_OF_MEMORY  
        If allocating a new storage object fails.  
@throws NS_ERROR_FILE_CORRUPTED  
        If the database file is corrupted.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aDatabaseFile</td>
<td>       A nsIFile that represents the database that is to be opened..  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>a mozIStorageConnection for the requested database file.  
</td>
</tr>

</table>

### openUnsharedDatabase(aDatabaseFile) ###
<code>  
Open a connection to the specified file that doesn't share a sqlite cache.  
  
Without a shared-cache, each connection uses its own pages cache, which  
may be memory inefficient with a large number of connections, in such a  
case so you should use openDatabase instead.  On the other side, if cache  
contention may be an issue, for instance when concurrency is important to  
ensure responsiveness, using unshared connections may be a performance win.  
  
==========  
  DANGER  
==========  
  
If you have more than one connection to a file, you MUST use the EXACT  
SAME NAME for the file each time, including case. The sqlite code uses  
a simple string compare to see if there is already a connection. Opening  
a connection to "Foo.sqlite" and "foo.sqlite" will CORRUPT YOUR DATABASE.  
  
The connection object returned by this function is not threadsafe. You must  
use it only from the thread you created it from.  
  
@param aDatabaseFile  
       A nsIFile that represents the database that is to be opened.  
  
@returns a mozIStorageConnection for the requested database file.  
  
@throws NS_ERROR_OUT_OF_MEMORY  
        If allocating a new storage object fails.  
@throws NS_ERROR_FILE_CORRUPTED  
        If the database file is corrupted.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aDatabaseFile</td>
<td>       A nsIFile that represents the database that is to be opened.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>a mozIStorageConnection for the requested database file.  
</td>
</tr>

</table>

### openDatabaseWithFileURL(aFileURL) ###
<code>  
See openDatabase(). Exactly the same only initialized with a file URL.  
Custom parameters can be passed to SQLite and VFS implementations through  
the query part of the URL.  
  
@param aURL  
       A nsIFileURL that represents the database that is to be opened.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aURL</td>
<td>       A nsIFileURL that represents the database that is to be opened.  
</td>
</tr>

</table>

### backupDatabaseFile(aDBFile, aBackupFileName, aBackupParentDirectory) ###
<code>  
Copies the specified database file to the specified parent directory with  
the specified file name.  If the parent directory is not specified, it  
places the backup in the same directory as the current file.  This function  
ensures that the file being created is unique.  
  
@param aDBFile  
       The database file that will be backed up.  
@param aBackupFileName  
       The name of the new backup file to create.  
@param [optional] aBackupParentDirectory  
       The directory you'd like the backup file to be placed.  
@return The nsIFile representing the backup file.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aDBFile</td>
<td>       The database file that will be backed up.  
</td>
</tr>

<tr>
<td>aBackupFileName</td>
<td>       The name of the new backup file to create.  
</td>
</tr>

<tr>
<td>[optional]</td>
<td>aBackupParentDirectory  
       The directory you'd like the backup file to be placed.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The nsIFile representing the backup file.  
</td>
</tr>

</table>
