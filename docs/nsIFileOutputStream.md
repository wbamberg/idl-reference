---
layout: default
---

# nsIFileOutputStream #
  
An output stream that lets you stream to a file.  
  

## Methods ##

### init(file, ioFlags, perm, behaviorFlags) ###
  
@param file          file to write to  
@param ioFlags       file open flags listed in prio.h (see  
                     PR_Open documentation) or -1 to open the  
                     file in default mode (PR_WRONLY |  
                     PR_CREATE_FILE | PR_TRUNCATE)  
@param perm          file mode bits listed in prio.h or -1 to  
                     use the default permissions (0664)  
@param behaviorFlags flags specifying various behaviors of the class  
       (currently none supported)  
  

#### Parameters ####

<table>

<tr>
<td>file</td>
<td>file to write to  
</td>
</tr>

<tr>
<td>file</td>
<td>file to write to  
</td>
</tr>

<tr>
<td>file</td>
<td>file to write to  
</td>
</tr>

<tr>
<td>file</td>
<td>file to write to  
</td>
</tr>

</table>

## Constants ##

### DEFER_OPEN ###
  
See the same constant in nsIFileInputStream. The deferred open will  
be performed when one of the following is called:  
  - Seek  
  - Tell  
  - SetEOF  
  - Write  
  - Flush  
  
@note Using this flag results in the file not being opened  
      during the call to Init.  This means that any errors that might  
      happen when this flag is not set would happen during the  
      first write, and if the file is to be created, then it will not  
      appear on the disk until the first write.  
  
