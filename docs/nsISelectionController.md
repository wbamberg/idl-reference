---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/base/nsISelectionController.idl">Source file</a>
</div>

# nsISelectionController #

## Methods ##

### setDisplaySelection(toggle) ###
<pre>  
SetDisplaySelection will set the display mode for the selection. OFF,ON,DISABLED  
  
</pre>
### getDisplaySelection() ###
<pre>  
GetDisplaySelection will get the display mode for the selection. OFF,ON,DISABLED  
  
</pre>
### getSelection(type) ###
<pre>  
GetSelection will return the selection that the presentation  
 shell may implement.  
  
@param aType will hold the type of selection //SelectionType  
@param _return will hold the return value  
  
</pre>
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
<pre>  
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
  
</pre>
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
<pre>  
RepaintSelection repaints the selection specified by aType.  
  
@param aType specifies the selection to repaint.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aType</td>
<td>specifies the selection to repaint.  
</td>
</tr>

</table>

### setCaretEnabled(enabled) ###
<pre>  
Set the caret as enabled or disabled. An enabled caret will  
draw or blink when made visible. A disabled caret will never show up.  
Can be called any time.  
@param aEnable PR_TRUE to enable caret.  PR_FALSE to disable.  
@return always NS_OK  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aEnable</td>
<td>PR_TRUE to enable caret.  PR_FALSE to disable.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>always NS_OK  
</td>
</tr>

</table>

### setCaretReadOnly(readOnly) ###
<pre>  
Set the caret readonly or not. An readonly caret will  
draw but not blink when made visible.   
@param aReadOnly PR_TRUE to enable caret.  PR_FALSE to disable.  
@return always NS_OK  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aReadOnly</td>
<td>PR_TRUE to enable caret.  PR_FALSE to disable.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>always NS_OK  
</td>
</tr>

</table>

### getCaretEnabled() ###
<pre>  
Gets the current state of the caret.  
@param aEnabled  [OUT] set to the current caret state, as set by SetCaretEnabled  
@return   if aOutEnabled==null, returns NS_ERROR_INVALID_ARG  
          else NS_OK  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aEnabled</td>
<td>[OUT] set to the current caret state, as set by SetCaretEnabled  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>if aOutEnabled==null, returns NS_ERROR_INVALID_ARG  
          else NS_OK  
</td>
</tr>

</table>

### setCaretVisibilityDuringSelection(visibility) ###
<pre>  
Show the caret even in selections. By default the caret is hidden unless the  
selection is collapsed. Use this function to show the caret even in selections.  
@param aVisibility PR_TRUE to show the caret in selections.  PR_FALSE to hide.  
@return always NS_OK  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aVisibility</td>
<td>PR_TRUE to show the caret in selections.  PR_FALSE to hide.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>always NS_OK  
</td>
</tr>

</table>

### characterMove(forward, extend) ###
<pre> CharacterMove will move the selection one character forward/backward in the document.  
 this will also have the effect of collapsing the selection if the aExtend = PR_FALSE  
 the "point" of selection that is extended is considered the "focus" point.   
 or the last point adjusted by the selection.  
 @param aForward forward or backward if PR_FALSE  
 @param aExtend  should it collapse the selection of extend it?  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aForward</td>
<td>forward or backward if PR_FALSE  
</td>
</tr>

<tr>
<td>aExtend</td>
<td>should it collapse the selection of extend it?  
</td>
</tr>

</table>

### characterExtendForDelete() ###
<pre>  
CharacterExtendForDelete will extend the selection one character cell  
forward in the document.  
this method is used internally for handling del key.  
  
</pre>
### characterExtendForBackspace() ###
<pre>  
CharacterExtendForBackspace will extend the selection one character cell  
backward in the document.  
this method is used internally for handling backspace key only when we're  
after UTF-16 surrogates.  
  
</pre>
### wordMove(forward, extend) ###
<pre> WordMove will move the selection one word forward/backward in the document.  
 this will also have the effect of collapsing the selection if the aExtend = PR_FALSE  
 the "point" of selection that is extended is considered the "focus" point.   
 or the last point adjusted by the selection.  
 @param aForward forward or backward if PR_FALSE  
 @param aExtend  should it collapse the selection of extend it?  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aForward</td>
<td>forward or backward if PR_FALSE  
</td>
</tr>

<tr>
<td>aExtend</td>
<td>should it collapse the selection of extend it?  
</td>
</tr>

</table>

### wordExtendForDelete(forward) ###
<pre> wordExtendForDelete will extend the selection one word forward/backward in the document.  
 this method is used internally for handling ctrl[option]-backspace and ctrl[option]-del.  
 @param aForward forward or backward if PR_FALSE  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aForward</td>
<td>forward or backward if PR_FALSE  
</td>
</tr>

</table>

### lineMove(forward, extend) ###
<pre> LineMove will move the selection one line forward/backward in the document.  
 this will also have the effect of collapsing the selection if the aExtend = PR_FALSE  
 the "point" of selection that is extended is considered the "focus" point.   
 or the last point adjusted by the selection.  
 @param aForward forward or backward if PR_FALSE  
 @param aExtend  should it collapse the selection of extend it?  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aForward</td>
<td>forward or backward if PR_FALSE  
</td>
</tr>

<tr>
<td>aExtend</td>
<td>should it collapse the selection of extend it?  
</td>
</tr>

</table>

### intraLineMove(forward, extend) ###
<pre> IntraLineMove will move the selection to the front of the line or end of the line  
 in the document.  
 this will also have the effect of collapsing the selection if the aExtend = PR_FALSE  
 the "point" of selection that is extended is considered the "focus" point.   
 or the last point adjusted by the selection.  
 @param aForward forward or backward if PR_FALSE  
 @param aExtend  should it collapse the selection of extend it?  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aForward</td>
<td>forward or backward if PR_FALSE  
</td>
</tr>

<tr>
<td>aExtend</td>
<td>should it collapse the selection of extend it?  
</td>
</tr>

</table>

### pageMove(forward, extend) ###
<pre> PageMove will move the selection one page forward/backward in the document.  
 this will also have the effect of collapsing the selection if the aExtend = PR_FALSE  
 the "point" of selection that is extended is considered the "focus" point.   
 or the last point adjusted by the selection.  
 @param aForward forward or backward if PR_FALSE  
 @param aExtend  should it collapse the selection of extend it?  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aForward</td>
<td>forward or backward if PR_FALSE  
</td>
</tr>

<tr>
<td>aExtend</td>
<td>should it collapse the selection of extend it?  
</td>
</tr>

</table>

### completeScroll(forward) ###
<pre> CompleteScroll will move page view to the top or bottom of the document  
 @param aForward forward or backward if PR_FALSE  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aForward</td>
<td>forward or backward if PR_FALSE  
</td>
</tr>

</table>

### completeMove(forward, extend) ###
<pre> CompleteMove will move page view to the top or bottom of the document  
 this will also have the effect of collapsing the selection if the aExtend = PR_FALSE  
 the "point" of selection that is extended is considered the "focus" point.   
 or the last point adjusted by the selection.  
 @param aForward forward or backward if PR_FALSE  
 @param aExtend  should it collapse the selection of extend it?  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aForward</td>
<td>forward or backward if PR_FALSE  
</td>
</tr>

<tr>
<td>aExtend</td>
<td>should it collapse the selection of extend it?  
</td>
</tr>

</table>

### scrollPage(forward) ###
<pre> ScrollPage will scroll the page without affecting the selection.  
 @param aForward scroll forward or backwards in selection  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aForward</td>
<td>scroll forward or backwards in selection  
</td>
</tr>

</table>

### scrollLine(forward) ###
<pre> ScrollLine will scroll line up or down dependent on the boolean  
 @param aForward scroll forward or backwards in selection  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aForward</td>
<td>scroll forward or backwards in selection  
</td>
</tr>

</table>

### scrollCharacter(right) ###
<pre> ScrollCharacter will scroll right or left dependent on the boolean  
 @param aRight if true will scroll right. if not will scroll left.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aRight</td>
<td>if true will scroll right. if not will scroll left.  
</td>
</tr>

</table>

### selectAll() ###
<pre> SelectAll will select the whole page  
  
</pre>
### checkVisibility(node, startOffset, endOffset) ###
<pre> CheckVisibility will return true if textnode and offsets are actually rendered   
 in the current precontext.  
 @param aNode textNode to test  
 @param aStartOffset  offset in dom to first char of textnode to test  
 @param aEndOffset    offset in dom to last char of textnode to test  
 @param aReturnBool   boolean returned TRUE if visible FALSE if not  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aNode</td>
<td>textNode to test  
</td>
</tr>

<tr>
<td>aStartOffset</td>
<td>offset in dom to first char of textnode to test  
</td>
</tr>

<tr>
<td>aEndOffset</td>
<td>offset in dom to last char of textnode to test  
</td>
</tr>

<tr>
<td>aReturnBool</td>
<td>boolean returned TRUE if visible FALSE if not  
</td>
</tr>

</table>

### checkVisibilityContent(node, startOffset, endOffset) ###

## Attributes ##

### caretVisible ###
<pre>  
This is true if the caret is enabled, visible, and currently blinking.  
This is still true when the caret is enabled, visible, but in its "off"  
blink cycle.  
  
</pre>
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
