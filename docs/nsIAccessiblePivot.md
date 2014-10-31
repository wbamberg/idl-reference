---
layout: default
---

# nsIAccessiblePivot #
  
The pivot interface encapsulates a reference to a single place in an accessible  
subtree. The pivot is a point or a range in the accessible tree. This interface  
provides traversal methods to move the pivot to next/prev state that complies   
to a given rule.  
  

## Methods ##

### setTextRange(aTextAccessible, aStartOffset, aEndOffset, aIsFromUserInput) ###
  
Set the pivot's text range in a text accessible.  
  
@param aTextAccessible  [in] the text accessible that contains the desired  
                          range.  
@param aStartOffset     [in] the start offset to set.  
@param aEndOffset       [in] the end offset to set.  
@param aIsFromUserInput [in] the pivot changed because of direct user input  
                          (default is true).  
@throws NS_ERROR_INVALID_ARG when the offset exceeds the accessible's  
  character count.  
  

#### Parameters ####

<table>

<tr>
<td>aTextAccessible</td>
<td>[in] the text accessible that contains the desired  
                          range.  
</td>
</tr>

<tr>
<td>aTextAccessible</td>
<td>[in] the text accessible that contains the desired  
                          range.  
</td>
</tr>

<tr>
<td>aTextAccessible</td>
<td>[in] the text accessible that contains the desired  
                          range.  
</td>
</tr>

<tr>
<td>aTextAccessible</td>
<td>[in] the text accessible that contains the desired  
                          range.  
</td>
</tr>

</table>

### moveNext(aRule, aAnchor, aIncludeStart, aIsFromUserInput) ###
  
Move pivot to next object, from current position or given anchor,  
complying to given traversal rule.  
  
@param aRule            [in] traversal rule to use.  
@param aAnchor          [in] accessible to start search from, if not provided,  
                          current position will be used.  
@param aIncludeStart    [in] include anchor accessible in search.  
@param aIsFromUserInput [in] the pivot changed because of direct user input  
                          (default is true).  
@return true on success, false if there are no new nodes to traverse to.  
  

#### Parameters ####

<table>

<tr>
<td>aRule</td>
<td>[in] traversal rule to use.  
</td>
</tr>

<tr>
<td>aRule</td>
<td>[in] traversal rule to use.  
</td>
</tr>

<tr>
<td>aRule</td>
<td>[in] traversal rule to use.  
</td>
</tr>

<tr>
<td>aRule</td>
<td>[in] traversal rule to use.  
</td>
</tr>

</table>

### movePrevious(aRule, aAnchor, aIncludeStart, aIsFromUserInput) ###
  
Move pivot to previous object, from current position or given anchor,  
complying to given traversal rule.  
  
@param aRule            [in] traversal rule to use.  
@param aAnchor          [in] accessible to start search from, if not provided,  
                          current position will be used.  
@param aIncludeStart    [in] include anchor accessible in search.  
@param aIsFromUserInput [in] the pivot changed because of direct user input  
                          (default is true).  
@return true on success, false if there are no new nodes to traverse to.  
  

#### Parameters ####

<table>

<tr>
<td>aRule</td>
<td>[in] traversal rule to use.  
</td>
</tr>

<tr>
<td>aRule</td>
<td>[in] traversal rule to use.  
</td>
</tr>

<tr>
<td>aRule</td>
<td>[in] traversal rule to use.  
</td>
</tr>

<tr>
<td>aRule</td>
<td>[in] traversal rule to use.  
</td>
</tr>

</table>

### moveFirst(aRule, aIsFromUserInput) ###
  
Move pivot to first object in subtree complying to given traversal rule.  
  
@param aRule            [in] traversal rule to use.  
@param aIsFromUserInput [in] the pivot changed because of direct user input  
                          (default is true).  
@return true on success, false if there are no new nodes to traverse to.  
  

#### Parameters ####

<table>

<tr>
<td>aRule</td>
<td>[in] traversal rule to use.  
</td>
</tr>

<tr>
<td>aRule</td>
<td>[in] traversal rule to use.  
</td>
</tr>

</table>

### moveLast(aRule, aIsFromUserInput) ###
  
Move pivot to last object in subtree complying to given traversal rule.  
  
@param aRule            [in] traversal rule to use.  
@param aIsFromUserInput [in] the pivot changed because of direct user input  
                          (default is true).  
  

#### Parameters ####

<table>

<tr>
<td>aRule</td>
<td>[in] traversal rule to use.  
</td>
</tr>

<tr>
<td>aRule</td>
<td>[in] traversal rule to use.  
</td>
</tr>

</table>

### moveNextByText(aBoundary, aIsFromUserInput) ###
  
Move pivot to next text range.  
  
@param aBoundary        [in] type of boundary for next text range,  
                          character, word, etc.  
@param aIsFromUserInput [in] the pivot changed because of direct user input  
                          (default is true).  
@return true on success, false if there are is no more text.  
  

#### Parameters ####

<table>

<tr>
<td>aBoundary</td>
<td>[in] type of boundary for next text range,  
                          character, word, etc.  
</td>
</tr>

<tr>
<td>aBoundary</td>
<td>[in] type of boundary for next text range,  
                          character, word, etc.  
</td>
</tr>

</table>

### movePreviousByText(aBoundary, aIsFromUserInput) ###
  
Move pivot to previous text range.  
  
@param aBoundary        [in] type of boundary for next text range,  
                          character, word, etc.  
@param aIsFromUserInput [in] the pivot changed because of direct user input  
                          (default is true).  
@return true on success, false if there are is no more text.  
  

#### Parameters ####

<table>

<tr>
<td>aBoundary</td>
<td>[in] type of boundary for next text range,  
                          character, word, etc.  
</td>
</tr>

<tr>
<td>aBoundary</td>
<td>[in] type of boundary for next text range,  
                          character, word, etc.  
</td>
</tr>

</table>

### moveToPoint(aRule, aX, aY, aIgnoreNoMatch, aIsFromUserInput) ###
  
Move pivot to given coordinate in screen pixels.  
  
@param aRule            [in]  raversal rule to use.  
@param aX               [in]  screen's x coordinate  
@param aY               [in]  screen's y coordinate  
@param aIgnoreNoMatch   [in]  don't unset position if no object was found  
                          at point.  
@param aIsFromUserInput [in] the pivot changed because of direct user input  
                          (default is true).  
@return true on success, false if the pivot has not been moved.  
  

#### Parameters ####

<table>

<tr>
<td>aRule</td>
<td>[in]  raversal rule to use.  
</td>
</tr>

<tr>
<td>aRule</td>
<td>[in]  raversal rule to use.  
</td>
</tr>

<tr>
<td>aRule</td>
<td>[in]  raversal rule to use.  
</td>
</tr>

<tr>
<td>aRule</td>
<td>[in]  raversal rule to use.  
</td>
</tr>

<tr>
<td>aRule</td>
<td>[in]  raversal rule to use.  
</td>
</tr>

</table>

### addObserver(aObserver) ###
  
Add an observer for pivot changes.  
  
@param aObserver [in] the observer object to be notified of pivot changes.  
  

#### Parameters ####

<table>

<tr>
<td>aObserver</td>
<td>[in] the observer object to be notified of pivot changes.  
</td>
</tr>

</table>

### removeObserver(aObserver) ###
  
Remove an observer for pivot changes.  
  
@param aObserver [in] the observer object to remove from being notified.  
  

#### Parameters ####

<table>

<tr>
<td>aObserver</td>
<td>[in] the observer object to remove from being notified.  
</td>
</tr>

</table>

## Attributes ##

### position ###
  
The accessible the pivot is currently pointed at.  
  

### root ###
  
The root of the subtree in which the pivot traverses.  
  

### modalRoot ###
  
The temporary modal root to which traversal is limited to.  
  

### startOffset ###
  
The start offset of the text range the pivot points at, otherwise -1.  
  

### endOffset ###
  
The end offset of the text range the pivot points at, otherwise -1.  
  

## Constants ##

### CHAR_BOUNDARY ###

### WORD_BOUNDARY ###

### LINE_BOUNDARY ###

### ATTRIBUTE_RANGE_BOUNDARY ###

### REASON_NONE ###

### REASON_NEXT ###

### REASON_PREV ###

### REASON_FIRST ###

### REASON_LAST ###

### REASON_TEXT ###

### REASON_POINT ###
