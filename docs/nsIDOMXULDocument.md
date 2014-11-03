---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/xul/nsIDOMXULDocument.idl">Source file</a>
</div>

# nsIDOMXULDocument #

## Methods ##

### getElementsByAttribute(name, value) ###

### getElementsByAttributeNS(namespaceURI, name, value) ###

### addBroadcastListenerFor(broadcaster, observer, attr) ###

### removeBroadcastListenerFor(broadcaster, observer, attr) ###

### persist(id, attr) ###

### getBoxObjectFor(elt) ###

### loadOverlay(url, aObserver) ###
<code>  
Loads a XUL overlay and merges it with the current document, notifying an  
observer when the merge is complete.   
@param   url  
         The URL of the overlay to load and merge  
@param   observer  
         An object implementing nsIObserver that will be notified with a  
         message of topic "xul-overlay-merged" when the merge is complete.   
         The subject parameter of |observe| will QI to a nsIURI - the URI   
         of the merged overlay. This parameter is optional and may be null.  
  
NOTICE:  In the 2.0 timeframe this API will change such that the   
         implementation will fire a DOMXULOverlayMerged event upon merge  
         completion rather than notifying an observer. Do not rely on this  
         API's behavior _not_ to change because it will!  
         - Ben Goodger (8/23/2005)  
  
</code>
#### Parameters ####

<table>

<tr>
<td>url</td>
<td>         The URL of the overlay to load and merge  
</td>
</tr>

<tr>
<td>observer</td>
<td>         An object implementing nsIObserver that will be notified with a  
         message of topic "xul-overlay-merged" when the merge is complete.   
         The subject parameter of |observe| will QI to a nsIURI - the URI   
         of the merged overlay. This parameter is optional and may be null.  
</td>
</tr>

</table>

## Attributes ##

### popupNode ###

### popupRangeParent ###
  
These attributes correspond to trustedGetPopupNode().rangeOffset and  
rangeParent. They will help you find where in the DOM the popup is  
happening. Can be accessed from chrome only, and only during a popup  
event. Accessing any other time will be an error.  
  

### popupRangeOffset ###

### tooltipNode ###

### commandDispatcher ###

### width ###

### height ###
