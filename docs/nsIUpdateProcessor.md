---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/mozapps/update/nsIUpdateService.idl">Source file</a>
</div>

# nsIUpdateProcessor #
  
An interface describing a component which handles the job of processing  
an update after it's been downloaded.  
  

## Methods ##

### processUpdate(update) ###
  
Processes the update which has been downloaded.  
This happens without restarting the application.  
On Windows, this can also be used for switching to an applied  
update request.  
@param update The update being applied, or null if this is a switch  
              to updated application request.  Must be non-null on GONK.  
  

#### Parameters ####

<table>

<tr>
<td>update</td>
<td>The update being applied, or null if this is a switch  
              to updated application request.  Must be non-null on GONK.  
</td>
</tr>

</table>
