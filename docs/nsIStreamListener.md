---
layout: default
---

# nsIStreamListener #
  
nsIStreamListener  
  

## Methods ##

### onDataAvailable(aRequest, aContext, aInputStream, aOffset, aCount) ###
  
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
  

#### Parameters ####

<table>

<tr>
<td>aRequest</td>
<td>request corresponding to the source of the data  
</td>
</tr>

<tr>
<td>aRequest</td>
<td>request corresponding to the source of the data  
</td>
</tr>

<tr>
<td>aRequest</td>
<td>request corresponding to the source of the data  
</td>
</tr>

<tr>
<td>aRequest</td>
<td>request corresponding to the source of the data  
</td>
</tr>

<tr>
<td>aRequest</td>
<td>request corresponding to the source of the data  
</td>
</tr>

</table>
