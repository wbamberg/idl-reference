---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIBackgroundFileSaver.idl">Source file</a>
</div>

# nsIBackgroundFileSaverObserver #

## Methods ##

### onTargetChange(aSaver, aTarget) ###
  
Called when the name of the output file has been determined.  This function  
may be called more than once if the target file is renamed while saving.  
  
@param aSaver  
       Reference to the object that raised the notification.  
@param aTarget  
       Name of the file that is being written.  
  

#### Parameters ####

<table>

<tr>
<td>aSaver</td>
<td>       Reference to the object that raised the notification.  
</td>
</tr>

<tr>
<td>aTarget</td>
<td>       Name of the file that is being written.  
</td>
</tr>

</table>

### onSaveComplete(aSaver, aStatus) ###
  
Called when the operation completed, and the target file has been closed.  
If the operation succeeded, the target file is ready to be used, otherwise  
it might have been already deleted.  
  
@param aSaver  
       Reference to the object that raised the notification.  
@param aStatus  
       Result code that determines whether the operation succeeded or  
       failed, as well as the failure reason.  
  

#### Parameters ####

<table>

<tr>
<td>aSaver</td>
<td>       Reference to the object that raised the notification.  
</td>
</tr>

<tr>
<td>aStatus</td>
<td>       Result code that determines whether the operation succeeded or  
       failed, as well as the failure reason.  
</td>
</tr>

</table>
