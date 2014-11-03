---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIApplicationCacheChannel.idl">Source file</a>
</div>

# nsIApplicationCacheChannel #
<pre>  
Interface implemented by channels that support application caches.  
  
</pre>
## Methods ##

### markOfflineCacheEntryAsForeign() ###
<pre>  
A shortcut method to mark the cache item of this channel as 'foreign'.  
See the 'cache selection algorithm' and CACHE_SELECTION_RELOAD  
action handling in nsContentSink.  
  
</pre>
## Attributes ##

### loadedFromApplicationCache ###
<pre>  
TRUE when the resource came from the application cache. This  
might be false even there is assigned an application cache  
e.g. in case of fallback of load of an entry matching bypass  
namespace.  
  
</pre>
### inheritApplicationCache ###
<pre>  
When true, the channel will ask its notification callbacks for  
an application cache if one is not explicitly provided.  Default  
value is true.  
  
NS_ERROR_ALREADY_OPENED will be thrown if set after AsyncOpen()  
is called.  
  
</pre>
### chooseApplicationCache ###
<pre>  
When true, the channel will choose an application cache if one  
was not explicitly provided and none is available from the  
notification callbacks.  Default value is false.  
  
This attribute will not be transferred through a redirect.  
  
NS_ERROR_ALREADY_OPENED will be thrown if set after AsyncOpen()  
is called.  
  
</pre>
### applicationCacheForWrite ###
<pre>  
Set offline application cache object to instruct the channel  
to cache for offline use using this application cache.  
  
</pre>