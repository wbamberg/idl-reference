---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/io/nsIStreamBufferAccess.idl">Source file</a>
</div>

# nsIStreamBufferAccess #
  
An interface for access to a buffering stream implementation's underlying  
memory buffer.  
  
Stream implementations that QueryInterface to nsIStreamBufferAccess must  
ensure that all buffers are aligned on the most restrictive type size for  
the current architecture (e.g., sizeof(double) for RISCy CPUs).  malloc(3)  
satisfies this requirement.  
  

## Methods ##

### getBuffer(aLength, aAlignMask) ###
  
Get access to a contiguous, aligned run of bytes in the stream's buffer.  
Exactly one successful getBuffer call must occur before a putBuffer call  
taking the non-null pointer returned by the successful getBuffer.  
  
The run of bytes are the next bytes (modulo alignment padding) to read  
for an input stream, and the next bytes (modulo alignment padding) to  
store before (eventually) writing buffered data to an output stream.  
There can be space beyond this run of bytes in the buffer for further  
accesses before the fill or flush point is reached.  
  
@param aLength  
   Count of contiguous bytes requested at the address A that satisfies  
   (A & aAlignMask) == 0 in the buffer, starting from the current stream  
   position, mapped to a buffer address B.  The stream implementation  
   must pad from B to A by skipping bytes (if input stream) or storing  
   zero bytes (if output stream).  
  
@param aAlignMask  
   Bit-mask computed by subtracting 1 from the power-of-two alignment  
   modulus (e.g., 3 or sizeof(uint32_t)-1 for uint32_t alignment).  
  
@return  
   The aligned pointer to aLength bytes in the buffer, or null if the  
   buffer has no room for aLength bytes starting at the next address A  
   after the current position that satisfies (A & aAlignMask) == 0.  
  

#### Parameters ####

<table>

<tr>
<td>aLength</td>
<td>   Count of contiguous bytes requested at the address A that satisfies  
   (A & aAlignMask) == 0 in the buffer, starting from the current stream  
   position, mapped to a buffer address B.  The stream implementation  
   must pad from B to A by skipping bytes (if input stream) or storing  
   zero bytes (if output stream).  
</td>
</tr>

<tr>
<td>aAlignMask</td>
<td>   Bit-mask computed by subtracting 1 from the power-of-two alignment  
   modulus (e.g., 3 or sizeof(uint32_t)-1 for uint32_t alignment).  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>   The aligned pointer to aLength bytes in the buffer, or null if the  
   buffer has no room for aLength bytes starting at the next address A  
   after the current position that satisfies (A & aAlignMask) == 0.  
</td>
</tr>

</table>

### putBuffer(aBuffer, aLength) ###
  
Relinquish access to the stream's buffer, filling if at end of an input  
buffer, flushing if completing an output buffer.  After a getBuffer call  
that returns non-null, putBuffer must be called.  
  
@param aBuffer  
   A non-null pointer returned by getBuffer on the same stream buffer  
   access object.  
  
@param aLength  
   The same count of contiguous bytes passed to the getBuffer call that  
   returned aBuffer.  
  

#### Parameters ####

<table>

<tr>
<td>aBuffer</td>
<td>   A non-null pointer returned by getBuffer on the same stream buffer  
   access object.  
</td>
</tr>

<tr>
<td>aLength</td>
<td>   The same count of contiguous bytes passed to the getBuffer call that  
   returned aBuffer.  
</td>
</tr>

</table>

### disableBuffering() ###
  
Disable and enable buffering on the stream implementing this interface.  
DisableBuffering flushes an output stream's buffer, and invalidates an  
input stream's buffer.  
  

### enableBuffering() ###

## Attributes ##

### unbufferedStream ###
  
The underlying, unbuffered input or output stream.  
  
