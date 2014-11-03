---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/quota/nsIQuotaManager.idl">Source file</a>
</div>

# nsIQuotaManager #

## Methods ##

### getUsageForURI(aURI, aCallback, aAppId, aInMozBrowserOnly) ###
<pre>  
Schedules an asynchronous callback that will return the total amount of  
disk space being used by storages for the given origin.  
  
@param aURI  
       The URI whose usage is being queried.  
@param aCallback  
       The callback that will be called when the usage is available.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>       The URI whose usage is being queried.  
</td>
</tr>

<tr>
<td>aCallback</td>
<td>       The callback that will be called when the usage is available.  
</td>
</tr>

</table>

### clear() ###
<pre>  
Removes all storages. The files may not be deleted immediately depending  
on prohibitive concurrent operations.  
Be careful, this removes *all* the data that has ever been stored!  
  
If the dom.quotaManager.testing preference is not true the call will be  
a no-op.  
  
</pre>
### clearStoragesForURI(aURI, aAppId, aInMozBrowserOnly, aPersistenceType) ###
<pre>  
Removes all storages stored for the given URI. The files may not be  
deleted immediately depending on prohibitive concurrent operations.  
  
@param aURI  
       The URI whose storages are to be cleared.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>       The URI whose storages are to be cleared.  
</td>
</tr>

</table>

### reset() ###
<pre>  
Resets quota and storage management. This can be used to force  
reinitialization of the temp storage, for example when the pref for  
overriding the temp storage limit has changed.  
Be carefull, this invalidates all live storages!  
  
If the dom.quotaManager.testing preference is not true the call will be  
a no-op.  
  
</pre>