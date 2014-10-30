---
layout: default
---

# nsIAccessibleHyperLink #
  
A cross-platform interface that supports hyperlink-specific properties and  
methods.  Anchors, image maps, xul:labels with class="text-link" implement this interface.  
  

## Methods ##

### getURI ###
  
Returns the URI at the given index.  
  
@note  ARIA hyperlinks do not have an URI to point to, since clicks are  
processed via JavaScript. Therefore this property does not work on ARIA  
links.  
  
@param index  The 0-based index of the URI to be returned.  
  
@return the nsIURI object containing the specifications for the URI.  
  

### getAnchor ###
  
Returns a reference to the object at the given index.  
  
@param index  The 0-based index whose object is to be returned.  
  
@return the nsIAccessible object at the desired index.  
  

## Attributes ##

### startIndex ###
  
Returns the offset of the link within the parent accessible.  
  

### endIndex ###
  
Returns the end index of the link within the parent accessible.  
  
@note  The link itself is represented by one embedded character within the  
parent text, so the endIndex should be startIndex + 1.  
  

### valid ###
  
Determines whether the link is valid (e. g. points to a valid URL).  
  
@note  XXX Currently only used with ARIA links, and the author has to  
specify that the link is invalid via the aria-invalid="true" attribute.  
In all other cases, TRUE is returned.  
  

### anchorCount ###
  
The numbber of anchors within this Hyperlink. Is normally 1 for anchors.  
This anchor is, for example, the visible output of the html:a tag.  
With an Image Map, reflects the actual areas within the map.  
  
