---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/accessible/interfaces/nsIAccessiblePivot.idl">Source file</a>
</div>

# nsIAccessiblePivotObserver #
  
An observer interface for pivot changes.  
  

## Methods ##

### onPivotChanged(aPivot, aOldAccessible, aOldStart, aOldEnd, aReason, aIsFromUserInput) ###
  
Called when the pivot changes.  
  
@param aPivot           [in] the pivot that has changed.  
@param aOldAccessible   [in] the old pivot position before the change,  
                          or null.  
@param aOldStart        [in] the old start offset, or -1.  
@param aOldEnd          [in] the old end offset, or -1.  
@param aReason          [in] the reason for the pivot change.  
@param aIsFromUserInput [in] the pivot changed because of direct user input  
                          (default is true).  
  

#### Parameters ####

<table>

<tr>
<td>aPivot</td>
<td>[in] the pivot that has changed.  
</td>
</tr>

<tr>
<td>aOldAccessible</td>
<td>[in] the old pivot position before the change,  
                          or null.  
</td>
</tr>

<tr>
<td>aOldStart</td>
<td>[in] the old start offset, or -1.  
</td>
</tr>

<tr>
<td>aOldEnd</td>
<td>[in] the old end offset, or -1.  
</td>
</tr>

<tr>
<td>aReason</td>
<td>[in] the reason for the pivot change.  
</td>
</tr>

<tr>
<td>aIsFromUserInput</td>
<td>[in] the pivot changed because of direct user input  
                          (default is true).  
</td>
</tr>

</table>
