---
layout: default
---

# nsIDocShellLoadInfo #

## Attributes ##

### referrer ###
 This is the referrer for the load. */  

### owner ###
 The owner of the load, that is, the entity responsible for   
 causing the load to occur. This should be a nsIPrincipal typically.  
  

### inheritOwner ###
 If this attribute is true and no owner is specified, copy  
 the owner from the referring document.  
  

### ownerIsExplicit ###
 If this attribute is true only ever use the owner specify by  
 the owner and inheritOwner attributes.  
 If there are security reasons for why this is unsafe, such  
 as trying to use a systemprincipal owner for a content docshell  
 the load fails.  
  

### loadType ###
 Contains a load type as specified by the load* constants */  

### SHEntry ###
 SHEntry for this page */  

### target ###
 Target for load, like _content, _blank etc. */  

### postDataStream ###
 Post data */  

### headersStream ###
 Additional headers */  

### sendReferrer ###
 True if the referrer should be sent, false if it shouldn't be  
 sent, even if it's available. This attribute defaults to true.  
  

### isSrcdocLoad ###
 True if the docshell has been created to load an iframe where the  
srcdoc attribute has been set.  Set when srcdocData is specified.  
  

### srcdocData ###
 When set, the load will be interpreted as a srcdoc load, where contents  
of this string will be loaded instead of the URI.  Setting srcdocData  
sets isSrcdocLoad to true  
  

### sourceDocShell ###
 When set, this is the Source Browsing Context for the navigation. */  

### baseURI ###
  
Used for srcdoc loads to give view-source knowledge of the load's base  
URI as this information isn't embedded in the load's URI.  
  

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
