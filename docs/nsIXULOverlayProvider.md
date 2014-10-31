---
layout: default
---

# nsIXULOverlayProvider #
  
The chrome registry implements this interface to give overlays  
to the gecko XUL engine.  
  

## Methods ##

### getXULOverlays(aURI) ###
  
Get the XUL overlays for a particular chrome URI.  
  
@param aURI  The URI being loaded  
@return      An enumerator of nsIURI for the overlays of this URI   
  

#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>The URI being loaded  
</td>
</tr>

</table>

### getStyleOverlays(aURI) ###
  
Get the style overlays for a particular chrome URI.  
  
@param aURI  The URI being loaded  
@return      An enumerator of nsIURI for the overlays of this URI   
  

#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>The URI being loaded  
</td>
</tr>

</table>
