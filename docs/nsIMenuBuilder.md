---
layout: default
---

# nsIMenuBuilder #

An interface used to construct native toolbar or context menus from <menu>


## Methods ##

### openContainer ###

Create the top level menu or a submenu. The implementation should create
a new context for this menu, so all subsequent methods will add new items
to this newly created menu.


### addItemFor ###

Add a new menu item. All menu item details can be obtained from
the element. This method is not called for hidden elements or elements
with no or empty label. The icon should be loaded only if aCanLoadIcon
is true.


### addSeparator ###

Create a new separator.


### undoAddSeparator ###

Remove last added separator.
Sometimes it's needed to remove last added separator, otherwise it's not
possible to implement the postprocessing in one pass.
See http://www.whatwg.org/specs/web-apps/current-work/multipage/interactive-elements.html#building-menus-and-toolbars


### closeContainer ###

Set the context to the parent menu.

