---
layout: default
---

# fuelIBrowserTab #

Interface representing a browser tab.


## Methods ##

### load ###

Load a new URI into this browser tab.
@param   aURI
         The uri to load into the browser tab


### focus ###

Give focus to this browser tab, and bring it to the front.


### close ###

Close the browser tab. This may not actually close the tab
as script may abort the close operation.


### moveBefore ###

Moves this browser tab before another browser tab within the window.
@param   aBefore
         The tab before which the target tab will be moved


### moveToEnd ###

Move this browser tab to the last tab within the window.


## Attributes ##

### uri ###

The current uri of this tab.


### index ###

The current index of this tab in the browser window.


### window ###

The browser window that is holding the tab.


### document ###

The content document of the browser tab.


### events ###

The events object for the browser tab.
supports: "load"

