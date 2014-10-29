---
layout: default
---

# nsIStandaloneNativeMenu #

Platform-independent interface to platform native menu objects.


## init ##

Initialize the native menu using given XUL DOM element.

@param aDOMElement A XUL DOM element of tag type |menu| or |menupopup|.


## menuWillOpen ##

This method must be called before the menu is opened and displayed to the
user. It allows the platform code to update the menu and also determine
whether the menu should even be shown.

@return true if the menu can be shown, false if it should not be shown


## nativeMenu ##

The native object representing the XUL menu that was passed to Init(). On
Mac OS X, this will be a NSMenu pointer, which will be retained and
autoreleased when the attribute is retrieved.


## activateNativeMenuItemAt ##

Activate the native menu item specified by |anIndexString|. This method
is intended to be used by the test suite.

@param anIndexString string containing a list of indices separated by
       pipe ('|') characters


## forceUpdateNativeMenuAt ##

Force an update of the native menu item specified by |anIndexString|. This
method is intended to be used by the test suite.

@param anIndexString string containing a list of indices separated by
       pipe ('|') characters

