---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/events/nsIDOMMessageEvent.idl">Source file</a>
</div>

# nsIDOMMessageEvent #
<pre>  
The nsIDOMMessageEvent interface is used for server-sent events and for  
cross-domain messaging.  
  
For more information on this interface, please see  
http://www.whatwg.org/specs/web-apps/current-work/#messageevent  
  
</pre>
## Methods ##

### initMessageEvent(aType, aCanBubble, aCancelable, aData, aOrigin, aLastEventId, aSource) ###
<pre>  
Initializes this event with the given data, in a manner analogous to  
the similarly-named method on the nsIDOMEvent interface, also setting the  
data, origin, source, and lastEventId attributes of this appropriately.  
  
</pre>
## Attributes ##

### data ###
<pre>  
Custom string data associated with this event.  
  
</pre>
### origin ###
<pre>  
The origin of the site from which this event originated, which is the  
scheme, ":", and if the URI has a host, "//" followed by the  
host, and if the port is not the default for the given scheme,  
":" followed by that port.  This value does not have a trailing slash.  
  
</pre>
### lastEventId ###
<pre>  
The last event ID string of the event source, for server-sent DOM events; this  
value is the empty string for cross-origin messaging.  
  
</pre>
### source ###
<pre>  
The window which originated this event.  
  
</pre>