---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/editor/nsIEditorMailSupport.idl">Source file</a>
</div>

# nsIEditorMailSupport #

## Methods ##

### pasteAsQuotation(aSelectionType) ###
 Paste the text in the OS clipboard at the cursor position,  
as a quotation (whose representation is dependant on the editor type),  
replacing the selected text (if any).  
  

#### Parameters ####

<table>

<tr>
<td>aSelectionType</td>
<td>Text or html?  
</td>
</tr>

</table>

### insertAsQuotation(aQuotedText) ###
 Insert a string as quoted text  
(whose representation is dependant on the editor type),  
replacing the selected text (if any).  
  

#### Parameters ####

<table>

<tr>
<td>aQuotedText</td>
<td>The actual text to be quoted  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The node which was inserted  
</td>
</tr>

</table>

### insertTextWithQuotations(aStringToInsert) ###
  
Inserts a plaintext string at the current location,  
with special processing for lines beginning with ">",  
which will be treated as mail quotes and inserted  
as plaintext quoted blocks.  
If the selection is not collapsed, the selection is deleted  
and the insertion takes place at the resulting collapsed selection.  
  
  

#### Parameters ####

<table>

<tr>
<td>aString</td>
<td>the string to be inserted  
</td>
</tr>

</table>

### pasteAsCitedQuotation(aCitation, aSelectionType) ###
 Paste a string as quoted text,  
whose representation is dependant on the editor type,  
replacing the selected text (if any)  
  

#### Parameters ####

<table>

<tr>
<td>aCitation</td>
<td>The "mid" URL of the source message  
</td>
</tr>

<tr>
<td>aSelectionType</td>
<td>Text or html?  
</td>
</tr>

</table>

### insertAsCitedQuotation(aQuotedText, aCitation, aInsertHTML) ###
 Insert a string as quoted text  
(whose representation is dependant on the editor type),  
replacing the selected text (if any),  
including, if possible, a "cite" attribute.  
  

#### Parameters ####

<table>

<tr>
<td>aQuotedText</td>
<td>The actual text to be quoted  
</td>
</tr>

<tr>
<td>aCitation</td>
<td>The "mid" URL of the source message  
</td>
</tr>

<tr>
<td>aInsertHTML</td>
<td>Insert as html?  (vs plaintext)  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The node which was inserted  
</td>
</tr>

</table>

### rewrap(aRespectNewlines) ###
  
Rewrap the selected part of the document, re-quoting if necessary.  
  

#### Parameters ####

<table>

<tr>
<td>aRespectNewlines</td>
<td>Try to maintain newlines in the original?  
</td>
</tr>

</table>

### stripCites() ###
  
Strip any citations in the selected part of the document.  
  

### getEmbeddedObjects() ###
  
Get a list of IMG and OBJECT tags in the current document.  
  
