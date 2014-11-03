---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/power/nsIDOMWakeLockListener.idl">Source file</a>
</div>

# nsIDOMMozWakeLockListener #

## Methods ##

### callback(aTopic, aState) ###
  
The callback will be called when a lock topic changes its lock  
state.  
  
Possible states are:  
  
 - "unlocked" - nobody holds the wake lock.  
  
 - "locked-foreground" - at least one window holds the wake lock,  
   and it is visible.  
  
 - "locked-background" - at least one window holds the wake lock,  
   but all of them are hidden.  
  
  

#### Parameters ####

<table>

<tr>
<td>aTopic</td>
<td>The resource name related to the wake lock.  
</td>
</tr>

<tr>
<td>aState</td>
<td>The wake lock state  
</td>
</tr>

</table>
