---
layout: default
---

# nsIApplicationReputationService #

## Methods ##

### queryReputation ###

Start querying the application reputation service.

@param aQuery
       The nsIApplicationReputationQuery containing metadata of the
       downloaded file.

@param aCallback
       The callback for receiving the results of the query.

@remarks aCallback may not be null.  onComplete is guaranteed to be called
         on aCallback. This function may not be called more than once with
         the same query object. If any of the attributes of aQuery have
         not been set or have been set with empty data (with the exception
         of sourceURI), then a valid request can still be constructed and
         will solicit a valid response, but won't produce any useful
         information.

