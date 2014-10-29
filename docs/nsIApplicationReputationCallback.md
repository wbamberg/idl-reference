---
layout: default
---

# nsIApplicationReputationCallback #

## onComplete ##

Callback for the result of the application reputation query.
@param aStatus
       NS_OK if and only if the query succeeded. If it did, then
       shouldBlock is meaningful (otherwise it defaults to false). This
       may be NS_ERROR_FAILURE if the response cannot be parsed, or
       NS_ERROR_NOT_AVAILABLE if the service has been disabled or is not
       reachable.
@param aShouldBlock
       Whether or not the download should be blocked.

