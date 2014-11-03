---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIRequestObserver.idl">Source file</a>
</div>

# nsIRequestObserver #
<code>  
nsIRequestObserver  
  
</code>
## Methods ##

### onStartRequest(aRequest, aContext) ###
<code>  
Called to signify the beginning of an asynchronous request.  
  
@param aRequest request being observed  
@param aContext user defined context  
  
An exception thrown from onStartRequest has the side-effect of  
causing the request to be canceled.  
  
</code>
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
<code>  
Called to signify the end of an asynchronous request.  This  
call is always preceded by a call to onStartRequest.  
  
@param aRequest request being observed  
@param aContext user defined context  
@param aStatusCode reason for stopping (NS_OK if completed successfully)  
  
An exception thrown from onStopRequest is generally ignored.  
  
</code>
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
