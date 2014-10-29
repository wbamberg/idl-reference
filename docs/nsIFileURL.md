---
layout: default
---

# nsIFileURL #

nsIFileURL provides access to the underlying nsIFile object corresponding to
an URL.  The URL scheme need not be file:, since other local protocols may
map URLs to files (e.g., resource:).


## Attributes ##

### file ###

Get/Set nsIFile corresponding to this URL.

 - Getter returns a reference to an immutable object.  Callers must clone
   before attempting to modify the returned nsIFile object.  NOTE: this
   constraint might not be enforced at runtime, so beware!!

 - Setter clones the nsIFile object (allowing the caller to safely modify
   the nsIFile object after setting it on this interface).

