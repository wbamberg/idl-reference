---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/accessible/interfaces/nsIAccessible.idl">Source file</a>
</div>

# nsIAccessible #
<pre>  
A cross-platform interface that supports platform-specific   
accessibility APIs like MSAA and ATK. Contains the sum of what's needed  
to support IAccessible as well as ATK's generic accessibility objects.  
Can also be used by in-process accessibility clients to get information  
about objects in the accessible tree. The accessible tree is a subset of   
nodes in the DOM tree -- such as documents, focusable elements and text.  
Mozilla creates the implementations of nsIAccessible on demand.  
See http://www.mozilla.org/projects/ui/accessibility for more information.  
  
</pre>
## Methods ##

### getState(aState, aExtraState) ###
<pre>  
Accessible states -- bit fields which describe boolean properties of node.  
Many states are only valid given a certain role attribute that supports  
them.  
  
@param aState - the first bit field (see nsIAccessibleStates::STATE_*  
                constants)  
@param aExtraState - the second bit field  
                     (see nsIAccessibleStates::EXT_STATE_* constants)  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aState</td>
<td>- the first bit field (see nsIAccessibleStates::STATE_*  
                constants)  
</td>
</tr>

<tr>
<td>aExtraState</td>
<td>- the second bit field  
                     (see nsIAccessibleStates::EXT_STATE_* constants)  
</td>
</tr>

</table>

### groupPosition(aGroupLevel, aSimilarItemsInGroup, aPositionInGroup) ###
<pre>  
Returns grouping information. Used for tree items, list items, tab panel  
labels, radio buttons, etc. Also used for collectons of non-text objects.  
  
@param groupLevel - 1-based, similar to ARIA 'level' property  
@param similarItemsInGroup - 1-based, similar to ARIA 'setsize' property,  
                             inclusive of the current item  
@param positionInGroup - 1-based, similar to ARIA 'posinset' property  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>groupLevel</td>
<td>- 1-based, similar to ARIA 'level' property  
</td>
</tr>

<tr>
<td>similarItemsInGroup</td>
<td>- 1-based, similar to ARIA 'setsize' property,  
                             inclusive of the current item  
</td>
</tr>

<tr>
<td>positionInGroup</td>
<td>- 1-based, similar to ARIA 'posinset' property  
</td>
</tr>

</table>

### getChildAtPoint(x, y) ###
<pre>  
Accessible child which contains the coordinate at (x, y) in screen pixels.  
If the point is in the current accessible but not in a child, the  
current accessible will be returned.  
If the point is in neither the current accessible or a child, then  
null will be returned.  
  
@param x  screen's x coordinate  
@param y  screen's y coordinate  
@return   the deepest accessible child containing the given point  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>x</td>
<td>screen's x coordinate  
</td>
</tr>

<tr>
<td>y</td>
<td>screen's y coordinate  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>the deepest accessible child containing the given point  
</td>
</tr>

</table>

### getDeepestChildAtPoint(x, y) ###
<pre>  
Deepest accessible child which contains the coordinate at (x, y) in screen  
pixels. If the point is in the current accessible but not in a child, the  
current accessible will be returned. If the point is in neither the current  
accessible or a child, then null will be returned.  
  
@param x  screen's x coordinate  
@param y  screen's y coordinate  
@return   the deepest accessible child containing the given point  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>x</td>
<td>screen's x coordinate  
</td>
</tr>

<tr>
<td>y</td>
<td>screen's y coordinate  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>the deepest accessible child containing the given point  
</td>
</tr>

</table>

### getChildAt(aChildIndex) ###
<pre>  
Nth accessible child using zero-based index or last child if index less than zero  
  
</pre>
### getRelationByType(aRelationType) ###
<pre>  
Return accessible relation by the given relation type (see.  
constants defined in nsIAccessibleRelation).  
  
</pre>
### getRelations() ###
<pre>  
Returns multiple accessible relations for this object.  
  
</pre>
### getBounds(x, y, width, height) ###
<pre>  
Return accessible's x and y coordinates relative to the screen and  
accessible's width and height.  
  
</pre>
### setSelected(isSelected) ###
<pre>  
Add or remove this accessible to the current selection  
  
</pre>
### extendSelection() ###
<pre>  
Extend the current selection from its current accessible anchor node  
to this accessible  
  
</pre>
### takeSelection() ###
<pre>  
Select this accessible node only  
  
</pre>
### takeFocus() ###
<pre>  
Focus this accessible node,  
The state STATE_FOCUSABLE indicates whether this node is normally focusable.  
It is the callers responsibility to determine whether this node is focusable.  
accTakeFocus on a node that is not normally focusable (such as a table),  
will still set focus on that node, although normally that will not be visually  
indicated in most style sheets.  
  
</pre>
### getActionName(index) ###
<pre>  
The name of the accessible action at the given zero-based index  
  
</pre>
### getActionDescription(aIndex) ###
<pre>  
The description of the accessible action at the given zero-based index  
  
</pre>
### doAction(index) ###
<pre>  
Perform the accessible action at the given zero-based index  
Action number 0 is the default action  
  
</pre>
### scrollTo(aScrollType) ###
<pre>  
Makes an object visible on screen.  
  
@param scrollType - defines where the object should be placed on  
                    the screen (see nsIAccessibleScrollType for  
                    available constants).  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>scrollType</td>
<td>- defines where the object should be placed on  
                    the screen (see nsIAccessibleScrollType for  
                    available constants).  
</td>
</tr>

</table>

### scrollToPoint(coordinateType, x, y) ###
<pre>  
Moves the top left of an object to a specified location.  
  
@param coordinateType [in] - specifies whether the coordinates are relative to  
                        the screen or the parent object (for available  
                        constants refer to nsIAccessibleCoordinateType)  
@param x [in] - defines the x coordinate  
@param y [in] - defines the y coordinate  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>coordinateType</td>
<td>[in] - specifies whether the coordinates are relative to  
                        the screen or the parent object (for available  
                        constants refer to nsIAccessibleCoordinateType)  
</td>
</tr>

<tr>
<td>x</td>
<td>[in] - defines the x coordinate  
</td>
</tr>

<tr>
<td>y</td>
<td>[in] - defines the y coordinate  
</td>
</tr>

</table>

## Attributes ##

### parent ###
<pre>  
Parent node in accessible tree.  
  
</pre>
### nextSibling ###
<pre>  
Next sibling in accessible tree  
  
</pre>
### previousSibling ###
<pre>  
Previous sibling in accessible tree  
  
</pre>
### firstChild ###
<pre>  
First child in accessible tree  
  
</pre>
### lastChild ###
<pre>  
Last child in accessible tree  
  
</pre>
### children ###
<pre>  
Array of all this element's children.  
  
</pre>
### childCount ###
<pre>  
Number of accessible children  
  
</pre>
### indexInParent ###
<pre>  
The 0-based index of this accessible in its parent's list of children,  
or -1 if this accessible does not have a parent.  
  
</pre>
### DOMNode ###
<pre>  
The DOM node this nsIAccessible is associated with.  
  
</pre>
### document ###
<pre>  
The document accessible that this access node resides in.  
  
</pre>
### rootDocument ###
<pre>  
The root document accessible that this access node resides in.  
  
</pre>
### language ###
<pre>  
The language for the current DOM node, e.g. en, de, etc.  
  
</pre>
### name ###
<pre>  
Accessible name -- the main text equivalent for this node. The name is  
specified by ARIA or by native markup. Example of ARIA markup is  
aria-labelledby attribute placed on element of this accessible. Example  
of native markup is HTML label linked with HTML element of this accessible.  
  
Value can be string or null. A null value indicates that AT may attempt to  
compute the name. Any string value, including the empty string, should be  
considered author-intentional, and respected.  
  
</pre>
### value ###
<pre>  
Accessible value -- a number or a secondary text equivalent for this node  
Widgets that use role attribute can force a value using the valuenow attribute  
  
</pre>
### description ###
<pre>  
Accessible description -- long text associated with this node  
  
</pre>
### accessKey ###
<pre>  
Provides localized string of accesskey name, such as Alt+D.  
The modifier may be affected by user and platform preferences.  
Usually alt+letter, or just the letter alone for menu items.   
  
</pre>
### keyboardShortcut ###
<pre>  
Provides localized string of global keyboard accelerator for default  
action, such as Ctrl+O for Open file  
  
</pre>
### role ###
<pre>  
Enumerated accessible role (see the constants defined in nsIAccessibleRole).  
  
@note  The values might depend on platform because of variations. Widgets  
       can use ARIA role attribute to force the final role.  
  
</pre>
### help ###
<pre>  
Help text associated with node  
  
</pre>
### focusedChild ###
<pre>  
Focused accessible child of node  
  
</pre>
### attributes ###
<pre>  
Attributes of accessible  
  
</pre>
### actionCount ###
<pre>  
The number of accessible actions associated with this accessible  
  
</pre>