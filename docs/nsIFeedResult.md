---
layout: default
---

# nsIFeedResult #

The nsIFeedResult interface provides access to HTTP and parsing
metadata for a feed or entry.


## bozo ##
 
The Feed parser will set the bozo bit when a feed triggers a fatal
error during XML parsing. There may be entries and feed metadata
that were parsed before the error.  Thanks to Tim Bray for
suggesting this terminology.
<http://www.tbray.org/ongoing/When/200x/2004/01/11/PostelPilgrim>


## doc ##

The parsed feed or entry. 

Will be null if a non-feed is processed.


## uri ##
 
The address from which the feed was fetched. 


## version ##
 
Feed Version: 
atom, rss2, rss09, rss091, rss091userland, rss092, rss1, atom03, 
atomEntry, rssItem

Will be null if a non-feed is processed.


## stylesheet ##

An XSLT stylesheet available to transform the source of the
feed. Some feeds include this information in a processing
instruction. It's generally intended for clients with specific
feed capabilities.


## headers ##

HTTP response headers that accompanied the feed. 


## registerExtensionPrefix ##

Registers a prefix used to access an extension in the feed/entry 

