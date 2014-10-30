---
layout: default
---

# nsIBrowserHistory #

## Methods ##

### removePage ###
  
Removes a page from global history.  
  
@note It is preferrable to use this one rather then RemovePages when  
      removing less than 10 pages, since it won't start a full batch  
      operation.  
  

### removePages ###
  
Removes a list of pages from global history.  
  
@param aURIs  
       Array of URIs to be removed.  
@param aLength  
       Length of the array.  
  
@note the removal happens in a batch.  
  

### removePagesFromHost ###
  
Removes all global history information about pages for a given host.  
  
@param aHost  
       Hostname to be removed.  
       An empty host name means local files and anything else with no  
       hostname.  You can also pass in the localized "(local files)"  
       title given to you from a history query to remove all  
       history information from local files.  
@param aEntireDomain  
       If true, will also delete pages from sub hosts (so if  
       passed in "microsoft.com" will delete "www.microsoft.com",  
       "msdn.microsoft.com", etc.).  
  
@note The removal happens in a batch.  
  

### removePagesByTimeframe ###
  
Removes all pages for a given timeframe.  
Limits are included: aBeginTime <= timeframe <= aEndTime  
  
@param aBeginTime  
       Microseconds from epoch, representing the initial time.  
@param aEndTime  
       Microseconds from epoch, representing the final time.  
  
@note The removal happens in a batch.  
  

### removeVisitsByTimeframe ###
  
Removes all visits in a given timeframe.  
Limits are included: aBeginTime <= timeframe <= aEndTime.  
Any pages that becomes unvisited as a result will also be deleted.  
  
@param aBeginTime  
       Microseconds from epoch, representing the initial time.  
@param aEndTime  
       Microseconds from epoch, representing the final time.  
  
@note The removal happens in a batch.  
  

### removeAllPages ###
  
Removes all existing pages from global history.  
Visits are removed synchronously, but pages are expired asynchronously  
off the main-thread.  
  
@note The removal happens in a batch. Single removals are not notified,  
      instead an onClearHistory notification is sent to  
      nsINavHistoryObserver implementers.  
  
