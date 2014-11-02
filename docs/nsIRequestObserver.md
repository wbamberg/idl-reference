---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIRequestObserver.idl">Source file</a>
</div>

# nsIRequestObserver #
  
nsIRequestObserver  
  

## Methods ##

### onStartRequest(aRequest, aContext) ###
  
Called to signify the beginning of an asynchronous request.  
  
@param aRequest request being observed  
@param aContext user defined context  
  
An exception thrown from onStartRequest has the side-effect of  
causing the request to be canceled.  
  

#### Parameters ####

<table>

<tr>
<td>aRequest</td>
<td>request being observed  
</td>
</tr>

<tr>
<td>aContext</td>
<td>user defined context  
</td>
</tr>

</table>

### onStopRequest(aRequest, aContext, aStatusCode) ###
  
Called to signify the end of an asynchronous request.  This  
call is always preceded by a call to onStartRequest.  
  
@param aRequest request being observed  
@param aContext user defined context  
@param aStatusCode reason for stopping (NS_OK if completed successfully)  
  
An exception thrown from onStopRequest is generally ignored.  
  

#### Parameters ####

<table>

<tr>
<td>aRequest</td>
<td>request being observed  
</td>
</tr>

<tr>
<td>aContext</td>
<td>user defined context  
</td>
</tr>

<tr>
<td>aStatusCode</td>
<td>reason for stopping (NS_OK if completed successfully)  
</td>
</tr>

</table>
