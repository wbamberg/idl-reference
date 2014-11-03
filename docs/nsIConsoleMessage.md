---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/base/nsIConsoleMessage.idl">Source file</a>
</div>

# nsIConsoleMessage #
<pre>  
This is intended as a base interface; implementations may want to  
provide an object that can be qi'ed to provide more specific  
message information.  
  
</pre>
## Methods ##

### toString() ###

## Attributes ##

### logLevel ###
<pre>  
The log level of this message.  
  
</pre>
### timeStamp ###
<pre>  
The time (in milliseconds from the Epoch) that the message instance  
was initialised.  
The timestamp is initialized as JS_now/1000 so that it can be  
compared to Date.now in Javascript.  
  
</pre>
### message ###

## Constants ##

### debug ###
<pre> Log level constants. */  
</pre>
### info ###

### warn ###

### error ###
