---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/profile/nsIProfileUnlocker.idl">Source file</a>
</div>

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
