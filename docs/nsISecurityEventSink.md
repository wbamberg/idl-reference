---
layout: default
---

# nsISecurityEventSink #

## Methods ##

### onSecurityChange ###
  
Fired when a security change occurs due to page transitions,  
or end document load. This interface should be called by  
a security package (eg Netscape Personal Security Manager)  
to notify nsIWebProgressListeners that security state has  
changed. State flags are in nsIWebProgressListener.idl  
  
