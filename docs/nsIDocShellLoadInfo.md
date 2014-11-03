---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/docshell/base/nsIDocShellLoadInfo.idl">Source file</a>
</div>

# nsIDocShellLoadInfo #

## Attributes ##

### referrer ###
<pre> This is the referrer for the load. */  
</pre>
### owner ###
<pre> The owner of the load, that is, the entity responsible for   
 causing the load to occur. This should be a nsIPrincipal typically.  
  
</pre>
### inheritOwner ###
<pre> If this attribute is true and no owner is specified, copy  
 the owner from the referring document.  
  
</pre>
### ownerIsExplicit ###
<pre> If this attribute is true only ever use the owner specify by  
 the owner and inheritOwner attributes.  
 If there are security reasons for why this is unsafe, such  
 as trying to use a systemprincipal owner for a content docshell  
 the load fails.  
  
</pre>
### loadType ###
<pre> Contains a load type as specified by the load* constants */  
</pre>
### SHEntry ###
<pre> SHEntry for this page */  
</pre>
### target ###
<pre> Target for load, like _content, _blank etc. */  
</pre>
### postDataStream ###
<pre> Post data */  
</pre>
### headersStream ###
<pre> Additional headers */  
</pre>
### sendReferrer ###
<pre> True if the referrer should be sent, false if it shouldn't be  
 sent, even if it's available. This attribute defaults to true.  
  
</pre>
### isSrcdocLoad ###
<pre> True if the docshell has been created to load an iframe where the  
srcdoc attribute has been set.  Set when srcdocData is specified.  
  
</pre>
### srcdocData ###
<pre> When set, the load will be interpreted as a srcdoc load, where contents  
of this string will be loaded instead of the URI.  Setting srcdocData  
sets isSrcdocLoad to true  
  
</pre>
### sourceDocShell ###
<pre> When set, this is the Source Browsing Context for the navigation. */  
</pre>
### baseURI ###
<pre>  
Used for srcdoc loads to give view-source knowledge of the load's base  
URI as this information isn't embedded in the load's URI.  
  
</pre>
## Constants ##

### loadNormal ###

### loadNormalReplace ###

### loadHistory ###

### loadReloadNormal ###

### loadReloadBypassCache ###

### loadReloadBypassProxy ###

### loadReloadBypassProxyAndCache ###

### loadLink ###

### loadRefresh ###

### loadReloadCharsetChange ###

### loadBypassHistory ###

### loadStopContent ###

### loadStopContentAndReplace ###

### loadNormalExternal ###

### loadNormalBypassCache ###

### loadNormalBypassProxy ###

### loadNormalBypassProxyAndCache ###

### loadPushState ###

### loadReplaceBypassCache ###

### loadReloadMixedContent ###

### loadNormalAllowMixedContent ###
