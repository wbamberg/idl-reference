---
layout: default
---

# nsIUrlClassifierUtils #

## getKeyForURI ##

Get the lookup string for a given URI.  This normalizes the hostname,
url-decodes the string, and strips off the protocol.

@param uri URI to get the lookup key for.

@returns String containing the canonicalized URI.

