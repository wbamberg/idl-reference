---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/io/nsIBinaryOutputStream.idl">Source file</a>
</div>

# nsIBinaryOutputStream #
<code>  
This interface allows writing of primitive data types (integers,  
floating-point values, booleans, etc.) to a stream in a binary, untagged,  
fixed-endianness format.  This might be used, for example, to implement  
network protocols or to produce architecture-neutral binary disk files,  
i.e. ones that can be read and written by both big-endian and little-endian  
platforms.  Output is written in big-endian order (high-order byte first),  
as this is traditional network order.  
  
@See nsIBinaryInputStream  
  
</code>
## Methods ##

### setOutputStream(aOutputStream) ###

### writeBoolean(aBoolean) ###
<code>  
Write a boolean as an 8-bit char to the stream.  
  
</code>
### write8(aByte) ###

### write16(a16) ###

### write32(a32) ###

### write64(a64) ###

### writeFloat(aFloat) ###

### writeDouble(aDouble) ###

### writeStringZ(aString) ###
<code>  
Write an 8-bit pascal style string to the stream.  
32-bit length field, followed by length 8-bit chars.  
  
</code>
### writeWStringZ(aString) ###
<code>  
Write a 16-bit pascal style string to the stream.  
32-bit length field, followed by length PRUnichars.  
  
</code>
### writeUtf8Z(aString) ###
<code>  
Write an 8-bit pascal style string (UTF8-encoded) to the stream.  
32-bit length field, followed by length 8-bit chars.  
  
</code>
### writeBytes(aString, aLength) ###
<code>  
Write an opaque byte array to the stream.  
  
</code>
### writeByteArray(aBytes, aLength) ###
<code>  
Write an opaque byte array to the stream.  
  
</code>