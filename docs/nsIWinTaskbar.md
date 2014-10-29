---
layout: default
---

# nsIWinTaskbar #

## Methods ##

### createTaskbarTabPreview ###

Taskbar window and tab preview management


Creates a taskbar preview. The docshell should be a toplevel docshell and
is used to find the toplevel window. See the documentation for
nsITaskbarTabPreview for more information.


### getTaskbarWindowPreview ###

Gets the taskbar preview for a window. The docshell is used to find the
toplevel window. See the documentation for nsITaskbarTabPreview for more
information.

Note: to implement custom drawing or buttons, a controller is required.


### getTaskbarProgress ###

Taskbar icon progress indicator


Gets the taskbar progress for a window. The docshell is used to find the
toplevel window. See the documentation for nsITaskbarProgress for more
information.


### getOverlayIconController ###

Taskbar icon overlay


Gets the taskbar icon overlay controller for a window. The docshell is used
to find the toplevel window. See the documentation in
nsITaskbarOverlayIconController for more details.


### createJumpListBuilder ###

Taskbar and start menu jump list management


Retrieve a taskbar jump list builder

Fails if a jump list build operation has already been initiated, developers
should make use of a single instance of nsIJumpListBuilder for building lists
within an application.

@throw NS_ERROR_ALREADY_INITIALIZED if an nsIJumpListBuilder instance is
currently building a list.


### setGroupIdForWindow ###

Application window taskbar group settings


Set the grouping id for a window.

The runtime sets a default, global grouping id for all windows on startup.
setGroupIdForWindow allows individual windows to be grouped independently
on the taskbar. Ids should be unique to the app and window to insure
conflicts with other pinned applications do no arise.

The default group id is based on application.ini vendor, application, and
version values, with a format of 'vendor.app.version'. The default can be
retrieved via defaultGroupId.

Note, when a window changes taskbar window stacks, it is placed at the
bottom of the new stack.

@throw NS_ERROR_INVALID_ARG if the window is not a valid top level window
associated with a widget.
@throw NS_ERROR_FAILURE if the property on the window could not be set.
@throw NS_ERROR_UNEXPECTED for general failures.


### prepareFullScreen ###

Notify the taskbar that a window is about to enter full screen mode.

A Windows autohide taskbar will not behave correctly in all cases if
it is not notified when full screen operations start and end.

@throw NS_ERROR_INVALID_ARG if the window is not a valid top level window
@throw NS_ERROR_UNEXPECTED for general failures.
@throw NS_ERROR_NOT_AVAILABLE if the taskbar cannot be obtained.


### prepareFullScreenHWND ###

Notify the taskbar that a window identified by its HWND is about to enter
full screen mode.

A Windows autohide taskbar will not behave correctly in all cases if
it is not notified when full screen operations start and end.

@throw NS_ERROR_INVALID_ARG if the window is not a valid top level window
@throw NS_ERROR_UNEXPECTED for general failures.
@throw NS_ERROR_NOT_AVAILABLE if the taskbar cannot be obtained.


## Attributes ##

### available ###

Returns true if the operating system supports Win7+ taskbar features.
This property acts as a replacement for in-place os version checking.


### defaultGroupId ###

Returns the default application user model identity the application
registers with the system. This id is used by the taskbar in grouping
windows and in associating pinned shortcuts with running instances and
jump lists.

