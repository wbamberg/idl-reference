---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsITaskbarWindowPreview.idl">Source file</a>
</div>

# nsITaskbarWindowPreview #

## Methods ##

### getButton(index) ###
<pre>  
Gets the nth button for the preview image. By default, all of the buttons  
are invisible.  
  
@see nsITaskbarPreviewButton  
  
@param index The index into the button array. Must be >= 0 and <  
             MAX_TOOLBAR_BUTTONS.  
  
</pre>
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
<pre>  
Enables/disables custom drawing of thumbnails and previews  
  
Default value: false  
  
</pre>
## Constants ##

### NUM_TOOLBAR_BUTTONS ###
<pre>  
Max 7 buttons per preview per the Windows Taskbar API  
  
</pre>