---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/places/nsIAnnotationService.idl">Source file</a>
</div>

# mozIAnnotatedResult #
<code>  
Represents a place annotated with a given annotation.  If a place has  
multiple annotations, it can be represented by multiple  
mozIAnnotatedResult(s).  
  
</code>
## Attributes ##

### guid ###
  
The globally unique identifier of the place with this annotation.  
  
@note if itemId is valid this is the guid of the bookmark, otherwise  
      of the page.  
  

### uri ###
  
The URI of the place with this annotation, if available, null otherwise.  
  

### itemId ###
  
The bookmark id of the place with this annotation, if available,  
-1 otherwise.  
  
@note if itemId is -1, it doesn't mean the page is not bookmarked, just  
      that this annotation is relative to the page, not to the bookmark.  
  

### annotationName ###
  
Name of the annotation.  
  

### annotationValue ###
  
Value of the annotation.  
  
