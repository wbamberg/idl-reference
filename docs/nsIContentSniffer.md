---
layout: default
---

# nsIContentSniffer #

Content sniffer interface. Components implementing this interface can
determine a MIME type from a chunk of bytes.


## getMIMETypeFromContent ##

Given a chunk of data, determines a MIME type. Information from the given
request may be used in order to make a better decision.

@param aRequest The request where this data came from. May be null.
@param aData Data to check
@param aLength Length of the data

@return The content type

@throw NS_ERROR_NOT_AVAILABLE if no MIME type could be determined.

@note Implementations should consider the request read-only. Especially,
they should not attempt to set the content type property that subclasses of
nsIRequest might offer.

