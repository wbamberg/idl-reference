---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/io/nsIStorageStream.idl">Source file</a>
</div>

# nsIStorageStream #
<pre>  
The nsIStorageStream interface maintains an internal data buffer that can be  
filled using a single output stream.  One or more independent input streams  
can be created to read the data from the buffer non-destructively.  
  
</pre>
## Methods ##

### init(segmentSize, maxSize) ###
<pre>  
  
Initialize the stream, setting up the amount of space that will be  
allocated for the stream's backing-store.  
  
@param segmentSize  
       Size of each segment. Must be a power of two.  
@param maxSize  
       Maximum total size of this stream. length will always be less  
       than or equal to this value. Passing UINT32_MAX is safe.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>segmentSize</td>
<td>       Size of each segment. Must be a power of two.  
</td>
</tr>

<tr>
<td>maxSize</td>
<td>       Maximum total size of this stream. length will always be less  
       than or equal to this value. Passing UINT32_MAX is safe.  
</td>
</tr>

</table>

### getOutputStream(startPosition) ###
<pre>  
Get a reference to the one and only output stream for this instance.  
The zero-based startPosition argument is used is used to set the initial  
write cursor position.  The startPosition cannot be set larger than the  
current buffer length.  Calling this method has the side-effect of  
truncating the internal buffer to startPosition bytes.  
  
</pre>
### newInputStream(startPosition) ###
<pre>  
Create a new input stream to read data (written by the singleton output  
stream) from the internal buffer.  Multiple, independent input streams  
can be created.  
  
</pre>
## Attributes ##

### length ###
<pre>   
The length attribute indicates the total number of bytes stored in the  
nsIStorageStream internal buffer, regardless of any consumption by input  
streams.  Assigning to the length field can be used to truncate the  
buffer data, but can not be used when either the instance's output  
stream is in use.  
  
@See #writeInProgress */  
</pre>
### writeInProgress ###
<pre>  
True, when output stream has not yet been Close'ed  
  
</pre>