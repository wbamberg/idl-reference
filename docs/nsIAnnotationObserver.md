---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/places/nsIAnnotationService.idl">Source file</a>
</div>

# nsIAnnotationObserver #

## Methods ##

### onPageAnnotationSet(aPage, aName) ###
<pre>  
Called when an annotation value is set. It could be a new annotation,  
or it could be a new value for an existing annotation.  
  
</pre>
### onItemAnnotationSet(aItemId, aName) ###

### onPageAnnotationRemoved(aURI, aName) ###
<pre>  
Called when an annotation is deleted. If aName is empty, then ALL  
annotations for the given URI have been deleted. This is not called when  
annotations are expired (normally happens when the app exits).  
  
</pre>
### onItemAnnotationRemoved(aItemId, aName) ###
