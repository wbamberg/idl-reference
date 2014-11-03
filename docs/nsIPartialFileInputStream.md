---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIFileStreams.idl">Source file</a>
</div>

# nsIPartialFileInputStream #
  
An input stream that allows you to read from a slice of a file.  
  

## Methods ##

### init(file, start, length, ioFlags, perm, behaviorFlags) ###
  
Initialize with a file and new start/end positions. Both start and  
start+length must be smaller than the size of the file. Not doing so  
will lead to undefined behavior.  
You must initialize the stream, and only initialize it once, before it  
can be used.  
  
  

#### Parameters ####

<table>

<tr>
<td>file</td>
<td>file to read from  
</td>
</tr>

<tr>
<td>start</td>
<td>start offset of slice to read. Must be smaller  
                     than the size of the file.  
</td>
</tr>

<tr>
<td>length</td>
<td>length of slice to read. Must be small enough that  
                     start+length is smaller than the size of the file.  
</td>
</tr>

<tr>
<td>ioFlags</td>
<td>file open flags listed in prio.h (see  
                     PR_Open documentation) or -1 to open the  
                     file in default mode (PR_RDONLY).  
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
       (see enumerations in nsIFileInputStream)  
</td>
</tr>

</table>
