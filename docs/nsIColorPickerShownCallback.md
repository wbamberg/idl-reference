---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsIColorPicker.idl">Source file</a>
</div>

# nsIColorPickerShownCallback #
  
nsIColorPicker is representing colors as strings because the internal  
representation will depend on the underlying backend.  
The format of the colors taken in input and returned will always follow the  
format of the <input type='color'> value as described in the HTML  
specifications.  
  

## Methods ##

### update(color) ###
  
Callback called when the color picker requests a color update.  
This callback can not be called after done() was called.  
When this callback is used, the consumer can assume that the color value has  
changed.  
  
@param  color  The new selected color value following the format specifed on  
               top of this file.  
  

#### Parameters ####

<table>

<tr>
<td>color</td>
<td>The new selected color value following the format specifed on  
               top of this file.  
</td>
</tr>

</table>

### done(color) ###
  
Callback called when the color picker is dismissed.  
When this callback is used, the color might have changed or could stay the  
same.  
If the color has not changed, the color parameter will be the empty string.  
  
@param  color  The new selected color value following the format specifed on  
               top of this file or the empty string.  
  

#### Parameters ####

<table>

<tr>
<td>color</td>
<td>The new selected color value following the format specifed on  
               top of this file or the empty string.  
</td>
</tr>

</table>
