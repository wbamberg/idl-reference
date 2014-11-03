---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIBufferedStreams.idl">Source file</a>
</div>

# nsIBufferedInputStream #
<pre>  
An input stream that reads ahead and keeps a buffer coming from another input  
stream so that fewer accesses to the underlying stream are necessary.  
  
</pre>
## Methods ##

### init(fillFromStream, bufferSize) ###
<pre>  
@param fillFromStream - add buffering to this stream  
@param bufferSize     - specifies the maximum buffer size  
  
</pre>
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
