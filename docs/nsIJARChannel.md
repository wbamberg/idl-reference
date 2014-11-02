---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/modules/libjar/nsIJARChannel.idl">Source file</a>
</div>

# nsIJARChannel #

## Methods ##

### setAppURI(uri) ###
  
Forces the uri to be a app:// uri.  
  

### ensureChildFd() ###
  
For child process, set this to make sure that a valid file descriptor of  
JAR file is always provided when calling NSPRFileDesc().  
Must be set before Open() or AsyncOpen() to be effective.  
  
Note that the file descriptor returned by NSPRFileDesc() is duplicated  
from the original, which shares its file offset with the original.  If  
the file offset is modified (ex: by lseek/read/write) on one of the  
shared descriptors, the offset is also changed for the other.  
It can be safely used only with operations that take absolute offsets,  
such as mmap/pread/pwrite.  
  

## Attributes ##

### isUnsafe ###
  
Returns TRUE if the JAR file is not safe (if the content type reported  
by the server for a remote JAR is not of an expected type).  Scripting,  
redirects, and plugins should be disabled when loading from this  
channel.  
  

### jarFile ###
  
Returns the JAR file.  
  

### zipEntry ###
  
Returns the zip entry if the file is synchronously accessible.  
This will work even without opening the channel.  
  
