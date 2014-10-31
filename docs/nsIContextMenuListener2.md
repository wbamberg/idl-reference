---
layout: default
---

# nsIContextMenuListener2 #
  
nsIContextMenuListener2  
  
This is an extended version of nsIContextMenuListener  
It provides a helper class, nsIContextMenuInfo, to allow access to  
background images as well as various utilities.  
  
@see nsIContextMenuListener  
@see nsIContextMenuInfo  
  

## Methods ##

### onShowContextMenu(aContextFlags, aUtils) ###
  
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
 Flag. No context. */  

### CONTEXT_LINK ###
 Flag. Context is a link element. */  

### CONTEXT_IMAGE ###
 Flag. Context is an image element. */  

### CONTEXT_DOCUMENT ###
 Flag. Context is the whole document. */  

### CONTEXT_TEXT ###
 Flag. Context is a text area element. */  

### CONTEXT_INPUT ###
 Flag. Context is an input element. */  

### CONTEXT_BACKGROUND_IMAGE ###
 Flag. Context is a background image. */  
