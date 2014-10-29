---
layout: default
---

# nsIWebContentHandlerInfo #

## Methods ##

### getHandlerURI ###
 
Gets the service URL Spec, with the loading document URI encoded in it.
@param   uri
         The URI of the document being loaded
@returns The URI of the service with the loading document URI encoded in 
         it.


## Attributes ##

### contentType ###

The content type handled by the handler


### uri ###

The uri of the handler, with an embedded %s where the URI of the loaded
document will be encoded.

