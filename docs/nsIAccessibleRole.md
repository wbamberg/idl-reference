---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/accessible/interfaces/nsIAccessibleRole.idl">Source file</a>
</div>

# nsIAccessibleRole #
  
Defines cross platform (Gecko) roles.  
  

## Constants ##

### ROLE_NOTHING ###
  
Used when accessible hans't strong defined role.  
  

### ROLE_TITLEBAR ###
  
Represents a title or caption bar for a window. It is used by MSAA only,  
supported automatically by MS Windows.  
  

### ROLE_MENUBAR ###
  
Represents the menu bar (positioned beneath the title bar of a window)  
from which menus are selected by the user. The role is used by  
xul:menubar or role="menubar".  
  

### ROLE_SCROLLBAR ###
  
Represents a vertical or horizontal scroll bar, which is part of the client  
area or used in a control.  
  

### ROLE_GRIP ###
  
Represents a special mouse pointer, which allows a user to manipulate user  
interface elements such as windows. For example, a user clicks and drags  
a sizing grip in the lower-right corner of a window to resize it.  
  

### ROLE_SOUND ###
  
Represents a system sound, which is associated with various system events.  
  

### ROLE_CURSOR ###
  
Represents the system mouse pointer.  
  

### ROLE_CARET ###
  
Represents the system caret. The role is supported for caret.  
  

### ROLE_ALERT ###
  
Represents an alert or a condition that a user should be notified about.  
Assistive Technologies typically respond to the role by reading the entire  
onscreen contents of containers advertising this role. Should be used for  
warning dialogs, etc. The role is used by xul:browsermessage,  
role="alert".  
  

### ROLE_WINDOW ###
  
Represents the window frame, which contains child objects such as  
a title bar, client, and other objects contained in a window. The role  
is supported automatically by MS Windows.  
  

### ROLE_INTERNAL_FRAME ###
  
A sub-document (<frame> or <iframe>)  
  

### ROLE_MENUPOPUP ###
  
Represents a menu, which presents a list of options from which the user can  
make a selection to perform an action. It is used for role="menu".  
  

### ROLE_MENUITEM ###
  
Represents a menu item, which is an entry in a menu that a user can choose  
to carry out a command, select an option. It is used for xul:menuitem,  
role="menuitem".  
  

### ROLE_TOOLTIP ###
  
Represents a ToolTip that provides helpful hints.  
  

### ROLE_APPLICATION ###
  
Represents a main window for an application. It is used for  
role="application". Also refer to ROLE_APP_ROOT  
  

### ROLE_DOCUMENT ###
  
Represents a document window. A document window is always contained within  
an application window. It is used for role="document".  
  

### ROLE_PANE ###
  
Represents a pane within a frame or document window. Users can navigate  
between panes and within the contents of the current pane, but cannot  
navigate between items in different panes. Thus, panes represent a level  
of grouping lower than frame windows or documents, but above individual  
controls. It is used for the first child of a <frame> or <iframe>.  
  

### ROLE_CHART ###
  
Represents a graphical image used to represent data.  
  

### ROLE_DIALOG ###
  
Represents a dialog box or message box. It is used for xul:dialog,   
role="dialog".  
  

### ROLE_BORDER ###
  
Represents a window border.  
  

### ROLE_GROUPING ###
  
Logically groups other objects. There is not always a parent-child  
relationship between the grouping object and the objects it contains. It  
is used for html:textfield, xul:groupbox, role="group".  
  

### ROLE_SEPARATOR ###
  
Used to visually divide a space into two regions, such as a separator menu  
item or a bar that divides split panes within a window. It is used for  
xul:separator, html:hr, role="separator".  
  

### ROLE_TOOLBAR ###
  
Represents a toolbar, which is a grouping of controls (push buttons or  
toggle buttons) that provides easy access to frequently used features. It  
is used for xul:toolbar, role="toolbar".  
  

### ROLE_STATUSBAR ###
  
Represents a status bar, which is an area at the bottom of a window that  
displays information about the current operation, state of the application,  
or selected object. The status bar has multiple fields, which display  
different kinds of information. It is used for xul:statusbar.  
  

### ROLE_TABLE ###
  
Represents a table that contains rows and columns of cells, and optionally,  
row headers and column headers. It is used for html:table,  
role="grid". Also refer to the following roles: ROLE_COLUMNHEADER,  
ROLE_ROWHEADER, ROLE_COLUMN, ROLE_ROW, ROLE_CELL.  
  

### ROLE_COLUMNHEADER ###
  
Represents a column header, providing a visual label for a column in  
a table. It is used for XUL tree column headers, html:th,  
role="colheader". Also refer to ROLE_TABLE.  
  

### ROLE_ROWHEADER ###
  
Represents a row header, which provides a visual label for a table row.  
It is used for role="rowheader". Also, see ROLE_TABLE.  
  

### ROLE_COLUMN ###
  
Represents a column of cells within a table. Also, see ROLE_TABLE.  
  

### ROLE_ROW ###
  
Represents a row of cells within a table. Also, see ROLE_TABLE.  
  

### ROLE_CELL ###
  
Represents a cell within a table. It is used for html:td,  
xul:tree cell and xul:listcell. Also, see ROLE_TABLE.  
  

### ROLE_LINK ###
  
Represents a link to something else. This object might look like text or  
a graphic, but it acts like a button. It is used for  
xul:label@class="text-link", html:a, html:area.  
  

### ROLE_HELPBALLOON ###
  
Displays a Help topic in the form of a ToolTip or Help balloon.  
  

### ROLE_CHARACTER ###
  
Represents a cartoon-like graphic object, such as Microsoft Office  
Assistant, which is displayed to provide help to users of an application.  
  

### ROLE_LIST ###
  
Represents a list box, allowing the user to select one or more items. It  
is used for xul:listbox, html:select@size, role="list". See also  
ROLE_LIST_ITEM.  
  

### ROLE_LISTITEM ###
  
Represents an item in a list. See also ROLE_LIST.  
  

### ROLE_OUTLINE ###
  
Represents an outline or tree structure, such as a tree view control,  
that displays a hierarchical list and allows the user to expand and  
collapse branches. Is is used for role="tree".  
  

### ROLE_OUTLINEITEM ###
  
Represents an item in an outline or tree structure. It is used for  
role="treeitem".  
  

### ROLE_PAGETAB ###
  
Represents a page tab, it is a child of a page tab list. It is used for  
xul:tab, role="treeitem". Also refer to ROLE_PAGETABLIST.  
  

### ROLE_PROPERTYPAGE ###
  
Represents a property sheet. It is used for xul:tabpanel,  
role="tabpanel".  
  

### ROLE_INDICATOR ###
  
Represents an indicator, such as a pointer graphic, that points to the  
current item.  
  

### ROLE_GRAPHIC ###
  
Represents a picture. Is is used for xul:image, html:img.  
  

### ROLE_STATICTEXT ###
  
Represents read-only text, such as labels for other controls or  
instructions in a dialog box. Static text cannot be modified or selected.  
Is is used for xul:label, xul:description, html:label, role="label".  
  

### ROLE_TEXT_LEAF ###
  
Represents selectable text that allows edits or is designated read-only.  
  

### ROLE_PUSHBUTTON ###
  
Represents a push button control. It is used for xul:button, html:button,  
role="button".  
  

### ROLE_CHECKBUTTON ###
  
Represents a check box control. It is used for xul:checkbox,  
html:input@type="checkbox", role="checkbox".  
  

### ROLE_RADIOBUTTON ###
  
Represents an option button, also called a radio button. It is one of a  
group of mutually exclusive options. All objects sharing a single parent  
that have this attribute are assumed to be part of single mutually  
exclusive group. It is used for xul:radio, html:input@type="radio",  
role="radio".  
  

### ROLE_COMBOBOX ###
  
Represents a combo box; an edit control with an associated list box that  
provides a set of predefined choices. It is used for html:select,  
xul:menulist, role="combobox".  
  

### ROLE_DROPLIST ###
  
Represents the calendar control.  
  

### ROLE_PROGRESSBAR ###
  
Represents a progress bar, dynamically showing the user the percent  
complete of an operation in progress. It is used for xul:progressmeter,  
role="progressbar".  
  

### ROLE_DIAL ###
  
Represents a dial or knob whose purpose is to allow a user to set a value.  
  

### ROLE_HOTKEYFIELD ###
  
Represents a hot-key field that allows the user to enter a combination or  
sequence of keystrokes.  
  

### ROLE_SLIDER ###
  
Represents a slider, which allows the user to adjust a setting in given  
increments between minimum and maximum values. It is used by xul:scale,  
role="slider".  
  

### ROLE_SPINBUTTON ###
  
Represents a spin box, which is a control that allows the user to increment  
or decrement the value displayed in a separate "buddy" control associated  
with the spin box. It is used for xul:spinbuttons.  
  

### ROLE_DIAGRAM ###
  
Represents a graphical image used to diagram data. It is used for svg:svg.  
  

### ROLE_ANIMATION ###
  
Represents an animation control, which contains content that changes over  
time, such as a control that displays a series of bitmap frames.  
  

### ROLE_EQUATION ###
  
Represents a mathematical equation. It is used by MATHML, where there is a  
rich DOM subtree for an equation. Use ROLE_FLAT_EQUATION for <img role="math" alt="[TeX]"/>  
  

### ROLE_BUTTONDROPDOWN ###
  
Represents a button that drops down a list of items.  
  

### ROLE_BUTTONMENU ###
  
Represents a button that drops down a menu.  
  

### ROLE_BUTTONDROPDOWNGRID ###
  
Represents a button that drops down a grid. It is used for xul:colorpicker.  
  

### ROLE_WHITESPACE ###
  
Represents blank space between other objects.  
  

### ROLE_PAGETABLIST ###
  
Represents a container of page tab controls. Is it used for xul:tabs,  
DHTML: role="tabs". Also refer to ROLE_PAGETAB.  
  

### ROLE_CLOCK ###
  
Represents a control that displays time.  
  

### ROLE_SPLITBUTTON ###
  
Represents a button on a toolbar that has a drop-down list icon directly  
adjacent to the button.  
  

### ROLE_IPADDRESS ###
  
Represents an edit control designed for an Internet Protocol (IP) address.  
The edit control is divided into sections for the different parts of the  
IP address.  
  

### ROLE_ACCEL_LABEL ###
  
Represents a label control that has an accelerator.  
  

### ROLE_ARROW ###
  
Represents an arrow in one of the four cardinal directions.  
  

### ROLE_CANVAS ###
  
Represents a control that can be drawn into and is used to trap events.  
It is used for html:canvas.  
  

### ROLE_CHECK_MENU_ITEM ###
  
Represents a menu item with a check box.  
  

### ROLE_COLOR_CHOOSER ###
  
Represents a specialized dialog that lets the user choose a color.  
  

### ROLE_DATE_EDITOR ###
  
Represents control whose purpose is to allow a user to edit a date.  
  

### ROLE_DESKTOP_ICON ###
  
An iconified internal frame in an ROLE_DESKTOP_PANE. Also refer to  
ROLE_INTERNAL_FRAME.  
  

### ROLE_DESKTOP_FRAME ###
  
A desktop pane. A pane that supports internal frames and iconified  
versions of those internal frames.  
  

### ROLE_DIRECTORY_PANE ###
  
A directory pane. A pane that allows the user to navigate through  
and select the contents of a directory. May be used by a file chooser.  
Also refer to ROLE_FILE_CHOOSER.  
  

### ROLE_FILE_CHOOSER ###
  
A file chooser. A specialized dialog that displays the files in the  
directory and lets the user select a file, browse a different directory,  
or specify a filename. May use the directory pane to show the contents of  
a directory. Also refer to ROLE_DIRECTORY_PANE.  
  

### ROLE_FONT_CHOOSER ###
  
A font chooser. A font chooser is a component that lets the user pick  
various attributes for fonts.  
  

### ROLE_CHROME_WINDOW ###
  
Frame role. A top level window with a title bar, border, menu bar, etc.  
It is often used as the primary window for an application.  
  

### ROLE_GLASS_PANE ###
  
 A glass pane. A pane that is guaranteed to be painted on top of all  
panes beneath it. Also refer to ROLE_ROOT_PANE.  
  

### ROLE_HTML_CONTAINER ###
  
A document container for HTML, whose children represent the document  
content.  
  

### ROLE_ICON ###
  
A small fixed size picture, typically used to decorate components.  
  

### ROLE_LABEL ###
  
Presents an icon or short string in an interface.  
  

### ROLE_LAYERED_PANE ###
  
A layered pane. A specialized pane that allows its children to be drawn  
in layers, providing a form of stacking order. This is usually the pane  
that holds the menu bar as  well as the pane that contains most of the  
visual components in a window. Also refer to ROLE_GLASS_PANE and  
ROLE_ROOT_PANE.  
  

### ROLE_OPTION_PANE ###
  
A specialized pane whose primary use is inside a dialog.  
  

### ROLE_PASSWORD_TEXT ###
  
A text object uses for passwords, or other places where the text content  
is not shown visibly to the user.  
  

### ROLE_POPUP_MENU ###
  
A temporary window that is usually used to offer the user a list of  
choices, and then hides when the user selects one of those choices.  
  

### ROLE_RADIO_MENU_ITEM ###
  
A radio button that is a menu item.  
  

### ROLE_ROOT_PANE ###
  
A root pane. A specialized pane that has a glass pane and a layered pane  
as its children. Also refer to ROLE_GLASS_PANE and ROLE_LAYERED_PANE.  
  

### ROLE_SCROLL_PANE ###
  
A scroll pane. An object that allows a user to incrementally view a large  
amount of information.  Its children can include scroll bars and a  
viewport. Also refer to ROLE_VIEW_PORT.  
  

### ROLE_SPLIT_PANE ###
  
A split pane. A specialized panel that presents two other panels at the  
same time. Between the two panels is a divider the user can manipulate to  
make one panel larger and the other panel smaller.  
  

### ROLE_TABLE_COLUMN_HEADER ###
  
The header for a column of a table.  
XXX: it looks this role is dupe of ROLE_COLUMNHEADER.  
  

### ROLE_TABLE_ROW_HEADER ###
  
The header for a row of a table.  
XXX: it looks this role is dupe of ROLE_ROWHEADER  
  

### ROLE_TEAR_OFF_MENU_ITEM ###
  
A menu item used to tear off and reattach its menu.  
  

### ROLE_TERMINAL ###
  
Represents an accessible terminal.  
  

### ROLE_TEXT_CONTAINER ###
  
Collection of objects that constitute a logical text entity.  
  

### ROLE_TOGGLE_BUTTON ###
  
A toggle button. A specialized push button that can be checked or  
unchecked, but does not provide a separate indicator for the current state.  
  

### ROLE_TREE_TABLE ###
  
Representas a control that is capable of expanding and collapsing rows as  
well as showing multiple columns of data.  
XXX: it looks like this role is dupe of ROLE_OUTLINE.  
  

### ROLE_VIEWPORT ###
  
A viewport. An object usually used in a scroll pane. It represents the  
portion of the entire data that the user can see. As the user manipulates  
the scroll bars, the contents of the viewport can change. Also refer to  
ROLE_SCROLL_PANE.  
  

### ROLE_HEADER ###
  
Header of a document page. Also refer to ROLE_FOOTER.  
  

### ROLE_FOOTER ###
  
Footer of a document page. Also refer to ROLE_HEADER.  
  

### ROLE_PARAGRAPH ###
  
A paragraph of text.  
  

### ROLE_RULER ###
  
A ruler such as those used in word processors.  
  

### ROLE_AUTOCOMPLETE ###
  
A text entry having dialog or list containing items for insertion into  
an entry widget, for instance a list of words for completion of a  
text entry. It is used for xul:textbox@autocomplete  
  

### ROLE_EDITBAR ###
  
 An editable text object in a toolbar.  
  

### ROLE_ENTRY ###
  
An control whose textual content may be entered or modified by the user.  
  

### ROLE_CAPTION ###
  
A caption describing another object.  
  

### ROLE_DOCUMENT_FRAME ###
  
A visual frame or container which contains a view of document content.  
Document frames may occur within another Document instance, in which case  
the second document may be said to be embedded in the containing instance.  
HTML frames are often ROLE_DOCUMENT_FRAME. Either this object, or a  
singleton descendant, should implement the Document interface.  
  

### ROLE_HEADING ###
  
Heading.  
  

### ROLE_PAGE ###
  
An object representing a page of document content.  It is used in documents  
which are accessed by the user on a page by page basis.  
  

### ROLE_SECTION ###
  
A container of document content.  An example of the use of this role is to  
represent an html:div.  
  

### ROLE_REDUNDANT_OBJECT ###
  
An object which is redundant with another object in the accessible  
hierarchy. ATs typically ignore objects with this role.  
  

### ROLE_FORM ###
  
A container of form controls. An example of the use of this role is to  
represent an html:form.  
  

### ROLE_IME ###
  
An object which is used to allow input of characters not found on a  
keyboard, such as the input of Chinese characters on a Western keyboard.  
  

### ROLE_APP_ROOT ###
  
XXX: document this.  
  

### ROLE_PARENT_MENUITEM ###
  
Represents a menu item, which is an entry in a menu that a user can choose  
to display another menu.  
  

### ROLE_CALENDAR ###
  
A calendar that allows the user to select a date.  
  

### ROLE_COMBOBOX_LIST ###
  
A list of items that is shown by combobox.  
  

### ROLE_COMBOBOX_OPTION ###
  
A item of list that is shown by combobox;  
  

### ROLE_IMAGE_MAP ###
  
An image map -- has child links representing the areas  
  

### ROLE_OPTION ###
  
An option in a listbox  
  

### ROLE_RICH_OPTION ###
  
A rich option in a listbox, it can have other widgets as children  
  

### ROLE_LISTBOX ###
  
A list of options  
  

### ROLE_FLAT_EQUATION ###
  
Represents a mathematical equation in the accessible name  
  

### ROLE_GRID_CELL ###
  
Represents a cell within a grid. It is used for role="gridcell". Unlike  
ROLE_CELL, it allows the calculation of the accessible name from subtree.  
Also, see ROLE_TABLE.  
  

### ROLE_EMBEDDED_OBJECT ###
  
Represents an embedded object. It is used for html:object or html:embed.  
  

### ROLE_NOTE ###
  
A note. Originally intended to be hidden until activated, but now also used  
for things like html 'aside'.  
  

### ROLE_FIGURE ###
  
A figure. Used for things like HTML5 figure element.  
  

### ROLE_CHECK_RICH_OPTION ###
  
Represents a rich item with a check box.  
  

### ROLE_DEFINITION_LIST ###
  
An HTML definition list <dl>  
  

### ROLE_TERM ###
  
An HTML definition term <dt>  
  

### ROLE_DEFINITION ###
  
An HTML definition <dd>  
  

### ROLE_KEY ###
  
A keyboard or keypad key.  
  
