---
layout: default
---

# nsIXULOverlayProvider #
  
The chrome registry implements this interface to give overlays  
to the gecko XUL engine.  
  

## Methods ##

### getXULOverlays ###
  
Get the XUL overlays for a particular chrome URI.  
  
@param aURI  The URI being loaded  
@return      An enumerator of nsIURI for the overlays of this URI   
  

### getStyleOverlays ###
  
Get the style overlays for a particular chrome URI.  
  
@param aURI  The URI being loaded  
@return      An enumerator of nsIURI for the overlays of this URI   
  
