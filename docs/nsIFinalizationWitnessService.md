---
layout: default
---

# nsIFinalizationWitnessService #

## make ##

Create a new Finalization Witness.

A finalization witness is an object whose sole role is to
broadcast when it is garbage-collected. Once the witness is
created, call method its method |forget()| to prevent the
broadcast.

@param aTopic The topic that the witness will broadcast using
              Services.obs.
@param aString The string that the witness will broadcast.
@return An object with a single method |forget()|.

