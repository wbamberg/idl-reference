---
layout: default
---

# nsIWindowMediator #

## getEnumerator ##
 Return an enumerator which iterates over all windows of type aWindowType
from the oldest window to the youngest.
@param  aWindowType the returned enumerator will enumerate only
                    windows of this type. ("type" is the
                    |windowtype| attribute of the XML <window> element.)
                    If null, all windows will be enumerated.
@return an enumerator of nsIDOMWindows.  Note that windows close
        asynchronously in many cases, so windows returned from this
        enumerator can have .closed set to true.  Caveat enumerator!


## getXULWindowEnumerator ##
 Identical to getEnumerator except:
@return an enumerator of nsIXULWindows


## getZOrderDOMWindowEnumerator ##
 Return an enumerator which iterates over all windows of type aWindowType
in their z (front-to-back) order. Note this interface makes
no requirement that a window couldn't be revisited if windows
are re-ordered while z-order enumerators are active.
@param  aWindowType the returned enumerator will enumerate only
                    windows of this type. ("type" is the
                    |windowtype| attribute of the XML <window> element.)
                    If null, all windows will be enumerated.
@param  aFrontToBack if true, the enumerator enumerates windows in order
                     from front to back. back to front if false.
@return an enumerator of nsIDOMWindows


## getZOrderXULWindowEnumerator ##
 Identical to getZOrderDOMWindowEnumerator except:
@return an enumerator of nsIXULWindows


## getMostRecentWindow ##
 This is a shortcut for simply fetching the first window in
front to back order.
@param  aWindowType return the topmost window of this type.
                    ("type" is the |windowtype| attribute of
                    the XML <window> element.)
                    If null, return the topmost window of any type.
@return the topmost window


## getOuterWindowWithId ##

Return the outer window with the given ID, if any.  Can return null.


## getCurrentInnerWindowWithId ##

Return the outer window with the given current window ID, if any.
Can return null if no inner window with the ID exists or if it's not
a current inner anymore.


## registerWindow ##
 Add the window to the list of known windows. Listeners (see
addListener) will be notified through their onOpenWindow method.
@param aWindow the window to add


## unregisterWindow ##
 Remove the window from the list of known windows. Listeners (see
addListener) will be be notified through their onCloseWindow method.
@param aWindow the window to remove


## updateWindowTimeStamp ##
 Call this method when a window gains focus. It's a primitive means of
determining the most recent window. It's no longer necessary and it
really should be removed.
@param aWindow the window which has gained focus


## updateWindowTitle ##
 Call this method when a window's title changes. Listeners (see
addListener) will be notified through their onWindowTitleChange method.
@param aWindow the window whose title has changed
@param inTitle the window's new title


## zLevelTop ##

## zLevelBottom ##

## zLevelBelow ##

## calculateZPosition ##
 A window wants to be moved in z-order. Calculate whether and how
it should be constrained. Note this method is advisory only:
it changes nothing either in WindowMediator's internal state
or with the window.
Note it compares the nsIXULWindow to nsIWidgets. A pure interface
would use all nsIXULWindows. But we expect this to be called from
callbacks originating in native window code. They are expected to
hand us comparison values which are pulled from general storage
in the native widget, and may not correspond to an nsIWidget at all.
For that reason this interface requires only objects one step
removed from the native window (nsIWidgets), and its implementation
must be very understanding of what may be completely invalid
pointers in those parameters.

@param inWindow the window in question
@param inPosition requested position
                  values: zLevelTop: topmost window. zLevelBottom: bottom.
                  zLevelBelow: below ioBelow. (the value of ioBelow will
                  be ignored for zLevelTop and Bottom.)
@param inBelow if inPosition==zLevelBelow, the window
                below which inWindow wants to be placed. Otherwise this
                variable is ignored.
@param outPosition constrained position, values like inPosition.
@param outBelow if outPosition==zLevelBelow, the window
                below which inWindow should be placed. Otherwise this
                this value will be null.
@return PR_TRUE if the position returned is different from
        the position given.


## setZPosition ##
 A window has been positioned behind another. Inform WindowMediator
@param inWindow the window in question
@param inPosition new position. values:
                  zLevelTop: topmost window.
                  zLevelBottom: bottom.
                  zLevelBelow: below inBelow. (inBelow is ignored
                               for other values of inPosition.)
@param inBelow the window inWindow is behind, if zLevelBelow


## getZLevel ##
 Return the window's Z level (as defined in nsIXULWindow).
@param aWindow the window in question
@return aWindow's z level


## setZLevel ##
 Set the window's Z level (as defined in nsIXULWindow). The implementation
will reposition the window as necessary to match its new Z level.
The implementation will assume a window's Z level to be
nsIXULWindow::normalZ until it has been informed of a different level.
@param aWindow the window in question
@param aZLevel the window's new Z level


## addListener ##
 Register a listener for window status changes.
keeps strong ref? (to be decided)
@param aListener the listener to register


## removeListener ##
 Unregister a listener of window status changes.
@param aListener the listener to unregister

