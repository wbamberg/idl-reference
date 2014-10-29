---
layout: default
---

# nsIRefreshURI #

## Methods ##

### refreshURI ###

Load a uri after waiting for aMillis milliseconds. If the docshell
is busy loading a page currently, the refresh request will be
queued and executed when the current load finishes. 

@param aUri The uri to refresh.
@param aMillis The number of milliseconds to wait.
@param aRepeat Flag to indicate if the uri is to be 
               repeatedly refreshed every aMillis milliseconds.
@param aMetaRefresh Flag to indicate if this is a Meta refresh.


### forceRefreshURI ###

Loads a URI immediately as if it were a refresh.

@param aURI The URI to refresh.
@param aMillis The number of milliseconds by which this refresh would
               be delayed if it were not being forced.
@param aMetaRefresh Flag to indicate if this is a meta refresh.


### setupRefreshURI ###

Checks the passed in channel to see if there is a refresh header, 
if there is, will setup a timer to refresh the uri found
in the header. If docshell is busy loading a page currently, the
request will be queued and executed when the current page 
finishes loading. 

Returns the NS_REFRESHURI_HEADER_FOUND success code if a refresh
header was found and successfully setup.

@param aChannel The channel to be parsed. 


### setupRefreshURIFromHeader ###

Parses the passed in header string and sets up a refreshURI if
a "refresh" header is found. If docshell is busy loading a page 
currently, the request will be queued and executed when 
the current page finishes loading. 

@param aBaseURI base URI to resolve refresh uri with.
@param principal the associated principal
@param aHeader  The meta refresh header string.


### cancelRefreshURITimers ###

Cancels all timer loads.


## Attributes ##

### refreshPending ###

True when there are pending refreshes, false otherwise.

