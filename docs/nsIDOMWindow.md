---
layout: default
---

# nsIDOMWindow #
  
The nsIDOMWindow interface is the primary interface for a DOM  
window object. It represents a single window object that may  
contain child windows if the document in the window contains a  
HTML frameset document or if the document contains iframe elements.  
  
@see <http://www.whatwg.org/html/#window>  
  

## Methods ##

### close() ###

### stop() ###

### focus() ###

### blur() ###

### alert(text) ###

### confirm(text) ###

### prompt(aMessage, aInitial) ###

### print() ###

### showModalDialog(aURI, aArgs, aOptions) ###

### postMessage(message, targetOrigin, transfer) ###
  
Implements a safe message-passing system which can cross same-origin  
boundaries.  
  
This method, when called, causes a MessageEvent to be asynchronously  
dispatched at the primary document for the window upon which this method is  
called.  (Note that the postMessage property on windows is allAccess and  
thus is readable cross-origin.)  The dispatched event will have message as  
its data, the calling context's window as its source, and an origin  
determined by the calling context's main document URI.  The targetOrigin  
argument specifies a URI and is used to restrict the message to be sent  
only when the target window has the same origin as targetOrigin (since,  
when the sender and the target have different origins, neither can read the  
location of the other).  
  
@see <http://www.whatwg.org/html/#dom-window-postmessage>  
  

### atob(aAsciiString) ###

### btoa(aBase64Data) ###

### getSelection() ###
  
Method for accessing this window's selection object.  
  

### matchMedia(media_query_list) ###

### scroll(xScroll, yScroll) ###

### scrollTo(xScroll, yScroll) ###
  
Method for scrolling this window to an absolute pixel offset.  
  

### scrollBy(xScrollDif, yScrollDif) ###
  
Method for scrolling this window to a pixel offset relative to  
the current scroll position.  
  

### getComputedStyle(elt, pseudoElt) ###
  
@see <http://dev.w3.org/csswg/cssom/#dom-window-getcomputedstyle>  
  

### getDefaultComputedStyle(elt, pseudoElt) ###

### scrollByLines(numLines) ###
  
Method for scrolling this window by a number of lines.  
  

### scrollByPages(numPages) ###
  
Method for scrolling this window by a number of pages.  
  

### sizeToContent() ###
  
Method for sizing this window to the content in the window.  
  

### back() ###

### forward() ###

### home() ###

### moveTo(xPos, yPos) ###

### moveBy(xDif, yDif) ###

### resizeTo(width, height) ###

### resizeBy(widthDif, heightDif) ###

### open(url, name, options) ###
  
Open a new window with this one as the parent.  This method will  
NOT examine the JS stack for purposes of determining a caller.  
This window will be used for security checks during the search by  
name and the default character set on the newly opened window  
will just be the default character set of this window.  
  

### openDialog(url, name, options, aExtraArgument) ###
  
This method works like open except that aExtraArgument gets  
converted into the array window.arguments in JS, if  
aExtraArgument is a nsISupportsArray then the individual items in  
the array are inserted into window.arguments, and primitive  
nsISupports (nsISupportsPrimitives) types are converted to native  
JS types when possible.  
  

### updateCommands(action, sel, reason) ###

### find(str, caseSensitive, backwards, wrapAround, wholeWord, searchInFrames, showDialog) ###

### mozRequestAnimationFrame(aCallback) ###
  
Request a refresh of this browser window.  
  
@see <http://dvcs.w3.org/hg/webperf/raw-file/tip/specs/RequestAnimationFrame/Overview.html>  
  

### requestAnimationFrame(aCallback) ###

### mozCancelAnimationFrame(aHandle) ###
  
Cancel a refresh callback.  
  

### mozCancelRequestAnimationFrame(aHandle) ###

### cancelAnimationFrame(aHandle) ###

## Attributes ##

### window ###

### self ###

### document ###
  
Accessor for the document in this window.  
  

### name ###
  
Set/Get the name of this window.  
  
This attribute is "replaceable" in JavaScript  
  

### location ###

### history ###

### locationbar ###

### menubar ###

### personalbar ###

### scrollbars ###
  
Accessor for the object that controls whether or not scrollbars  
are shown in this window.  
  
This attribute is "replaceable" in JavaScript  
  

### statusbar ###

### toolbar ###

### status ###

### length ###

### top ###
  
|top| gets the root of the window hierarchy.  
  
This function does not cross chrome-content boundaries, so if this  
window's parent is of a different type, |top| will return this window.  
  
When script reads the top property, we run GetScriptableTop, which  
will not cross an <iframe mozbrowser> boundary.  
  
In contrast, C++ calls to GetTop are forwarded to GetRealTop, which  
ignores <iframe mozbrowser> boundaries.  
  
This property is "replaceable" in JavaScript.  
  

### realTop ###
  
You shouldn't need to call this function directly; call GetTop instead.  
  

### parent ###
  
|parent| gets this window's parent window.  If this window has no parent,  
we return the window itself.  
  
This property does not cross chrome-content boundaries, so if this  
window's parent is of a different type, we return the window itself as its  
parent.  
  
When script reads the property (or when C++ calls ScriptableTop), this  
property does not cross <iframe mozbrowser> boundaries.  In contrast, when  
C++ calls GetParent, we ignore the mozbrowser attribute.  
  

### realParent ###
  
You shouldn't need to read this property directly; call GetParent instead.  
  

### opener ###

### openerWindow ###

### frameElement ###
  
|frameElement| gets this window's <iframe> or <frame> element, if it has  
one.  
  
When script reads this property (or when C++ calls  
ScriptableFrameElement), we return |null| if the window is inside an  
<iframe mozbrowser>.  In contrast, when C++ calls GetFrameElement, we  
ignore the mozbrowser attribute.  
  

### realFrameElement ###
  
You shouldn't need to read this property directly; call GetFrameElement  
instead.  
  

### navigator ###

### applicationCache ###
  
Get the application cache object for this window.  
  

### sessionStorage ###
  
Session storage for the current browsing context.  
This attribute is a DOMStorage  
  

### localStorage ###
  
Local storage for the current browsing context.  
This attribute is a DOMStorage  
  

### indexedDB ###

### mozIndexedDB ###

### screen ###

### innerWidth ###

### innerHeight ###

### scrollX ###
  
Accessor for the current x scroll position in this window in  
pixels.  
  
This attribute is "replaceable" in JavaScript  
  

### pageXOffset ###

### scrollY ###
  
Accessor for the current y scroll position in this window in  
pixels.  
  
This attribute is "replaceable" in JavaScript  
  

### pageYOffset ###

### screenX ###

### screenY ###

### outerWidth ###

### outerHeight ###

### windowRoot ###
  
Get the window root for this window. This is useful for hooking  
up event listeners to this window and every other window nested  
in the window root.  
  

### frames ###
  
Accessor for the child windows in this window.  
  

### textZoom ###
  
Set/Get the document scale factor as a multiplier on the default  
size. When setting this attribute, a NS_ERROR_NOT_IMPLEMENTED  
error may be returned by implementations not supporting  
zoom. Implementations not supporting zoom should return 1.0 all  
the time for the Get operation. 1.0 is equals normal size,  
i.e. no zoom.  
  

### content ###

### prompter ###

### closed ###

### crypto ###

### controllers ###

### mozInnerScreenX ###

### mozInnerScreenY ###

### devicePixelRatio ###

### scrollMaxX ###

### scrollMaxY ###

### fullScreen ###

### mozPaintCount ###
  
Returns the number of times this document for this window has  
been painted to the screen.  
  

### mozAnimationStartTime ###
  
The current animation start time in milliseconds since the epoch.  
  

### console ###
  
Console API  
  
