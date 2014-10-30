---
layout: default
---

# nsINavHistoryObserver #
  
Similar to nsIRDFObserver for history. Note that we don't pass the data  
source since that is always the global history.  
  
DANGER! If you are in the middle of a batch transaction, there may be a  
database transaction active. You can still access the DB, but be careful.  
  

## Methods ##

### onBeginUpdateBatch ###
  
Notifies you that a bunch of things are about to change, don't do any  
heavy-duty processing until onEndUpdateBatch is called.  
  

### onEndUpdateBatch ###
  
Notifies you that we are done doing a bunch of things and you should go  
ahead and update UI, etc.  
  

### onVisit ###
  
Called when a resource is visited. This is called the first time a  
resource (page, image, etc.) is seen as well as every subsequent time.  
  
Normally, transition types of TRANSITION_EMBED (corresponding to images in  
a page, for example) are not displayed in history results (unless  
includeHidden is set). Many observers can ignore _EMBED notifications  
(which will comprise the majority of visit notifications) to save work.  
  
@param aVisitID        ID of the visit that was just created.  
@param aTime           Time of the visit  
@param aSessionID      No longer supported (always set to 0).  
@param aReferringID    The ID of the visit the user came from. 0 if empty.  
@param aTransitionType One of nsINavHistory.TRANSITION_*  
@param aGUID           The unique ID associated with the page.  
@param aHidden         Whether the visited page is marked as hidden.  
  

### onTitleChanged ###
  
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
  
@param aURI  
       The URI of the page.  
@param aPageTitle  
       The new title of the page.  
@param aGUID  
       The unique ID associated with the page.  
  

### onFrecencyChanged ###
  
Called when an individual page's frecency has changed.  
  
This is not called for pages whose frecencies change as the result of some  
large operation where some large or unknown number of frecencies change at  
once.  Use onManyFrecenciesChanged to detect such changes.  
  
@param aURI  
       The page's URI.  
@param aNewFrecency  
       The page's new frecency.  
@param aGUID  
       The page's GUID.  
@param aHidden  
       True if the page is marked as hidden.  
@param aVisitDate  
       The page's last visit date.  
  

### onManyFrecenciesChanged ###
  
Called when the frecencies of many pages have changed at once.  
  
onFrecencyChanged is not called for each of those pages.  
  

### onDeleteURI ###
  
This page and all of its visits are being deleted. Note: the page may not  
necessarily have actually existed for this function to be called.  
  
Delete notifications are only 99.99% accurate. Batch delete operations  
must be done in two steps, so first come notifications, then a bulk  
delete. If there is some error in the middle (for example, out of memory)  
then you'll get a notification and it won't get deleted. There's no easy  
way around this.  
  
@param aURI  
       The URI that was deleted.  
@param aGUID  
       The unique ID associated with the page.  
@param aReason  
       Indicates the reason for the removal.  see REASON_* constants.  
  

### onClearHistory ###
  
Notification that all of history is being deleted.  
  

### onPageChanged ###
  
An attribute of this page changed.  
  
@param aURI  
       The URI of the page on which an attribute changed.  
@param aChangedAttribute  
       The attribute whose value changed.  See ATTRIBUTE_* constants.  
@param aNewValue  
       The attribute's new value.  
@param aGUID  
       The unique ID associated with the page.  
  

### onDeleteVisits ###
  
Called when some visits of an history entry are expired.  
  
@param aURI  
       The page whose visits have been expired.  
@param aVisitTime  
       The largest visit time in microseconds that has been expired.  We  
       guarantee that we don't have any visit older than this date.  
@param aGUID  
       The unique ID associated with the page.  
  
@note: when all visits for a page are expired and also the full page entry  
       is expired, you will only get an onDeleteURI notification.  If a  
       page entry is removed, then you can be sure that we don't have  
       anymore visits for it.  
@param aReason  
       Indicates the reason for the removal.  see REASON_* constants.  
@param aTransitionType  
       If it's a valid TRANSITION_* value, all visits of the specified type  
       have been removed.  
  

## Constants ##

### REASON_DELETED ###
  
Removed by the user.  
  

### REASON_EXPIRED ###
  
Removed by automatic expiration.  
  

### ATTRIBUTE_FAVICON ###
  
onPageChanged attribute indicating that favicon has been updated.  
aNewValue parameter will be set to the new favicon URI string.  
  
