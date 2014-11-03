---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/exthelper/extIApplication.idl">Source file</a>
</div>

# extIEventItem #
<pre>  
Interface holds information about an event.  
  
</pre>
## Methods ##

### preventDefault() ###
<pre>  
Cancels the event if it is cancelable.  
  
</pre>
## Attributes ##

### type ###
<pre>  
The name of the event  
  
</pre>
### data ###
<pre>  
Can hold extra details and data associated with the event. This  
is optional and event specific. If the event does not send extra  
details, this is null.  
  
</pre>