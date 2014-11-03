---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/feeds/nsIFeedResult.idl">Source file</a>
</div>

# nsIFeedResult #
<pre>  
The nsIFeedResult interface provides access to HTTP and parsing  
metadata for a feed or entry.  
  
</pre>
## Methods ##

### registerExtensionPrefix(aNamespace, aPrefix) ###
<pre>  
Registers a prefix used to access an extension in the feed/entry   
  
</pre>
## Attributes ##

### bozo ###
<pre>   
The Feed parser will set the bozo bit when a feed triggers a fatal  
error during XML parsing. There may be entries and feed metadata  
that were parsed before the error.  Thanks to Tim Bray for  
suggesting this terminology.  
<http://www.tbray.org/ongoing/When/200x/2004/01/11/PostelPilgrim>  
  
</pre>
### doc ###
<pre>  
The parsed feed or entry.   
  
Will be null if a non-feed is processed.  
  
</pre>
### uri ###
<pre>   
The address from which the feed was fetched.   
  
</pre>
### version ###
<pre>   
Feed Version:   
atom, rss2, rss09, rss091, rss091userland, rss092, rss1, atom03,   
atomEntry, rssItem  
  
Will be null if a non-feed is processed.  
  
</pre>
### stylesheet ###
<pre>  
An XSLT stylesheet available to transform the source of the  
feed. Some feeds include this information in a processing  
instruction. It's generally intended for clients with specific  
feed capabilities.  
  
</pre>
### headers ###
<pre>  
HTTP response headers that accompanied the feed.   
  
</pre>