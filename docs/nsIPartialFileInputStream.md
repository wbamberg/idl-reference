---
layout: default
---

# nsIPartialFileInputStream #
  
An input stream that allows you to read from a slice of a file.  
  

## Methods ##

### init(file, start, length, ioFlags, perm, behaviorFlags) ###
  
Initialize with a file and new start/end positions. Both start and  
start+length must be smaller than the size of the file. Not doing so  
will lead to undefined behavior.  
You must initialize the stream, and only initialize it once, before it  
can be used.  
  
@param file          file to read from  
@param start         start offset of slice to read. Must be smaller  
                     than the size of the file.  
@param length        length of slice to read. Must be small enough that  
                     start+length is smaller than the size of the file.  
@param ioFlags       file open flags listed in prio.h (see  
                     PR_Open documentation) or -1 to open the  
                     file in default mode (PR_RDONLY).  
@param perm          file mode bits listed in prio.h or -1 to  
                     use the default value (0)  
@param behaviorFlags flags specifying various behaviors of the class  
       (see enumerations in nsIFileInputStream)  
  
