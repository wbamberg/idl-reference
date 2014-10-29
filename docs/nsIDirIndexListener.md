---
layout: default
---

# nsIDirIndexListener #

This interface is used to receive contents of directory index listings
from a protocol. They can then be transformed into an output format
(such as rdf, html, etc)


## onIndexAvailable ##

Called for each directory entry

@param request - the request
@param ctxt - opaque parameter
@param index - new index to add


## onInformationAvailable ##

Called for each information line

@param request - the request
@param ctxt - opaque parameter
@param info - new info to add

