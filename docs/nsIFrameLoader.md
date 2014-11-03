---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/base/nsIFrameLoader.idl">Source file</a>
</div>

# nsIFrameLoader #

## Methods ##

### loadFrame() ###
<pre>  
Start loading the frame. This method figures out what to load  
from the owner content in the frame loader.  
  
</pre>
### loadURI(aURI) ###
<pre>  
Loads the specified URI in this frame. Behaves identically to loadFrame,  
except that this method allows specifying the URI to load.  
  
</pre>
### destroy() ###
<pre>  
Destroy the frame loader and everything inside it. This will  
clear the weak owner content reference.  
  
</pre>
### updatePositionAndSize(aIFrame) ###
<pre>  
Updates the position and size of the subdocument loaded by this frameloader.  
  
 @param aIFrame The nsIFrame for the content node that owns this frameloader  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aIFrame</td>
<td>The nsIFrame for the content node that owns this frameloader  
</td>
</tr>

</table>

### activateRemoteFrame() ###
<pre>  
Activate remote frame.  
Throws an exception with non-remote frames.  
  
</pre>
### deactivateRemoteFrame() ###
<pre>  
Deactivate remote frame.  
Throws an exception with non-remote frames.  
  
</pre>
### sendCrossProcessMouseEvent(aType, aX, aY, aButton, aClickCount, aModifiers, aIgnoreRootScrollFrame) ###
<pre>  
@see nsIDOMWindowUtils sendMouseEvent.  
  
</pre>
### activateFrameEvent(aType, capture) ###
<pre>  
Activate event forwarding from client (remote frame) to parent.  
  
</pre>
### sendCrossProcessKeyEvent(aType, aKeyCode, aCharCode, aModifiers, aPreventDefault) ###
<pre>  
@see nsIDOMWindowUtils sendKeyEvent.  
  
</pre>
### requestNotifyAfterRemotePaint() ###
<pre>  
Request that the next time a remote layer transaction has been  
received by the Compositor, a MozAfterRemoteFrame event be sent  
to the window.  
  
</pre>
## Attributes ##

### docShell ###
<pre>  
Get the docshell from the frame loader.  
  
</pre>
### tabParent ###
<pre>  
Get this frame loader's TabParent, if it has a remote frame.  Otherwise,  
returns null.  
  
</pre>
### loadContext ###
<pre>  
Get an nsILoadContext for the top-level docshell. For remote  
frames, a shim is returned that contains private browsing and app  
information.  
  
</pre>
### depthTooGreat ###
<pre>  
Find out whether the loader's frame is at too great a depth in  
the frame tree.  This can be used to decide what operations may  
or may not be allowed on the loader's docshell.  
  
</pre>
### messageManager ###

### eventMode ###

### clipSubdocument ###
<pre>  
If false, then the subdocument is not clipped to its CSS viewport, and the  
subdocument's viewport scrollbar(s) are not rendered.  
Defaults to true.  
  
</pre>
### clampScrollPosition ###
<pre>  
If false, then the subdocument's scroll coordinates will not be clamped  
to their scroll boundaries.  
Defaults to true.  
  
</pre>
### ownerElement ###
<pre>  
The element which owns this frame loader.  
  
For example, if this is a frame loader for an <iframe>, this attribute  
returns the iframe element.  
  
</pre>
### childID ###
<pre>  
Cached childID of the ContentParent owning the TabParent in this frame  
loader. This can be used to obtain the childID after the TabParent died.  
  
</pre>
### visible ###
<pre>  
Get or set this frame loader's visibility.  
  
The notion of "visibility" here is separate from the notion of a  
window/docshell's visibility.  This field is mostly here so that we can  
have a notion of visibility in the parent process when frames are OOP.  
  
</pre>
### ownerIsBrowserOrAppFrame ###
<pre>  
Find out whether the owner content really is a browser or app frame  
Especially, a widget frame is regarded as an app frame.  
  
</pre>
### ownerIsWidget ###
<pre>  
Find out whether the owner content really is a widget. If this attribute  
returns true, |ownerIsBrowserOrAppFrame| must return true.  
  
</pre>
## Constants ##

### EVENT_MODE_NORMAL_DISPATCH ###
<pre>  
The default event mode automatically forwards the events  
handled in EventStateManager::HandleCrossProcessEvent to  
the child content process when these events are targeted to  
the remote browser element.  
  
Used primarly for input events (mouse, keyboard)  
  
</pre>
### EVENT_MODE_DONT_FORWARD_TO_CHILD ###
<pre>  
With this event mode, it's the application's responsability to   
convert and forward events to the content process  
  
</pre>