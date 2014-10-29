---
layout: default
---

# nsIDirectoryServiceProvider2 #

nsIDirectoryServiceProvider2

An extension of nsIDirectoryServiceProvider which allows
multiple files to be returned for the given key.


## getFiles ##

getFiles

Directory Service calls this when it gets a request for
a prop and the requested type is nsISimpleEnumerator.

@param prop         The symbolic name of the file list.

@return             An enumerator for a list of file locations.
                    The elements in the enumeration are nsIFile
@returnCode         NS_SUCCESS_AGGREGATE_RESULT if this result should be
                    aggregated with other "lower" providers.

