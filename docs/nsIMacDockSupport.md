---
layout: default
---

# nsIMacDockSupport #

Allow applications to interface with the Mac OS X Dock.

Applications may indicate progress on their Dock icon. Only one such
progress indicator is available to the entire application.


## Methods ##

### activateApplication ###

Activate the application. This should be used by an application to
activate itself when a dock menu is selected as selection of a dock menu
item does not automatically activate the application.

@param aIgnoreOtherApplications If false, the application is activated
       only if no other application is currently active. If true, the
       application activates regardless. 


## Attributes ##

### dockMenu ###

Menu to use for application-specific dock menu items.


### badgeText ###

Text used to badge the dock tile.

