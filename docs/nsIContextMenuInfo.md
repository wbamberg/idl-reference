---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/embedding/browser/nsIContextMenuListener2.idl">Source file</a>
</div>
# nsIContextMenuInfo #
  
nsIContextMenuInfo  
  
A helper object for implementors of nsIContextMenuListener2.  
  

## Attributes ##

### mouseEvent ###
  
The DOM context menu event.  
  

### targetNode ###
  
The DOM node most relevant to the context.  
  

### associatedLink ###
  
Given the <CODE>CONTEXT_LINK</CODE> flag, <CODE>targetNode</CODE> may not  
nescesarily be a link. This returns the anchor from <CODE>targetNode</CODE>  
if it has one or that of its nearest ancestor if it does not.  
  

### imageContainer ###
  
Given the <CODE>CONTEXT_IMAGE</CODE> flag, these methods can be  
used in order to get the image for viewing, saving, or for the clipboard.  
  
@return <CODE>NS_OK</CODE> if successful, otherwise <CODE>NS_ERROR_FAILURE</CODE> if no  
image was found, or NS_ERROR_NULL_POINTER if an internal error occurs where we think there   
is an image, but for some reason it cannot be returned.  
  

### imageSrc ###

### backgroundImageContainer ###
  
Given the <CODE>CONTEXT_BACKGROUND_IMAGE</CODE> flag, these methods can be  
used in order to get the image for viewing, saving, or for the clipboard.  
  
@return <CODE>NS_OK</CODE> if successful, otherwise <CODE>NS_ERROR_FAILURE</CODE> if no background  
image was found, or NS_ERROR_NULL_POINTER if an internal error occurs where we think there is a   
background image, but for some reason it cannot be returned.  
  

### backgroundImageSrc ###
