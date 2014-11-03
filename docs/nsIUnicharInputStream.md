---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/io/nsIUnicharInputStream.idl">Source file</a>
</div>

# nsIUnicharInputStream #
  
Abstract unicode character input stream  
@see nsIInputStream  
  

## Methods ##

### read(aBuf, aCount) ###
  
Reads into a caller-provided character array.  
  
@return The number of characters that were successfully read. May be less  
        than aCount, even if there is more data in the input stream.  
        A return value of 0 means EOF.  
  
@note To read more than 2^32 characters, call this method multiple times.  
  

#### Returns ####

<table>

<tr>
<td>The number of characters that were successfully read. May be less  
        than aCount, even if there is more data in the input stream.  
        A return value of 0 means EOF.  
</td>
</tr>

</table>

### readSegments(aWriter, aClosure, aCount) ###
  
Low-level read method that has access to the stream's underlying buffer.  
The writer function may be called multiple times for segmented buffers.  
ReadSegments is expected to keep calling the writer until either there is  
nothing left to read or the writer returns an error.  ReadSegments should  
not call the writer with zero characters to consume.  
  
@param aWriter the "consumer" of the data to be read  
@param aClosure opaque parameter passed to writer   
@param aCount the maximum number of characters to be read  
  
@return number of characters read (may be less than aCount)  
@return 0 if reached end of file (or if aWriter refused to consume data)  
  
@throws NS_BASE_STREAM_WOULD_BLOCK if reading from the input stream would  
  block the calling thread (non-blocking mode only)  
@throws <other-error> on failure  
  
NOTE: this function may be unimplemented if a stream has no underlying  
buffer  
  

#### Parameters ####

<table>

<tr>
<td>aWriter</td>
<td>the "consumer" of the data to be read  
</td>
</tr>

<tr>
<td>aClosure</td>
<td>opaque parameter passed to writer   
</td>
</tr>

<tr>
<td>aCount</td>
<td>the maximum number of characters to be read  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>0 if reached end of file (or if aWriter refused to consume data)  
</td>
</tr>

</table>

### readString(aCount, aString) ###
  
Read into a string object.  
@param aCount The number of characters that should be read  
@return The number of characters that were read.  
  

#### Parameters ####

<table>

<tr>
<td>aCount</td>
<td>The number of characters that should be read  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The number of characters that were read.  
</td>
</tr>

</table>

### close() ###
  
Close the stream and free associated resources. This also closes the  
underlying stream, if any.  
  
