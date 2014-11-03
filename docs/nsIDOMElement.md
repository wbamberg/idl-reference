---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/core/nsIDOMElement.idl">Source file</a>
</div>

# nsIDOMElement #
<pre>  
The nsIDOMElement interface represents an element in an HTML or   
XML document.   
  
For more information on this interface please see   
http://dvcs.w3.org/hg/domcore/raw-file/tip/Overview.html#interface-element  
  
</pre>
## Methods ##

### getAttribute(name) ###

### getAttributeNS(namespaceURI, localName) ###

### setAttribute(name, value) ###

### setAttributeNS(namespaceURI, qualifiedName, value) ###

### removeAttribute(name) ###

### removeAttributeNS(namespaceURI, localName) ###

### hasAttribute(name) ###

### hasAttributeNS(namespaceURI, localName) ###

### hasAttributes() ###

### getAttributeNode(name) ###

### setAttributeNode(newAttr) ###

### removeAttributeNode(oldAttr) ###

### getAttributeNodeNS(namespaceURI, localName) ###

### setAttributeNodeNS(newAttr) ###

### getElementsByTagName(name) ###

### getElementsByTagNameNS(namespaceURI, localName) ###

### getElementsByClassName(classes) ###
<pre>  
Retrieve elements matching all classes listed in a  
space-separated string.  
  
</pre>
### remove() ###

### getClientRects() ###
<pre>  
Retrieve a list of rectangles, one for each CSS border-box associated with  
the element. The coordinates are in CSS pixels, and relative to  
the top-left of the document's viewport, unless the document  
has an SVG foreignobject ancestor, in which case the coordinates are  
relative to the top-left of the content box of the nearest SVG foreignobject  
ancestor. The coordinates are calculated as if every scrollable element  
is scrolled to its default position.  
  
Note: the boxes of overflowing children do not affect these rectangles.  
Note: some elements have empty CSS boxes. Those return empty rectangles,  
but the coordinates may still be meaningful.  
Note: some elements have no CSS boxes (including display:none elements,  
HTML AREA elements, and SVG elements that do not render). Those return  
an empty list.  
  
</pre>
### getBoundingClientRect() ###
<pre>  
Returns the union of all rectangles in the getClientRects() list. Empty  
rectangles are ignored, except that if all rectangles are empty,  
we return an empty rectangle positioned at the top-left of the first  
rectangle in getClientRects().  
  
</pre>
### mozMatchesSelector(selector) ###
<pre>  
Returns whether this element would be selected by the given selector  
string.  
  
See <http://dev.w3.org/2006/webapi/selectors-api2/#matchesselector>  
  
</pre>
### setCapture(retargetToElement) ###
<pre>  
Set this during a mousedown event to grab and retarget all mouse events  
to this element until the mouse button is released or releaseCapture is  
called. If retargetToElement is true, then all events are targetted at  
this element. If false, events can also fire at descendants of this  
element.  
  
  
</pre>
### releaseCapture() ###
<pre>  
If this element has captured the mouse, release the capture. If another  
element has captured the mouse, this method has no effect.  
  
</pre>
### mozRequestFullScreen() ###
<pre>  
Requests that this element be made the full-screen element, as per the DOM  
full-screen api.  
  
@see <https://wiki.mozilla.org/index.php?title=Gecko:FullScreenAPI>  
  
</pre>
### mozRequestPointerLock() ###
<pre>  
Requests that this element be made the pointer-locked element, as per the DOM  
pointer lock api.  
  
@see <http://dvcs.w3.org/hg/pointerlock/raw-file/default/index.html>  
  
</pre>
### querySelector(selectors) ###
<pre>  
Return nodes that match a given CSS selector.  
  
@see <http://dev.w3.org/2006/webapi/selectors-api/>  
  
</pre>
### querySelectorAll(selectors) ###

## Attributes ##

### tagName ###

### id ###

### className ###

### classList ###
<pre>  
Returns a DOMTokenList object reflecting the class attribute.  
  
</pre>
### attributes ###

### children ###
<pre>  
Returns a live nsIDOMNodeList of the current child elements.  
  
</pre>
### firstElementChild ###
<pre>  
Similar as the attributes on nsIDOMNode, but navigates just elements  
rather than all nodes.  
  
</pre>
### lastElementChild ###

### previousElementSibling ###

### nextElementSibling ###

### childElementCount ###
<pre>  
Returns the number of child nodes that are nsIDOMElements.  
  
</pre>
### scrollTop ###
<pre>  
The vertical scroll position of the element, or 0 if the element is not  
scrollable. This property may be assigned a value to change the  
vertical scroll position.  
  
</pre>
### scrollLeft ###
<pre>  
The horizontal scroll position of the element, or 0 if the element is not  
scrollable. This property may be assigned a value to change the  
horizontal scroll position.  
  
</pre>
### scrollWidth ###
<pre>  
The width of the scrollable area of the element. If the element is not  
scrollable, scrollWidth is equivalent to the offsetWidth.  
  
</pre>
### scrollHeight ###
<pre>  
The height of the scrollable area of the element. If the element is not  
scrollable, scrollHeight is equivalent to the offsetHeight.  
  
</pre>
### clientTop ###
<pre>  
The height in CSS pixels of the element's top border.  
  
</pre>
### clientLeft ###
<pre>  
The width in CSS pixels of the element's left border and scrollbar  
if it is present on the left side.  
  
</pre>
### clientWidth ###
<pre>  
The height in CSS pixels of the element's padding box. If the element is  
scrollable, the scroll bars are included inside this width.  
  
</pre>
### clientHeight ###
<pre>  
The width in CSS pixels of the element's padding box. If the element is  
scrollable, the scroll bars are included inside this height.  
  
</pre>
### scrollLeftMax ###

### scrollTopMax ###
