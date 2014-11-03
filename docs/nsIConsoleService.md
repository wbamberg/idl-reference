---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/base/nsIConsoleService.idl">Source file</a>
</div>

# nsIConsoleService #

## Methods ##

### logMessage(message) ###

### logStringMessage(message) ###
<code>  
Convenience method for logging simple messages.  
  
</code>
### getMessageArray(count, messages) ###
<code>  
Get an array of all the messages logged so far.  If no messages  
are logged, this function will return a count of 0, but still  
will allocate one word for messages, so as to show up as a  
0-length array when called from script.  
  
</code>
### registerListener(listener) ###
<code>  
To guard against stack overflows from listeners that could log  
messages (it's easy to do this inadvertently from listeners  
implemented in JavaScript), we don't call any listeners when  
another error is already being logged.  
  
</code>
### unregisterListener(listener) ###
<code>  
Each registered listener should also be unregistered.  
  
</code>
### reset() ###
<code>  
Clear the message buffer (e.g. for privacy reasons).  
  
</code>