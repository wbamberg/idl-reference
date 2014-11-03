---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/base/nsISelectionPrivate.idl">Source file</a>
</div>

# nsISelectionPrivate #

## Methods ##

### startBatchChanges() ###

### endBatchChanges() ###

### toStringWithFormat(formatType, flags, wrapColumn) ###

### addSelectionListener(newListener) ###

### removeSelectionListener(listenerToRemove) ###

### getTableSelectionType(range) ###
<pre> Test if supplied range points to a single table element:  
   Result is one of above constants. "None" means  
   a table element isn't selected.  
  
</pre>
### getCachedFrameOffset(aFrame, inOffset, aPoint) ###

### setTextRangeStyle(range, textRangeStyle) ###
<pre>  
Set the painting style for the range. The range must be a range in  
the selection. The textRangeStyle will be used by text frame  
when it is painting the selection.  
  
</pre>
### getSelectionDirection() ###
<pre>  
Get the direction of the selection.  
  
</pre>
### setSelectionDirection(aDirection) ###

### GetRangesForInterval(beginNode, beginOffset, endNode, endOffset, allowAdjacent, resultCount, results) ###
<pre>  
Return array of ranges intersecting with the given DOM interval.  
  
</pre>
### GetRangesForIntervalArray(beginNode, beginOffset, endNode, endOffset, allowAdjacent, results) ###

### scrollIntoView(aRegion, aIsSynchronous, aVPercent, aHPercent) ###
<pre>  
Scrolls a region of the selection, so that it is visible in  
the scrolled view.  
  
@param aRegion - the region inside the selection to scroll into view  
                 (see selection region constants defined in  
                  nsISelectionController).  
@param aIsSynchronous - when true, scrolls the selection into view  
                        before returning. If false, posts a request which  
                        is processed at some point after the method returns.  
@param aVPercent - how to align the frame vertically.  
@param aHPercent - how to align the frame horizontally.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aRegion</td>
<td>- the region inside the selection to scroll into view  
                 (see selection region constants defined in  
                  nsISelectionController).  
</td>
</tr>

<tr>
<td>aIsSynchronous</td>
<td>- when true, scrolls the selection into view  
                        before returning. If false, posts a request which  
                        is processed at some point after the method returns.  
</td>
</tr>

<tr>
<td>aVPercent</td>
<td>- how to align the frame vertically.  
</td>
</tr>

<tr>
<td>aHPercent</td>
<td>- how to align the frame horizontally.  
</td>
</tr>

</table>

### scrollIntoViewInternal(aRegion, aIsSynchronous, aVertical, aHorizontal) ###
<pre>  
Scrolls a region of the selection, so that it is visible in  
the scrolled view.  
  
@param aRegion - the region inside the selection to scroll into view  
                 (see selection region constants defined in  
                  nsISelectionController).  
@param aIsSynchronous - when true, scrolls the selection into view  
                        before returning. If false, posts a request which  
                        is processed at some point after the method returns.  
@param aVertical - how to align the frame vertically and when.  
                   See nsIPresShell.h:ScrollAxis for details.  
@param aHorizontal - how to align the frame horizontally and when.  
                   See nsIPresShell.h:ScrollAxis for details.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aRegion</td>
<td>- the region inside the selection to scroll into view  
                 (see selection region constants defined in  
                  nsISelectionController).  
</td>
</tr>

<tr>
<td>aIsSynchronous</td>
<td>- when true, scrolls the selection into view  
                        before returning. If false, posts a request which  
                        is processed at some point after the method returns.  
</td>
</tr>

<tr>
<td>aVertical</td>
<td>- how to align the frame vertically and when.  
                   See nsIPresShell.h:ScrollAxis for details.  
</td>
</tr>

<tr>
<td>aHorizontal</td>
<td>- how to align the frame horizontally and when.  
                   See nsIPresShell.h:ScrollAxis for details.  
</td>
</tr>

</table>

### selectionLanguageChange(langRTL) ###
<pre>  
Modifies the cursor Bidi level after a change in keyboard direction  
@param langRTL is PR_TRUE if the new language is right-to-left or  
               PR_FALSE if the new language is left-to-right.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>langRTL</td>
<td>is PR_TRUE if the new language is right-to-left or  
               PR_FALSE if the new language is left-to-right.  
</td>
</tr>

</table>

## Attributes ##

### interlinePosition ###

### ancestorLimiter ###

### canCacheFrameOffset ###

### type ###
<pre>  
Returns the type of the selection (see nsISelectionController for  
available constants).  
  
</pre>
## Constants ##

### ENDOFPRECEDINGLINE ###

### STARTOFNEXTLINE ###

### TABLESELECTION_NONE ###

### TABLESELECTION_CELL ###

### TABLESELECTION_ROW ###

### TABLESELECTION_COLUMN ###

### TABLESELECTION_TABLE ###

### TABLESELECTION_ALLCELLS ###
