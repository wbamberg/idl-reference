---
layout: default
---

# nsIContentPrefCallback2 #

The callback used by the above methods.


## Methods ##

### handleResult ###

For the retrieval methods, this is called once for each retrieved
preference.  It is not called for other methods.

@param pref  The retrieved preference.


### handleError ###

Called when an error occurs.  This may be called multiple times before
handleCompletion is called.

@param error  A number in Components.results describing the error.


### handleCompletion ###

Called when the method finishes.  This will be called exactly once for
each method invocation, and afterward no other callback methods will be
called.

@param reason  One of the COMPLETE_* values indicating the manner in which
               the method completed.


## Constants ##

### COMPLETE_OK ###

### COMPLETE_ERROR ###
