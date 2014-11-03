---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/docshell/shistory/public/nsISHistoryInternal.idl">Source file</a>
</div>

# nsISHistoryInternal #

## Methods ##

### addEntry(aEntry, aPersist) ###
<code>  
Add a new Entry to the History List  
@param aEntry - The entry to add  
@param aPersist - If true this specifies that the entry should persist  
in the list.  If false, this means that when new entries are added  
this element will not appear in the session history list.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aEntry</td>
<td>- The entry to add  
</td>
</tr>

<tr>
<td>aPersist</td>
<td>- If true this specifies that the entry should persist  
in the list.  If false, this means that when new entries are added  
this element will not appear in the session history list.  
</td>
</tr>

</table>

### updateIndex() ###
<code>   
Update the index maintained by sessionHistory  
  
</code>
### replaceEntry(aIndex, aReplaceEntry) ###
<code>  
Replace the nsISHEntry at a particular index  
@param aIndex - The index at which the entry should be replaced  
@param aReplaceEntry - The replacement entry for the index.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aIndex</td>
<td>- The index at which the entry should be replaced  
</td>
</tr>

<tr>
<td>aReplaceEntry</td>
<td>- The replacement entry for the index.  
</td>
</tr>

</table>

### notifyOnHistoryReload(aReloadURI, aReloadFlags) ###
<code>  
Notifies all registered session history listeners about an impending  
reload.  
  
@param aReloadURI    The URI of the document to be reloaded.  
@param aReloadFlags  Flags that indicate how the document is to be  
                     refreshed. See constants on the nsIWebNavigation  
                     interface.  
@return              Whether the operation can proceed.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aReloadURI</td>
<td>The URI of the document to be reloaded.  
</td>
</tr>

<tr>
<td>aReloadFlags</td>
<td>Flags that indicate how the document is to be  
                     refreshed. See constants on the nsIWebNavigation  
                     interface.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>Whether the operation can proceed.  
</td>
</tr>

</table>

### evictOutOfRangeContentViewers(aIndex) ###
<code>  
Evict content viewers which don't lie in the "safe" range around aIndex.  
In practice, this should leave us with no more than gHistoryMaxViewers  
viewers associated with this SHistory object.  
  
Also make sure that the total number of content viewers in all windows is  
not greater than our global max; if it is, evict viewers as appropriate.  
  
@param aIndex - The index around which the "safe" range is centered.  In  
  general, if you just navigated the history, aIndex should be the index  
  history was navigated to.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aIndex</td>
<td>- The index around which the "safe" range is centered.  In  
  general, if you just navigated the history, aIndex should be the index  
  history was navigated to.  
</td>
</tr>

</table>

### evictExpiredContentViewerForEntry(aEntry) ###
<code>  
Evict the content viewer associated with a bfcache entry  
that has timed out.  
  
</code>
### evictAllContentViewers() ###
<code>  
Evict all the content viewers in this session history  
  
</code>
### RemoveEntries(aIDs, aStartIndex) ###
<code>  
Removes entries from the history if their docshellID is in  
aIDs array.  
  
</code>
## Attributes ##

### rootTransaction ###
  
Get the root transaction  
  

### rootDocShell ###
  
The toplevel docshell object to which this SHistory object belongs to.  
  
