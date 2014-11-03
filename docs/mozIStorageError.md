---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/storage/public/mozIStorageError.idl">Source file</a>
</div>

# mozIStorageError #

## Attributes ##

### result ###
<pre>  
Indicates what type of error occurred.  
  
</pre>
### message ###
<pre>  
An error string the gives more details, if available.  
  
</pre>
## Constants ##

### ERROR ###
<pre>  
General SQL error or missing database.  
  
</pre>
### INTERNAL ###
<pre>  
Internal logic error.  
  
</pre>
### PERM ###
<pre>  
Access permission denied.  
  
</pre>
### ABORT ###
<pre>  
A callback routine requested an abort.  
  
</pre>
### BUSY ###
<pre>  
The database file is locked.  
  
</pre>
### LOCKED ###
<pre>  
A table in the database is locked.  
  
</pre>
### NOMEM ###
<pre>  
An allocation failed.  
  
</pre>
### READONLY ###
<pre>  
Attempt to write to a readonly database.  
  
</pre>
### INTERRUPT ###
<pre>  
Operation was terminated by an interrupt.  
  
</pre>
### IOERR ###
<pre>  
Some kind of disk I/O error occurred.  
  
</pre>
### CORRUPT ###
<pre>  
The database disk image is malformed.  
  
</pre>
### FULL ###
<pre>  
An insertion failed because the database is full.  
  
</pre>
### CANTOPEN ###
<pre>  
Unable to open the database file.  
  
</pre>
### EMPTY ###
<pre>  
The database is empty.  
  
</pre>
### SCHEMA ###
<pre>  
The database scheme changed.  
  
</pre>
### TOOBIG ###
<pre>  
A string or blob exceeds the size limit.  
  
</pre>
### CONSTRAINT ###
<pre>  
Abort due to a constraint violation.  
  
</pre>
### MISMATCH ###
<pre>  
Data type mismatch.  
  
</pre>
### MISUSE ###
<pre>  
Library used incorrectly.  
  
</pre>
### NOLFS ###
<pre>  
Uses OS features not supported on the host system.  
  
</pre>
### AUTH ###
<pre>  
Authorization denied.  
  
</pre>
### FORMAT ###
<pre>  
Auxiliary database format error.  
  
</pre>
### RANGE ###
<pre>  
Attempt to bind a parameter using an out-of-range index or nonexistent  
named parameter name.  
  
</pre>
### NOTADB ###
<pre>  
File opened that is not a database file.  
  
</pre>