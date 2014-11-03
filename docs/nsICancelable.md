---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsICancelable.idl">Source file</a>
</div>

# nsICancelable #
<pre>  
This interface provides a means to cancel an operation that is in progress.  
  
</pre>
## Methods ##

### cancel(aReason) ###
<pre>  
Call this method to request that this object abort whatever operation it  
may be performing.  
  
@param aReason  
       Pass a failure code to indicate the reason why this operation is  
       being canceled.  It is an error to pass a success code.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aReason</td>
<td>       Pass a failure code to indicate the reason why this operation is  
       being canceled.  It is an error to pass a success code.  
</td>
</tr>

</table>
