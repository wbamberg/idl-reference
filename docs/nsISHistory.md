---
layout: default
---

# nsISHistory #
  
An interface to the primary properties of the Session History  
component. In an embedded browser environment, the nsIWebBrowser  
object creates an instance of session history for each open window.  
A handle to the session history object can be obtained from  
nsIWebNavigation. In a non-embedded situation, the  owner of the  
session history component must create a instance of it and set  
it in the nsIWebNavigation object.  
This interface is accessible from javascript.  
  

## Methods ##

### getEntryAtIndex(index, modifyIndex) ###
  
Called to obtain handle to the history entry at a  
given index.  
  
@param index             The index value whose entry is requested.  
                         The oldest entry is located at index == 0.  
@param modifyIndex       A boolean flag that indicates if the current  
                         index of session history should be modified   
                         to the parameter index.  
  
@return                  <code>NS_OK</code> history entry for   
                         the index is obtained successfully.  
                         <code>NS_ERROR_FAILURE</code> Error in obtaining  
                         history entry for the given index.  
  

#### Parameters ####

<table>

<tr>
<td>index</td>
<td>The index value whose entry is requested.  
                         The oldest entry is located at index == 0.  
</td>
</tr>

<tr>
<td>modifyIndex</td>
<td>A boolean flag that indicates if the current  
                         index of session history should be modified   
                         to the parameter index.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td><code>NS_OK</code> history entry for   
                         the index is obtained successfully.  
                         <code>NS_ERROR_FAILURE</code> Error in obtaining  
                         history entry for the given index.  
</td>
</tr>

</table>

### PurgeHistory(numEntries) ###
  
Called to purge older documents from history.  
Documents can be removed from session history for various   
reasons. For example to  control memory usage of the browser, to   
prevent users from loading documents from history, to erase evidence of  
prior page loads etc...  
  
@param numEntries        The number of toplevel documents to be  
                         purged from history. During purge operation,  
                         the latest documents are maintained and older   
                         'numEntries' documents are removed from history.  
@throws                  <code>NS_SUCCESS_LOSS_OF_INSIGNIFICANT_DATA</code> Purge was vetod.  
@throws                  <code>NS_ERROR_FAILURE</code> numEntries is  
                         invalid or out of bounds with the size of history.  
                           
  

#### Parameters ####

<table>

<tr>
<td>numEntries</td>
<td>The number of toplevel documents to be  
                         purged from history. During purge operation,  
                         the latest documents are maintained and older   
                         'numEntries' documents are removed from history.  
@throws                  <code>NS_SUCCESS_LOSS_OF_INSIGNIFICANT_DATA</code> Purge was vetod.  
@throws                  <code>NS_ERROR_FAILURE</code> numEntries is  
                         invalid or out of bounds with the size of history.  
</td>
</tr>

</table>

### addSHistoryListener(aListener) ###
  
Called to register a listener for the session history component.  
Listeners are notified when pages are loaded or purged from history.  
  
@param aListener         Listener object to be notified for all  
                         page loads that initiate in session history.  
  
@note                    A listener object must implement   
                         nsISHistoryListener and nsSupportsWeakReference  
  
@see nsISHistoryListener  
@see nsSupportsWeakReference  
  

#### Parameters ####

<table>

<tr>
<td>aListener</td>
<td>Listener object to be notified for all  
                         page loads that initiate in session history.  
</td>
</tr>

</table>

### removeSHistoryListener(aListener) ###
  
Called to remove a listener for the session history component.  
Listeners are notified when pages are loaded from history.  
  
@param aListener         Listener object to be removed from   
                         session history.  
  
@note                    A listener object must implement   
                         nsISHistoryListener and nsSupportsWeakReference  
@see nsISHistoryListener  
@see nsSupportsWeakReference  
  

#### Parameters ####

<table>

<tr>
<td>aListener</td>
<td>Listener object to be removed from   
                         session history.  
</td>
</tr>

</table>

### reloadCurrentEntry() ###

### getIndexOfEntry(aEntry) ###
  
Called to obtain the index to a given history entry.  
  
@param aEntry            The entry to obtain the index of.  
  
@return                  <code>NS_OK</code> index for the history entry  
                         is obtained successfully.  
                         <code>NS_ERROR_FAILURE</code> Error in obtaining  
                         index for the given history entry.  
  

#### Parameters ####

<table>

<tr>
<td>aEntry</td>
<td>The entry to obtain the index of.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td><code>NS_OK</code> index for the history entry  
                         is obtained successfully.  
                         <code>NS_ERROR_FAILURE</code> Error in obtaining  
                         index for the given history entry.  
</td>
</tr>

</table>

## Attributes ##

### count ###
  
A readonly property of the interface that returns   
the number of toplevel documents currently available  
in session history.  
  

### index ###
  
A readonly property of the interface that returns   
the index of the current document in session history.  
  

### requestedIndex ###
  
A readonly property of the interface that returns   
the index of the last document that started to load and  
didn't finished yet. When document finishes the loading  
value -1 is returned.  
  

### maxLength ###
  
A read/write property of the interface, used to Get/Set  
the maximum number of toplevel documents, session history   
can hold for each instance.   
  

### SHistoryEnumerator ###
  
Called to obtain a enumerator for all the  documents stored in   
session history. The enumerator object thus returned by this method  
can be traversed using nsISimpleEnumerator.   
  
@note  To access individual history entries of the enumerator, perform the  
       following steps:  
       1) Call nsISHistory->GetSHistoryEnumerator() to obtain handle   
          the nsISimpleEnumerator object.  
       2) Use nsISimpleEnumerator->GetNext() on the object returned  
          by step #1 to obtain handle to the next object in the list.   
          The object returned by this step is of type nsISupports.  
       3) Perform a QueryInterface on the object returned by step #2   
          to nsISHEntry.  
       4) Use nsISHEntry to access properties of each history entry.   
  
@see nsISimpleEnumerator  
@see nsISHEntry  
@see QueryInterface()  
@see do_QueryInterface()  
  
