---
layout: default
---

# nsIXULWindow #

## docShell ##

The docshell owning the XUL for this window.


## intrinsicallySized ##

Indicates if this window is instrinsically sized.	


## primaryContentShell ##

The primary content shell.  

Note that this is a docshell tree item and therefore can not be assured of
what object it is. It could be an editor, a docshell, or a browser object.
Or down the road any other object that supports being a DocShellTreeItem
Query accordingly to determine the capabilities.


## getContentShellById ##

The content shell specified by the supplied id.

Note that this is a docshell tree item and therefore can not be assured of
what object it is.  It could be an editor, a docshell, or a browser object.
Or down the road any other object that supports being a DocShellTreeItem
Query accordingly to determine the capabilities.


## addChildWindow ##

Tell this window that it has picked up a child XUL window
@param aChild the child window being added


## removeChildWindow ##

Tell this window that it has lost a child XUL window
@param aChild the child window being removed


## center ##

Move the window to a centered position.
@param aRelative If not null, the window relative to which the window is
                 moved. See aScreen parameter for details.
@param aScreen   PR_TRUE to center the window relative to the screen
                 containing aRelative if aRelative is not null. If
                 aRelative is null then relative to the screen of the
                 opener window if it was initialized by passing it to
                 nsWebShellWindow::Initialize. Failing that relative to
                 the main screen.
                 PR_FALSE to center it relative to aRelative itself.
@param aAlert    PR_TRUE to move the window to an alert position,
                 generally centered horizontally and 1/3 down from the top.


## showModal ##

Shows the window as a modal window. That is, ensures that it is visible
and runs a local event loop, exiting only once the window has been closed.


## lowestZ ##

## loweredZ ##

## normalZ ##

## raisedZ ##

## highestZ ##

## zLevel ##

## contextFlags ##

contextFlags are from nsIWindowCreator2


## chromeFlags ##

## assumeChromeFlagsAreFrozen ##

Begin assuming |chromeFlags| don't change hereafter, and assert
if they do change.  The state change is one-way and idempotent.


## createNewWindow ##

Create a new window.
@param aChromeFlags see nsIWebBrowserChrome
@param aOpeningTab the TabParent that requested this new window be opened.
                   Can be left null.
@return the newly minted window


## XULBrowserWindow ##

## applyChromeFlags ##

Back-door method to force application of chrome flags at a particular
time.  Do NOT call this unless you know what you're doing!  In particular,
calling this when this XUL window doesn't yet have a document in its
docshell could cause problems.

