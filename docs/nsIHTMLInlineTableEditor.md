---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/editor/nsIHTMLInlineTableEditor.idl">Source file</a>
</div>

# nsIHTMLInlineTableEditor #

## Methods ##

### showInlineTableEditingUI(aCell) ###
<pre>  
Shows inline table editing UI around a table cell  
@param aCell [IN] a DOM Element being a table cell, td or th  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aCell</td>
<td>[IN] a DOM Element being a table cell, td or th  
</td>
</tr>

</table>

### hideInlineTableEditingUI() ###
<pre>  
Hide all inline table editing UI  
  
</pre>
### doInlineTableEditingAction(aUIAnonymousElement) ###
<pre>  
Modifies the table containing the selection according to the  
activation of an inline table editing UI element  
@param aUIAnonymousElement [IN] the inline table editing UI element  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aUIAnonymousElement</td>
<td>[IN] the inline table editing UI element  
</td>
</tr>

</table>

### refreshInlineTableEditingUI() ###
<pre>  
Refresh already visible inline table editing UI  
  
</pre>
## Attributes ##

### inlineTableEditingEnabled ###
<pre>  
boolean indicating if inline table editing is enabled in the editor.  
When inline table editing is enabled, and when the selection is  
contained in a table cell, special buttons allowing to add/remove  
a line/column are available on the cell's border.  
  
</pre>