---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsISimpleStreamListener.idl">Source file</a>
</div>

# nsISimpleStreamListener #
<pre>  
A simple stream listener can be used with AsyncRead to supply data to  
a output stream.  
  
</pre>
## Methods ##

### init(aSink, aObserver) ###
<pre>  
Initialize the simple stream listener.  
  
@param aSink data will be read from the channel to this output stream.  
             Must implement writeFrom.  
@param aObserver optional stream observer (can be NULL)  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aSink</td>
<td>data will be read from the channel to this output stream.  
             Must implement writeFrom.  
</td>
</tr>

<tr>
<td>aObserver</td>
<td>optional stream observer (can be NULL)  
</td>
</tr>

</table>
