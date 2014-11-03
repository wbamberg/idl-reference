---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIStreamListener.idl">Source file</a>
</div>

# nsIStreamListener #
<code>  
nsIStreamListener  
  
</code>
## Methods ##

### onDataAvailable(aRequest, aContext, aInputStream, aOffset, aCount) ###
<code>  
Called when the next chunk of data (corresponding to the request) may  
be read without blocking the calling thread.  The onDataAvailable impl  
must read exactly |aCount| bytes of data before returning.  
  
@param aRequest request corresponding to the source of the data  
@param aContext user defined context  
@param aInputStream input stream containing the data chunk  
@param aOffset  
       Number of bytes that were sent in previous onDataAvailable calls  
       for this request. In other words, the sum of all previous count  
       parameters.  
@param aCount number of bytes available in the stream  
  
NOTE: The aInputStream parameter must implement readSegments.  
  
An exception thrown from onDataAvailable has the side-effect of  
causing the request to be canceled.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aRequest</td>
<td>request corresponding to the source of the data  
</td>
</tr>

<tr>
<td>aContext</td>
<td>user defined context  
</td>
</tr>

<tr>
<td>aInputStream</td>
<td>input stream containing the data chunk  
</td>
</tr>

<tr>
<td>aOffset</td>
<td>       Number of bytes that were sent in previous onDataAvailable calls  
       for this request. In other words, the sum of all previous count  
       parameters.  
</td>
</tr>

<tr>
<td>aCount</td>
<td>number of bytes available in the stream  
</td>
</tr>

</table>
