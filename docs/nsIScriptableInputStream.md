---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/io/nsIScriptableInputStream.idl">Source file</a>
</div>

# nsIScriptableInputStream #
<code>  
nsIScriptableInputStream provides scriptable access to an nsIInputStream  
instance.  
  
</code>
## Methods ##

### close() ###
<code>   
Closes the stream.   
  
</code>
### init(aInputStream) ###
<code>  
Wrap the given nsIInputStream with this nsIScriptableInputStream.   
  
@param aInputStream parameter providing the stream to wrap   
  
</code>
#### Parameters ####

<table>

<tr>
<td>aInputStream</td>
<td>parameter providing the stream to wrap   
</td>
</tr>

</table>

### available() ###
<code>  
Return the number of bytes currently available in the stream   
  
@return the number of bytes   
  
@throws NS_BASE_STREAM_CLOSED if called after the stream has been closed  
  
</code>
#### Returns ####

<table>

<tr>
<td>the number of bytes   
</td>
</tr>

</table>

### read(aCount) ###
<code>  
Read data from the stream.  
  
WARNING: If the data contains a null byte, then this method will return  
a truncated string.  
  
@param aCount the maximum number of bytes to read   
  
@return the data, which will be an empty string if the stream is at EOF.  
  
@throws NS_BASE_STREAM_CLOSED if called after the stream has been closed  
@throws NS_ERROR_NOT_INITIALIZED if init was not called  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aCount</td>
<td>the maximum number of bytes to read   
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>the data, which will be an empty string if the stream is at EOF.  
</td>
</tr>

</table>

### readBytes(aCount) ###
<code>  
Read data from the stream, including NULL bytes.  
  
@param aCount the maximum number of bytes to read.  
  
@return the data from the stream, which will be an empty string if EOF  
        has been reached.  
  
@throws NS_BASE_STREAM_WOULD_BLOCK if reading from the input stream  
        would block the calling thread (non-blocking mode only).  
@throws NS_ERROR_FAILURE if there are not enough bytes available to read  
        aCount amount of data.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aCount</td>
<td>the maximum number of bytes to read.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>the data from the stream, which will be an empty string if EOF  
        has been reached.  
</td>
</tr>

</table>
