---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/feeds/nsIFeedContainer.idl">Source file</a>
</div>

# nsIFeedContainer #
<pre>  
A shared base for feeds and items, which are pretty similar,  
but they have some divergent attributes and require  
different convenience methods.  
  
</pre>
## Methods ##

### normalize() ###
<pre>  
Syncs a container's fields with its convenience attributes.  
  
</pre>
## Attributes ##

### id ###
<pre>  
Many feeds contain an ID distinct from their URI, and  
entries have standard fields for this in all major formats.  
  
</pre>
### fields ###
<pre>  
The fields found in the document. Common Atom  
and RSS fields are normalized. This includes some namespaced  
extensions such as dc:subject and content:encoded.   
Consumers can avoid normalization by checking the feed type  
and accessing specific fields.  
  
Common namespaces are accessed using prefixes, like get("dc:subject");.  
See nsIFeedResult::registerExtensionPrefix.  
  
</pre>
### title ###
<pre>  
Sometimes there's no title, or the title contains markup, so take  
care in decoding the attribute.  
  
</pre>
### link ###
<pre>  
Returns the primary link for the feed or entry.  
  
</pre>
### links ###
<pre>  
Returns all links for a feed or entry.  
  
</pre>
### categories ###
<pre>  
Returns the categories found in a feed or entry.  
  
</pre>
### rights ###
<pre>  
The rights or license associated with a feed or entry.  
  
</pre>
### authors ###
<pre>  
A list of nsIFeedPersons that authored the feed.  
  
</pre>
### contributors ###
<pre>  
A list of nsIFeedPersons that contributed to the feed.  
  
</pre>
### updated ###
<pre>  
The date the feed was updated, in RFC822 form. Parsable by JS  
and mail code.  
  
</pre>