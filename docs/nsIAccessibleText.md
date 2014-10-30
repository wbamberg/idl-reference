---
layout: default
---

# nsIAccessibleText #

## Methods ##

### getText(startOffset, endOffset) ###
  
String methods may need to return multibyte-encoded strings,  
since some locales can't be encoded using 16-bit chars.  
So the methods below might return UTF-16 strings, or they could  
return "string" values which are UTF-8.  
  

### getTextAfterOffset(offset, boundaryType, startOffset, endOffset) ###

### getTextAtOffset(offset, boundaryType, startOffset, endOffset) ###

### getTextBeforeOffset(offset, boundaryType, startOffset, endOffset) ###

### getCharacterAtOffset(offset) ###
  
It would be better to return an unsigned long here,  
to allow unicode chars > 16 bits  
  

### getTextAttributes(includeDefAttrs, offset, rangeStartOffset, rangeEndOffset) ###
  
Get the accessible start/end offsets around the given offset,  
return the text attributes for this range of text.  
  
@param  includeDefAttrs   [in] points whether text attributes applied to  
                          the entire accessible should be included or not.  
@param  offset            [in] text offset  
@param  rangeStartOffset  [out] start offset of the range of text  
@param  rangeEndOffset    [out] end offset of the range of text  
  

### getCharacterExtents(offset, x, y, width, height, coordType) ###
  
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
  

### getRangeExtents(startOffset, endOffset, x, y, width, height, coordType) ###

### getOffsetAtPoint(x, y, coordType) ###
  
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
  

### getSelectionBounds(selectionNum, startOffset, endOffset) ###

### setSelectionBounds(selectionNum, startOffset, endOffset) ###
  
Set the bounds for the given selection range  
  

### addSelection(startOffset, endOffset) ###

### removeSelection(selectionNum) ###

### scrollSubstringTo(startIndex, endIndex, scrollType) ###
  
Makes a specific part of string visible on screen.  
  
@param startIndex  0-based character offset  
@param endIndex    0-based character offset - the offset of the  
                   character just past the last character of the  
                   string  
@param scrollType  defines how to scroll (see nsIAccessibleScrollType for  
                   available constants)  
  

### scrollSubstringToPoint(startIndex, endIndex, coordinateType, x, y) ###
  
Moves the top left of a substring to a specified location.  
  
@param startIndex      0-based character offset  
@param endIndex        0-based character offset - the offset of the  
                       character just past the last character of  
                       the string  
@param coordinateType  specifies the coordinates origin (for available  
                       constants refer to nsIAccessibleCoordinateType)  
@param x               defines the x coordinate  
@param y               defines the y coordinate  
  

### getRangeByChild(child) ###
  
Return a range containing the given accessible.  
  

### getRangeAtPoint(x, y) ###
  
Return a range containing an accessible at the given point.  
  

## Attributes ##

### caretOffset ###
  
The current current caret offset.  
If set < 0 then caret will be placed  at the end of the text  
  

### characterCount ###

### selectionCount ###

### defaultTextAttributes ###
  
Return the text attributes that apply to the entire accessible.  
  

### enclosingRange ###
  
Return a range that encloses this text control or otherwise the document  
this text accessible belongs to.  
  

### selectionRanges ###
  
Return an array of disjoint ranges for selected text within the text control  
or otherwise the document this accessible belongs to.  
  

### visibleRanges ###
  
Return an array of disjoint ranges of visible text within the text control  
or otherwise the document this accessible belongs to.  
  

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
