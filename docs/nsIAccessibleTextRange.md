---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/accessible/interfaces/nsIAccessibleTextRange.idl">Source file</a>
</div>

# nsIAccessibleTextRange #
<pre>  
A range representing a piece of text in the document.  
  
</pre>
## Methods ##

### compare(aOtherRange) ###
<pre>  
Return true if this range has the same end points of the given range.  
  
</pre>
### compareEndPoints(aEndPoint, aOtherRange, aOtherRangeEndPoint) ###
<pre>  
Compare this and given ranges end points.  
  
@return -1/0/1 if this range end point is before/equal/after the given  
         range end point.  
  
</pre>
#### Returns ####

<table>

<tr>
<td>-1/0/1 if this range end point is before/equal/after the given  
         range end point.  
</td>
</tr>

</table>

### move(aUnit, aCount) ###
<pre>  
 Move the boundary(ies) by the given number of the unit.  
  
</pre>
### moveStart(aUnit, aCount) ###

### moveEnd(aUnit, aCount) ###

### normalize(aUnit) ###
<pre>  
Normalize the range to the closest unit of the given type.  
  
</pre>
### findText(aText, aIsBackward, aIsIgnoreCase) ###
<pre>  
Return range enclosing the found text.  
  
</pre>
### findAttr(aAttr, aValue, aIsBackward) ###
<pre>  
Return range enslosing the text having requested attribute.  
  
</pre>
### addToSelection() ###
<pre>  
Add/remove the text range from selection.  
  
</pre>
### removeFromSelection() ###

### select() ###

### scrollIntoView(aHow) ###
<pre>  
Scroll the range into view.  
  
</pre>
## Attributes ##

### startContainer ###

### startOffset ###

### endContainer ###

### endOffset ###

### container ###
<pre>  
Return an accessible containing the whole range  
  
</pre>
### embeddedChildren ###
<pre>  
Return embedded children within the range.  
  
</pre>
### text ###
<pre>  
Return text within the range.  
  
</pre>
### bounds ###
<pre>  
Return list of rects of the range.  
  
</pre>
## Constants ##

### EndPoint_Start ###
<pre>  
The two endpoints of the range (starting and ending).  
  
</pre>
### EndPoint_End ###

### FormatUnit ###

### WordUnit ###

### LineUnit ###

### ParagraphUnit ###

### PageUnit ###

### DocumentUnit ###

### AnimationStyleAttr ###
<pre>  
Text attributes. Used in conjunction with findAttrs().  
  
</pre>
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
