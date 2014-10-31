---
layout: default
---

# nsIProfileUnlocker #

## Methods ##

### unlock(aSeverity) ###
  
Try to unlock the specified profile by attempting or forcing the  
process that currently holds the lock to quit.  
  
@param aSeverity either ATTEMPT_QUIT or FORCE_QUIT  
@throws NS_ERROR_FAILURE if unlocking failed.  
  

#### Parameters ####

<table>

<tr>
<td>aSeverity</td>
<td>either ATTEMPT_QUIT or FORCE_QUIT  
@throws NS_ERROR_FAILURE if unlocking failed.  
</td>
</tr>

</table>

## Constants ##

### ATTEMPT_QUIT ###

### FORCE_QUIT ###
