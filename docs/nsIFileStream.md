---
layout: default
---

# nsIFileStream #
  
A stream that allows you to read from a file or stream to a file.  
  

## Methods ##

### init(file, ioFlags, perm, behaviorFlags) ###
  
@param file          file to read from or stream to  
@param ioFlags       file open flags listed in prio.h (see  
                     PR_Open documentation) or -1 to open the  
                     file in default mode (PR_RDWR).  
@param perm          file mode bits listed in prio.h or -1 to  
                     use the default value (0)  
@param behaviorFlags flags specifying various behaviors of the class  
       (see enumerations in the class)  
  

## Constants ##

### DEFER_OPEN ###
  
See the same constant in nsIFileInputStream. The deferred open will  
be performed when one of the following is called:  
  - Seek  
  - Tell  
  - SetEOF  
  - Available  
  - Read  
  - Flush  
  - Write  
  - GetSize  
  - GetLastModified  
  
@note Using this flag results in the file not being opened  
      during the call to Init.  This means that any errors that might  
      happen when this flag is not set would happen during the  
      first read or write. The file is not locked when Init is called,  
      so it might be deleted before we try to read from it and if the  
      file is to be created, then it will not appear on the disk until  
      the first write.  
  
