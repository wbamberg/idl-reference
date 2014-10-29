---
layout: default
---

# nsIFeedProcessor #

An nsIFeedProcessor parses feeds, triggering callbacks based on
their contents.


## listener ##

The listener that will respond to feed events. 


## parseFromStream ##

Parse a feed from an nsIInputStream.

@param stream The input stream.
@param uri The base URI.


## parseFromString ##

Parse a feed from a string.

@param str The string to parse.
@param uri The base URI.


## parseAsync ##

Parse a feed asynchronously. The caller must then call the
nsIFeedProcessor's nsIStreamListener methods to drive the
parse. Do not call the other parse methods during an asynchronous
parse.

@param requestObserver The observer to notify on start/stop. This
                       argument can be null.
@param uri The base URI.

