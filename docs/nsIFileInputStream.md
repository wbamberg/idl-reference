---
layout: default
---

# nsIFileInputStream #
  
An input stream that allows you to read from a file.  
  

## Methods ##

### init ###
  
@param file          file to read from  
@param ioFlags       file open flags listed in prio.h (see  
                     PR_Open documentation) or -1 to open the  
                     file in default mode (PR_RDONLY).  
@param perm          file mode bits listed in prio.h or -1 to  
                     use the default value (0)  
@param behaviorFlags flags specifying various behaviors of the class  
       (see enumerations in the class)  
  

## Constants ##

### DELETE_ON_CLOSE ###
  
If this is set, the file will be deleted by the time the stream is  
closed.  It may be removed before the stream is closed if it is possible  
to delete it and still read from it.  
  
If OPEN_ON_READ is defined, and the file was recreated after the first  
delete, the file will be deleted again when it is closed again.  
  

### CLOSE_ON_EOF ###
  
If this is set, the file will close automatically when the end of the  
file is reached.  
  

### REOPEN_ON_REWIND ###
  
If this is set, the file will be reopened whenever we reach the start of  
the file, either by doing a Seek(0, NS_SEEK_CUR), or by doing a relative  
seek that happen to reach the beginning of the file. If the file is  
already open and the seek occurs, it will happen naturally.  (The file  
will only be reopened if it is closed for some reason.)  
  

### DEFER_OPEN ###
  
If this is set, the file will be opened (i.e., a call to  
PR_Open done) only when we do an actual operation on the stream,  
or more specifically, when one of the following is called:  
  - Seek  
  - Tell  
  - SetEOF  
  - Available  
  - Read  
  - ReadLine  
  
DEFER_OPEN is useful if we use the stream on a background  
thread, so that the opening and possible |stat|ing of the file  
happens there as well.  
  
@note Using this flag results in the file not being opened  
      during the call to Init.  This means that any errors that might  
      happen when this flag is not set would happen during the  
      first read.  Also, the file is not locked when Init is called,  
      so it might be deleted before we try to read from it.  
  

### SHARE_DELETE ###
  
This flag has no effect and is totally ignored on any platform except  
Windows since this is the default behavior on POSIX systems. On Windows  
if this flag is set then the stream is opened in a special mode that  
allows the OS to delete the file from disk just like POSIX.  
  
