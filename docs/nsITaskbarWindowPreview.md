---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsITaskbarWindowPreview.idl">Source file</a>
</div>
# nsITaskbarWindowPreview #

## Methods ##

### getButton(index) ###
  
Gets the nth button for the preview image. By default, all of the buttons  
are invisible.  
  
@see nsITaskbarPreviewButton  
  
@param index The index into the button array. Must be >= 0 and <  
             MAX_TOOLBAR_BUTTONS.  
  

#### Parameters ####

<table>

<tr>
<td>index</td>
<td>The index into the button array. Must be >= 0 and <  
             MAX_TOOLBAR_BUTTONS.  
</td>
</tr>

</table>

## Attributes ##

### enableCustomDrawing ###
  
Enables/disables custom drawing of thumbnails and previews  
  
Default value: false  
  

## Constants ##

### NUM_TOOLBAR_BUTTONS ###
  
Max 7 buttons per preview per the Windows Taskbar API  
  
