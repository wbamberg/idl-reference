---
layout: default
---

# nsISelectionController #

## Methods ##

### setDisplaySelection(toggle) ###
  
SetDisplaySelection will set the display mode for the selection. OFF,ON,DISABLED  
  

### getDisplaySelection() ###
  
GetDisplaySelection will get the display mode for the selection. OFF,ON,DISABLED  
  

### getSelection(type) ###
  
GetSelection will return the selection that the presentation  
 shell may implement.  
  
@param aType will hold the type of selection //SelectionType  
@param _return will hold the return value  
  

#### Parameters ####

<table>

<tr>
<td>aType</td>
<td>will hold the type of selection //SelectionType  
</td>
</tr>

<tr>
<td>_return</td>
<td>will hold the return value  
</td>
</tr>

</table>

### scrollSelectionIntoView(type, region, flags) ###
  
ScrollSelectionIntoView scrolls a region of the selection,  
so that it is visible in the scrolled view.  
  
@param aType the selection to scroll into view. //SelectionType  
@param aRegion the region inside the selection to scroll into view. //SelectionRegion  
@param aFlags the scroll flags.  Valid bits include:  
SCROLL_SYNCHRONOUS: when set, scrolls the selection into view  
before returning. If not set, posts a request which is processed  
at some point after the method returns.  
SCROLL_FIRST_ANCESTOR_ONLY: if set, only the first ancestor will be scrolled  
into view.  
SCROLL_OVERFLOW_HIDDEN: if set, scrolls even if the overflow is specified  
as hidden.  
  
Note that if isSynchronous is true, then this might flush the pending  
reflow. It's dangerous for some objects. See bug 418470 comment 12.  
  

#### Parameters ####

<table>

<tr>
<td>aType</td>
<td>the selection to scroll into view. //SelectionType  
</td>
</tr>

<tr>
<td>aRegion</td>
<td>the region inside the selection to scroll into view. //SelectionRegion  
</td>
</tr>

<tr>
<td>aFlags</td>
<td>the scroll flags.  Valid bits include:  
SCROLL_SYNCHRONOUS: when set, scrolls the selection into view  
before returning. If not set, posts a request which is processed  
at some point after the method returns.  
SCROLL_FIRST_ANCESTOR_ONLY: if set, only the first ancestor will be scrolled  
into view.  
SCROLL_OVERFLOW_HIDDEN: if set, scrolls even if the overflow is specified  
as hidden.  
</td>
</tr>

</table>

### repaintSelection(type) ###
  
RepaintSelection repaints the selection specified by aType.  
  
@param aType specifies the selection to repaint.  
  

#### Parameters ####

<table>

<tr>
<td>aType</td>
<td>specifies the selection to repaint.  
</td>
</tr>

</table>

### setCaretEnabled(enabled) ###
  
Set the caret as enabled or disabled. An enabled caret will  
draw or blink when made visible. A disabled caret will never show up.  
Can be called any time.  
@param aEnable PR_TRUE to enable caret.  PR_FALSE to disable.  
@return always NS_OK  
  

#### Parameters ####

<table>

<tr>
<td>aEnable</td>
<td>PR_TRUE to enable caret.  PR_FALSE to disable.  
</td>
</tr>

</table>

### setCaretReadOnly(readOnly) ###
  
Set the caret readonly or not. An readonly caret will  
draw but not blink when made visible.   
@param aReadOnly PR_TRUE to enable caret.  PR_FALSE to disable.  
@return always NS_OK  
  

#### Parameters ####

<table>

<tr>
<td>aReadOnly</td>
<td>PR_TRUE to enable caret.  PR_FALSE to disable.  
</td>
</tr>

</table>

### getCaretEnabled() ###
  
Gets the current state of the caret.  
@param aEnabled  [OUT] set to the current caret state, as set by SetCaretEnabled  
@return   if aOutEnabled==null, returns NS_ERROR_INVALID_ARG  
          else NS_OK  
  

#### Parameters ####

<table>

<tr>
<td>aEnabled</td>
<td>[OUT] set to the current caret state, as set by SetCaretEnabled  
</td>
</tr>

</table>

### setCaretVisibilityDuringSelection(visibility) ###
  
Show the caret even in selections. By default the caret is hidden unless the  
selection is collapsed. Use this function to show the caret even in selections.  
@param aVisibility PR_TRUE to show the caret in selections.  PR_FALSE to hide.  
@return always NS_OK  
  

#### Parameters ####

<table>

<tr>
<td>aVisibility</td>
<td>PR_TRUE to show the caret in selections.  PR_FALSE to hide.  
</td>
</tr>

</table>

### characterMove(forward, extend) ###
 CharacterMove will move the selection one character forward/backward in the document.  
 this will also have the effect of collapsing the selection if the aExtend = PR_FALSE  
 the "point" of selection that is extended is considered the "focus" point.   
 or the last point adjusted by the selection.  
 @param aForward forward or backward if PR_FALSE  
 @param aExtend  should it collapse the selection of extend it?  
  

### characterExtendForDelete() ###
  
CharacterExtendForDelete will extend the selection one character cell  
forward in the document.  
this method is used internally for handling del key.  
  

### characterExtendForBackspace() ###
  
CharacterExtendForBackspace will extend the selection one character cell  
backward in the document.  
this method is used internally for handling backspace key only when we're  
after UTF-16 surrogates.  
  

### wordMove(forward, extend) ###
 WordMove will move the selection one word forward/backward in the document.  
 this will also have the effect of collapsing the selection if the aExtend = PR_FALSE  
 the "point" of selection that is extended is considered the "focus" point.   
 or the last point adjusted by the selection.  
 @param aForward forward or backward if PR_FALSE  
 @param aExtend  should it collapse the selection of extend it?  
  

### wordExtendForDelete(forward) ###
 wordExtendForDelete will extend the selection one word forward/backward in the document.  
 this method is used internally for handling ctrl[option]-backspace and ctrl[option]-del.  
 @param aForward forward or backward if PR_FALSE  
  

### lineMove(forward, extend) ###
 LineMove will move the selection one line forward/backward in the document.  
 this will also have the effect of collapsing the selection if the aExtend = PR_FALSE  
 the "point" of selection that is extended is considered the "focus" point.   
 or the last point adjusted by the selection.  
 @param aForward forward or backward if PR_FALSE  
 @param aExtend  should it collapse the selection of extend it?  
  

### intraLineMove(forward, extend) ###
 IntraLineMove will move the selection to the front of the line or end of the line  
 in the document.  
 this will also have the effect of collapsing the selection if the aExtend = PR_FALSE  
 the "point" of selection that is extended is considered the "focus" point.   
 or the last point adjusted by the selection.  
 @param aForward forward or backward if PR_FALSE  
 @param aExtend  should it collapse the selection of extend it?  
  

### pageMove(forward, extend) ###
 PageMove will move the selection one page forward/backward in the document.  
 this will also have the effect of collapsing the selection if the aExtend = PR_FALSE  
 the "point" of selection that is extended is considered the "focus" point.   
 or the last point adjusted by the selection.  
 @param aForward forward or backward if PR_FALSE  
 @param aExtend  should it collapse the selection of extend it?  
  

### completeScroll(forward) ###
 CompleteScroll will move page view to the top or bottom of the document  
 @param aForward forward or backward if PR_FALSE  
  

### completeMove(forward, extend) ###
 CompleteMove will move page view to the top or bottom of the document  
 this will also have the effect of collapsing the selection if the aExtend = PR_FALSE  
 the "point" of selection that is extended is considered the "focus" point.   
 or the last point adjusted by the selection.  
 @param aForward forward or backward if PR_FALSE  
 @param aExtend  should it collapse the selection of extend it?  
  

### scrollPage(forward) ###
 ScrollPage will scroll the page without affecting the selection.  
 @param aForward scroll forward or backwards in selection  
  

### scrollLine(forward) ###
 ScrollLine will scroll line up or down dependent on the boolean  
 @param aForward scroll forward or backwards in selection  
  

### scrollCharacter(right) ###
 ScrollCharacter will scroll right or left dependent on the boolean  
 @param aRight if true will scroll right. if not will scroll left.  
  

### selectAll() ###
 SelectAll will select the whole page  
  

### checkVisibility(node, startOffset, endOffset) ###
 CheckVisibility will return true if textnode and offsets are actually rendered   
 in the current precontext.  
 @param aNode textNode to test  
 @param aStartOffset  offset in dom to first char of textnode to test  
 @param aEndOffset    offset in dom to last char of textnode to test  
 @param aReturnBool   boolean returned TRUE if visible FALSE if not  
  

### checkVisibilityContent(node, startOffset, endOffset) ###

## Attributes ##

### caretVisible ###
  
This is true if the caret is enabled, visible, and currently blinking.  
This is still true when the caret is enabled, visible, but in its "off"  
blink cycle.  
  

## Constants ##

### SELECTION_NONE ###

### SELECTION_NORMAL ###

### SELECTION_SPELLCHECK ###

### SELECTION_IME_RAWINPUT ###

### SELECTION_IME_SELECTEDRAWTEXT ###

### SELECTION_IME_CONVERTEDTEXT ###

### SELECTION_IME_SELECTEDCONVERTEDTEXT ###

### SELECTION_ACCESSIBILITY ###

### SELECTION_FIND ###

### SELECTION_URLSECONDARY ###

### NUM_SELECTIONTYPES ###

### SELECTION_ANCHOR_REGION ###

### SELECTION_FOCUS_REGION ###

### SELECTION_WHOLE_SELECTION ###

### NUM_SELECTION_REGIONS ###

### SELECTION_OFF ###

### SELECTION_HIDDEN ###

### SELECTION_ON ###

### SELECTION_DISABLED ###

### SELECTION_ATTENTION ###

### SCROLL_SYNCHRONOUS ###

### SCROLL_FIRST_ANCESTOR_ONLY ###

### SCROLL_CENTER_VERTICALLY ###

### SCROLL_OVERFLOW_HIDDEN ###
