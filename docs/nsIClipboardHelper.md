---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsIClipboardHelper.idl">Source file</a>
</div>

# nsIClipboardHelper #
<pre>  
helper service for common uses of nsIClipboard.  
  
</pre>
## Methods ##

### copyStringToClipboard(aString, aClipboardID, aDoc) ###
<pre>  
copy string to given clipboard  
  
@param aString, the string to copy to the clipboard  
@param aDoc, the source document for the string, if available  
@param aClipboardID, the ID of the clipboard to copy to  
       (eg. kSelectionClipboard -- see nsIClipboard.idl)  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aString,</td>
<td>the string to copy to the clipboard  
</td>
</tr>

<tr>
<td>aDoc,</td>
<td>the source document for the string, if available  
</td>
</tr>

<tr>
<td>aClipboardID,</td>
<td>the ID of the clipboard to copy to  
       (eg. kSelectionClipboard -- see nsIClipboard.idl)  
</td>
</tr>

</table>

### copyString(aString, aDoc) ###
<pre>  
copy string to (default) clipboard  
  
@param aString, the string to copy to the clipboard  
@param aDoc, the source document for the string, if available  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aString,</td>
<td>the string to copy to the clipboard  
</td>
</tr>

<tr>
<td>aDoc,</td>
<td>the source document for the string, if available  
</td>
</tr>

</table>
