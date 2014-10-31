---
layout: default
---

# nsIUpdateManager #
  
An interface describing a global application service that maintains a list  
of updates previously performed as well as the current active update.  
  

## Methods ##

### getUpdateAt(index) ###
  
Gets the update at the specified index  
@param   index  
         The index within the updates array  
@returns The nsIUpdate object at the specified index  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>index  
         The index within the updates array  
</td>
</tr>

</table>

### saveUpdates() ###
  
Saves all updates to disk.  
  

### refreshUpdateStatus(update) ###
  
Refresh the update status based on the information in update.status.  
  

## Attributes ##

### updateCount ###
  
Gets the total number of updates in the history list.  
  

### activeUpdate ###
  
The active (current) update. The active update is not in the history list.  
  
