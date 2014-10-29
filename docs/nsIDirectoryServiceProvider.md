---
layout: default
---

# nsIDirectoryServiceProvider #

nsIDirectoryServiceProvider

Used by Directory Service to get file locations.


## Methods ##

### getFile ###

getFile

Directory Service calls this when it gets the first request for
a prop or on every request if the prop is not persistent.

@param prop         The symbolic name of the file.
@param persistent   TRUE - The returned file will be cached by Directory
                    Service. Subsequent requests for this prop will
                    bypass the provider and use the cache.
                    FALSE - The provider will be asked for this prop
                    each time it is requested.

@return             The file represented by the property.


