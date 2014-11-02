---
layout: default
---

# nsIMultiplexInputStream #
  
The multiplex stream concatenates a list of input streams into a single  
stream.  
  

## Methods ##

### appendStream(stream) ###
  
Appends a stream to the end of the streams. The cursor of the stream  
should be located at the beginning of the stream if the implementation  
of this nsIMultiplexInputStream also is used as an nsISeekableStream.  
@param stream  stream to append  
  

#### Parameters ####

<table>

<tr>
<td>stream</td>
<td>stream to append  
</td>
</tr>

</table>

### insertStream(stream, index) ###
  
Insert a stream at specified index.  If the cursor of this stream is at  
the beginning of the stream at index, the cursor will be placed at the  
beginning of the inserted stream instead.  
The cursor of the new stream should be located at the beginning of the  
stream if the implementation of this nsIMultiplexInputStream also is  
used as an nsISeekableStream.  
@param stream  stream to insert  
@param index   index to insert stream at, must be <= count  
  

#### Parameters ####

<table>

<tr>
<td>stream</td>
<td>stream to insert  
</td>
</tr>

<tr>
<td>index</td>
<td>index to insert stream at, must be <= count  
</td>
</tr>

</table>

### removeStream(index) ###
  
Remove stream at specified index. If this stream is the one currently  
being read the readcursor is moved to the beginning of the next  
stream  
@param index   remove stream at this index, must be < count  
  

#### Parameters ####

<table>

<tr>
<td>index</td>
<td>remove stream at this index, must be < count  
</td>
</tr>

</table>

### getStream(index) ###
  
Get stream at specified index.  
@param index   return stream at this index, must be < count  
@return        stream at specified index  
  

#### Parameters ####

<table>

<tr>
<td>index</td>
<td>return stream at this index, must be < count  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>stream at specified index  
</td>
</tr>

</table>

## Attributes ##

### count ###
  
Number of streams in this multiplex-stream  
  
