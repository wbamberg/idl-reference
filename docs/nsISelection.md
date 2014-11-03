---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/base/nsISelection.idl">Source file</a>
</div>

# nsISelection #
<pre>  
Interface for manipulating and querying the current selected range  
of nodes within the document.  
  
@version 1.0  
  
</pre>
## Methods ##

### collapsed() ###

### getRangeAt(index) ###
<pre>  
Returns the range at the specified index.  
  
</pre>
### collapse(parentNode, offset) ###
<pre>  
Collapses the selection to a single point, at the specified offset  
in the given DOM node. When the selection is collapsed, and the content  
is focused and editable, the caret will blink there.  
@param parentNode      The given dom node where the selection will be set  
@param offset          Where in given dom node to place the selection (the offset into the given node)  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>parentNode</td>
<td>The given dom node where the selection will be set  
</td>
</tr>

<tr>
<td>offset</td>
<td>Where in given dom node to place the selection (the offset into the given node)  
</td>
</tr>

</table>

### collapseNative(parentNode, offset) ###

### extend(parentNode, offset) ###
<pre>  
Extends the selection by moving the selection end to the specified node and offset,  
preserving the selection begin position. The new selection end result will always  
be from the anchorNode to the new focusNode, regardless of direction.  
@param parentNode      The node where the selection will be extended to  
@param offset          Where in node to place the offset in the new selection end  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>parentNode</td>
<td>The node where the selection will be extended to  
</td>
</tr>

<tr>
<td>offset</td>
<td>Where in node to place the offset in the new selection end  
</td>
</tr>

</table>

### extendNative(parentNode, offset) ###

### collapseToStart() ###
<pre>  
Collapses the whole selection to a single point at the start  
of the current selection (irrespective of direction).  If content  
is focused and editable, the caret will blink there.  
  
</pre>
### collapseToEnd() ###
<pre>  
Collapses the whole selection to a single point at the end  
of the current selection (irrespective of direction).  If content  
is focused and editable, the caret will blink there.  
  
</pre>
### containsNode(node, partlyContained) ###
<pre>  
Indicates whether the node is part of the selection. If partlyContained   
is set to PR_TRUE, the function returns true when some part of the node   
is part of the selection. If partlyContained is set to PR_FALSE, the  
function only returns true when the entire node is part of the selection.  
  
</pre>
### selectAllChildren(parentNode) ###
<pre>  
Adds all children of the specified node to the selection.  
@param parentNode  the parent of the children to be added to the selection.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>parentNode</td>
<td>the parent of the children to be added to the selection.  
</td>
</tr>

</table>

### addRange(range) ###
<pre>  
Adds a range to the current selection.  
  
</pre>
### removeRange(range) ###
<pre>  
Removes a range from the current selection.  
  
</pre>
### removeAllRanges() ###
<pre>  
Removes all ranges from the current selection.  
  
</pre>
### deleteFromDocument() ###
<pre>  
Deletes this selection from document the nodes belong to.  
  
</pre>
### toString() ###
<pre>  
Returns the whole selection into a plain text string.  
  
</pre>
### modify(alter, direction, granularity) ###
<pre>  
Modifies the selection.  Note that the parameters are case-insensitive.  
  
@param alter can be one of { "move", "extend" }  
  - "move" collapses the selection to the end of the selection and  
     applies the movement direction/granularity to the collapsed  
     selection.  
  - "extend" leaves the start of the selection unchanged, and applies  
     movement direction/granularity to the end of the selection.  
@param direction can be one of { "forward", "backward", "left", "right" }  
@param granularity can be one of { "character", "word",  
                                   "line", "lineboundary" }  
  
@returns NS_ERROR_NOT_IMPLEMENTED if the granularity is "sentence",  
"sentenceboundary", "paragraph", "paragraphboundary", or  
"documentboundary".  Returns NS_ERROR_INVALID_ARG if alter, direction,  
or granularity has an unrecognized value.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>alter</td>
<td>can be one of { "move", "extend" }  
  - "move" collapses the selection to the end of the selection and  
     applies the movement direction/granularity to the collapsed  
     selection.  
  - "extend" leaves the start of the selection unchanged, and applies  
     movement direction/granularity to the end of the selection.  
</td>
</tr>

<tr>
<td>direction</td>
<td>can be one of { "forward", "backward", "left", "right" }  
</td>
</tr>

<tr>
<td>granularity</td>
<td>can be one of { "character", "word",  
                                   "line", "lineboundary" }  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>NS_ERROR_NOT_IMPLEMENTED if the granularity is "sentence",  
"sentenceboundary", "paragraph", "paragraphboundary", or  
"documentboundary".  Returns NS_ERROR_INVALID_ARG if alter, direction,  
or granularity has an unrecognized value.  
</td>
</tr>

</table>

## Attributes ##

### anchorNode ###
<pre>  
Returns the node in which the selection begins.  
  
</pre>
### anchorOffset ###
<pre>  
The offset within the (text) node where the selection begins.  
  
</pre>
### focusNode ###
<pre>  
Returns the node in which the selection ends.  
  
</pre>
### focusOffset ###
<pre>  
The offset within the (text) node where the selection ends.  
  
</pre>
### isCollapsed ###
<pre>  
Indicates if the selection is collapsed or not.  
  
</pre>
### rangeCount ###
<pre>  
Returns the number of ranges in the selection.  
  
</pre>