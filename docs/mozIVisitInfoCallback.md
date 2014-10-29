---
layout: default
---

# mozIVisitInfoCallback #

Shared Callback interface for mozIAsyncHistory methods. The semantics
for each method are detailed in mozIAsyncHistory.


## handleError ##

Called when the given place could not be processed.

@param aResultCode
       nsresult indicating the failure reason.
@param aPlaceInfo
       The information that was given to the caller for the place.


## handleResult ##

Called for each place processed successfully.

@param aPlaceInfo
       The current info stored for the place.


## handleCompletion ##

Called when all records were processed.

