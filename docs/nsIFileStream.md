---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIFileStreams.idl">Source file</a>
</div>

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
  

#### Parameters ####

<table>

<tr>
<td>file</td>
<td>file to read from or stream to  
</td>
</tr>

<tr>
<td>ioFlags</td>
<td>file open flags listed in prio.h (see  
                     PR_Open documentation) or -1 to open the  
                     file in default mode (PR_RDWR).  
</td>
</tr>

<tr>
<td>perm</td>
<td>file mode bits listed in prio.h or -1 to  
                     use the default value (0)  
</td>
</tr>

<tr>
<td>behaviorFlags</td>
<td>flags specifying various behaviors of the class  
       (see enumerations in the class)  
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
  
