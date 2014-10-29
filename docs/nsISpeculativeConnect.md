---
layout: default
---

# nsISpeculativeConnect #

## Methods ##

### speculativeConnect ###

Called as a hint to indicate a new transaction for the URI is likely coming
soon. The implementer may use this information to start a TCP
and/or SSL level handshake for that resource immediately so that it is
ready and/or progressed when the transaction is actually submitted.

No obligation is taken on by the implementer, nor is the submitter obligated
to actually open the new channel. 

@param aURI the URI of the hinted transaction
@param aCallbacks any security callbacks for use with SSL for interfaces
       such as nsIBadCertListener. May be null.


