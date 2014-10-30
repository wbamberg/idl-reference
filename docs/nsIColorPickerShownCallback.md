---
layout: default
---

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
  

### done(color) ###
  
Callback called when the color picker is dismissed.  
When this callback is used, the color might have changed or could stay the  
same.  
If the color has not changed, the color parameter will be the empty string.  
  
@param  color  The new selected color value following the format specifed on  
               top of this file or the empty string.  
  
