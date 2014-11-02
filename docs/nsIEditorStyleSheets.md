---
layout: default
---

# nsIEditorStyleSheets #

## Methods ##

### replaceStyleSheet(aURL) ###
 Load and apply the style sheet, specified by aURL, to the  
editor's document, replacing the last style sheet added (if any).  
This is always asynchronous, and may cause network I/O.  
  
@param aURL The style sheet to be loaded and applied.  
  

#### Parameters ####

<table>

<tr>
<td>aURL</td>
<td>The style sheet to be loaded and applied.  
</td>
</tr>

</table>

### addStyleSheet(aURL) ###
 Add the given style sheet to the editor's document,  
on top of any that are already there.  
This is always asynchronous, and may cause network I/O.  
  
@param aURL The style sheet to be loaded and applied.  
  

#### Parameters ####

<table>

<tr>
<td>aURL</td>
<td>The style sheet to be loaded and applied.  
</td>
</tr>

</table>

### replaceOverrideStyleSheet(aURL) ###
 Load and apply the override style sheet, specified by aURL, to the  
editor's document, replacing the last override style sheet added (if any).  
This is always synchronous, so aURL should be a local file with only  
local @imports. This action is not undoable. It is not intended for  
"user" style sheets, only for editor developers to add sheets to change  
display behavior for editing (like showing special cursors) that will  
not be affected by loading "document" style sheets with addStyleSheet or  
especially replaceStyleSheet.  
  
@param aURL The style sheet to be loaded and applied.  
  

#### Parameters ####

<table>

<tr>
<td>aURL</td>
<td>The style sheet to be loaded and applied.  
</td>
</tr>

</table>

### addOverrideStyleSheet(aURL) ###
 Load and apply an override style sheet, specified by aURL, to  
the editor's document, on top of any that are already there.  
This is always synchronous, so the same caveats about local files and no  
non-local @import as replaceOverrideStyleSheet apply here, too.  
  
@param aURL The style sheet to be loaded and applied.  
  

#### Parameters ####

<table>

<tr>
<td>aURL</td>
<td>The style sheet to be loaded and applied.  
</td>
</tr>

</table>

### removeStyleSheet(aURL) ###
 Remove the given style sheet from the editor's document  
This is always synchronous  
  
@param aURL The style sheet to be removed  
  

#### Parameters ####

<table>

<tr>
<td>aURL</td>
<td>The style sheet to be removed  
</td>
</tr>

</table>

### removeOverrideStyleSheet(aURL) ###
 Remove the given override style sheet from the editor's document  
This is always synchronous  
  
@param aURL The style sheet to be removed.  
  

#### Parameters ####

<table>

<tr>
<td>aURL</td>
<td>The style sheet to be removed.  
</td>
</tr>

</table>

### enableStyleSheet(aURL, aEnable) ###
 Enable or disable the given style sheet from the editor's document  
This is always synchronous  
  
@param aURL  The style sheet to be enabled or disabled  
@param aEnable true to enable, or false to disable the style sheet  
  

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
 Get the CSSStyleSheet associated with the given URL.  
  
@param aURL         The style sheet's URL  
@return             the style sheet  
  

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
 Get the URL associated with the given CSSStyleSheet.  
  
@param aStyleSheet  The style sheet  
@return             the style sheet's URL  
  

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
