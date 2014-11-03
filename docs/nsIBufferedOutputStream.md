---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIBufferedStreams.idl">Source file</a>
</div>

# nsIBufferedOutputStream #
  
An output stream that stores up data to write out to another output stream  
and does the entire write only when the buffer is full, so that fewer writes  
to the underlying output stream are necessary.  
  

## Methods ##

### init(sinkToStream, bufferSize) ###
  
  

#### Parameters ####

<table>

<tr>
<td>sinkToStream</td>
<td>- add buffering to this stream  
</td>
</tr>

<tr>
<td>bufferSize</td>
<td>- specifies the maximum buffer size  
</td>
</tr>

</table>
