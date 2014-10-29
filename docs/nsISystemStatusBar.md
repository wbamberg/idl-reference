---
layout: default
---

# nsISystemStatusBar #

Allow applications to interface with the Mac OS X system status bar.


## Methods ##

### addItem ###

Add an item to the system status bar. Each item can only be present once,
subsequent addItem calls with the same element will be ignored.
The system status bar holds a strong reference to the added XUL menu
element and the item will stay in the status bar until it is removed via
a call to removeItem, or until the process shuts down.
@param aDOMMenuElement A XUL menu element that contains a XUL menupopup
                       with regular menu content. The menu's icon is put
                       into the system status bar; clicking it will open
                       a menu with the contents of the menupopup.
                       The menu label is not shown.


### removeItem ###

Remove a previously-added item from the menu bar. Calling this with an
element that has not been added before will be silently ignored.
@param aDOMMenuElement The XUL menu element that you called addItem with.

