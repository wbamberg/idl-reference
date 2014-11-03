---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/io/nsISeekableStream.idl">Source file</a>
</div>

# nsISeekableStream #

## Methods ##

### seek(whence, offset) ###
  
 seek  
  
 This method moves the stream offset of the steam implementing this  
 interface.  
  
      
  
  @throws NS_BASE_STREAM_CLOSED if called on a closed stream.  
  

#### Parameters ####

<table>

<tr>
<td>whence</td>
<td>specifies how to interpret the 'offset' parameter in  
                setting the stream offset associated with the implementing  
                stream.  
</td>
</tr>

<tr>
<td>offset</td>
<td>specifies a value, in bytes, that is used in conjunction  
                with the 'whence' parameter to set the stream offset of the   
                implementing stream.  A negative value causes seeking in   
                the reverse direction.  
</td>
</tr>

</table>

### tell() ###
  
 tell  
  
 This method reports the current offset, in bytes, from the start of the   
 stream.   
  
  @throws NS_BASE_STREAM_CLOSED if called on a closed stream.  
  

### setEOF() ###
  
 setEOF  
  
 This method truncates the stream at the current offset.  
  
  @throws NS_BASE_STREAM_CLOSED if called on a closed stream.  
  

## Constants ##

### NS_SEEK_SET ###

### NS_SEEK_CUR ###

### NS_SEEK_END ###
