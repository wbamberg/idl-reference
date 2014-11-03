---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/editor/nsIHTMLObjectResizeListener.idl">Source file</a>
</div>

# nsIHTMLObjectResizeListener #

## Methods ##

### onStartResizing(aElement) ###
<pre>  
Listener's callback called by the editor when the user  
starts resizing an element  
@param aElement [IN] the element  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aElement</td>
<td>[IN] the element  
</td>
</tr>

</table>

### onEndResizing(aElement, aOldWidth, aOldHeight, aNewWidth, aNewHeight) ###
<pre>  
Listener's callback called by the editor when the user  
has finalized the resizing of an element  
@param aElement [IN] the element that was resized  
@param aOldWidth  [IN] the width of the element before resizing  
@param aOldHeight [IN] the height of the element before resizing  
@param aNewWidth  [IN] the width of the element after resizing  
@param aNewHeight [IN] the height of the element after resizing  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aElement</td>
<td>[IN] the element that was resized  
</td>
</tr>

<tr>
<td>aOldWidth</td>
<td>[IN] the width of the element before resizing  
</td>
</tr>

<tr>
<td>aOldHeight</td>
<td>[IN] the height of the element before resizing  
</td>
</tr>

<tr>
<td>aNewWidth</td>
<td>[IN] the width of the element after resizing  
</td>
</tr>

<tr>
<td>aNewHeight</td>
<td>[IN] the height of the element after resizing  
</td>
</tr>

</table>
