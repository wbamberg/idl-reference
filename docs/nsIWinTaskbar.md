---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsIWinTaskbar.idl">Source file</a>
</div>

# nsIWinTaskbar #

## Methods ##

### createTaskbarTabPreview(shell, controller) ###
<code>  
Taskbar window and tab preview management  
  
</code><code>  
Creates a taskbar preview. The docshell should be a toplevel docshell and  
is used to find the toplevel window. See the documentation for  
nsITaskbarTabPreview for more information.  
  
</code>
### getTaskbarWindowPreview(shell) ###
<code>  
Gets the taskbar preview for a window. The docshell is used to find the  
toplevel window. See the documentation for nsITaskbarTabPreview for more  
information.  
  
Note: to implement custom drawing or buttons, a controller is required.  
  
</code>
### getTaskbarProgress(shell) ###
<code>  
Taskbar icon progress indicator  
  
</code><code>  
Gets the taskbar progress for a window. The docshell is used to find the  
toplevel window. See the documentation for nsITaskbarProgress for more  
information.  
  
</code>
### getOverlayIconController(shell) ###
<code>  
Taskbar icon overlay  
  
</code><code>  
Gets the taskbar icon overlay controller for a window. The docshell is used  
to find the toplevel window. See the documentation in  
nsITaskbarOverlayIconController for more details.  
  
</code>
### createJumpListBuilder() ###
<code>  
Taskbar and start menu jump list management  
  
</code><code>  
Retrieve a taskbar jump list builder  
  
Fails if a jump list build operation has already been initiated, developers  
should make use of a single instance of nsIJumpListBuilder for building lists  
within an application.  
  
@throw NS_ERROR_ALREADY_INITIALIZED if an nsIJumpListBuilder instance is  
currently building a list.  
  
</code>
### setGroupIdForWindow(aParent, aIdentifier) ###
<code>  
Application window taskbar group settings  
  
</code><code>  
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
  
</code>
### prepareFullScreen(aWindow, aFullScreen) ###
<code>  
Notify the taskbar that a window is about to enter full screen mode.  
  
A Windows autohide taskbar will not behave correctly in all cases if  
it is not notified when full screen operations start and end.  
  
@throw NS_ERROR_INVALID_ARG if the window is not a valid top level window  
@throw NS_ERROR_UNEXPECTED for general failures.  
@throw NS_ERROR_NOT_AVAILABLE if the taskbar cannot be obtained.  
  
</code>
### prepareFullScreenHWND(aWindow, aFullScreen) ###
<code>  
Notify the taskbar that a window identified by its HWND is about to enter  
full screen mode.  
  
A Windows autohide taskbar will not behave correctly in all cases if  
it is not notified when full screen operations start and end.  
  
@throw NS_ERROR_INVALID_ARG if the window is not a valid top level window  
@throw NS_ERROR_UNEXPECTED for general failures.  
@throw NS_ERROR_NOT_AVAILABLE if the taskbar cannot be obtained.  
  
</code>
## Attributes ##

### available ###
  
Returns true if the operating system supports Win7+ taskbar features.  
This property acts as a replacement for in-place os version checking.  
  

### defaultGroupId ###
  
Returns the default application user model identity the application  
registers with the system. This id is used by the taskbar in grouping  
windows and in associating pinned shortcuts with running instances and  
jump lists.  
  
