---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/editor/nsIEditorStyleSheets.idl">Source file</a>
</div>

# nsIEditorStyleSheets #

## Methods ##

### replaceStyleSheet(aURL) ###
<pre> Load and apply the style sheet, specified by aURL, to the  
editor's document, replacing the last style sheet added (if any).  
This is always asynchronous, and may cause network I/O.  
  
@param aURL The style sheet to be loaded and applied.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aURL</td>
<td>The style sheet to be loaded and applied.  
</td>
</tr>

</table>

### addStyleSheet(aURL) ###
<pre> Add the given style sheet to the editor's document,  
on top of any that are already there.  
This is always asynchronous, and may cause network I/O.  
  
@param aURL The style sheet to be loaded and applied.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aURL</td>
<td>The style sheet to be loaded and applied.  
</td>
</tr>

</table>

### replaceOverrideStyleSheet(aURL) ###
<pre> Load and apply the override style sheet, specified by aURL, to the  
editor's document, replacing the last override style sheet added (if any).  
This is always synchronous, so aURL should be a local file with only  
local @imports. This action is not undoable. It is not intended for  
"user" style sheets, only for editor developers to add sheets to change  
display behavior for editing (like showing special cursors) that will  
not be affected by loading "document" style sheets with addStyleSheet or  
especially replaceStyleSheet.  
  
@param aURL The style sheet to be loaded and applied.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aURL</td>
<td>The style sheet to be loaded and applied.  
</td>
</tr>

</table>

### addOverrideStyleSheet(aURL) ###
<pre> Load and apply an override style sheet, specified by aURL, to  
the editor's document, on top of any that are already there.  
This is always synchronous, so the same caveats about local files and no  
non-local @import as replaceOverrideStyleSheet apply here, too.  
  
@param aURL The style sheet to be loaded and applied.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aURL</td>
<td>The style sheet to be loaded and applied.  
</td>
</tr>

</table>

### removeStyleSheet(aURL) ###
<pre> Remove the given style sheet from the editor's document  
This is always synchronous  
  
@param aURL The style sheet to be removed  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aURL</td>
<td>The style sheet to be removed  
</td>
</tr>

</table>

### removeOverrideStyleSheet(aURL) ###
<pre> Remove the given override style sheet from the editor's document  
This is always synchronous  
  
@param aURL The style sheet to be removed.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aURL</td>
<td>The style sheet to be removed.  
</td>
</tr>

</table>

### enableStyleSheet(aURL, aEnable) ###
<pre> Enable or disable the given style sheet from the editor's document  
This is always synchronous  
  
@param aURL  The style sheet to be enabled or disabled  
@param aEnable true to enable, or false to disable the style sheet  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aURL</td>
<td>The style sheet to be enabled or disabled  
</td>
</tr>

<tr>
<td>aEnable</td>
<td>true to enable, or false to disable the style sheet  
</td>
</tr>

</table>

### getStyleSheetForURL(aURL) ###
<pre> Get the CSSStyleSheet associated with the given URL.  
  
@param aURL         The style sheet's URL  
@return             the style sheet  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aURL</td>
<td>The style sheet's URL  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>the style sheet  
</td>
</tr>

</table>

### getURLForStyleSheet(aStyleSheet) ###
<pre> Get the URL associated with the given CSSStyleSheet.  
  
@param aStyleSheet  The style sheet  
@return             the style sheet's URL  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aStyleSheet</td>
<td>The style sheet  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>the style sheet's URL  
</td>
</tr>

</table>
