---
layout: default
---

# nsIAnnotationObserver #

## Methods ##

### onPageAnnotationSet(aPage, aName) ###
  
Called when an annotation value is set. It could be a new annotation,  
or it could be a new value for an existing annotation.  
  

### onItemAnnotationSet(aItemId, aName) ###

### onPageAnnotationRemoved(aURI, aName) ###
  
Called when an annotation is deleted. If aName is empty, then ALL  
annotations for the given URI have been deleted. This is not called when  
annotations are expired (normally happens when the app exits).  
  

### onItemAnnotationRemoved(aItemId, aName) ###
