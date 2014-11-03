---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/accessible/interfaces/nsIAccessibleEvent.idl">Source file</a>
</div>

# nsIAccessibleEvent #
<code>  
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
  
</code>
## Attributes ##

### eventType ###
  
The type of event, based on the enumerated event values  
defined in this interface.  
  

### accessible ###
  
The nsIAccessible associated with the event.  
May return null if no accessible is available  
  

### accessibleDocument ###
  
The nsIAccessibleDocument that the event target nsIAccessible  
resides in. This can be used to get the DOM window,  
the DOM document and the window handler, among other things.  
  

### DOMNode ###
  
The nsIDOMNode associated with the event  
May return null if accessible for event has been shut down  
  

### isFromUserInput ###
  
Returns true if the event was caused by explicit user input,  
as opposed to purely originating from a timer or mouse movement  
  

## Constants ##

### EVENT_SHOW ###
  
An object has been created.  
  

### EVENT_HIDE ###
  
An object has been destroyed.  
  

### EVENT_REORDER ###
  
An object's children have changed  
  

### EVENT_ACTIVE_DECENDENT_CHANGED ###
  
The active descendant of a component has changed. The active descendant  
is used in objects with transient children.  
  

### EVENT_FOCUS ###
  
An object has received the keyboard focus.  
  

### EVENT_STATE_CHANGE ###
  
An object's state has changed.  
  

### EVENT_LOCATION_CHANGE ###
  
An object has changed location, shape, or size.  
  

### EVENT_NAME_CHANGE ###
  
An object's Name property has changed.  
  

### EVENT_DESCRIPTION_CHANGE ###
  
An object's Description property has changed.  
  

### EVENT_VALUE_CHANGE ###
  
An object's Value property has changed.  
  

### EVENT_HELP_CHANGE ###
  
An object's help has changed.  
  

### EVENT_DEFACTION_CHANGE ###
  
An object's default action has changed.  
  

### EVENT_ACTION_CHANGE ###
  
An object's action has changed.  
  

### EVENT_ACCELERATOR_CHANGE ###
  
An object's keyboard shortcut has changed.  
  

### EVENT_SELECTION ###
  
The selection within a container object has changed.  
  

### EVENT_SELECTION_ADD ###
  
An item within a container object has been added to the selection.  
  

### EVENT_SELECTION_REMOVE ###
  
An item within a container object has been removed from the selection.  
  

### EVENT_SELECTION_WITHIN ###
  
Numerous selection changes have occurred within a container object.  
  

### EVENT_ALERT ###
  
An alert has been generated. Server applications send this event when a  
user needs to know that a user interface element has changed.  
  

### EVENT_FOREGROUND ###
  
The foreground window has changed.  
  

### EVENT_MENU_START ###
  
A menu item on the menu bar has been selected.  
  

### EVENT_MENU_END ###
  
A menu from the menu bar has been closed.  
  

### EVENT_MENUPOPUP_START ###
  
A pop-up menu has been displayed.  
  

### EVENT_MENUPOPUP_END ###
  
A pop-up menu has been closed.  
  

### EVENT_CAPTURE_START ###
  
A window has received mouse capture.  
  

### EVENT_CAPTURE_END ###
  
A window has lost mouse capture.  
  

### EVENT_MOVESIZE_START ###
  
A window is being moved or resized.  
  

### EVENT_MOVESIZE_END ###
  
The movement or resizing of a window has finished  
  

### EVENT_CONTEXTHELP_START ###
  
A window has entered context-sensitive Help mode  
  

### EVENT_CONTEXTHELP_END ###
  
A window has exited context-sensitive Help mode  
  

### EVENT_DRAGDROP_START ###
  
An application is about to enter drag-and-drop mode  
  

### EVENT_DRAGDROP_END ###
  
An application is about to exit drag-and-drop mode  
  

### EVENT_DIALOG_START ###
  
A dialog box has been displayed  
  

### EVENT_DIALOG_END ###
  
A dialog box has been closed  
  

### EVENT_SCROLLING_START ###
  
Scrolling has started on a scroll bar  
  

### EVENT_SCROLLING_END ###
  
Scrolling has ended on a scroll bar  
  

### EVENT_MINIMIZE_START ###
  
A window object is about to be minimized or maximized  
  

### EVENT_MINIMIZE_END ###
  
A window object has been minimized or maximized  
  

### EVENT_DOCUMENT_LOAD_COMPLETE ###
  
The loading of the document has completed.  
  

### EVENT_DOCUMENT_RELOAD ###
  
The document contents are being reloaded.  
  

### EVENT_DOCUMENT_LOAD_STOPPED ###
  
The loading of the document was interrupted.  
  

### EVENT_DOCUMENT_ATTRIBUTES_CHANGED ###
  
The document wide attributes of the document object have changed.  
  

### EVENT_DOCUMENT_CONTENT_CHANGED ###
  
The contents of the document have changed.  
  

### EVENT_PROPERTY_CHANGED ###

### EVENT_PAGE_CHANGED ###
  
A slide changed in a presentation document or a page boundary was  
crossed in a word processing document.  
  

### EVENT_TEXT_ATTRIBUTE_CHANGED ###
  
A text object's attributes changed.  
Also see EVENT_OBJECT_ATTRIBUTE_CHANGED.  
  

### EVENT_TEXT_CARET_MOVED ###
  
The caret has moved to a new position.  
  

### EVENT_TEXT_CHANGED ###
  
This event indicates general text changes, i.e. changes to text that is  
exposed through the IAccessibleText and IAccessibleEditableText interfaces.  
  

### EVENT_TEXT_INSERTED ###
  
Text was inserted.  
  

### EVENT_TEXT_REMOVED ###
  
Text was removed.  
  

### EVENT_TEXT_UPDATED ###
  
Text was updated.  
  

### EVENT_TEXT_SELECTION_CHANGED ###
  
The text selection changed.  
  

### EVENT_VISIBLE_DATA_CHANGED ###
  
A visibile data event indicates the change of the visual appearance  
of an accessible object.  This includes for example most of the  
attributes available via the IAccessibleComponent interface.  
  

### EVENT_TEXT_COLUMN_CHANGED ###
  
The caret moved from one column to the next.  
  

### EVENT_SECTION_CHANGED ###
  
The caret moved from one section to the next.  
  

### EVENT_TABLE_CAPTION_CHANGED ###
  
A table caption changed.  
  

### EVENT_TABLE_MODEL_CHANGED ###
  
A table's data changed.  
  

### EVENT_TABLE_SUMMARY_CHANGED ###
  
A table's summary changed.  
  

### EVENT_TABLE_ROW_DESCRIPTION_CHANGED ###
  
A table's row description changed.  
  

### EVENT_TABLE_ROW_HEADER_CHANGED ###
  
A table's row header changed.  
  

### EVENT_TABLE_ROW_INSERT ###

### EVENT_TABLE_ROW_DELETE ###

### EVENT_TABLE_ROW_REORDER ###

### EVENT_TABLE_COLUMN_DESCRIPTION_CHANGED ###
  
A table's column description changed.  
  

### EVENT_TABLE_COLUMN_HEADER_CHANGED ###
  
A table's column header changed.  
  

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
  
The ending index of this link within the containing string has changed.  
  

### EVENT_HYPERLINK_NUMBER_OF_ANCHORS_CHANGED ###
  
The number of anchors assoicated with this hyperlink object has changed.  
  

### EVENT_HYPERLINK_SELECTED_LINK_CHANGED ###
  
The hyperlink selected state changed from selected to unselected or  
from unselected to selected.  
  

### EVENT_HYPERTEXT_LINK_ACTIVATED ###
  
One of the links associated with the hypertext object has been activated.  
  

### EVENT_HYPERTEXT_LINK_SELECTED ###
  
One of the links associated with the hypertext object has been selected.  
  

### EVENT_HYPERLINK_START_INDEX_CHANGED ###
  
The starting index of this link within the containing string has changed.  
  

### EVENT_HYPERTEXT_CHANGED ###
  
Focus has changed from one hypertext object to another, or focus moved  
from a non-hypertext object to a hypertext object, or focus moved from a  
hypertext object to a non-hypertext object.  
  

### EVENT_HYPERTEXT_NLINKS_CHANGED ###
  
The number of hyperlinks associated with a hypertext object changed.  
  

### EVENT_OBJECT_ATTRIBUTE_CHANGED ###
  
An object's attributes changed. Also see EVENT_TEXT_ATTRIBUTE_CHANGED.  
  

### EVENT_VIRTUALCURSOR_CHANGED ###
  
A cursorable's virtual cursor has changed.  
  

### EVENT_LAST_ENTRY ###
  
Help make sure event map does not get out-of-line.  
  
