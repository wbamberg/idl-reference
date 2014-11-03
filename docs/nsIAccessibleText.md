---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/accessible/interfaces/nsIAccessibleText.idl">Source file</a>
</div>

# nsIAccessibleText #

## Methods ##

### getText(startOffset, endOffset) ###
<pre>  
String methods may need to return multibyte-encoded strings,  
since some locales can't be encoded using 16-bit chars.  
So the methods below might return UTF-16 strings, or they could  
return "string" values which are UTF-8.  
  
</pre>
### getTextAfterOffset(offset, boundaryType, startOffset, endOffset) ###

### getTextAtOffset(offset, boundaryType, startOffset, endOffset) ###

### getTextBeforeOffset(offset, boundaryType, startOffset, endOffset) ###

### getCharacterAtOffset(offset) ###
<pre>  
It would be better to return an unsigned long here,  
to allow unicode chars > 16 bits  
  
</pre>
### getTextAttributes(includeDefAttrs, offset, rangeStartOffset, rangeEndOffset) ###
<pre>  
Get the accessible start/end offsets around the given offset,  
return the text attributes for this range of text.  
  
@param  includeDefAttrs   [in] points whether text attributes applied to  
                          the entire accessible should be included or not.  
@param  offset            [in] text offset  
@param  rangeStartOffset  [out] start offset of the range of text  
@param  rangeEndOffset    [out] end offset of the range of text  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>includeDefAttrs</td>
<td>[in] points whether text attributes applied to  
                          the entire accessible should be included or not.  
</td>
</tr>

<tr>
<td>offset</td>
<td>[in] text offset  
</td>
</tr>

<tr>
<td>rangeStartOffset</td>
<td>[out] start offset of the range of text  
</td>
</tr>

<tr>
<td>rangeEndOffset</td>
<td>[out] end offset of the range of text  
</td>
</tr>

</table>

### getCharacterExtents(offset, x, y, width, height, coordType) ###
<pre>  
Returns the bounding box of the specified position.  
  
The virtual character after the last character of the represented text,  
i.e. the one at position length is a special case. It represents the  
current input position and will therefore typically be queried by AT more  
often than other positions. Because it does not represent an existing  
character its bounding box is defined in relation to preceding characters.  
It should be roughly equivalent to the bounding box of some character when  
inserted at the end of the text. Its height typically being the maximal  
height of all the characters in the text or the height of the preceding  
character, its width being at least one pixel so that the bounding box is  
not degenerate.  
  
@param offset - Index of the character for which to return its bounding  
                 box. The valid range is 0..length.  
@param x - X coordinate of the bounding box of the referenced character.  
@param y - Y coordinate of the bounding box of the referenced character.  
@param width - Width of the bounding box of the referenced character.  
@param height - Height of the bounding box of the referenced character.  
@param coordType - Specifies if the coordinates are relative to the screen  
                   or to the parent window (see constants declared in  
                   nsIAccessibleCoordinateType).  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>offset</td>
<td>- Index of the character for which to return its bounding  
                 box. The valid range is 0..length.  
</td>
</tr>

<tr>
<td>x</td>
<td>- X coordinate of the bounding box of the referenced character.  
</td>
</tr>

<tr>
<td>y</td>
<td>- Y coordinate of the bounding box of the referenced character.  
</td>
</tr>

<tr>
<td>width</td>
<td>- Width of the bounding box of the referenced character.  
</td>
</tr>

<tr>
<td>height</td>
<td>- Height of the bounding box of the referenced character.  
</td>
</tr>

<tr>
<td>coordType</td>
<td>- Specifies if the coordinates are relative to the screen  
                   or to the parent window (see constants declared in  
                   nsIAccessibleCoordinateType).  
</td>
</tr>

</table>

### getRangeExtents(startOffset, endOffset, x, y, width, height, coordType) ###

### getOffsetAtPoint(x, y, coordType) ###
<pre>  
Get the text offset at the given point, or return -1  
if no character exists at that point  
  
@param x - The position's x value for which to look up the index of the  
           character that is rendered on to the display at that point.  
@param y - The position's y value for which to look up the index of the  
           character that is rendered on to the display at that point.  
@param coordType - Screen coordinates or window coordinates (see constants  
                   declared in nsIAccessibleCoordinateType).  
@return offset - Index of the character under the given point or -1 if  
                 the point is invalid or there is no character under  
                 the point.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>x</td>
<td>- The position's x value for which to look up the index of the  
           character that is rendered on to the display at that point.  
</td>
</tr>

<tr>
<td>y</td>
<td>- The position's y value for which to look up the index of the  
           character that is rendered on to the display at that point.  
</td>
</tr>

<tr>
<td>coordType</td>
<td>- Screen coordinates or window coordinates (see constants  
                   declared in nsIAccessibleCoordinateType).  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>offset - Index of the character under the given point or -1 if  
                 the point is invalid or there is no character under  
                 the point.  
</td>
</tr>

</table>

### getSelectionBounds(selectionNum, startOffset, endOffset) ###

### setSelectionBounds(selectionNum, startOffset, endOffset) ###
<pre>  
Set the bounds for the given selection range  
  
</pre>
### addSelection(startOffset, endOffset) ###

### removeSelection(selectionNum) ###

### scrollSubstringTo(startIndex, endIndex, scrollType) ###
<pre>  
Makes a specific part of string visible on screen.  
  
@param startIndex  0-based character offset  
@param endIndex    0-based character offset - the offset of the  
                   character just past the last character of the  
                   string  
@param scrollType  defines how to scroll (see nsIAccessibleScrollType for  
                   available constants)  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>startIndex</td>
<td>0-based character offset  
</td>
</tr>

<tr>
<td>endIndex</td>
<td>0-based character offset - the offset of the  
                   character just past the last character of the  
                   string  
</td>
</tr>

<tr>
<td>scrollType</td>
<td>defines how to scroll (see nsIAccessibleScrollType for  
                   available constants)  
</td>
</tr>

</table>

### scrollSubstringToPoint(startIndex, endIndex, coordinateType, x, y) ###
<pre>  
Moves the top left of a substring to a specified location.  
  
@param startIndex      0-based character offset  
@param endIndex        0-based character offset - the offset of the  
                       character just past the last character of  
                       the string  
@param coordinateType  specifies the coordinates origin (for available  
                       constants refer to nsIAccessibleCoordinateType)  
@param x               defines the x coordinate  
@param y               defines the y coordinate  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>startIndex</td>
<td>0-based character offset  
</td>
</tr>

<tr>
<td>endIndex</td>
<td>0-based character offset - the offset of the  
                       character just past the last character of  
                       the string  
</td>
</tr>

<tr>
<td>coordinateType</td>
<td>specifies the coordinates origin (for available  
                       constants refer to nsIAccessibleCoordinateType)  
</td>
</tr>

<tr>
<td>x</td>
<td>defines the x coordinate  
</td>
</tr>

<tr>
<td>y</td>
<td>defines the y coordinate  
</td>
</tr>

</table>

### getRangeByChild(child) ###
<pre>  
Return a range containing the given accessible.  
  
</pre>
### getRangeAtPoint(x, y) ###
<pre>  
Return a range containing an accessible at the given point.  
  
</pre>
## Attributes ##

### caretOffset ###
<pre>  
The current current caret offset.  
If set < 0 then caret will be placed  at the end of the text  
  
</pre>
### characterCount ###

### selectionCount ###

### defaultTextAttributes ###
<pre>  
Return the text attributes that apply to the entire accessible.  
  
</pre>
### enclosingRange ###
<pre>  
Return a range that encloses this text control or otherwise the document  
this text accessible belongs to.  
  
</pre>
### selectionRanges ###
<pre>  
Return an array of disjoint ranges for selected text within the text control  
or otherwise the document this accessible belongs to.  
  
</pre>
### visibleRanges ###
<pre>  
Return an array of disjoint ranges of visible text within the text control  
or otherwise the document this accessible belongs to.  
  
</pre>
## Constants ##

### TEXT_OFFSET_END_OF_TEXT ###

### TEXT_OFFSET_CARET ###

### BOUNDARY_CHAR ###

### BOUNDARY_WORD_START ###

### BOUNDARY_WORD_END ###

### BOUNDARY_SENTENCE_START ###

### BOUNDARY_SENTENCE_END ###

### BOUNDARY_LINE_START ###

### BOUNDARY_LINE_END ###
