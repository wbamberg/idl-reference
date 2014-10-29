---
layout: default
---

# nsIErrorService #

nsIErrorService: This is an interim service that allows nsresult codes to be mapped to 
string bundles that can be used to look up error messages. String bundle keys can also
be mapped. 

This service will eventually get replaced by extending xpidl to allow errors to be defined.
(http://bugzilla.mozilla.org/show_bug.cgi?id=13423).


## Methods ##

### registerErrorStringBundle ###

Registers a string bundle URL for an error module. Error modules are obtained from
nsresult code with NS_ERROR_GET_MODULE.


### unregisterErrorStringBundle ###

Unregisters a string bundle URL for an error module.


### getErrorStringBundle ###

Retrieves a string bundle URL for an error module.

