---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/editor/nsIPlaintextEditor.idl">Source file</a>
</div>

# nsIPlaintextEditor #

## Methods ##

### setWrapColumn(aWrapColumn) ###
  
Similar to the setter for wrapWidth, but just sets the editor  
internal state without actually changing the content being edited  
to wrap at that column.  This should only be used by callers who  
are sure that their content is already set up correctly.  
  

### insertText(aStringToInsert) ###
  
Inserts a string at the current location,  
given by the selection.  
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

### insertLineBreak() ###
  
Insert a line break into the content model.  
The interpretation of a break is up to the implementation:  
it may enter a character, split a node in the tree, etc.  
This may be more efficient than calling InsertText with a newline.  
  

## Attributes ##

### textLength ###
  
The length of the contents in characters.  
XXX change this type to 'unsigned long'  
  

### maxTextLength ###
  
The maximum number of characters allowed.  
  default: -1 (unlimited).  
  

### wrapWidth ###
 Get and set the body wrap width.  
  
Special values:  
   0 = wrap to window width  
  -1 = no wrap at all  
  

### newlineHandling ###
 Get and set newline handling.  
  
 Values are the constants defined above.  
  

## Constants ##

### eEditorPlaintextMask ###

### eEditorSingleLineMask ###

### eEditorPasswordMask ###

### eEditorReadonlyMask ###

### eEditorDisabledMask ###

### eEditorFilterInputMask ###

### eEditorMailMask ###

### eEditorEnableWrapHackMask ###

### eEditorWidgetMask ###

### eEditorNoCSSMask ###

### eEditorAllowInteraction ###

### eEditorDontEchoPassword ###

### eEditorRightToLeft ###

### eEditorLeftToRight ###

### eEditorSkipSpellCheck ###

### eNewlinesPasteIntact ###

### eNewlinesPasteToFirst ###

### eNewlinesReplaceWithSpaces ###

### eNewlinesStrip ###

### eNewlinesReplaceWithCommas ###

### eNewlinesStripSurroundingWhitespace ###
