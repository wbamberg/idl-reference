---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/streamconv/public/nsIDirIndexListener.idl">Source file</a>
</div>

# nsIDirIndexParser #
<pre>  
A parser for application/http-index-format  
  
</pre>
## Attributes ##

### listener ###
<pre>  
The interface to use as a callback for new entries  
  
</pre>
### comment ###
<pre>  
The comment given, if any  
This result is only valid _after_ OnStopRequest has occurred,  
because it can occur anywhere in the datastream  
  
</pre>
### encoding ###
<pre>  
The encoding to use  
  
</pre>