---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/mozapps/update/nsIUpdateService.idl">Source file</a>
</div>

# nsIUpdateManager #
<pre>  
An interface describing a global application service that maintains a list  
of updates previously performed as well as the current active update.  
  
</pre>
## Methods ##

### getUpdateAt(index) ###
<pre>  
Gets the update at the specified index  
@param   index  
         The index within the updates array  
@returns The nsIUpdate object at the specified index  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>index</td>
<td>         The index within the updates array  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The nsIUpdate object at the specified index  
</td>
</tr>

</table>

### saveUpdates() ###
<pre>  
Saves all updates to disk.  
  
</pre>
### refreshUpdateStatus(update) ###
<pre>  
Refresh the update status based on the information in update.status.  
  
</pre>
## Attributes ##

### updateCount ###
<pre>  
Gets the total number of updates in the history list.  
  
</pre>
### activeUpdate ###
<pre>  
The active (current) update. The active update is not in the history list.  
  
</pre>