---
layout: default
---

# mozIVisitInfo #

## Attributes ##

### visitId ###

The machine-local (internal) id of the visit.


### visitDate ###

The time the visit occurred.


### transitionType ###

The transition type used to get to this visit.  One of the TRANSITION_TYPE
constants on nsINavHistory.

@see nsINavHistory.idl


### referrerURI ###

The referring URI of this visit.  This may be null.

