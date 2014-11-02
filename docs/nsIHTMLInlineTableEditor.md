---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/editor/nsIHTMLInlineTableEditor.idl">Source file</a>
</div>

# nsIHTMLInlineTableEditor #

## Methods ##

### showInlineTableEditingUI(aCell) ###
  
Shows inline table editing UI around a table cell  
@param aCell [IN] a DOM Element being a table cell, td or th  
  

#### Parameters ####

<table>

<tr>
<td>aCell</td>
<td>[IN] a DOM Element being a table cell, td or th  
</td>
</tr>

</table>

### hideInlineTableEditingUI() ###
  
Hide all inline table editing UI  
  

### doInlineTableEditingAction(aUIAnonymousElement) ###
  
Modifies the table containing the selection according to the  
activation of an inline table editing UI element  
@param aUIAnonymousElement [IN] the inline table editing UI element  
  

#### Parameters ####

<table>

<tr>
<td>aUIAnonymousElement</td>
<td>[IN] the inline table editing UI element  
</td>
</tr>

</table>

### refreshInlineTableEditingUI() ###
  
Refresh already visible inline table editing UI  
  

## Attributes ##

### inlineTableEditingEnabled ###
  
boolean indicating if inline table editing is enabled in the editor.  
When inline table editing is enabled, and when the selection is  
contained in a table cell, special buttons allowing to add/remove  
a line/column are available on the cell's border.  
  
