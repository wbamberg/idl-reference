---
layout: default
---

# nsILoadContext #

An nsILoadContext represents the context of a load.  This interface
can be queried for various information about where the load is
happening.


## associatedWindow ##

associatedWindow is the window with which the load is associated, if any.
Note that the load may be triggered by a document which is different from
the document in associatedWindow, and in fact the source of the load need
not be same-origin with the document in associatedWindow.  This attribute
may be null if there is no associated window.


## topWindow ##

topWindow is the top window which is of same type as associatedWindow.
This is equivalent to associatedWindow.top, but is provided here as a
convenience.  All the same caveats as associatedWindow of apply, of
course.  This attribute may be null if there is no associated window.


## topFrameElement ##

topFrameElement is the <iframe> or <frame> element which contains the
topWindow with which the load is associated.

Note that we may have a topFrameElement even when we don't have an
associatedWindow, if the topFrameElement's content lives out of process.


## nestedFrameId ##

If this LoadContext corresponds to a nested remote iframe, we don't have
access to the topFrameElement.  Instead, we must use this id to send
messages. A return value of 0 signifies that this load context is not for
a nested frame.


## isAppOfType ##

Check whether the load is happening in a particular type of application.

@param an application type.  For now, the constants to be passed here are
       the nsIDocShell APP_TYPE_* constants.

@return whether there is some ancestor of the associatedWindow that is of
        the given app type.


## isContent ##

True if the load context is content (as opposed to chrome).  This is
determined based on the type of window the load is performed in, NOT based
on any URIs that might be around.


## usePrivateBrowsing ##

## useRemoteTabs ##

Attribute that determines if remote (out-of-process) tabs should be used.


## SetPrivateBrowsing ##

Set the private browsing state of the load context, meant to be used internally.


## SetRemoteTabs ##

Set the remote tabs state of the load context, meant to be used internally.


## isInBrowserElement ##

Returns true iff the load is occurring inside a browser element.


## appId ##

Returns the app id of the app the load is occurring is in. Returns
nsIScriptSecurityManager::NO_APP_ID if the load is not part of an app.

