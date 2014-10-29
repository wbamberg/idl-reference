---
layout: default
---

# fuelIBookmark #

Interface representing a bookmark item.


## id ##

The id of the bookmark.


## title ##

The title of the bookmark.


## uri ##

The uri of the bookmark.


## description ##

The description of the bookmark.


## keyword ##

The keyword associated with the bookmark.


## type ##

The type of the bookmark.
values: "bookmark", "separator"


## parent ##

The parent folder of the bookmark.


## annotations ##

The annotations object for the bookmark.


## events ##

The events object for the bookmark.
supports: "remove", "change", "visit", "move"


## remove ##

Removes the item from the parent folder. Used to
delete a bookmark or separator

