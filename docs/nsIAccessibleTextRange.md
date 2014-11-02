---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/accessible/interfaces/nsIAccessibleTextRange.idl">Source file</a>
</div>
# nsIAccessibleTextRange #
  
A range representing a piece of text in the document.  
  

## Methods ##

### compare(aOtherRange) ###
  
Return true if this range has the same end points of the given range.  
  

### compareEndPoints(aEndPoint, aOtherRange, aOtherRangeEndPoint) ###
  
Compare this and given ranges end points.  
  
@return -1/0/1 if this range end point is before/equal/after the given  
         range end point.  
  

#### Returns ####

<table>

<tr>
<td>-1/0/1 if this range end point is before/equal/after the given  
         range end point.  
</td>
</tr>

</table>

### move(aUnit, aCount) ###
  
 Move the boundary(ies) by the given number of the unit.  
  

### moveStart(aUnit, aCount) ###

### moveEnd(aUnit, aCount) ###

### normalize(aUnit) ###
  
Normalize the range to the closest unit of the given type.  
  

### findText(aText, aIsBackward, aIsIgnoreCase) ###
  
Return range enclosing the found text.  
  

### findAttr(aAttr, aValue, aIsBackward) ###
  
Return range enslosing the text having requested attribute.  
  

### addToSelection() ###
  
Add/remove the text range from selection.  
  

### removeFromSelection() ###

### select() ###

### scrollIntoView(aHow) ###
  
Scroll the range into view.  
  

## Attributes ##

### startContainer ###

### startOffset ###

### endContainer ###

### endOffset ###

### container ###
  
Return an accessible containing the whole range  
  

### embeddedChildren ###
  
Return embedded children within the range.  
  

### text ###
  
Return text within the range.  
  

### bounds ###
  
Return list of rects of the range.  
  

## Constants ##

### EndPoint_Start ###
  
The two endpoints of the range (starting and ending).  
  

### EndPoint_End ###

### FormatUnit ###

### WordUnit ###

### LineUnit ###

### ParagraphUnit ###

### PageUnit ###

### DocumentUnit ###

### AnimationStyleAttr ###
  
Text attributes. Used in conjunction with findAttrs().  
  

### AnnotationObjectsAttr ###

### AnnotationTypesAttr ###

### BackgroundColorAttr ###

### BulletStyleAttr ###

### CapStyleAttr ###

### CaretBidiModeAttr ###

### CaretPositionAttr ###

### CultureAttr ###

### FontNameAttr ###

### FontSizeAttr ###

### FontWeightAttr ###

### ForegroundColorAttr ###

### HorizontalTextAlignmentAttr ###

### IndentationFirstLineAttr ###

### IndentationLeadingAttr ###

### IndentationTrailingAttr ###

### IsActiveAttr ###

### IsHiddenAttr ###

### IsItalicAttr ###

### IsReadOnlyAttr ###

### IsSubscriptAttr ###

### IsSuperscriptAttr ###

### LinkAttr ###

### MarginBottomAttr ###

### MarginLeadingAttr ###

### MarginTopAttr ###

### MarginTrailingAttr ###

### OutlineStylesAttr ###

### OverlineColorAttr ###

### OverlineStyleAttr ###

### SelectionActiveEndAttr ###

### StrikethroughColorAttr ###

### StrikethroughStyleAttr ###

### StyleIdAttr ###

### StyleNameAttr ###

### TabsAttr ###

### TextFlowDirectionsAttr ###

### UnderlineColorAttr ###

### UnderlineStyleAttr ###

### AlignToTop ###

### AlignToBottom ###
