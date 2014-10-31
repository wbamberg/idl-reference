---
layout: default
---

# nsIBufferedInputStream #
  
An input stream that reads ahead and keeps a buffer coming from another input  
stream so that fewer accesses to the underlying stream are necessary.  
  

## Methods ##

### init(fillFromStream, bufferSize) ###
  
@param fillFromStream - add buffering to this stream  
@param bufferSize     - specifies the maximum buffer size  
  

#### Parameters ####

<table>

<tr>
<td>fillFromStream</td>
<td>- add buffering to this stream  
</td>
</tr>

<tr>
<td>bufferSize</td>
<td>- specifies the maximum buffer size  
</td>
</tr>

</table>
