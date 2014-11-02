---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIBrowserSearchService.idl">Source file</a>
</div>

# nsISearchParseSubmissionResult #

## Attributes ##

### engine ###
  
The search engine associated with the URL passed in to  
nsISearchEngine::parseSubmissionURL, or null if the URL does not represent  
a search submission.  
  

### terms ###
  
String containing the sought terms.  This can be an empty string in case no  
terms were specified or the URL does not represent a search submission.  
  

### termsOffset ###
  
The offset of the string |terms| in the URL passed in to  
nsISearchEngine::parseSubmissionURL, or -1 if the URL does not represent  
a search submission.  
  

### termsLength ###
  
The length of the |terms| in the original encoding of the URL passed in to  
nsISearchEngine::parseSubmissionURL. If the search term in the original  
URL is encoded then this will be bigger than |terms.length|.  
  
