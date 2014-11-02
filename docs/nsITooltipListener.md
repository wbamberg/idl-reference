---
layout: default
---

# nsITooltipListener #
  
An optional interface for embedding clients wishing to receive  
notifications for when a tooltip should be displayed or removed.  
The embedder implements this interface on the web browser chrome  
object associated with the window that notifications are required  
for.  
  
@see nsITooltipTextProvider  
  

## Methods ##

### onShowTooltip(aXCoords, aYCoords, aTipText) ###
  
Called when a tooltip should be displayed.  
  
@param aXCoords The tooltip left edge X coordinate.  
@param aYCoords The tooltip top edge Y coordinate.  
@param aTipText The text to display in the tooltip, typically obtained  
       from the TITLE attribute of the node (or containing parent)  
       over which the pointer has been positioned.  
  
@note  
Coordinates are specified in pixels, relative to the top-left  
corner of the browser area.  
  
@return <code>NS_OK</code> if the tooltip was displayed.  
  

#### Parameters ####

<table>

<tr>
<td>aXCoords</td>
<td>The tooltip left edge X coordinate.  
</td>
</tr>

<tr>
<td>aYCoords</td>
<td>The tooltip top edge Y coordinate.  
</td>
</tr>

<tr>
<td>aTipText</td>
<td>The text to display in the tooltip, typically obtained  
       from the TITLE attribute of the node (or containing parent)  
       over which the pointer has been positioned.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td><code>NS_OK</code> if the tooltip was displayed.  
</td>
</tr>

</table>

### onHideTooltip() ###
  
Called when the tooltip should be hidden, either because the pointer  
has moved or the tooltip has timed out.  
  
