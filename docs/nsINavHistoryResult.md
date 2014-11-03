---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/places/nsINavHistoryService.idl">Source file</a>
</div>

# nsINavHistoryResult #
<code>  
The result of a history/bookmark query.  
  
</code>
## Methods ##

### addObserver(aObserver, aOwnsWeak) ###
<code>  
Adds an observer for changes done in the result.  
  
@param aObserver  
       a result observer.  
@param aOwnsWeak  
       If false, the result will keep an owning reference to the observer,  
       which must be removed using removeObserver.  
       If true, the result will keep a weak reference to the observer, which  
       must implement nsISupportsWeakReference.  
  
@see nsINavHistoryResultObserver  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aObserver</td>
<td>       a result observer.  
</td>
</tr>

<tr>
<td>aOwnsWeak</td>
<td>       If false, the result will keep an owning reference to the observer,  
       which must be removed using removeObserver.  
       If true, the result will keep a weak reference to the observer, which  
       must implement nsISupportsWeakReference.  
</td>
</tr>

</table>

### removeObserver(aObserver) ###
<code>  
Removes an observer that was added by addObserver.  
  
@param aObserver  
       a result observer that was added by addObserver.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aObserver</td>
<td>       a result observer that was added by addObserver.  
</td>
</tr>

</table>

## Attributes ##

### sortingMode ###
  
Sorts all nodes recursively by the given parameter, one of  
nsINavHistoryQueryOptions.SORT_BY_*  This will update the corresponding  
options for this result, so that re-using the current options/queries will  
always give you the current view.  
  

### sortingAnnotation ###
  
The annotation to use in SORT_BY_ANNOTATION_* sorting modes, set this  
before setting the sortingMode attribute.  
  

### suppressNotifications ###
  
Whether or not notifications on result changes are suppressed.  
Initially set to false.  
  
Use this to avoid flickering and to improve performance when you  
do temporary changes to the result structure (e.g. when searching for a  
node recursively).  
  

### root ###
  
This is the root of the results. Remember that you need to open all  
containers for their contents to be valid.  
  
When a result goes out of scope it will continue to observe changes till  
it is cycle collected.  While the result waits to be collected it will stay  
in memory, and continue to update itself, potentially causing unwanted  
additional work.  When you close the root node the result will stop  
observing changes, so it is good practice to close the root node when you  
are done with a result, since that will avoid unwanted performance hits.  
  
