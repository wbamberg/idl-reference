---
layout: default
---

# nsINavHistoryService #

## Methods ##

### getPageTitle ###
  
Gets the original title of the page.  
@deprecated use mozIAsyncHistory.getPlacesInfo instead.  
  

### markPageAsFollowedBookmark ###
  
This is just like markPageAsTyped (in nsIBrowserHistory, also implemented  
by the history service), but for bookmarks. It declares that the given URI  
is being opened as a result of following a bookmark. If this URI is loaded  
soon after this message has been received, that transition will be marked  
as following a bookmark.  
  

### markPageAsTyped ###
  
Designates the url as having been explicitly typed in by the user.  
  
@param aURI  
       URI of the page to be marked.  
  

### markPageAsFollowedLink ###
  
Designates the url as coming from a link explicitly followed by  
the user (for example by clicking on it).  
  
@param aURI  
       URI of the page to be marked.  
  

### canAddURI ###
  
Returns true if this URI would be added to the history. You don't have to  
worry about calling this, adding a visit will always check before  
actually adding the page. This function is public because some components  
may want to check if this page would go in the history (i.e. for  
annotations).  
  

### getNewQuery ###
  
This returns a new query object that you can pass to executeQuer[y/ies].  
It will be initialized to all empty (so using it will give you all history).  
  

### getNewQueryOptions ###
  
This returns a new options object that you can pass to executeQuer[y/ies]  
after setting the desired options.  
  

### executeQuery ###
  
Executes a single query.  
  

### executeQueries ###
  
Executes an array of queries. All of the query objects are ORed  
together. Within a query, all the terms are ANDed together as in  
executeQuery. See executeQuery()  
  

### queryStringToQueries ###
  
Converts a query URI-like string to an array of actual query objects for  
use to executeQueries(). The output query array may be empty if there is  
no information. However, there will always be an options structure returned  
(if nothing is defined, it will just have the default values).  
  

### queriesToQueryString ###
  
Converts a query into an equivalent string that can be persisted. Inverse  
of queryStringToQueries()  
  

### addObserver ###
  
Adds a history observer. If ownsWeak is false, the history service will  
keep an owning reference to the observer.  If ownsWeak is true, then  
aObserver must implement nsISupportsWeakReference, and the history service  
will keep a weak reference to the observer.  
  

### removeObserver ###
  
Removes a history observer.  
  

### runInBatchMode ###
  
Runs the passed callback in batch mode. Use this when a lot of things  
are about to change. Calls can be nested, observers will only be  
notified when all batches begin/end.  
  
@param aCallback  
       nsINavHistoryBatchCallback interface to call.  
@param aUserData  
       Opaque parameter passed to nsINavBookmarksBatchCallback  
  

### clearEmbedVisits ###
  
Clear all TRANSITION_EMBED visits.  
  

## Attributes ##

### databaseStatus ###
  
Returns the current database status  
  

### hasHistoryEntries ###
  
True if there is any history. This can be used in UI to determine whether  
the "clear history" button should be enabled or not. This is much better  
than using BrowserHistory.count since that can be very slow if there is  
a lot of history (it must enumerate each item). This is pretty fast.  
  

### historyDisabled ###
   
True if history is disabled. currently,   
history is disabled if the places.history.enabled pref is false.  
  

## Constants ##

### TRANSITION_LINK ###
  
System Notifications:  
  
places-init-complete - Sent once the History service is completely  
                       initialized successfully.  
places-database-locked - Sent if initialization of the History service  
                         failed due to the inability to open the places.sqlite  
                         for access reasons.  
  
  
This transition type means the user followed a link and got a new toplevel  
window.  
  

### TRANSITION_TYPED ###
  
This transition type means that the user typed the page's URL in the  
URL bar or selected it from URL bar autocomplete results, clicked on  
it from a history query (from the History sidebar, History menu,   
or history query in the personal toolbar or Places organizer.  
  

### TRANSITION_BOOKMARK ###
  
This transition is set when the user followed a bookmark to get to the  
page.  
  

### TRANSITION_EMBED ###
  
This transition type is set when some inner content is loaded. This is  
true of all images on a page, and the contents of the iframe. It is also  
true of any content in a frame if the user did not explicitly follow  
a link to get there.  
  

### TRANSITION_REDIRECT_PERMANENT ###
  
Set when the transition was a permanent redirect.  
  

### TRANSITION_REDIRECT_TEMPORARY ###
  
Set when the transition was a temporary redirect.  
  

### TRANSITION_DOWNLOAD ###
  
Set when the transition is a download.  
  

### TRANSITION_FRAMED_LINK ###
  
This transition type means the user followed a link and got a visit in  
a frame.  
  

### DATABASE_STATUS_OK ###
  
Set when database is coherent  
  

### DATABASE_STATUS_CREATE ###
  
Set when database did not exist and we created a new one  
  

### DATABASE_STATUS_CORRUPT ###
  
Set when database was corrupt and we replaced it  
  

### DATABASE_STATUS_UPGRADED ###
  
Set when database schema has been upgraded  
  
