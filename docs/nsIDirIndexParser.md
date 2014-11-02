---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/streamconv/public/nsIDirIndexListener.idl">Source file</a>
</div>

# nsIDirIndexParser #
  
A parser for application/http-index-format  
  

## Attributes ##

### listener ###
  
The interface to use as a callback for new entries  
  

### comment ###
  
The comment given, if any  
This result is only valid _after_ OnStopRequest has occurred,  
because it can occur anywhere in the datastream  
  

### encoding ###
  
The encoding to use  
  
