---
layout: default
---

# nsIJumpListShortcut #

A generic application shortcut with command line support.


## app ##

Set or get the handler app for this shortcut item.

The handler app may also be used along with iconIndex to generate an icon
for the jump list item.

@throw NS_ERROR_FILE_NOT_FOUND if the handler app can
not be found on  the system.

@see faviconPageUri


## iconIndex ##

Set or get the icon displayed with the jump list item.

Indicates the resource index of the icon contained within the handler
executable which may be used as the jump list icon.

@see faviconPageUri


## faviconPageUri ##

Set or get the URI of a page whose favicon may be used as the icon.

When a jump list build occurs, the favicon to be used for the item is
obtained using the following steps:
- First, attempt to use the asynchronously retrieved and scaled favicon
associated with the faviconPageUri.
- If faviconPageUri is null, or if retrieving the favicon fails, fall
back to using the handler executable and iconIndex.  

