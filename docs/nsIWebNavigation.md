---
layout: default
---

# nsIWebNavigation #
  
The nsIWebNavigation interface defines an interface for navigating the web.  
It provides methods and attributes to direct an object to navigate to a new  
location, stop or restart an in process load, or determine where the object  
has previously gone.  
  

## Methods ##

### goBack() ###
  
Tells the object to navigate to the previous session history item.  When a  
page is loaded from session history, all content is loaded from the cache  
(if available) and page state (such as form values and scroll position) is  
restored.  
  
@throw NS_ERROR_UNEXPECTED  
       Indicates that the call was unexpected at this time, which implies  
       that canGoBack is false.  
  

### goForward() ###
  
Tells the object to navigate to the next session history item.  When a  
page is loaded from session history, all content is loaded from the cache  
(if available) and page state (such as form values and scroll position) is  
restored.  
  
@throw NS_ERROR_UNEXPECTED  
       Indicates that the call was unexpected at this time, which implies  
       that canGoForward is false.  
  

### gotoIndex(index) ###
  
Tells the object to navigate to the session history item at a given index.  
  
@throw NS_ERROR_UNEXPECTED  
       Indicates that the call was unexpected at this time, which implies  
       that session history entry at the given index does not exist.  
  

### loadURI(aURI, aLoadFlags, aReferrer, aPostData, aHeaders) ###
  
Loads a given URI.  This will give priority to loading the requested URI  
in the object implementing	this interface.  If it can't be loaded here  
however, the URI dispatcher will go through its normal process of content  
loading.  
  
@param aURI  
       The URI string to load.  For HTTP and FTP URLs and possibly others,  
       characters above U+007F will be converted to UTF-8 and then URL-  
       escaped per the rules of RFC 2396.  
@param aLoadFlags  
       Flags modifying load behaviour.  This parameter is a bitwise  
       combination of the load flags defined above.  (Undefined bits are  
       reserved for future use.)  Generally you will pass LOAD_FLAGS_NONE  
       for this parameter.  
@param aReferrer  
       The referring URI.  If this argument is null, then the referring  
       URI will be inferred internally.  
@param aPostData  
       If the URI corresponds to a HTTP request, then this stream is  
       appended directly to the HTTP request headers.  It may be prefixed  
       with additional HTTP headers.  This stream must contain a "\r\n"  
       sequence separating any HTTP headers from the HTTP request body.  
       This parameter is optional and may be null.  
@param aHeaders  
       If the URI corresponds to a HTTP request, then any HTTP headers  
       contained in this stream are set on the HTTP request.  The HTTP  
       header stream is formatted as:  
           ( HEADER "\r\n" )*  
       This parameter is optional and may be null.  
  

#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>       The URI string to load.  For HTTP and FTP URLs and possibly others,  
       characters above U+007F will be converted to UTF-8 and then URL-  
       escaped per the rules of RFC 2396.  
</td>
</tr>

<tr>
<td>aLoadFlags</td>
<td>       Flags modifying load behaviour.  This parameter is a bitwise  
       combination of the load flags defined above.  (Undefined bits are  
       reserved for future use.)  Generally you will pass LOAD_FLAGS_NONE  
       for this parameter.  
</td>
</tr>

<tr>
<td>aReferrer</td>
<td>       The referring URI.  If this argument is null, then the referring  
       URI will be inferred internally.  
</td>
</tr>

<tr>
<td>aPostData</td>
<td>       If the URI corresponds to a HTTP request, then this stream is  
       appended directly to the HTTP request headers.  It may be prefixed  
       with additional HTTP headers.  This stream must contain a "\r\n"  
       sequence separating any HTTP headers from the HTTP request body.  
       This parameter is optional and may be null.  
</td>
</tr>

<tr>
<td>aHeaders</td>
<td>       If the URI corresponds to a HTTP request, then any HTTP headers  
       contained in this stream are set on the HTTP request.  The HTTP  
       header stream is formatted as:  
           ( HEADER "\r\n" )*  
       This parameter is optional and may be null.  
</td>
</tr>

</table>

### loadURIWithBase(aURI, aLoadFlags, aReferrer, aPostData, aHeaders, aBaseURI) ###
  
Loads a given URI.  This will give priority to loading the requested URI  
in the object implementing this interface.  If it can't be loaded here  
however, the URI dispatcher will go through its normal process of content  
loading.  
Behaves like loadURI, except an additional parameter is provided to supply  
a base URI to be used in specific situations where one cannot be inferred  
by other means, for example when this is called to view selection source.  
Outside of these situations, the behaviour of this function is no  
different to loadURI.  
  
@param aURI  
       The URI string to load.  For HTTP and FTP URLs and possibly others,  
       characters above U+007F will be converted to UTF-8 and then URL-  
       escaped per the rules of RFC 2396.  
@param aLoadFlags  
       Flags modifying load behaviour.  This parameter is a bitwise  
       combination of the load flags defined above.  (Undefined bits are  
       reserved for future use.)  Generally you will pass LOAD_FLAGS_NONE  
       for this parameter.  
@param aReferrer  
       The referring URI.  If this argument is null, then the referring  
       URI will be inferred internally.  
@param aPostData  
       If the URI corresponds to a HTTP request, then this stream is  
       appended directly to the HTTP request headers.  It may be prefixed  
       with additional HTTP headers.  This stream must contain a "\r\n"  
       sequence separating any HTTP headers from the HTTP request body.  
       This parameter is optional and may be null.  
@param aHeaders  
       If the URI corresponds to a HTTP request, then any HTTP headers  
       contained in this stream are set on the HTTP request.  The HTTP  
       header stream is formatted as:  
           ( HEADER "\r\n" )*  
       This parameter is optional and may be null.  
@param aBaseURI  
       Set to indicate a base URI to be associated with the load. Note  
       that at present this argument is only used with view-source aURIs  
       and cannot be used to resolve aURI.  
       This parameter is optional and may be null.  
  

#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>       The URI string to load.  For HTTP and FTP URLs and possibly others,  
       characters above U+007F will be converted to UTF-8 and then URL-  
       escaped per the rules of RFC 2396.  
</td>
</tr>

<tr>
<td>aLoadFlags</td>
<td>       Flags modifying load behaviour.  This parameter is a bitwise  
       combination of the load flags defined above.  (Undefined bits are  
       reserved for future use.)  Generally you will pass LOAD_FLAGS_NONE  
       for this parameter.  
</td>
</tr>

<tr>
<td>aReferrer</td>
<td>       The referring URI.  If this argument is null, then the referring  
       URI will be inferred internally.  
</td>
</tr>

<tr>
<td>aPostData</td>
<td>       If the URI corresponds to a HTTP request, then this stream is  
       appended directly to the HTTP request headers.  It may be prefixed  
       with additional HTTP headers.  This stream must contain a "\r\n"  
       sequence separating any HTTP headers from the HTTP request body.  
       This parameter is optional and may be null.  
</td>
</tr>

<tr>
<td>aHeaders</td>
<td>       If the URI corresponds to a HTTP request, then any HTTP headers  
       contained in this stream are set on the HTTP request.  The HTTP  
       header stream is formatted as:  
           ( HEADER "\r\n" )*  
       This parameter is optional and may be null.  
</td>
</tr>

<tr>
<td>aBaseURI</td>
<td>       Set to indicate a base URI to be associated with the load. Note  
       that at present this argument is only used with view-source aURIs  
       and cannot be used to resolve aURI.  
       This parameter is optional and may be null.  
</td>
</tr>

</table>

### reload(aReloadFlags) ###
  
Tells the Object to reload the current page.  There may be cases where the  
user will be asked to confirm the reload (for example, when it is  
determined that the request is non-idempotent).  
  
@param aReloadFlags  
       Flags modifying load behaviour.  This parameter is a bitwise  
       combination of the Load Flags defined above.  (Undefined bits are  
       reserved for future use.)  Generally you will pass LOAD_FLAGS_NONE  
       for this parameter.  
  
@throw NS_BINDING_ABORTED  
       Indicating that the user canceled the reload.  
  

#### Parameters ####

<table>

<tr>
<td>aReloadFlags</td>
<td>       Flags modifying load behaviour.  This parameter is a bitwise  
       combination of the Load Flags defined above.  (Undefined bits are  
       reserved for future use.)  Generally you will pass LOAD_FLAGS_NONE  
       for this parameter.  
</td>
</tr>

</table>

### stop(aStopFlags) ###
  
Stops a load of a URI.  
  
@param aStopFlags  
       This parameter is one of the stop flags defined above.  
  

#### Parameters ####

<table>

<tr>
<td>aStopFlags</td>
<td>       This parameter is one of the stop flags defined above.  
</td>
</tr>

</table>

## Attributes ##

### canGoBack ###
  
Indicates if the object can go back.  If true this indicates that  
there is back session history available for navigation.  
  

### canGoForward ###
  
Indicates if the object can go forward.  If true this indicates that  
there is forward session history available for navigation  
  

### document ###
  
Retrieves the current DOM document for the frame, or lazily creates a  
blank document if there is none.  This attribute never returns null except  
for unexpected error situations.  
  

### currentURI ###
  
The currently loaded URI or null.  
  

### referringURI ###
  
The referring URI for the currently loaded URI or null.  
  

### sessionHistory ###
  
The session history object used by this web navigation instance.  
  

## Constants ##

### LOAD_FLAGS_MASK ###
************************************************************************  
The following flags may be bitwise combined to form the load flags  
parameter passed to either the loadURI or reload method.  Some of these  
flags are only applicable to loadURI.  
  
  
This flags defines the range of bits that may be specified.  Flags  
outside this range may be used, but may not be passed to Reload().  
  

### LOAD_FLAGS_NONE ###
  
This is the default value for the load flags parameter.  
  

### LOAD_FLAGS_IS_REFRESH ###
  
Flags 0x1, 0x2, 0x4, 0x8 are reserved for internal use by  
nsIWebNavigation implementations for now.  
  
  
This flag specifies that the load should have the semantics of an HTML  
Meta-refresh tag (i.e., that the cache should be bypassed).  This flag  
is only applicable to loadURI.  
XXX the meaning of this flag is poorly defined.  
XXX no one uses this, so we should probably deprecate and remove it.  
  

### LOAD_FLAGS_IS_LINK ###
  
This flag specifies that the load should have the semantics of a link  
click.  This flag is only applicable to loadURI.  
XXX the meaning of this flag is poorly defined.  
  

### LOAD_FLAGS_BYPASS_HISTORY ###
  
This flag specifies that history should not be updated.  This flag is only  
applicable to loadURI.  
  

### LOAD_FLAGS_REPLACE_HISTORY ###
  
This flag specifies that any existing history entry should be replaced.  
This flag is only applicable to loadURI.  
  

### LOAD_FLAGS_BYPASS_CACHE ###
  
This flag specifies that the local web cache should be bypassed, but an  
intermediate proxy cache could still be used to satisfy the load.  
  

### LOAD_FLAGS_BYPASS_PROXY ###
  
This flag specifies that any intermediate proxy caches should be bypassed  
(i.e., that the content should be loaded from the origin server).  
  

### LOAD_FLAGS_CHARSET_CHANGE ###
  
This flag specifies that a reload was triggered as a result of detecting  
an incorrect character encoding while parsing a previously loaded  
document.  
  

### LOAD_FLAGS_STOP_CONTENT ###
  
If this flag is set, Stop() will be called before the load starts  
and will stop both content and network activity (the default is to  
only stop network activity).  Effectively, this passes the  
STOP_CONTENT flag to Stop(), in addition to the STOP_NETWORK flag.  
  

### LOAD_FLAGS_FROM_EXTERNAL ###
  
A hint this load was prompted by an external program: take care!  
  

### LOAD_FLAGS_ALLOW_MIXED_CONTENT ###
  
This flag is set when a user explicitly disables the Mixed Content  
Blocker, and allows Mixed Content to load on an https page.  
  

### LOAD_FLAGS_FIRST_LOAD ###
  
This flag specifies that this is the first load in this object.  
Set with care, since setting incorrectly can cause us to assume that  
nothing was actually loaded in this object if the load ends up being   
handled by an external application.  This flag must not be passed to  
Reload.  
  

### LOAD_FLAGS_ALLOW_POPUPS ###
  
This flag specifies that the load should not be subject to popup  
blocking checks.  This flag must not be passed to Reload.  
  

### LOAD_FLAGS_BYPASS_CLASSIFIER ###
  
This flag specifies that the URI classifier should not be checked for  
this load.  This flag must not be passed to Reload.  
  

### LOAD_FLAGS_FORCE_ALLOW_COOKIES ###
  
Force relevant cookies to be sent with this load even if normally they  
wouldn't be.  
  

### LOAD_FLAGS_DISALLOW_INHERIT_OWNER ###
  
Prevent the owner principal from being inherited for this load.  
  

### LOAD_FLAGS_ALLOW_THIRD_PARTY_FIXUP ###
  
This flag specifies that the URI may be submitted to a third-party  
server for correction. This should only be applied to non-sensitive  
URIs entered by users.  This flag must not be passed to Reload.  
  

### LOAD_FLAGS_FIXUP_SCHEME_TYPOS ###
  
This flag specifies that common scheme typos should be corrected.  
  

### STOP_NETWORK ###
************************************************************************  
The following flags may be passed as the stop flags parameter to the stop  
method defined on this interface.  
  
  
This flag specifies that all network activity should be stopped.  This  
includes both active network loads and pending META-refreshes.  
  

### STOP_CONTENT ###
  
This flag specifies that all content activity should be stopped.  This  
includes animated images, plugins and pending Javascript timeouts.  
  

### STOP_ALL ###
  
This flag specifies that all activity should be stopped.  
  
