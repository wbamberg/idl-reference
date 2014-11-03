---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/accessible/interfaces/nsIAccessibleRole.idl">Source file</a>
</div>

# nsIAccessibleRole #
<pre>  
Defines cross platform (Gecko) roles.  
  
</pre>
## Constants ##

### ROLE_NOTHING ###
<pre>  
Used when accessible hans't strong defined role.  
  
</pre>
### ROLE_TITLEBAR ###
<pre>  
Represents a title or caption bar for a window. It is used by MSAA only,  
supported automatically by MS Windows.  
  
</pre>
### ROLE_MENUBAR ###
<pre>  
Represents the menu bar (positioned beneath the title bar of a window)  
from which menus are selected by the user. The role is used by  
xul:menubar or role="menubar".  
  
</pre>
### ROLE_SCROLLBAR ###
<pre>  
Represents a vertical or horizontal scroll bar, which is part of the client  
area or used in a control.  
  
</pre>
### ROLE_GRIP ###
<pre>  
Represents a special mouse pointer, which allows a user to manipulate user  
interface elements such as windows. For example, a user clicks and drags  
a sizing grip in the lower-right corner of a window to resize it.  
  
</pre>
### ROLE_SOUND ###
<pre>  
Represents a system sound, which is associated with various system events.  
  
</pre>
### ROLE_CURSOR ###
<pre>  
Represents the system mouse pointer.  
  
</pre>
### ROLE_CARET ###
<pre>  
Represents the system caret. The role is supported for caret.  
  
</pre>
### ROLE_ALERT ###
<pre>  
Represents an alert or a condition that a user should be notified about.  
Assistive Technologies typically respond to the role by reading the entire  
onscreen contents of containers advertising this role. Should be used for  
warning dialogs, etc. The role is used by xul:browsermessage,  
role="alert".  
  
</pre>
### ROLE_WINDOW ###
<pre>  
Represents the window frame, which contains child objects such as  
a title bar, client, and other objects contained in a window. The role  
is supported automatically by MS Windows.  
  
</pre>
### ROLE_INTERNAL_FRAME ###
<pre>  
A sub-document (<frame> or <iframe>)  
  
</pre>
### ROLE_MENUPOPUP ###
<pre>  
Represents a menu, which presents a list of options from which the user can  
make a selection to perform an action. It is used for role="menu".  
  
</pre>
### ROLE_MENUITEM ###
<pre>  
Represents a menu item, which is an entry in a menu that a user can choose  
to carry out a command, select an option. It is used for xul:menuitem,  
role="menuitem".  
  
</pre>
### ROLE_TOOLTIP ###
<pre>  
Represents a ToolTip that provides helpful hints.  
  
</pre>
### ROLE_APPLICATION ###
<pre>  
Represents a main window for an application. It is used for  
role="application". Also refer to ROLE_APP_ROOT  
  
</pre>
### ROLE_DOCUMENT ###
<pre>  
Represents a document window. A document window is always contained within  
an application window. It is used for role="document".  
  
</pre>
### ROLE_PANE ###
<pre>  
Represents a pane within a frame or document window. Users can navigate  
between panes and within the contents of the current pane, but cannot  
navigate between items in different panes. Thus, panes represent a level  
of grouping lower than frame windows or documents, but above individual  
controls. It is used for the first child of a <frame> or <iframe>.  
  
</pre>
### ROLE_CHART ###
<pre>  
Represents a graphical image used to represent data.  
  
</pre>
### ROLE_DIALOG ###
<pre>  
Represents a dialog box or message box. It is used for xul:dialog,   
role="dialog".  
  
</pre>
### ROLE_BORDER ###
<pre>  
Represents a window border.  
  
</pre>
### ROLE_GROUPING ###
<pre>  
Logically groups other objects. There is not always a parent-child  
relationship between the grouping object and the objects it contains. It  
is used for html:textfield, xul:groupbox, role="group".  
  
</pre>
### ROLE_SEPARATOR ###
<pre>  
Used to visually divide a space into two regions, such as a separator menu  
item or a bar that divides split panes within a window. It is used for  
xul:separator, html:hr, role="separator".  
  
</pre>
### ROLE_TOOLBAR ###
<pre>  
Represents a toolbar, which is a grouping of controls (push buttons or  
toggle buttons) that provides easy access to frequently used features. It  
is used for xul:toolbar, role="toolbar".  
  
</pre>
### ROLE_STATUSBAR ###
<pre>  
Represents a status bar, which is an area at the bottom of a window that  
displays information about the current operation, state of the application,  
or selected object. The status bar has multiple fields, which display  
different kinds of information. It is used for xul:statusbar.  
  
</pre>
### ROLE_TABLE ###
<pre>  
Represents a table that contains rows and columns of cells, and optionally,  
row headers and column headers. It is used for html:table,  
role="grid". Also refer to the following roles: ROLE_COLUMNHEADER,  
ROLE_ROWHEADER, ROLE_COLUMN, ROLE_ROW, ROLE_CELL.  
  
</pre>
### ROLE_COLUMNHEADER ###
<pre>  
Represents a column header, providing a visual label for a column in  
a table. It is used for XUL tree column headers, html:th,  
role="colheader". Also refer to ROLE_TABLE.  
  
</pre>
### ROLE_ROWHEADER ###
<pre>  
Represents a row header, which provides a visual label for a table row.  
It is used for role="rowheader". Also, see ROLE_TABLE.  
  
</pre>
### ROLE_COLUMN ###
<pre>  
Represents a column of cells within a table. Also, see ROLE_TABLE.  
  
</pre>
### ROLE_ROW ###
<pre>  
Represents a row of cells within a table. Also, see ROLE_TABLE.  
  
</pre>
### ROLE_CELL ###
<pre>  
Represents a cell within a table. It is used for html:td,  
xul:tree cell and xul:listcell. Also, see ROLE_TABLE.  
  
</pre>
### ROLE_LINK ###
<pre>  
Represents a link to something else. This object might look like text or  
a graphic, but it acts like a button. It is used for  
xul:label@class="text-link", html:a, html:area.  
  
</pre>
### ROLE_HELPBALLOON ###
<pre>  
Displays a Help topic in the form of a ToolTip or Help balloon.  
  
</pre>
### ROLE_CHARACTER ###
<pre>  
Represents a cartoon-like graphic object, such as Microsoft Office  
Assistant, which is displayed to provide help to users of an application.  
  
</pre>
### ROLE_LIST ###
<pre>  
Represents a list box, allowing the user to select one or more items. It  
is used for xul:listbox, html:select@size, role="list". See also  
ROLE_LIST_ITEM.  
  
</pre>
### ROLE_LISTITEM ###
<pre>  
Represents an item in a list. See also ROLE_LIST.  
  
</pre>
### ROLE_OUTLINE ###
<pre>  
Represents an outline or tree structure, such as a tree view control,  
that displays a hierarchical list and allows the user to expand and  
collapse branches. Is is used for role="tree".  
  
</pre>
### ROLE_OUTLINEITEM ###
<pre>  
Represents an item in an outline or tree structure. It is used for  
role="treeitem".  
  
</pre>
### ROLE_PAGETAB ###
<pre>  
Represents a page tab, it is a child of a page tab list. It is used for  
xul:tab, role="treeitem". Also refer to ROLE_PAGETABLIST.  
  
</pre>
### ROLE_PROPERTYPAGE ###
<pre>  
Represents a property sheet. It is used for xul:tabpanel,  
role="tabpanel".  
  
</pre>
### ROLE_INDICATOR ###
<pre>  
Represents an indicator, such as a pointer graphic, that points to the  
current item.  
  
</pre>
### ROLE_GRAPHIC ###
<pre>  
Represents a picture. Is is used for xul:image, html:img.  
  
</pre>
### ROLE_STATICTEXT ###
<pre>  
Represents read-only text, such as labels for other controls or  
instructions in a dialog box. Static text cannot be modified or selected.  
Is is used for xul:label, xul:description, html:label, role="label".  
  
</pre>
### ROLE_TEXT_LEAF ###
<pre>  
Represents selectable text that allows edits or is designated read-only.  
  
</pre>
### ROLE_PUSHBUTTON ###
<pre>  
Represents a push button control. It is used for xul:button, html:button,  
role="button".  
  
</pre>
### ROLE_CHECKBUTTON ###
<pre>  
Represents a check box control. It is used for xul:checkbox,  
html:input@type="checkbox", role="checkbox".  
  
</pre>
### ROLE_RADIOBUTTON ###
<pre>  
Represents an option button, also called a radio button. It is one of a  
group of mutually exclusive options. All objects sharing a single parent  
that have this attribute are assumed to be part of single mutually  
exclusive group. It is used for xul:radio, html:input@type="radio",  
role="radio".  
  
</pre>
### ROLE_COMBOBOX ###
<pre>  
Represents a combo box; an edit control with an associated list box that  
provides a set of predefined choices. It is used for html:select,  
xul:menulist, role="combobox".  
  
</pre>
### ROLE_DROPLIST ###
<pre>  
Represents the calendar control.  
  
</pre>
### ROLE_PROGRESSBAR ###
<pre>  
Represents a progress bar, dynamically showing the user the percent  
complete of an operation in progress. It is used for xul:progressmeter,  
role="progressbar".  
  
</pre>
### ROLE_DIAL ###
<pre>  
Represents a dial or knob whose purpose is to allow a user to set a value.  
  
</pre>
### ROLE_HOTKEYFIELD ###
<pre>  
Represents a hot-key field that allows the user to enter a combination or  
sequence of keystrokes.  
  
</pre>
### ROLE_SLIDER ###
<pre>  
Represents a slider, which allows the user to adjust a setting in given  
increments between minimum and maximum values. It is used by xul:scale,  
role="slider".  
  
</pre>
### ROLE_SPINBUTTON ###
<pre>  
Represents a spin box, which is a control that allows the user to increment  
or decrement the value displayed in a separate "buddy" control associated  
with the spin box. It is used for xul:spinbuttons.  
  
</pre>
### ROLE_DIAGRAM ###
<pre>  
Represents a graphical image used to diagram data. It is used for svg:svg.  
  
</pre>
### ROLE_ANIMATION ###
<pre>  
Represents an animation control, which contains content that changes over  
time, such as a control that displays a series of bitmap frames.  
  
</pre>
### ROLE_EQUATION ###
<pre>  
Represents a mathematical equation. It is used by MATHML, where there is a  
rich DOM subtree for an equation. Use ROLE_FLAT_EQUATION for <img role="math" alt="[TeX]"/>  
  
</pre>
### ROLE_BUTTONDROPDOWN ###
<pre>  
Represents a button that drops down a list of items.  
  
</pre>
### ROLE_BUTTONMENU ###
<pre>  
Represents a button that drops down a menu.  
  
</pre>
### ROLE_BUTTONDROPDOWNGRID ###
<pre>  
Represents a button that drops down a grid. It is used for xul:colorpicker.  
  
</pre>
### ROLE_WHITESPACE ###
<pre>  
Represents blank space between other objects.  
  
</pre>
### ROLE_PAGETABLIST ###
<pre>  
Represents a container of page tab controls. Is it used for xul:tabs,  
DHTML: role="tabs". Also refer to ROLE_PAGETAB.  
  
</pre>
### ROLE_CLOCK ###
<pre>  
Represents a control that displays time.  
  
</pre>
### ROLE_SPLITBUTTON ###
<pre>  
Represents a button on a toolbar that has a drop-down list icon directly  
adjacent to the button.  
  
</pre>
### ROLE_IPADDRESS ###
<pre>  
Represents an edit control designed for an Internet Protocol (IP) address.  
The edit control is divided into sections for the different parts of the  
IP address.  
  
</pre>
### ROLE_ACCEL_LABEL ###
<pre>  
Represents a label control that has an accelerator.  
  
</pre>
### ROLE_ARROW ###
<pre>  
Represents an arrow in one of the four cardinal directions.  
  
</pre>
### ROLE_CANVAS ###
<pre>  
Represents a control that can be drawn into and is used to trap events.  
It is used for html:canvas.  
  
</pre>
### ROLE_CHECK_MENU_ITEM ###
<pre>  
Represents a menu item with a check box.  
  
</pre>
### ROLE_COLOR_CHOOSER ###
<pre>  
Represents a specialized dialog that lets the user choose a color.  
  
</pre>
### ROLE_DATE_EDITOR ###
<pre>  
Represents control whose purpose is to allow a user to edit a date.  
  
</pre>
### ROLE_DESKTOP_ICON ###
<pre>  
An iconified internal frame in an ROLE_DESKTOP_PANE. Also refer to  
ROLE_INTERNAL_FRAME.  
  
</pre>
### ROLE_DESKTOP_FRAME ###
<pre>  
A desktop pane. A pane that supports internal frames and iconified  
versions of those internal frames.  
  
</pre>
### ROLE_DIRECTORY_PANE ###
<pre>  
A directory pane. A pane that allows the user to navigate through  
and select the contents of a directory. May be used by a file chooser.  
Also refer to ROLE_FILE_CHOOSER.  
  
</pre>
### ROLE_FILE_CHOOSER ###
<pre>  
A file chooser. A specialized dialog that displays the files in the  
directory and lets the user select a file, browse a different directory,  
or specify a filename. May use the directory pane to show the contents of  
a directory. Also refer to ROLE_DIRECTORY_PANE.  
  
</pre>
### ROLE_FONT_CHOOSER ###
<pre>  
A font chooser. A font chooser is a component that lets the user pick  
various attributes for fonts.  
  
</pre>
### ROLE_CHROME_WINDOW ###
<pre>  
Frame role. A top level window with a title bar, border, menu bar, etc.  
It is often used as the primary window for an application.  
  
</pre>
### ROLE_GLASS_PANE ###
<pre>  
 A glass pane. A pane that is guaranteed to be painted on top of all  
panes beneath it. Also refer to ROLE_ROOT_PANE.  
  
</pre>
### ROLE_HTML_CONTAINER ###
<pre>  
A document container for HTML, whose children represent the document  
content.  
  
</pre>
### ROLE_ICON ###
<pre>  
A small fixed size picture, typically used to decorate components.  
  
</pre>
### ROLE_LABEL ###
<pre>  
Presents an icon or short string in an interface.  
  
</pre>
### ROLE_LAYERED_PANE ###
<pre>  
A layered pane. A specialized pane that allows its children to be drawn  
in layers, providing a form of stacking order. This is usually the pane  
that holds the menu bar as  well as the pane that contains most of the  
visual components in a window. Also refer to ROLE_GLASS_PANE and  
ROLE_ROOT_PANE.  
  
</pre>
### ROLE_OPTION_PANE ###
<pre>  
A specialized pane whose primary use is inside a dialog.  
  
</pre>
### ROLE_PASSWORD_TEXT ###
<pre>  
A text object uses for passwords, or other places where the text content  
is not shown visibly to the user.  
  
</pre>
### ROLE_POPUP_MENU ###
<pre>  
A temporary window that is usually used to offer the user a list of  
choices, and then hides when the user selects one of those choices.  
  
</pre>
### ROLE_RADIO_MENU_ITEM ###
<pre>  
A radio button that is a menu item.  
  
</pre>
### ROLE_ROOT_PANE ###
<pre>  
A root pane. A specialized pane that has a glass pane and a layered pane  
as its children. Also refer to ROLE_GLASS_PANE and ROLE_LAYERED_PANE.  
  
</pre>
### ROLE_SCROLL_PANE ###
<pre>  
A scroll pane. An object that allows a user to incrementally view a large  
amount of information.  Its children can include scroll bars and a  
viewport. Also refer to ROLE_VIEW_PORT.  
  
</pre>
### ROLE_SPLIT_PANE ###
<pre>  
A split pane. A specialized panel that presents two other panels at the  
same time. Between the two panels is a divider the user can manipulate to  
make one panel larger and the other panel smaller.  
  
</pre>
### ROLE_TABLE_COLUMN_HEADER ###
<pre>  
The header for a column of a table.  
XXX: it looks this role is dupe of ROLE_COLUMNHEADER.  
  
</pre>
### ROLE_TABLE_ROW_HEADER ###
<pre>  
The header for a row of a table.  
XXX: it looks this role is dupe of ROLE_ROWHEADER  
  
</pre>
### ROLE_TEAR_OFF_MENU_ITEM ###
<pre>  
A menu item used to tear off and reattach its menu.  
  
</pre>
### ROLE_TERMINAL ###
<pre>  
Represents an accessible terminal.  
  
</pre>
### ROLE_TEXT_CONTAINER ###
<pre>  
Collection of objects that constitute a logical text entity.  
  
</pre>
### ROLE_TOGGLE_BUTTON ###
<pre>  
A toggle button. A specialized push button that can be checked or  
unchecked, but does not provide a separate indicator for the current state.  
  
</pre>
### ROLE_TREE_TABLE ###
<pre>  
Representas a control that is capable of expanding and collapsing rows as  
well as showing multiple columns of data.  
XXX: it looks like this role is dupe of ROLE_OUTLINE.  
  
</pre>
### ROLE_VIEWPORT ###
<pre>  
A viewport. An object usually used in a scroll pane. It represents the  
portion of the entire data that the user can see. As the user manipulates  
the scroll bars, the contents of the viewport can change. Also refer to  
ROLE_SCROLL_PANE.  
  
</pre>
### ROLE_HEADER ###
<pre>  
Header of a document page. Also refer to ROLE_FOOTER.  
  
</pre>
### ROLE_FOOTER ###
<pre>  
Footer of a document page. Also refer to ROLE_HEADER.  
  
</pre>
### ROLE_PARAGRAPH ###
<pre>  
A paragraph of text.  
  
</pre>
### ROLE_RULER ###
<pre>  
A ruler such as those used in word processors.  
  
</pre>
### ROLE_AUTOCOMPLETE ###
<pre>  
A text entry having dialog or list containing items for insertion into  
an entry widget, for instance a list of words for completion of a  
text entry. It is used for xul:textbox@autocomplete  
  
</pre>
### ROLE_EDITBAR ###
<pre>  
 An editable text object in a toolbar.  
  
</pre>
### ROLE_ENTRY ###
<pre>  
An control whose textual content may be entered or modified by the user.  
  
</pre>
### ROLE_CAPTION ###
<pre>  
A caption describing another object.  
  
</pre>
### ROLE_DOCUMENT_FRAME ###
<pre>  
A visual frame or container which contains a view of document content.  
Document frames may occur within another Document instance, in which case  
the second document may be said to be embedded in the containing instance.  
HTML frames are often ROLE_DOCUMENT_FRAME. Either this object, or a  
singleton descendant, should implement the Document interface.  
  
</pre>
### ROLE_HEADING ###
<pre>  
Heading.  
  
</pre>
### ROLE_PAGE ###
<pre>  
An object representing a page of document content.  It is used in documents  
which are accessed by the user on a page by page basis.  
  
</pre>
### ROLE_SECTION ###
<pre>  
A container of document content.  An example of the use of this role is to  
represent an html:div.  
  
</pre>
### ROLE_REDUNDANT_OBJECT ###
<pre>  
An object which is redundant with another object in the accessible  
hierarchy. ATs typically ignore objects with this role.  
  
</pre>
### ROLE_FORM ###
<pre>  
A container of form controls. An example of the use of this role is to  
represent an html:form.  
  
</pre>
### ROLE_IME ###
<pre>  
An object which is used to allow input of characters not found on a  
keyboard, such as the input of Chinese characters on a Western keyboard.  
  
</pre>
### ROLE_APP_ROOT ###
<pre>  
XXX: document this.  
  
</pre>
### ROLE_PARENT_MENUITEM ###
<pre>  
Represents a menu item, which is an entry in a menu that a user can choose  
to display another menu.  
  
</pre>
### ROLE_CALENDAR ###
<pre>  
A calendar that allows the user to select a date.  
  
</pre>
### ROLE_COMBOBOX_LIST ###
<pre>  
A list of items that is shown by combobox.  
  
</pre>
### ROLE_COMBOBOX_OPTION ###
<pre>  
A item of list that is shown by combobox;  
  
</pre>
### ROLE_IMAGE_MAP ###
<pre>  
An image map -- has child links representing the areas  
  
</pre>
### ROLE_OPTION ###
<pre>  
An option in a listbox  
  
</pre>
### ROLE_RICH_OPTION ###
<pre>  
A rich option in a listbox, it can have other widgets as children  
  
</pre>
### ROLE_LISTBOX ###
<pre>  
A list of options  
  
</pre>
### ROLE_FLAT_EQUATION ###
<pre>  
Represents a mathematical equation in the accessible name  
  
</pre>
### ROLE_GRID_CELL ###
<pre>  
Represents a cell within a grid. It is used for role="gridcell". Unlike  
ROLE_CELL, it allows the calculation of the accessible name from subtree.  
Also, see ROLE_TABLE.  
  
</pre>
### ROLE_EMBEDDED_OBJECT ###
<pre>  
Represents an embedded object. It is used for html:object or html:embed.  
  
</pre>
### ROLE_NOTE ###
<pre>  
A note. Originally intended to be hidden until activated, but now also used  
for things like html 'aside'.  
  
</pre>
### ROLE_FIGURE ###
<pre>  
A figure. Used for things like HTML5 figure element.  
  
</pre>
### ROLE_CHECK_RICH_OPTION ###
<pre>  
Represents a rich item with a check box.  
  
</pre>
### ROLE_DEFINITION_LIST ###
<pre>  
An HTML definition list <dl>  
  
</pre>
### ROLE_TERM ###
<pre>  
An HTML definition term <dt>  
  
</pre>
### ROLE_DEFINITION ###
<pre>  
An HTML definition <dd>  
  
</pre>
### ROLE_KEY ###
<pre>  
A keyboard or keypad key.  
  
</pre>