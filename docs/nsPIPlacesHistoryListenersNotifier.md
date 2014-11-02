---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/places/nsPIPlacesHistoryListenersNotifier.idl">Source file</a>
</div>

# nsPIPlacesHistoryListenersNotifier #
  
This is a private interface used by Places components to notify history  
listeners about important notifications.  These should not be used by any  
code that is not part of core.  
  
@note See also: nsINavHistoryObserver  
  

## Methods ##

### notifyOnPageExpired(aURI, aVisitTime, aWholeEntry, aGUID, aReason, aTransitionType) ###
  
Calls onDeleteVisits and onDeleteURI notifications on registered listeners  
with the history service.  
  
@param aURI  
       The nsIURI object representing the URI of the page being expired.  
@param aVisitTime  
       The time, in microseconds, that the page being expired was visited.  
@param aWholeEntry  
       Indicates if this is the last visit for this URI.  
@param aGUID  
       The unique ID associated with the page.  
@param aReason  
       Indicates the reason for the removal.  
       See nsINavHistoryObserver::REASON_* constants.  
@param aTransitionType  
       If it's a valid TRANSITION_* value, all visits of the specified type  
       have been removed.  
  

#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>       The nsIURI object representing the URI of the page being expired.  
</td>
</tr>

<tr>
<td>aVisitTime</td>
<td>       The time, in microseconds, that the page being expired was visited.  
</td>
</tr>

<tr>
<td>aWholeEntry</td>
<td>       Indicates if this is the last visit for this URI.  
</td>
</tr>

<tr>
<td>aGUID</td>
<td>       The unique ID associated with the page.  
</td>
</tr>

<tr>
<td>aReason</td>
<td>       Indicates the reason for the removal.  
       See nsINavHistoryObserver::REASON_* constants.  
</td>
</tr>

<tr>
<td>aTransitionType</td>
<td>       If it's a valid TRANSITION_* value, all visits of the specified type  
       have been removed.  
</td>
</tr>

</table>
