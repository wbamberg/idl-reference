---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/cache2/nsICacheStorageService.idl">Source file</a>
</div>
# nsICacheStorageConsumptionObserver #

## Methods ##

### onNetworkCacheDiskConsumption(aDiskSize) ###
  
Callback invoked to answer asyncGetDiskConsumption call. Always triggered  
on the main thread.  
NOTE: implementers must also implement nsISupportsWeakReference.  
  
@param aDiskSize  
   The disk consumption in bytes.  
  

#### Parameters ####

<table>

<tr>
<td>aDiskSize</td>
<td>   The disk consumption in bytes.  
</td>
</tr>

</table>
