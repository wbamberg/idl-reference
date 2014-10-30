---
layout: default
---

# nsIRequest #
  
nsIRequest  
  

## Methods ##

### isPending ###
  
Indicates whether the request is pending. nsIRequest::isPending is  
true when there is an outstanding asynchronous event that will make  
the request no longer be pending.  Requests do not necessarily start  
out pending; in some cases, requests have to be explicitly initiated  
(e.g. nsIChannel implementations are only pending once asyncOpen  
returns successfully).  
  
Requests can become pending multiple times during their lifetime.  
  
@return TRUE if the request has yet to reach completion.  
@return FALSE if the request has reached completion (e.g., after  
  OnStopRequest has fired).  
@note Suspended requests are still considered pending.  
  

### cancel ###
  
Cancels the current request.  This will close any open input or  
output streams and terminate any async requests.  Users should   
normally pass NS_BINDING_ABORTED, although other errors may also  
be passed.  The error passed in will become the value of the   
status attribute.  
  
Implementations must not send any notifications (e.g. via  
nsIRequestObserver) synchronously from this function. Similarly,  
removal from the load group (if any) must also happen asynchronously.  
  
Requests that use nsIStreamListener must not call onDataAvailable  
anymore after cancel has been called.  
  
@param aStatus the reason for canceling this request.  
  
NOTE: most nsIRequest implementations expect aStatus to be a  
failure code; however, some implementations may allow aStatus to  
be a success code such as NS_OK.  In general, aStatus should be  
a failure code.  
  

### suspend ###
  
Suspends the current request.  This may have the effect of closing  
any underlying transport (in order to free up resources), although  
any open streams remain logically opened and will continue delivering  
data when the transport is resumed.  
  
Calling cancel() on a suspended request must not send any  
notifications (such as onstopRequest) until the request is resumed.  
  
NOTE: some implementations are unable to immediately suspend, and  
may continue to deliver events already posted to an event queue. In  
general, callers should be capable of handling events even after   
suspending a request.  
  

### resume ###
  
Resumes the current request.  This may have the effect of re-opening  
any underlying transport and will resume the delivery of data to   
any open streams.  
  

## Attributes ##

### name ###
  
The name of the request.  Often this is the URI of the request.  
  

### status ###
  
The error status associated with the request.  
  

### loadGroup ###
  
The load group of this request.  While pending, the request is a   
member of the load group.  It is the responsibility of the request  
to implement this policy.  
  

### loadFlags ###
  
The load flags of this request.  Bits 0-15 are reserved.  
  
When added to a load group, this request's load flags are merged with  
the load flags of the load group.  
  

## Constants ##

### LOAD_REQUESTMASK ###
  
Mask defining the bits reserved for nsIRequest LoadFlags  
  

### LOAD_NORMAL ###
**********************************************************************  
Listed below are the various load flags which may be or'd together.  
  
  
No special load flags:  
  

### LOAD_BACKGROUND ###
  
Do not deliver status notifications to the nsIProgressEventSink and  
do not block the loadgroup from completing (should this load belong to one).  
Note: Progress notifications will still be delivered.  
  

### INHIBIT_PIPELINE ###
**********************************************************************  
The following flags control the flow of data into the cache.  
  
  
 This flag prevents loading of the request with an HTTP pipeline.  
 Generally this is because the resource is expected to take a  
 while to load and may cause head of line blocking problems.  
  

### INHIBIT_CACHING ###
  
This flag prevents caching of any kind.  It does not, however, prevent  
cached content from being used to satisfy this request.  
  

### INHIBIT_PERSISTENT_CACHING ###
  
This flag prevents caching on disk (or other persistent media), which  
may be needed to preserve privacy.  For HTTPS, this flag is set auto-  
matically.  
  

### LOAD_BYPASS_CACHE ###
**********************************************************************  
The following flags control what happens when the cache contains data  
that could perhaps satisfy this request.  They are listed in descending  
order of precidence.  
  
  
Force an end-to-end download of content data from the origin server.  
This flag is used for a shift-reload.  
  

### LOAD_FROM_CACHE ###
  
Attempt to force a load from the cache, bypassing ALL validation logic  
(note: this is stronger than VALIDATE_NEVER, which still validates for  
certain conditions).  
  
If the resource is not present in cache, it will be loaded from the  
network.  Combine this flag with LOAD_ONLY_FROM_CACHE if you wish to  
perform cache-only loads without validation checks.  
  
This flag is used when browsing via history.  It is not recommended for  
normal browsing as it may likely violate reasonable assumptions made by  
the server and confuse users.  
  

### VALIDATE_ALWAYS ###
  
The following flags control the frequency of cached content validation  
when neither LOAD_BYPASS_CACHE or LOAD_FROM_CACHE are set.  By default,  
cached content is automatically validated if necessary before reuse.  
  
VALIDATE_ALWAYS forces validation of any cached content independent of  
its expiration time.  
  
VALIDATE_NEVER disables validation of cached content, unless it arrived  
with the "Cache: no-store" header, or arrived via HTTPS with the  
"Cache: no-cache" header.  
  
VALIDATE_ONCE_PER_SESSION disables validation of expired content,   
provided it has already been validated (at least once) since the start   
of this session.  
  
NOTE TO IMPLEMENTORS:  
  These flags are intended for normal browsing, and they should therefore  
  not apply to content that must be validated before each use.  Consider,  
  for example, a HTTP response with a "Cache-control: no-cache" header.  
  According to RFC2616, this response must be validated before it can  
  be taken from a cache.  Breaking this requirement could result in   
  incorrect and potentially undesirable side-effects.  
  

### VALIDATE_NEVER ###

### VALIDATE_ONCE_PER_SESSION ###

### LOAD_ANONYMOUS ###
  
When set, this flag indicates that no user-specific data should be added  
to the request when opened. This means that things like authorization  
tokens or cookie headers should not be added.  
  

### LOAD_FRESH_CONNECTION ###
  
When set, this flag indicates that caches of network connections,  
particularly HTTP persistent connections, should not be used.  
  
