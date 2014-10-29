---
layout: default
---

# nsIUpdateProcessor #

An interface describing a component which handles the job of processing
an update after it's been downloaded.


## processUpdate ##

Processes the update which has been downloaded.
This happens without restarting the application.
On Windows, this can also be used for switching to an applied
update request.
@param update The update being applied, or null if this is a switch
              to updated application request.  Must be non-null on GONK.

