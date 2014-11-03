---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/offline/nsIDOMOfflineResourceList.idl">Source file</a>
</div>

# nsIDOMOfflineResourceList #

## Methods ##

### mozHasItem(uri) ###
<code>  
Check that an entry exists in the list of dynamically-managed entries.  
  
@param uri  
       The resource to check.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>uri</td>
<td>       The resource to check.  
</td>
</tr>

</table>

### mozItem(index) ###
<code>  
Get the URI of a dynamically-managed entry.  
@status DEPRECATED  
        Clients should use the "items" attribute.  
  
</code>
### mozAdd(uri) ###
<code>  
Add an item to the list of dynamically-managed entries.  The resource  
will be fetched into the application cache.  
  
@param uri  
       The resource to add.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>uri</td>
<td>       The resource to add.  
</td>
</tr>

</table>

### mozRemove(uri) ###
<code>  
Remove an item from the list of dynamically-managed entries.  If this  
was the last reference to a URI in the application cache, the cache  
entry will be removed.  
  
@param uri  
       The resource to remove.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>uri</td>
<td>       The resource to remove.  
</td>
</tr>

</table>

### update() ###
<code>  
Begin the application update process on the associated application cache.  
  
</code>
### swapCache() ###
<code>  
Swap in the newest version of the application cache, or disassociate  
from the cache if the cache group is obsolete.  
  
</code>
## Attributes ##

### mozItems ###
  
Get the list of dynamically-managed entries.  
  

### mozLength ###
  
Get the number of dynamically-managed entries.  
@status DEPRECATED  
        Clients should use the "items" attribute.  
  

### status ###

### onchecking ###

### onerror ###

### onnoupdate ###

### ondownloading ###

### onprogress ###

### onupdateready ###

### oncached ###

### onobsolete ###

## Constants ##

### UNCACHED ###
  
State of the application cache this object is associated with.  
  

### IDLE ###

### CHECKING ###

### DOWNLOADING ###

### UPDATEREADY ###

### OBSOLETE ###
