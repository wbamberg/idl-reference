---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/places/nsINavHistoryService.idl">Source file</a>
</div>

# nsINavHistoryObserver #
  
Similar to nsIRDFObserver for history. Note that we don't pass the data  
source since that is always the global history.  
  
DANGER! If you are in the middle of a batch transaction, there may be a  
database transaction active. You can still access the DB, but be careful.  
  

## Methods ##

### onBeginUpdateBatch() ###
  
Notifies you that a bunch of things are about to change, don't do any  
heavy-duty processing until onEndUpdateBatch is called.  
  

### onEndUpdateBatch() ###
  
Notifies you that we are done doing a bunch of things and you should go  
ahead and update UI, etc.  
  

### onVisit(aURI, aVisitID, aTime, aSessionID, aReferringID, aTransitionType, aGUID, aHidden) ###
  
Called when a resource is visited. This is called the first time a  
resource (page, image, etc.) is seen as well as every subsequent time.  
  
Normally, transition types of TRANSITION_EMBED (corresponding to images in  
a page, for example) are not displayed in history results (unless  
includeHidden is set). Many observers can ignore _EMBED notifications  
(which will comprise the majority of visit notifications) to save work.  
  
  

#### Parameters ####

<table>

<tr>
<td>aVisitID</td>
<td>ID of the visit that was just created.  
</td>
</tr>

<tr>
<td>aTime</td>
<td>Time of the visit  
</td>
</tr>

<tr>
<td>aSessionID</td>
<td>No longer supported (always set to 0).  
</td>
</tr>

<tr>
<td>aReferringID</td>
<td>The ID of the visit the user came from. 0 if empty.  
</td>
</tr>

<tr>
<td>aTransitionType</td>
<td>One of nsINavHistory.TRANSITION_*  
</td>
</tr>

<tr>
<td>aGUID</td>
<td>The unique ID associated with the page.  
</td>
</tr>

<tr>
<td>aHidden</td>
<td>Whether the visited page is marked as hidden.  
</td>
</tr>

</table>

### onTitleChanged(aURI, aPageTitle, aGUID) ###
  
Called whenever either the "real" title or the custom title of the page  
changed. BOTH TITLES ARE ALWAYS INCLUDED in this notification, even though  
only one will change at a time. Often, consumers will want to display the  
user title if it is available, and fall back to the page title (the one  
specified in the <title> tag of the page).  
  
Note that there is a difference between an empty title and a NULL title.  
An empty string means that somebody specifically set the title to be  
nothing. NULL means nobody set it. From C++: use IsVoid() and SetIsVoid()  
to see whether an empty string is "null" or not (it will always be an  
empty string in either case).  
  
  

#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>       The URI of the page.  
</td>
</tr>

<tr>
<td>aPageTitle</td>
<td>       The new title of the page.  
</td>
</tr>

<tr>
<td>aGUID</td>
<td>       The unique ID associated with the page.  
</td>
</tr>

</table>

### onFrecencyChanged(aURI, aNewFrecency, aGUID, aHidden, aVisitDate) ###
  
Called when an individual page's frecency has changed.  
  
This is not called for pages whose frecencies change as the result of some  
large operation where some large or unknown number of frecencies change at  
once.  Use onManyFrecenciesChanged to detect such changes.  
  
  

#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>       The page's URI.  
</td>
</tr>

<tr>
<td>aNewFrecency</td>
<td>       The page's new frecency.  
</td>
</tr>

<tr>
<td>aGUID</td>
<td>       The page's GUID.  
</td>
</tr>

<tr>
<td>aHidden</td>
<td>       True if the page is marked as hidden.  
</td>
</tr>

<tr>
<td>aVisitDate</td>
<td>       The page's last visit date.  
</td>
</tr>

</table>

### onManyFrecenciesChanged() ###
  
Called when the frecencies of many pages have changed at once.  
  
onFrecencyChanged is not called for each of those pages.  
  

### onDeleteURI(aURI, aGUID, aReason) ###
  
This page and all of its visits are being deleted. Note: the page may not  
necessarily have actually existed for this function to be called.  
  
Delete notifications are only 99.99% accurate. Batch delete operations  
must be done in two steps, so first come notifications, then a bulk  
delete. If there is some error in the middle (for example, out of memory)  
then you'll get a notification and it won't get deleted. There's no easy  
way around this.  
  
  

#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>       The URI that was deleted.  
</td>
</tr>

<tr>
<td>aGUID</td>
<td>       The unique ID associated with the page.  
</td>
</tr>

<tr>
<td>aReason</td>
<td>       Indicates the reason for the removal.  see REASON_* constants.  
</td>
</tr>

</table>

### onClearHistory() ###
  
Notification that all of history is being deleted.  
  

### onPageChanged(aURI, aChangedAttribute, aNewValue, aGUID) ###
  
An attribute of this page changed.  
  
  

#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>       The URI of the page on which an attribute changed.  
</td>
</tr>

<tr>
<td>aChangedAttribute</td>
<td>       The attribute whose value changed.  See ATTRIBUTE_* constants.  
</td>
</tr>

<tr>
<td>aNewValue</td>
<td>       The attribute's new value.  
</td>
</tr>

<tr>
<td>aGUID</td>
<td>       The unique ID associated with the page.  
</td>
</tr>

</table>

### onDeleteVisits(aURI, aVisitTime, aGUID, aReason, aTransitionType) ###
  
Called when some visits of an history entry are expired.  
  
  
@note: when all visits for a page are expired and also the full page entry  
       is expired, you will only get an onDeleteURI notification.  If a  
       page entry is removed, then you can be sure that we don't have  
       anymore visits for it.  
  

#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>       The page whose visits have been expired.  
</td>
</tr>

<tr>
<td>aVisitTime</td>
<td>       The largest visit time in microseconds that has been expired.  We  
       guarantee that we don't have any visit older than this date.  
</td>
</tr>

<tr>
<td>aGUID</td>
<td>       The unique ID associated with the page.  
</td>
</tr>

<tr>
<td>aReason</td>
<td>       Indicates the reason for the removal.  see REASON_* constants.  
</td>
</tr>

<tr>
<td>aTransitionType</td>
<td>       If it's a valid TRANSITION_* value, all visits of the specified type  
       have been removed.  
</td>
</tr>

</table>

## Constants ##

### REASON_DELETED ###
  
Removed by the user.  
  

### REASON_EXPIRED ###
  
Removed by automatic expiration.  
  

### ATTRIBUTE_FAVICON ###
  
onPageChanged attribute indicating that favicon has been updated.  
aNewValue parameter will be set to the new favicon URI string.  
  
