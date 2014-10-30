---
layout: default
---

# nsICacheStorageConsumptionObserver #

## Methods ##

### onNetworkCacheDiskConsumption ###
  
Callback invoked to answer asyncGetDiskConsumption call. Always triggered  
on the main thread.  
NOTE: implementers must also implement nsISupportsWeakReference.  
  
@param aDiskSize  
   The disk consumption in bytes.  
  
