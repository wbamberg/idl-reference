---
layout: default
---

# nsISelectionPrivate #

## Methods ##

### startBatchChanges ###

### endBatchChanges ###

### toStringWithFormat ###

### addSelectionListener ###

### removeSelectionListener ###

### getTableSelectionType ###
 Test if supplied range points to a single table element:
   Result is one of above constants. "None" means
   a table element isn't selected.


### getCachedFrameOffset ###

### setTextRangeStyle ###

Set the painting style for the range. The range must be a range in
the selection. The textRangeStyle will be used by text frame
when it is painting the selection.


### getSelectionDirection ###

Get the direction of the selection.


### setSelectionDirection ###

### GetRangesForInterval ###

Return array of ranges intersecting with the given DOM interval.


### GetRangesForIntervalArray ###

### scrollIntoView ###

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


### scrollIntoViewInternal ###

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


### selectionLanguageChange ###

Modifies the cursor Bidi level after a change in keyboard direction
@param langRTL is PR_TRUE if the new language is right-to-left or
               PR_FALSE if the new language is left-to-right.


## Attributes ##

### interlinePosition ###

### ancestorLimiter ###

### canCacheFrameOffset ###

### type ###

Returns the type of the selection (see nsISelectionController for
available constants).


## Constants ##

### ENDOFPRECEDINGLINE ###

### STARTOFNEXTLINE ###

### TABLESELECTION_NONE ###

### TABLESELECTION_CELL ###

### TABLESELECTION_ROW ###

### TABLESELECTION_COLUMN ###

### TABLESELECTION_TABLE ###

### TABLESELECTION_ALLCELLS ###
