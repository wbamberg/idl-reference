---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/places/mozIAsyncHistory.idl">Source file</a>
</div>

# mozIVisitInfo #

## Attributes ##

### visitId ###
<pre>  
The machine-local (internal) id of the visit.  
  
</pre>
### visitDate ###
<pre>  
The time the visit occurred.  
  
</pre>
### transitionType ###
<pre>  
The transition type used to get to this visit.  One of the TRANSITION_TYPE  
constants on nsINavHistory.  
  
@see nsINavHistory.idl  
  
</pre>
### referrerURI ###
<pre>  
The referring URI of this visit.  This may be null.  
  
</pre>