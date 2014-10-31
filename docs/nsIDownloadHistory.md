---
layout: default
---

# nsIDownloadHistory #
  
This interface can be used to add a download to history.  There is a separate  
interface specifically for downloads in case embedders choose to track  
downloads differently from other types of history.  
  

## Methods ##

### addDownload(aSource, aReferrer, aStartTime, aDestination) ###
  
Adds a download to history.  This will also notify observers that the  
URI aSource is visited with the topic NS_LINK_VISITED_EVENT_TOPIC if  
aSource has not yet been visited.  
  
@param aSource  
       The source of the download we are adding to history.  This cannot be  
       null.  
@param aReferrer  
       [optional] The referrer of source URI.  
@param aStartTime  
       [optional] The time the download was started.  If the start time  
       is not given, the current time is used.  
@param aDestination  
       [optional] The target where the download is to be saved on the local  
       filesystem.  
@throws NS_ERROR_NOT_AVAILABLE  
        In a situation where a history implementation is not available,  
        where 'history implementation' refers to something like  
        nsIGlobalHistory and friends.  
@note This addition is not guaranteed to be synchronous, since it delegates  
      the actual addition to the underlying history implementation.  If you  
      need to observe the completion of the addition, use the underlying  
      history implementation's notifications system (e.g. nsINavHistoryObserver  
      for toolkit's implementation of this interface).  
  

#### Parameters ####

<table>

<tr>
<td>aSource</td>
<td>       The source of the download we are adding to history.  This cannot be  
       null.  
</td>
</tr>

<tr>
<td>aSource</td>
<td>       The source of the download we are adding to history.  This cannot be  
       null.  
</td>
</tr>

<tr>
<td>aSource</td>
<td>       The source of the download we are adding to history.  This cannot be  
       null.  
</td>
</tr>

<tr>
<td>aSource</td>
<td>       The source of the download we are adding to history.  This cannot be  
       null.  
</td>
</tr>

</table>

### removeAllDownloads() ###
  
Remove all downloads from history.  
  
@note This removal is not guaranteed to be synchronous, since it delegates  
      the actual removal to the underlying history implementation.  If you  
      need to observe the completion of the removal, use the underlying  
      history implementation's notifications system (e.g. nsINavHistoryObserver  
      for toolkit's implementation of this interface).  
  
