---
layout: default
---

# nsIAccessibleTextRange #

A range representing a piece of text in the document.


## startContainer ##

## startOffset ##

## endContainer ##

## endOffset ##

## container ##

Return an accessible containing the whole range


## embeddedChildren ##

Return embedded children within the range.


## compare ##

Return true if this range has the same end points of the given range.


## EndPoint_Start ##

The two endpoints of the range (starting and ending).


## EndPoint_End ##

## compareEndPoints ##

Compare this and given ranges end points.

@return -1/0/1 if this range end point is before/equal/after the given
         range end point.


## text ##

Return text within the range.


## bounds ##

Return list of rects of the range.


## FormatUnit ##

## WordUnit ##

## LineUnit ##

## ParagraphUnit ##

## PageUnit ##

## DocumentUnit ##

## move ##

 Move the boundary(ies) by the given number of the unit.


## moveStart ##

## moveEnd ##

## normalize ##

Normalize the range to the closest unit of the given type.


## findText ##

Return range enclosing the found text.


## AnimationStyleAttr ##

Text attributes. Used in conjunction with findAttrs().


## AnnotationObjectsAttr ##

## AnnotationTypesAttr ##

## BackgroundColorAttr ##

## BulletStyleAttr ##

## CapStyleAttr ##

## CaretBidiModeAttr ##

## CaretPositionAttr ##

## CultureAttr ##

## FontNameAttr ##

## FontSizeAttr ##

## FontWeightAttr ##

## ForegroundColorAttr ##

## HorizontalTextAlignmentAttr ##

## IndentationFirstLineAttr ##

## IndentationLeadingAttr ##

## IndentationTrailingAttr ##

## IsActiveAttr ##

## IsHiddenAttr ##

## IsItalicAttr ##

## IsReadOnlyAttr ##

## IsSubscriptAttr ##

## IsSuperscriptAttr ##

## LinkAttr ##

## MarginBottomAttr ##

## MarginLeadingAttr ##

## MarginTopAttr ##

## MarginTrailingAttr ##

## OutlineStylesAttr ##

## OverlineColorAttr ##

## OverlineStyleAttr ##

## SelectionActiveEndAttr ##

## StrikethroughColorAttr ##

## StrikethroughStyleAttr ##

## StyleIdAttr ##

## StyleNameAttr ##

## TabsAttr ##

## TextFlowDirectionsAttr ##

## UnderlineColorAttr ##

## UnderlineStyleAttr ##

## findAttr ##

Return range enslosing the text having requested attribute.


## addToSelection ##

Add/remove the text range from selection.


## removeFromSelection ##

## select ##

## AlignToTop ##

## AlignToBottom ##

## scrollIntoView ##

Scroll the range into view.

