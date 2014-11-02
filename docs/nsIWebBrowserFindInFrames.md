---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/embedding/components/find/nsIWebBrowserFind.idl">Source file</a>
</div>
# nsIWebBrowserFindInFrames #
  
nsIWebBrowserFindInFrames  
  
Controls how find behaves when multiple frames or iframes are present.  
  
Get by doing a QueryInterface from nsIWebBrowserFind.  
  

## Attributes ##

### currentSearchFrame ###
  
currentSearchFrame  
  
Frame at which to start the search. Once the search is done, this will  
be set to be the last frame searched, whether or not a result was found.  
Has to be equal to or contained within the rootSearchFrame.  
  

### rootSearchFrame ###
  
rootSearchFrame  
  
Frame within which to confine the search (normally the content area frame).  
Set this to only search a subtree of the frame hierarchy.  
  

### searchSubframes ###
  
searchSubframes  
  
Whether to recurse down into subframes while searching. Default is true.  
  
Setting nsIWebBrowserfind.searchFrames to true sets this to true.  
  

### searchParentFrames ###
  
searchParentFrames  
  
Whether to allow the search to propagate out of the currentSearchFrame into its  
parent frame(s). Search is always confined within the rootSearchFrame. Default  
is true.  
  
Setting nsIWebBrowserfind.searchFrames to true sets this to true.  
  
