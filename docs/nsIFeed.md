---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/feeds/nsIFeed.idl">Source file</a>
</div>

# nsIFeed #
<pre>  
An nsIFeed represents a single Atom or RSS feed.  
  
</pre>
## Attributes ##

### subtitle ###
<pre>   
Uses description, subtitle, and extensions  
to generate a summary.   
  
</pre>
### type ###
<pre>  
The type of feed. For example, a podcast would be TYPE_AUDIO.  
  
</pre>
### enclosureCount ###
<pre>  
The total number of enclosures found in the feed.  
  
</pre>
### items ###
<pre>  
The items or entries in feed.  
  
</pre>
### cloud ###
<pre>  
No one really knows what cloud is for.  
  
It supposedly enables some sort of interaction with an XML-RPC or  
SOAP service.  
  
</pre>
### generator ###
<pre>  
Information about the software that produced the feed.  
  
</pre>
### image ###
<pre>  
An image url and some metadata (as defined by RSS2).  
  
  
</pre>
### textInput ###
<pre>  
No one really knows what textInput is for.  
  
See  
<http://www.cadenhead.org/workbench/news/2894/rss-joy-textinput>  
for more details.  
  
</pre>
### skipDays ###
<pre>  
Days to skip fetching. This field was supposed to designate  
intervals for feed fetching. It's not generally implemented. For  
example, if this array contained "Monday", aggregators should not  
fetch the feed on Mondays.  
  
</pre>
### skipHours ###
<pre>  
Hours to skip fetching. This field was supposed to designate  
intervals for feed fetching. It's not generally implemented. See  
<http://blogs.law.harvard.edu/tech/rss> for more information.  
  
</pre>
## Constants ##

### TYPE_FEED ###

### TYPE_AUDIO ###

### TYPE_IMAGE ###

### TYPE_VIDEO ###
