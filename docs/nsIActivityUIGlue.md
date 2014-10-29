---
layout: default
---

# nsIActivityUIGlue #

To be implemented by @mozilla.org/dom/activities/ui-glue;1


## Methods ##

### chooseActivity ###

This method is called even if the size of {@code activities} is 0 so that the callee can
decide whether or not to defer the request to an alternate activity system.

@param options     The ActivityOptions object in the form of { name: "send", data: { ... } }
@param activities  A json blob which is an array of { "title":"...", "icon":"..." }.
@param callback    The callback to send the index of the choosen activity, or the result.

