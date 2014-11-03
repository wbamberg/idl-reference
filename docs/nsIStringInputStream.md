---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/io/nsIStringStream.idl">Source file</a>
</div>

# nsIStringInputStream #
  
nsIStringInputStream  
  
Provides scriptable and specialized C++-only methods for initializing a  
nsIInputStream implementation with a simple character array.  
  

## Methods ##

### setData(data, dataLen) ###
  
SetData - assign data to the input stream (copied on assignment).  
  
@param data    - stream data  
@param dataLen - stream data length (-1 if length should be computed)  
  
NOTE: C++ code should consider using AdoptData or ShareData to avoid  
making an extra copy of the stream data.  
  
NOTE: For JS callers, the given data must not contain null characters  
(other than a null terminator) because a null character in the middle of  
the data string will be seen as a terminator when the data is converted  
from a JS string to a C++ character array.  
  

#### Parameters ####

<table>

<tr>
<td>data</td>
<td>- stream data  
</td>
</tr>

<tr>
<td>dataLen</td>
<td>- stream data length (-1 if length should be computed)  
</td>
</tr>

</table>

### adoptData(data, dataLen) ###
  
NOTE: the following methods are designed to give C++ code added control  
over the ownership and lifetime of the stream data.  Use with care :-)  
  
  
AdoptData - assign data to the input stream.  the input stream takes  
ownership of the given data buffer and will nsMemory::Free it when  
the input stream is destroyed.  
  
@param data      - stream data  
@param dataLen   - stream data length (-1 if length should be computed)  
  

#### Parameters ####

<table>

<tr>
<td>data</td>
<td>- stream data  
</td>
</tr>

<tr>
<td>dataLen</td>
<td>- stream data length (-1 if length should be computed)  
</td>
</tr>

</table>

### shareData(data, dataLen) ###
  
ShareData - assign data to the input stream.  the input stream references  
the given data buffer until the input stream is destroyed.  the given  
data buffer must outlive the input stream.  
  
@param data      - stream data  
@param dataLen   - stream data length (-1 if length should be computed)  
  

#### Parameters ####

<table>

<tr>
<td>data</td>
<td>- stream data  
</td>
</tr>

<tr>
<td>dataLen</td>
<td>- stream data length (-1 if length should be computed)  
</td>
</tr>

</table>
