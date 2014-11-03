---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/embedding/browser/nsIContextMenuListener2.idl">Source file</a>
</div>

# nsIContextMenuListener2 #
<pre>  
nsIContextMenuListener2  
  
This is an extended version of nsIContextMenuListener  
It provides a helper class, nsIContextMenuInfo, to allow access to  
background images as well as various utilities.  
  
@see nsIContextMenuListener  
@see nsIContextMenuInfo  
  
</pre>
## Methods ##

### onShowContextMenu(aContextFlags, aUtils) ###
<pre>  
Called when the browser receives a context menu event (e.g. user is right-mouse  
clicking somewhere on the document). The combination of flags, along with the  
attributes of <CODE>aUtils</CODE>, indicate where and what was clicked on.  
  
The following table describes what context flags and node combinations are  
possible.  
  
aContextFlags                  aUtils.targetNode  
  
CONTEXT_LINK                   <A>  
CONTEXT_IMAGE                  <IMG>  
CONTEXT_IMAGE | CONTEXT_LINK   <IMG> with <A> as an ancestor  
CONTEXT_INPUT                  <INPUT>  
CONTEXT_INPUT | CONTEXT_IMAGE  <INPUT> with type=image  
CONTEXT_TEXT                   <TEXTAREA>  
CONTEXT_DOCUMENT               <HTML>  
CONTEXT_BACKGROUND_IMAGE       <HTML> with background image  
  
@param aContextFlags           Flags indicating the kind of context.  
@param aUtils                  Context information and helper utilities.  
  
@see nsIContextMenuInfo  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aContextFlags</td>
<td>Flags indicating the kind of context.  
</td>
</tr>

<tr>
<td>aUtils</td>
<td>Context information and helper utilities.  
</td>
</tr>

</table>

## Constants ##

### CONTEXT_NONE ###
<pre> Flag. No context. */  
</pre>
### CONTEXT_LINK ###
<pre> Flag. Context is a link element. */  
</pre>
### CONTEXT_IMAGE ###
<pre> Flag. Context is an image element. */  
</pre>
### CONTEXT_DOCUMENT ###
<pre> Flag. Context is the whole document. */  
</pre>
### CONTEXT_TEXT ###
<pre> Flag. Context is a text area element. */  
</pre>
### CONTEXT_INPUT ###
<pre> Flag. Context is an input element. */  
</pre>
### CONTEXT_BACKGROUND_IMAGE ###
<pre> Flag. Context is a background image. */  
</pre>