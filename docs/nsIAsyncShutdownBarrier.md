---
layout: default
---

# nsIAsyncShutdownBarrier #

A stage of shutdown that supports blocker registration.


## client ##

The blocker registration capability.  Most services may wish to
publish this capability to let services that depend on it register
blockers.


## state ##

The state of all the blockers of the barrier.

See the documentation of `nsIAsyncShutdownBlocker` for the
format.


## wait ##

Wait for all blockers to complete.

Method `aOnReady` will be called once all blockers have finished.
The callback always receives NS_OK.

