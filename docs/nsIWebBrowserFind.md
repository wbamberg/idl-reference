---
layout: default
---

# nsIWebBrowserFind #
  
nsIWebBrowserFind  
  
Searches for text in a web browser.  
  
Get one by doing a GetInterface on an nsIWebBrowser.  
  
By default, the implementation will search the focussed frame, or  
if there is no focussed frame, the web browser content area. It  
does not by default search subframes or iframes. To change this  
behaviour, and to explicitly set the frame to search,   
QueryInterface to nsIWebBrowserFindInFrames.  
  

## Methods ##

### findNext ###
  
findNext  
  
Finds, highlights, and scrolls into view the next occurrence of the  
search string, using the current search settings. Fails if the  
search string is empty.  
  
@return  Whether an occurrence was found  
  

## Attributes ##

### searchString ###
  
searchString  
  
The string to search for. This must be non-empty to search.  
  

### findBackwards ###
  
findBackwards  
  
Whether to find backwards (towards the beginning of the document).  
Default is false (search forward).  
  

### wrapFind ###
  
wrapFind  
  
Whether the search wraps around to the start (or end) of the document  
if no match was found between the current position and the end (or  
beginning). Works correctly when searching backwards. Default is  
false.  
  

### entireWord ###
  
entireWord  
  
Whether to match entire words only. Default is false.  
  

### matchCase ###
  
matchCase  
  
Whether to match case (case sensitive) when searching. Default is false.  
  

### searchFrames ###
  
searchFrames  
  
Whether to search through all frames in the content area. Default is true.  
  
Note that you can control whether the search propagates into child or  
parent frames explicitly using nsIWebBrowserFindInFrames, but if one,  
but not both, of searchSubframes and searchParentFrames are set, this  
returns false.  
  
