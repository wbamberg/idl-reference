---
layout: default
---

# nsITextScroll #
  
The nsITextScroll is an interface that can be implemented by a control that  
supports text scrolling.   
  

## Methods ##

### scrollByLines(numLines) ###
  
Scroll the view up or down by aNumLines lines. positive  
values move down in the view. Prevents scrolling off the  
end of the view.  
@param numLines number of lines to scroll the view by  
  

#### Parameters ####

<table>

<tr>
<td>numLines</td>
<td>number of lines to scroll the view by  
</td>
</tr>

</table>

### scrollByPages(numPages) ###
  
Scroll the view up or down by numPages pages. a page  
is considered to be the amount displayed by the clip view.  
positive values move down in the view. Prevents scrolling  
off the end of the view.  
@param numPages number of pages to scroll the view by  
  

#### Parameters ####

<table>

<tr>
<td>numPages</td>
<td>number of pages to scroll the view by  
</td>
</tr>

</table>
