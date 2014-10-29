---
layout: default
---

# nsIUrlClassifierLookupCallback #

This is an internal helper interface for communication between the
main thread and the dbservice worker thread.  It is called for each
lookup to provide a set of possible results, which the main thread
may need to expand using an nsIUrlClassifierCompleter.


## lookupComplete ##

The lookup process is complete.

@param results
       If this parameter is null, there were no results found.
       If not, it contains an array of nsUrlClassifierEntry objects
       with possible matches.  The callee is responsible for freeing
       this array.

