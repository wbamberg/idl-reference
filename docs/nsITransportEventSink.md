---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsITransport.idl">Source file</a>
</div>
# nsITransportEventSink #

## Methods ##

### onTransportStatus(aTransport, aStatus, aProgress, aProgressMax) ###
  
Transport status notification.  
  
@param aTransport  
       the transport sending this status notification.  
@param aStatus  
       the transport status (resolvable to a string using  
       nsIErrorService). See nsISocketTransport for socket specific  
       status codes and more comments.  
@param aProgress  
       the amount of data either read or written depending on the value  
       of the status code.  this value is relative to aProgressMax.  
@param aProgressMax  
       the maximum amount of data that will be read or written.  if  
       unknown, 0xFFFFFFFF will be passed.  
  

#### Parameters ####

<table>

<tr>
<td>aTransport</td>
<td>       the transport sending this status notification.  
</td>
</tr>

<tr>
<td>aStatus</td>
<td>       the transport status (resolvable to a string using  
       nsIErrorService). See nsISocketTransport for socket specific  
       status codes and more comments.  
</td>
</tr>

<tr>
<td>aProgress</td>
<td>       the amount of data either read or written depending on the value  
       of the status code.  this value is relative to aProgressMax.  
</td>
</tr>

<tr>
<td>aProgressMax</td>
<td>       the maximum amount of data that will be read or written.  if  
       unknown, 0xFFFFFFFF will be passed.  
</td>
</tr>

</table>
