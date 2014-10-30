---
layout: default
---

# nsIAccessibleHyperText #
  
A cross-platform interface that deals with text which contains hyperlinks.  
Each link is an embedded object representing exactly 1 character within  
the hypertext.  
  
Current implementation assumes every embedded object is a link.  
  

## Methods ##

### getLinkAt(index) ###
  
Return link accessible at the given index.  
  
@param index  [in] 0-based index of the link that is to be retrieved  
  
@return       link accessible or null if there is no link at that index  
  

### getLinkIndex(link) ###
  
Return index of the given link.  
  
@param link  [in] link accessible the index is requested for  
  
@return      index of the given link or null if there's no link within  
               hypertext accessible  
  

### getLinkIndexAtOffset(offset) ###

## Attributes ##

### linkCount ###
  
Return the number of links contained within this hypertext object.  
  
