---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsISecurityEventSink.idl">Source file</a>
</div>

# nsISecurityEventSink #

## Methods ##

### onSecurityChange(i_Context, state) ###
<code>  
Fired when a security change occurs due to page transitions,  
or end document load. This interface should be called by  
a security package (eg Netscape Personal Security Manager)  
to notify nsIWebProgressListeners that security state has  
changed. State flags are in nsIWebProgressListener.idl  
  
</code>