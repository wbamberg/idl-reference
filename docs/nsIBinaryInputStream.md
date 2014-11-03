---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/io/nsIBinaryInputStream.idl">Source file</a>
</div>

# nsIBinaryInputStream #
<code>  
This interface allows consumption of primitive data types from a "binary  
stream" containing untagged, big-endian binary data, i.e. as produced by an  
implementation of nsIBinaryOutputStream.  This might be used, for example,  
to implement network protocols or to read from architecture-neutral disk  
files, i.e. ones that can be read and written by both big-endian and  
little-endian platforms.  
  
@See nsIBinaryOutputStream  
  
</code>
## Methods ##

### setInputStream(aInputStream) ###

### readBoolean() ###
<code>  
Read 8-bits from the stream.  
  
@return that byte to be treated as a boolean.  
  
</code>
#### Returns ####

<table>

<tr>
<td>that byte to be treated as a boolean.  
</td>
</tr>

</table>

### read8() ###

### read16() ###

### read32() ###

### read64() ###

### readFloat() ###

### readDouble() ###

### readCString() ###
<code>  
Read an 8-bit pascal style string from the stream.  
32-bit length field, followed by length 8-bit chars.  
  
</code>
### readString() ###
<code>  
Read an 16-bit pascal style string from the stream.  
32-bit length field, followed by length PRUnichars.  
  
</code>
### readBytes(aLength, aString) ###
<code>  
Read an opaque byte array from the stream.  
  
@param aLength the number of bytes that must be read.  
  
@throws NS_ERROR_FAILURE if it can't read aLength bytes  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aLength</td>
<td>the number of bytes that must be read.  
</td>
</tr>

</table>

### readByteArray(aLength, aBytes) ###
<code>  
Read an opaque byte array from the stream, storing the results  
as an array of PRUint8s.  
  
@param aLength the number of bytes that must be read.  
  
@throws NS_ERROR_FAILURE if it can't read aLength bytes  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aLength</td>
<td>the number of bytes that must be read.  
</td>
</tr>

</table>

### readArrayBuffer(aLength, aArrayBuffer) ###
<code>  
Read opaque bytes from the stream, storing the results in an ArrayBuffer.  
  
@param aLength the number of bytes that must be read  
@param aArrayBuffer the arraybuffer in which to store the results  
Note: passing view.buffer, where view is an ArrayBufferView of an  
      ArrayBuffer, is not valid unless view.byteOffset == 0.  
  
@return The number of bytes actually read into aArrayBuffer.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aLength</td>
<td>the number of bytes that must be read  
</td>
</tr>

<tr>
<td>aArrayBuffer</td>
<td>the arraybuffer in which to store the results  
Note: passing view.buffer, where view is an ArrayBufferView of an  
      ArrayBuffer, is not valid unless view.byteOffset == 0.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The number of bytes actually read into aArrayBuffer.  
</td>
</tr>

</table>
