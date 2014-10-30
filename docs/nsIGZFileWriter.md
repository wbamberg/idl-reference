---
layout: default
---

# nsIGZFileWriter #
  
A simple interface for writing to a .gz file.  
  
Note that the file that this interface produces has a different format than  
what you'd get if you compressed your data as a gzip stream and dumped the  
result to a file.  
  
The standard gunzip tool cannot decompress a raw gzip stream, but can handle  
the files produced by this interface.  
  

## Methods ##

### init(file) ###
  
Initialize this object.  We'll write our gzip'ed data to the given file,  
overwriting its contents if the file exists.  
  
init() will return an error if called twice.  It's an error to call any  
other method on this interface without first calling init().  
  

### initANSIFileDesc(file) ###
  
Alternate version of init() for use when the file is already opened;  
e.g., with a FileDescriptor passed over IPC.  
  

### write(str) ###
  
Write the given string to the file.  
  

### finish() ###
  
Close this nsIGZFileWriter.  Classes implementing nsIGZFileWriter will run  
this method when the underlying object is destroyed, so it's not strictly  
necessary to explicitly call it from your code.  
  
It's an error to call this method twice, and it's an error to call write()  
after finish() has been called.  
  
