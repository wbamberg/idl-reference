---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/base/nsIFocusManager.idl">Source file</a>
</div>

# nsIFocusManager #
  
The focus manager deals with all focus related behaviour. Only one element  
in the entire application may have the focus at a time; this element  
receives any keyboard events. While there is only one application-wide  
focused element, each nsIDOMWindow maintains a reference to the element  
that would be focused if the window was active.  
  
If the window's reference is to a frame element (iframe, browser,  
editor), then the child window contains the element that is currently  
focused. If the window's reference is to a root element, then the root is  
focused. If a window's reference is null, then no element is focused, yet  
the window is still focused.  
  
The blur event is fired on an element when it loses the application focus.  
After this blur event, if the focus is moving away from a document, two  
additional blur events are fired on the old document and window containing  
the focus respectively.  
  
When a new document is focused, two focus events are fired on the new  
document and window respectively. Then the focus event is fired on an  
element when it gains the application focus.  
  
A special case is that the root element may be focused, yet does not  
receive the element focus and blur events. Instead a focus outline may be  
drawn around the document.  
  
Blur and focus events do not bubble as per the W3C DOM Events spec.  
  

## Methods ##

### getLastFocusMethod(window) ###
  
Returns the method that was used to focus the element in window. This  
will either be 0, FLAG_BYMOUSE or FLAG_BYKEY. If window is null, then  
the current focusedWindow will be used by default. This has the result  
of retrieving the method that was used to focus the currently focused  
element.  
  

### setFocus(aElement, aFlags) ###
  
Changes the focused element reference within the window containing  
aElement to aElement.  
  

### moveFocus(aWindow, aStartElement, aType, aFlags) ###
  
Move the focus to another element. If aStartElement is specified, then  
movement is done relative to aStartElement. If aStartElement is null,  
then movement is done relative to the currently focused element. If no  
element is focused, focus the first focusable element within the  
document (or the last focusable element if aType is MOVEFOCUS_END). This  
method is equivalent to setting the focusedElement to the new element.  
  
Specifying aStartElement and using MOVEFOCUS_LAST is not currently  
implemented.  
  
If no element is found, and aType is either MOVEFOCUS_ROOT or  
MOVEFOCUS_CARET, then the focus is cleared. If aType is any other value,  
the focus is not changed.  
  
Returns the element that was focused.  
  

### clearFocus(aWindow) ###
  
Clears the focused element within aWindow. If the current focusedWindow  
is a descendant of aWindow, sets the current focusedWindow to aWindow.  
  
@throws NS_ERROR_INVALID_ARG if aWindow is null  
  

### getFocusedElementForWindow(aWindow, aDeep, aFocusedWindow) ###
  
Returns the currently focused element within aWindow. If aWindow is equal  
to the current value of focusedWindow, then the returned element will be  
the application-wide focused element (the value of focusedElement). The  
return value will be null if no element is focused.  
  
If aDeep is true, then child frames are traversed and the return value  
may be the element within a child descendant window that is focused. If  
aDeep if false, then the return value will be the frame element if the  
focus is in a child frame.  
  
aFocusedWindow will be set to the currently focused descendant window of  
aWindow, or to aWindow if aDeep is false. This will be set even if no  
element is focused.  
  
@throws NS_ERROR_INVALID_ARG if aWindow is null  
  

### moveCaretToFocus(aWindow) ###
  
Moves the selection caret within aWindow to the current focus.  
  

### elementIsFocusable(aElement, aFlags) ###
  
Check if given element is focusable.  
  

### windowRaised(aWindow) ###
  
Called when a window has been raised.  
  

### windowLowered(aWindow) ###
  
Called when a window has been lowered.  
  

### windowShown(aWindow, aNeedsFocus) ###
  
Called when a new document in a window is shown.  
  
If aNeedsFocus is true, then focus events are expected to be fired on the  
window if this window is in the focused window chain.  
  

### windowHidden(aWindow) ###
  
Called when a document in a window has been hidden or otherwise can no  
longer accept focus.  
  

### fireDelayedEvents(aDocument) ###
  
Fire any events that have been delayed due to synchronized actions.  
  

### focusPlugin(aPlugin) ###
  
Indicate that a plugin wishes to take the focus. This is similar to a  
normal focus except that the widget focus is not changed. Updating the  
widget focus state is the responsibility of the caller.  
  

## Attributes ##

### activeWindow ###
  
The most active (frontmost) window, or null if no window that is part of  
the application is active. Setting the activeWindow raises it, and  
focuses the current child window's current element, if any. Setting this  
to null or to a non-top-level window throws an NS_ERROR_INVALID_ARG  
exception.  
  

### focusedWindow ###
  
The child window within the activeWindow that is focused. This will  
always be activeWindow, a child window of activeWindow or null if no  
child window is focused. Setting the focusedWindow changes the focused  
window and raises the toplevel window it is in. If the current focus  
within the new focusedWindow is a frame element, then the focusedWindow  
will actually be set to the child window and the current element within  
that set as the focused element. This process repeats downwards until a  
non-frame element is found.  
  

### focusedElement ###
  
The element that is currently focused. This will always be an element  
within the document loaded in focusedWindow or null if no element in that  
document is focused.  
  

## Constants ##

### FLAG_RAISE ###

### FLAG_NOSCROLL ###
  
Do not scroll the element to focus into view  
  

### FLAG_NOSWITCHFRAME ###
  
If attempting to change focus in a window that is not focused, do not  
switch focus to that window. Instead, just update the focus within that  
window and leave the application focus as is. This flag will have no  
effect if a child window is focused and an attempt is made to adjust the  
focus in an ancestor, as the frame must be switched in this case.  
  

### FLAG_NOPARENTFRAME ###
  
This flag is only used when passed to moveFocus. If set, focus is never  
moved to the parent frame of the starting element's document, instead  
iterating around to the beginning of that document again. Child frames  
are navigated as normal.  
  

### FLAG_BYMOUSE ###
  
Focus is changing due to a mouse operation, for instance the mouse was  
clicked on an element.  
  

### FLAG_BYKEY ###
  
Focus is changing due to a key operation, for instance pressing the tab  
key. This flag would normally be passed when MOVEFOCUS_FORWARD or  
MOVEFOCUS_BACKWARD is used.  
  

### FLAG_BYMOVEFOCUS ###
  
Focus is changing due to a call to MoveFocus. This flag will be implied  
when MoveFocus is called except when one of the other mechanisms (mouse  
or key) is specified, or when the type is MOVEFOCUS_ROOT or  
MOVEFOCUS_CARET.  
  

### FLAG_SHOWRING ###
  
Always show the focus ring or other indicator of focus, regardless of  
other state.  
  

### MOVEFOCUS_FORWARD ###
 move focus forward one element, used when pressing TAB */  

### MOVEFOCUS_BACKWARD ###
 move focus backward one element, used when pressing Shift+TAB */  

### MOVEFOCUS_FORWARDDOC ###
 move focus forward to the next frame document, used when pressing F6 */  

### MOVEFOCUS_BACKWARDDOC ###
 move focus forward to the previous frame document, used when pressing Shift+F6 */  

### MOVEFOCUS_FIRST ###
 move focus to the first focusable element */  

### MOVEFOCUS_LAST ###
 move focus to the last focusable element */  

### MOVEFOCUS_ROOT ###
 move focus to the root element in the document */  

### MOVEFOCUS_CARET ###
 move focus to a link at the position of the caret. This is a special value used to  
 focus links as the caret moves over them in caret browsing mode.  
  
