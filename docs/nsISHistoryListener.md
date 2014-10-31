---
layout: default
---

# nsISHistoryListener #
  
nsISHistoryListener defines the interface one can implement to receive  
notifications about activities in session history and to be able to  
cancel them.  
  
A session history listener will be notified when pages are added, removed  
and loaded from session history. It can prevent any action (except adding  
a new session history entry) from happening by returning false from the  
corresponding callback method.  
  
A session history listener can be registered on a particular nsISHistory  
instance via the nsISHistory::addSHistoryListener() method.  
  

## Methods ##

### OnHistoryNewEntry(aNewURI) ###
  
Called when a new document is added to session history. New documents are  
added to session history by docshell when new pages are loaded in a frame  
or content area, for example via nsIWebNavigation::loadURI()  
  
@param aNewURI     The URI of the document to be added to session history.  
  

#### Parameters ####

<table>

<tr>
<td>aNewURI</td>
<td>The URI of the document to be added to session history.  
</td>
</tr>

</table>

### OnHistoryGoBack(aBackURI) ###
  
Called when navigating to a previous session history entry, for example  
due to a nsIWebNavigation::goBack() call.  
  
@param aBackURI    The URI of the session history entry being navigated to.  
@return            Whether the operation can proceed.  
  

#### Parameters ####

<table>

<tr>
<td>aBackURI</td>
<td>The URI of the session history entry being navigated to.  
</td>
</tr>

</table>

### OnHistoryGoForward(aForwardURI) ###
  
Called when navigating to a next session history entry, for example  
due to a nsIWebNavigation::goForward() call.  
  
@param aForwardURI   The URI of the session history entry being navigated to.  
@return              Whether the operation can proceed.  
  

#### Parameters ####

<table>

<tr>
<td>aForwardURI</td>
<td>The URI of the session history entry being navigated to.  
</td>
</tr>

</table>

### OnHistoryReload(aReloadURI, aReloadFlags) ###
   
Called when the current document is reloaded, for example due to a  
nsIWebNavigation::reload() call.  
  
@param aReloadURI    The URI of the document to be reloaded.  
@param aReloadFlags  Flags that indicate how the document is to be   
                     refreshed. See constants on the nsIWebNavigation  
                     interface.  
@return              Whether the operation can proceed.  
  
@see  nsIWebNavigation  
  

#### Parameters ####

<table>

<tr>
<td>aReloadURI</td>
<td>The URI of the document to be reloaded.  
</td>
</tr>

<tr>
<td>aReloadURI</td>
<td>The URI of the document to be reloaded.  
</td>
</tr>

</table>

### OnHistoryGotoIndex(aIndex, aGotoURI) ###
  
Called when navigating to a session history entry by index, for example,  
when nsIWebNavigation::gotoIndex() is called.  
  
@param aIndex        The index in session history of the entry to be loaded.  
@param aGotoURI      The URI of the session history entry to be loaded.  
@return              Whether the operation can proceed.  
  

#### Parameters ####

<table>

<tr>
<td>aIndex</td>
<td>The index in session history of the entry to be loaded.  
</td>
</tr>

<tr>
<td>aIndex</td>
<td>The index in session history of the entry to be loaded.  
</td>
</tr>

</table>

### OnHistoryPurge(aNumEntries) ###
  
Called when entries are removed from session history. Entries can be  
removed from session history for various reasons, for example to control  
the memory usage of the browser, to prevent users from loading documents  
from history, to erase evidence of prior page loads, etc.  
  
To purge documents from session history call nsISHistory::PurgeHistory()  
  
@param aNumEntries   The number of entries to be removed from session history.  
@return              Whether the operation can proceed.  
  

#### Parameters ####

<table>

<tr>
<td>aNumEntries</td>
<td>The number of entries to be removed from session history.  
</td>
</tr>

</table>

### OnHistoryReplaceEntry(aIndex) ###
  
Called when an entry is replaced in the session history. Entries are  
replaced when navigating away from non-persistent history entries (such as  
about pages) and when history.replaceState is called.  
  
@param aIndex        The index in session history of the entry being  
                      replaced  
  

#### Parameters ####

<table>

<tr>
<td>aIndex</td>
<td>The index in session history of the entry being  
                      replaced  
</td>
</tr>

</table>
