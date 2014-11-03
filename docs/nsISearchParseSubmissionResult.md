---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIBrowserSearchService.idl">Source file</a>
</div>

# nsISearchParseSubmissionResult #

## Attributes ##

### engine ###
<pre>  
The search engine associated with the URL passed in to  
nsISearchEngine::parseSubmissionURL, or null if the URL does not represent  
a search submission.  
  
</pre>
### terms ###
<pre>  
String containing the sought terms.  This can be an empty string in case no  
terms were specified or the URL does not represent a search submission.  
  
</pre>
### termsOffset ###
<pre>  
The offset of the string |terms| in the URL passed in to  
nsISearchEngine::parseSubmissionURL, or -1 if the URL does not represent  
a search submission.  
  
</pre>
### termsLength ###
<pre>  
The length of the |terms| in the original encoding of the URL passed in to  
nsISearchEngine::parseSubmissionURL. If the search term in the original  
URL is encoded then this will be bigger than |terms.length|.  
  
</pre>