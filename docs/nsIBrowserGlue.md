---
layout: default
---

# nsIBrowserGlue #

nsIBrowserGlue is a dirty and rather fluid interface to host shared utility 
methods used by browser UI code, but which are not local to a browser window.
The component implementing this interface is meant to be a singleton
(service) and should progressively replace some of the shared "glue" code 
scattered in browser/base/content (e.g. bits of utilOverlay.js, 
contentAreaUtils.js, globalOverlay.js, browser.js), avoiding dynamic 
inclusion and initialization of a ton of JS code for *each* window.
Dued to its nature and origin, this interface won't probably be the most
elegant or stable in the mozilla codebase, but its aim is rather pragmatic:
1) reducing the performance overhead which affects browser window load;
2) allow global hooks (e.g. startup and shutdown observers) which survive
browser windows to accomplish browser-related activities, such as shutdown
sanitization (see bug #284086)



## sanitize ##
 
Deletes privacy sensitive data according to user preferences

@param aParentWindow an optionally null window which is the parent of the 
       sanitization dialog



## ensurePlacesDefaultQueriesInitialized ##

Add Smart Bookmarks special queries to bookmarks menu and toolbar folder.


## getMostRecentBrowserWindow ##

Gets the most recent window that's a browser (but not a popup)

