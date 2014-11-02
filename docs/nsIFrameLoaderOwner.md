---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/base/nsIFrameLoader.idl">Source file</a>
</div>
# nsIFrameLoaderOwner #

## Methods ##

### GetFrameLoader() ###

### swapFrameLoaders(aOtherOwner) ###
  
Swap frame loaders with the given nsIFrameLoaderOwner.  This may  
only be posible in a very limited range of circumstances, or  
never, depending on the object implementing this interface.  
  
@throws NS_ERROR_NOT_IMPLEMENTED if the swapping logic is not  
  implemented for the two given frame loader owners.  
@throws NS_ERROR_DOM_SECURITY_ERR if the swap is not allowed on  
  security grounds.  
  

## Attributes ##

### frameLoader ###
  
The frame loader owned by this nsIFrameLoaderOwner  
  
