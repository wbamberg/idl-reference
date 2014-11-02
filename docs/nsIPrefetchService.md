---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/uriloader/prefetch/nsIPrefetchService.idl">Source file</a>
</div>

# nsIPrefetchService #

## Methods ##

### prefetchURI(aURI, aReferrerURI, aSource, aExplicit) ###
  
Enqueue a request to prefetch the specified URI.  
  
@param aURI the URI of the document to prefetch  
@param aReferrerURI the URI of the referring page  
@param aSource the DOM node (such as a <link> tag) that requested this  
       fetch, or null if the prefetch was not requested by a DOM node.  
@param aExplicit the link element has an explicit prefetch link type  
  

#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>the URI of the document to prefetch  
</td>
</tr>

<tr>
<td>aReferrerURI</td>
<td>the URI of the referring page  
</td>
</tr>

<tr>
<td>aSource</td>
<td>the DOM node (such as a <link> tag) that requested this  
       fetch, or null if the prefetch was not requested by a DOM node.  
</td>
</tr>

<tr>
<td>aExplicit</td>
<td>the link element has an explicit prefetch link type  
</td>
</tr>

</table>

### enumerateQueue() ###
  
Enumerate the items in the prefetch queue.  
  
