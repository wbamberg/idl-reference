---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsIColorPicker.idl">Source file</a>
</div>

# nsIColorPicker #

## Methods ##

### init(parent, title, initialColor) ###
<code>  
Initialize the color picker widget. The color picker will not be shown until  
open() is called.  
If the backend doesn't support setting a title to the native color picker  
widget, the title parameter might be ignored.  
If the initialColor parameter does not follow the format specified on top of  
this file, the behavior will be unspecified. The initialColor could be the  
one used by the underlying backend or an arbitrary one. The backend could  
also assert.  
  
@param      parent       nsIDOMWindow parent. This dialog will be dependent  
                         on this parent. parent must be non-null.  
@param      title        The title for the color picker widget.  
@param      initialColor The color to show when the widget is opened. The  
                         parameter has to follow the format specified on top  
                         of this file.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>parent</td>
<td>nsIDOMWindow parent. This dialog will be dependent  
                         on this parent. parent must be non-null.  
</td>
</tr>

<tr>
<td>title</td>
<td>The title for the color picker widget.  
</td>
</tr>

<tr>
<td>initialColor</td>
<td>The color to show when the widget is opened. The  
                         parameter has to follow the format specified on top  
                         of this file.  
</td>
</tr>

</table>

### open(aColorPickerShownCallback) ###
<code>  
Opens the color dialog asynchrounously.  
The results are provided via the callback object.  
  
</code>