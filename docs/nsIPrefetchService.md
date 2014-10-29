---
layout: default
---

# nsIPrefetchService #

## Methods ##

### prefetchURI ###

Enqueue a request to prefetch the specified URI.

@param aURI the URI of the document to prefetch
@param aReferrerURI the URI of the referring page
@param aSource the DOM node (such as a <link> tag) that requested this
       fetch, or null if the prefetch was not requested by a DOM node.
@param aExplicit the link element has an explicit prefetch link type


### enumerateQueue ###

Enumerate the items in the prefetch queue.

