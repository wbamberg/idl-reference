---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsIClipboardDragDropHookList.idl">Source file</a>
</div>

# nsIClipboardDragDropHookList #
<pre>  
Please note that the following api is not intended for embedders;  
it is intended as an internal (to gecko).  Embedders can indirectly  
call these by sending commands (see description in   
nsIClipboardDragDropHooks.idl).  
  
Internal gecko usage is accomplished by calling get_Interface on a  
docshell.  
  
</pre>
## Methods ##

### addClipboardDragDropHooks(aHooks) ###
<pre>  
Add a hook to list.  
@param aHooks  implementation of hooks  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aHooks</td>
<td>implementation of hooks  
</td>
</tr>

</table>

### removeClipboardDragDropHooks(aHooks) ###
<pre>  
Remove a hook from list (note if this implementation is not present  
in the list then removal will be ignored).  
@param aHooks  implementation of hooks  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aHooks</td>
<td>implementation of hooks  
</td>
</tr>

</table>

### getHookEnumerator() ###
<pre>  
Gets an enumerator for all hooks which have been added.  
@return nsISimpleEnumerator for nsIClipboardDragDropHooks  
  
</pre>
#### Returns ####

<table>

<tr>
<td>nsISimpleEnumerator for nsIClipboardDragDropHooks  
</td>
</tr>

</table>
