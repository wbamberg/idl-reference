---
layout: default
---

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
