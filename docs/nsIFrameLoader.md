---
layout: default
---

# nsIFrameLoader #

## Methods ##

### loadFrame ###

Start loading the frame. This method figures out what to load
from the owner content in the frame loader.


### loadURI ###

Loads the specified URI in this frame. Behaves identically to loadFrame,
except that this method allows specifying the URI to load.


### destroy ###

Destroy the frame loader and everything inside it. This will
clear the weak owner content reference.


### updatePositionAndSize ###

Updates the position and size of the subdocument loaded by this frameloader.

 @param aIFrame The nsIFrame for the content node that owns this frameloader


### activateRemoteFrame ###

Activate remote frame.
Throws an exception with non-remote frames.


### deactivateRemoteFrame ###

Deactivate remote frame.
Throws an exception with non-remote frames.


### sendCrossProcessMouseEvent ###

@see nsIDOMWindowUtils sendMouseEvent.


### activateFrameEvent ###

Activate event forwarding from client (remote frame) to parent.


### sendCrossProcessKeyEvent ###

@see nsIDOMWindowUtils sendKeyEvent.


### requestNotifyAfterRemotePaint ###

Request that the next time a remote layer transaction has been
received by the Compositor, a MozAfterRemoteFrame event be sent
to the window.


## Attributes ##

### docShell ###

Get the docshell from the frame loader.


### tabParent ###

Get this frame loader's TabParent, if it has a remote frame.  Otherwise,
returns null.


### loadContext ###

Get an nsILoadContext for the top-level docshell. For remote
frames, a shim is returned that contains private browsing and app
information.


### depthTooGreat ###

Find out whether the loader's frame is at too great a depth in
the frame tree.  This can be used to decide what operations may
or may not be allowed on the loader's docshell.


### messageManager ###

### eventMode ###

### clipSubdocument ###

If false, then the subdocument is not clipped to its CSS viewport, and the
subdocument's viewport scrollbar(s) are not rendered.
Defaults to true.


### clampScrollPosition ###

If false, then the subdocument's scroll coordinates will not be clamped
to their scroll boundaries.
Defaults to true.


### ownerElement ###

The element which owns this frame loader.

For example, if this is a frame loader for an <iframe>, this attribute
returns the iframe element.


### childID ###

Cached childID of the ContentParent owning the TabParent in this frame
loader. This can be used to obtain the childID after the TabParent died.


### visible ###

Get or set this frame loader's visibility.

The notion of "visibility" here is separate from the notion of a
window/docshell's visibility.  This field is mostly here so that we can
have a notion of visibility in the parent process when frames are OOP.


### ownerIsBrowserOrAppFrame ###

Find out whether the owner content really is a browser or app frame
Especially, a widget frame is regarded as an app frame.


### ownerIsWidget ###

Find out whether the owner content really is a widget. If this attribute
returns true, |ownerIsBrowserOrAppFrame| must return true.


## Constants ##

### EVENT_MODE_NORMAL_DISPATCH ###

The default event mode automatically forwards the events
handled in EventStateManager::HandleCrossProcessEvent to
the child content process when these events are targeted to
the remote browser element.

Used primarly for input events (mouse, keyboard)


### EVENT_MODE_DONT_FORWARD_TO_CHILD ###

With this event mode, it's the application's responsability to 
convert and forward events to the content process

