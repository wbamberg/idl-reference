---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/accessible/interfaces/nsIAccessibleEditableText.idl">Source file</a>
</div>

# nsIAccessibleEditableText #

## Methods ##

### setTextContents(text) ###
<code>  
Replaces the text represented by this object by the given text.  
  
</code>
### insertText(text, position) ###
<code>  
Inserts text at the specified position.  
  
@param text - text that is inserted.  
@param position - index at which to insert the text.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>text</td>
<td>- text that is inserted.  
</td>
</tr>

<tr>
<td>position</td>
<td>- index at which to insert the text.  
</td>
</tr>

</table>

### copyText(startPos, endPos) ###
<code>  
Copies the text range into the clipboard.  
  
@param startPos - start index of the text to moved into the clipboard.  
@param endPos - end index of the text to moved into the clipboard.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>startPos</td>
<td>- start index of the text to moved into the clipboard.  
</td>
</tr>

<tr>
<td>endPos</td>
<td>- end index of the text to moved into the clipboard.  
</td>
</tr>

</table>

### cutText(startPos, endPos) ###
<code>  
Deletes a range of text and copies it to the clipboard.  
  
@param startPos - start index of the text to be deleted.  
@param endOffset - end index of the text to be deleted.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>startPos</td>
<td>- start index of the text to be deleted.  
</td>
</tr>

<tr>
<td>endOffset</td>
<td>- end index of the text to be deleted.  
</td>
</tr>

</table>

### deleteText(startPos, endPos) ###
<code>  
Deletes a range of text.  
  
@param startPos - start index of the text to be deleted.  
@param endPos - end index of the text to be deleted.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>startPos</td>
<td>- start index of the text to be deleted.  
</td>
</tr>

<tr>
<td>endPos</td>
<td>- end index of the text to be deleted.  
</td>
</tr>

</table>

### pasteText(position) ###
<code>  
Pastes text from the clipboard.  
  
@param position - index at which to insert the text from the system  
                  clipboard into the text represented by this object.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>position</td>
<td>- index at which to insert the text from the system  
                  clipboard into the text represented by this object.  
</td>
</tr>

</table>
