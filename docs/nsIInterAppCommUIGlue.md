---
layout: default
---

# nsIInterAppCommUIGlue #

To be implemented by @mozilla.org/dom/apps/inter-app-comm-ui-glue;1


## selectApps ##

This method is to notify the prompt to let the user select some of the
IAC-eligible apps.

@param callerID           The generated UUID to identify the caller and
                          should be unique for each call.
@param pubAppManifestURL  The manifest URL of the publisher.
@param keyword            The IAC keyword.
@param appsToSelect       The IAC-eligible apps for selection.

Returns a promise.

