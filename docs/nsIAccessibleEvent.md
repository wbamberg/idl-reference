---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/accessible/interfaces/nsIAccessibleEvent.idl">Source file</a>
</div>

# nsIAccessibleEvent #
<pre>  
An interface for accessibility events listened to  
by in-process accessibility clients, which can be used  
to find out how to get accessibility and DOM interfaces for  
the event and its target. To listen to in-process accessibility invents,  
make your object an nsIObserver, and listen for accessible-event by   
using code something like this:  
  nsCOMPtr<nsIObserverService> observerService =   
    do_GetService("@mozilla.org/observer-service;1", &rv);  
  if (NS_SUCCEEDED(rv))   
    rv = observerService->AddObserver(this, "accessible-event", PR_TRUE);  
  
</pre>
## Attributes ##

### eventType ###
<pre>  
The type of event, based on the enumerated event values  
defined in this interface.  
  
</pre>
### accessible ###
<pre>  
The nsIAccessible associated with the event.  
May return null if no accessible is available  
  
</pre>
### accessibleDocument ###
<pre>  
The nsIAccessibleDocument that the event target nsIAccessible  
resides in. This can be used to get the DOM window,  
the DOM document and the window handler, among other things.  
  
</pre>
### DOMNode ###
<pre>  
The nsIDOMNode associated with the event  
May return null if accessible for event has been shut down  
  
</pre>
### isFromUserInput ###
<pre>  
Returns true if the event was caused by explicit user input,  
as opposed to purely originating from a timer or mouse movement  
  
</pre>
## Constants ##

### EVENT_SHOW ###
<pre>  
An object has been created.  
  
</pre>
### EVENT_HIDE ###
<pre>  
An object has been destroyed.  
  
</pre>
### EVENT_REORDER ###
<pre>  
An object's children have changed  
  
</pre>
### EVENT_ACTIVE_DECENDENT_CHANGED ###
<pre>  
The active descendant of a component has changed. The active descendant  
is used in objects with transient children.  
  
</pre>
### EVENT_FOCUS ###
<pre>  
An object has received the keyboard focus.  
  
</pre>
### EVENT_STATE_CHANGE ###
<pre>  
An object's state has changed.  
  
</pre>
### EVENT_LOCATION_CHANGE ###
<pre>  
An object has changed location, shape, or size.  
  
</pre>
### EVENT_NAME_CHANGE ###
<pre>  
An object's Name property has changed.  
  
</pre>
### EVENT_DESCRIPTION_CHANGE ###
<pre>  
An object's Description property has changed.  
  
</pre>
### EVENT_VALUE_CHANGE ###
<pre>  
An object's Value property has changed.  
  
</pre>
### EVENT_HELP_CHANGE ###
<pre>  
An object's help has changed.  
  
</pre>
### EVENT_DEFACTION_CHANGE ###
<pre>  
An object's default action has changed.  
  
</pre>
### EVENT_ACTION_CHANGE ###
<pre>  
An object's action has changed.  
  
</pre>
### EVENT_ACCELERATOR_CHANGE ###
<pre>  
An object's keyboard shortcut has changed.  
  
</pre>
### EVENT_SELECTION ###
<pre>  
The selection within a container object has changed.  
  
</pre>
### EVENT_SELECTION_ADD ###
<pre>  
An item within a container object has been added to the selection.  
  
</pre>
### EVENT_SELECTION_REMOVE ###
<pre>  
An item within a container object has been removed from the selection.  
  
</pre>
### EVENT_SELECTION_WITHIN ###
<pre>  
Numerous selection changes have occurred within a container object.  
  
</pre>
### EVENT_ALERT ###
<pre>  
An alert has been generated. Server applications send this event when a  
user needs to know that a user interface element has changed.  
  
</pre>
### EVENT_FOREGROUND ###
<pre>  
The foreground window has changed.  
  
</pre>
### EVENT_MENU_START ###
<pre>  
A menu item on the menu bar has been selected.  
  
</pre>
### EVENT_MENU_END ###
<pre>  
A menu from the menu bar has been closed.  
  
</pre>
### EVENT_MENUPOPUP_START ###
<pre>  
A pop-up menu has been displayed.  
  
</pre>
### EVENT_MENUPOPUP_END ###
<pre>  
A pop-up menu has been closed.  
  
</pre>
### EVENT_CAPTURE_START ###
<pre>  
A window has received mouse capture.  
  
</pre>
### EVENT_CAPTURE_END ###
<pre>  
A window has lost mouse capture.  
  
</pre>
### EVENT_MOVESIZE_START ###
<pre>  
A window is being moved or resized.  
  
</pre>
### EVENT_MOVESIZE_END ###
<pre>  
The movement or resizing of a window has finished  
  
</pre>
### EVENT_CONTEXTHELP_START ###
<pre>  
A window has entered context-sensitive Help mode  
  
</pre>
### EVENT_CONTEXTHELP_END ###
<pre>  
A window has exited context-sensitive Help mode  
  
</pre>
### EVENT_DRAGDROP_START ###
<pre>  
An application is about to enter drag-and-drop mode  
  
</pre>
### EVENT_DRAGDROP_END ###
<pre>  
An application is about to exit drag-and-drop mode  
  
</pre>
### EVENT_DIALOG_START ###
<pre>  
A dialog box has been displayed  
  
</pre>
### EVENT_DIALOG_END ###
<pre>  
A dialog box has been closed  
  
</pre>
### EVENT_SCROLLING_START ###
<pre>  
Scrolling has started on a scroll bar  
  
</pre>
### EVENT_SCROLLING_END ###
<pre>  
Scrolling has ended on a scroll bar  
  
</pre>
### EVENT_MINIMIZE_START ###
<pre>  
A window object is about to be minimized or maximized  
  
</pre>
### EVENT_MINIMIZE_END ###
<pre>  
A window object has been minimized or maximized  
  
</pre>
### EVENT_DOCUMENT_LOAD_COMPLETE ###
<pre>  
The loading of the document has completed.  
  
</pre>
### EVENT_DOCUMENT_RELOAD ###
<pre>  
The document contents are being reloaded.  
  
</pre>
### EVENT_DOCUMENT_LOAD_STOPPED ###
<pre>  
The loading of the document was interrupted.  
  
</pre>
### EVENT_DOCUMENT_ATTRIBUTES_CHANGED ###
<pre>  
The document wide attributes of the document object have changed.  
  
</pre>
### EVENT_DOCUMENT_CONTENT_CHANGED ###
<pre>  
The contents of the document have changed.  
  
</pre>
### EVENT_PROPERTY_CHANGED ###

### EVENT_PAGE_CHANGED ###
<pre>  
A slide changed in a presentation document or a page boundary was  
crossed in a word processing document.  
  
</pre>
### EVENT_TEXT_ATTRIBUTE_CHANGED ###
<pre>  
A text object's attributes changed.  
Also see EVENT_OBJECT_ATTRIBUTE_CHANGED.  
  
</pre>
### EVENT_TEXT_CARET_MOVED ###
<pre>  
The caret has moved to a new position.  
  
</pre>
### EVENT_TEXT_CHANGED ###
<pre>  
This event indicates general text changes, i.e. changes to text that is  
exposed through the IAccessibleText and IAccessibleEditableText interfaces.  
  
</pre>
### EVENT_TEXT_INSERTED ###
<pre>  
Text was inserted.  
  
</pre>
### EVENT_TEXT_REMOVED ###
<pre>  
Text was removed.  
  
</pre>
### EVENT_TEXT_UPDATED ###
<pre>  
Text was updated.  
  
</pre>
### EVENT_TEXT_SELECTION_CHANGED ###
<pre>  
The text selection changed.  
  
</pre>
### EVENT_VISIBLE_DATA_CHANGED ###
<pre>  
A visibile data event indicates the change of the visual appearance  
of an accessible object.  This includes for example most of the  
attributes available via the IAccessibleComponent interface.  
  
</pre>
### EVENT_TEXT_COLUMN_CHANGED ###
<pre>  
The caret moved from one column to the next.  
  
</pre>
### EVENT_SECTION_CHANGED ###
<pre>  
The caret moved from one section to the next.  
  
</pre>
### EVENT_TABLE_CAPTION_CHANGED ###
<pre>  
A table caption changed.  
  
</pre>
### EVENT_TABLE_MODEL_CHANGED ###
<pre>  
A table's data changed.  
  
</pre>
### EVENT_TABLE_SUMMARY_CHANGED ###
<pre>  
A table's summary changed.  
  
</pre>
### EVENT_TABLE_ROW_DESCRIPTION_CHANGED ###
<pre>  
A table's row description changed.  
  
</pre>
### EVENT_TABLE_ROW_HEADER_CHANGED ###
<pre>  
A table's row header changed.  
  
</pre>
### EVENT_TABLE_ROW_INSERT ###

### EVENT_TABLE_ROW_DELETE ###

### EVENT_TABLE_ROW_REORDER ###

### EVENT_TABLE_COLUMN_DESCRIPTION_CHANGED ###
<pre>  
A table's column description changed.  
  
</pre>
### EVENT_TABLE_COLUMN_HEADER_CHANGED ###
<pre>  
A table's column header changed.  
  
</pre>
### EVENT_TABLE_COLUMN_INSERT ###

### EVENT_TABLE_COLUMN_DELETE ###

### EVENT_TABLE_COLUMN_REORDER ###

### EVENT_WINDOW_ACTIVATE ###

### EVENT_WINDOW_CREATE ###

### EVENT_WINDOW_DEACTIVATE ###

### EVENT_WINDOW_DESTROY ###

### EVENT_WINDOW_MAXIMIZE ###

### EVENT_WINDOW_MINIMIZE ###

### EVENT_WINDOW_RESIZE ###

### EVENT_WINDOW_RESTORE ###

### EVENT_HYPERLINK_END_INDEX_CHANGED ###
<pre>  
The ending index of this link within the containing string has changed.  
  
</pre>
### EVENT_HYPERLINK_NUMBER_OF_ANCHORS_CHANGED ###
<pre>  
The number of anchors assoicated with this hyperlink object has changed.  
  
</pre>
### EVENT_HYPERLINK_SELECTED_LINK_CHANGED ###
<pre>  
The hyperlink selected state changed from selected to unselected or  
from unselected to selected.  
  
</pre>
### EVENT_HYPERTEXT_LINK_ACTIVATED ###
<pre>  
One of the links associated with the hypertext object has been activated.  
  
</pre>
### EVENT_HYPERTEXT_LINK_SELECTED ###
<pre>  
One of the links associated with the hypertext object has been selected.  
  
</pre>
### EVENT_HYPERLINK_START_INDEX_CHANGED ###
<pre>  
The starting index of this link within the containing string has changed.  
  
</pre>
### EVENT_HYPERTEXT_CHANGED ###
<pre>  
Focus has changed from one hypertext object to another, or focus moved  
from a non-hypertext object to a hypertext object, or focus moved from a  
hypertext object to a non-hypertext object.  
  
</pre>
### EVENT_HYPERTEXT_NLINKS_CHANGED ###
<pre>  
The number of hyperlinks associated with a hypertext object changed.  
  
</pre>
### EVENT_OBJECT_ATTRIBUTE_CHANGED ###
<pre>  
An object's attributes changed. Also see EVENT_TEXT_ATTRIBUTE_CHANGED.  
  
</pre>
### EVENT_VIRTUALCURSOR_CHANGED ###
<pre>  
A cursorable's virtual cursor has changed.  
  
</pre>
### EVENT_LAST_ENTRY ###
<pre>  
Help make sure event map does not get out-of-line.  
  
</pre>