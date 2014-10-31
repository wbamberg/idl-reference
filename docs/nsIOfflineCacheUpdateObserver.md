---
layout: default
---

# nsIOfflineCacheUpdateObserver #

## Methods ##

### updateStateChanged(aUpdate, state) ###
  
aUpdate has changed its state.  
  
@param aUpdate  
       The nsIOfflineCacheUpdate being processed.  
@param event  
       See enumeration above  
  

#### Parameters ####

<table>

<tr>
<td>aUpdate</td>
<td>       The nsIOfflineCacheUpdate being processed.  
</td>
</tr>

<tr>
<td>event</td>
<td>       See enumeration above  
</td>
</tr>

</table>

### applicationCacheAvailable(applicationCache) ###
  
Informs the observer about an application being available to associate.  
  
@param applicationCache  
       The application cache instance that has been created or found by the   
       update to associate with  
  

#### Parameters ####

<table>

<tr>
<td>applicationCache</td>
<td>       The application cache instance that has been created or found by the   
       update to associate with  
</td>
</tr>

</table>

## Constants ##

### STATE_ERROR ###

### STATE_CHECKING ###

### STATE_NOUPDATE ###

### STATE_OBSOLETE ###

### STATE_DOWNLOADING ###

### STATE_ITEMSTARTED ###

### STATE_ITEMCOMPLETED ###

### STATE_ITEMPROGRESS ###

### STATE_FINISHED ###
