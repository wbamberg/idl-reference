---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/events/nsIDOMNotifyPaintEvent.idl">Source file</a>
</div>

# nsIDOMNotifyPaintEvent #
  
The nsIDOMNotifyPaintEvent interface is used for the MozDOMAfterPaint  
event, which fires at a window when painting has happened in  
that window.  
  

## Attributes ##

### clientRects ###
  
Get a list of rectangles which are affected. The rectangles are in CSS pixels  
relative to the viewport origin.  
If the caller is not trusted (e.g., regular Web content) then only painting  
caused by the current document is reported; in particular, painting in subdocuments  
is not reported.  
  

### boundingClientRect ###
  
Get the bounding box of the rectangles which are affected. The rectangle  
is in CSS pixels relative to the viewport origin.  
If the caller is not trusted (e.g., regular Web content) then only painting  
caused by the current document is reported; in particular, painting in subdocuments  
is not reported.  
  

### paintRequests ###
