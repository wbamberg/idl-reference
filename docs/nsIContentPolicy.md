---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/base/nsIContentPolicy.idl">Source file</a>
</div>

# nsIContentPolicy #
<pre>  
Interface for content policy mechanism.  Implementations of this  
interface can be used to control loading of various types of out-of-line  
content, or processing of certain types of in-line content.  
  
WARNING: do not block the caller from shouldLoad or shouldProcess (e.g.,  
by launching a dialog to prompt the user for something).  
  
</pre>
## Methods ##

### shouldLoad(aContentType, aContentLocation, aRequestOrigin, aContext, aMimeTypeGuess, aExtra, aRequestPrincipal) ###
<pre>  
Should the resource at this location be loaded?  
ShouldLoad will be called before loading the resource at aContentLocation  
to determine whether to start the load at all.  
  
@param aContentType      the type of content being tested. This will be one  
                         one of the TYPE_* constants.  
  
@param aContentLocation  the location of the content being checked; must  
                         not be null  
  
@param aRequestOrigin    OPTIONAL. the location of the resource that  
                         initiated this load request; can be null if  
                         inapplicable  
  
@param aContext          OPTIONAL. the nsIDOMNode or nsIDOMWindow that  
                         initiated the request, or something that can QI  
                         to one of those; can be null if inapplicable.  
                         Note that for navigation events (new windows and  
                         link clicks), this is the NEW window.  
  
@param aMimeTypeGuess    OPTIONAL. a guess for the requested content's  
                         MIME type, based on information available to  
                         the request initiator (e.g., an OBJECT's type  
                         attribute); does not reliably reflect the  
                         actual MIME type of the requested content  
  
@param aExtra            an OPTIONAL argument, pass-through for non-Gecko  
                         callers to pass extra data to callees.  
  
@param aRequestPrincipal an OPTIONAL argument, defines the principal that  
                         caused the load. This is optional only for  
                         non-gecko code: all gecko code should set this  
                         argument.  For navigation events, this is  
                         the principal of the page that caused this load.  
  
@return ACCEPT or REJECT_*  
  
@note shouldLoad can be called while the DOM and layout of the document  
involved is in an inconsistent state.  This means that implementors of  
this method MUST NOT do any of the following:  
1)  Modify the DOM in any way (e.g. setting attributes is a no-no).  
2)  Query any DOM properties that depend on layout (e.g. offset*  
    properties).  
3)  Query any DOM properties that depend on style (e.g. computed style).  
4)  Query any DOM properties that depend on the current state of the DOM  
    outside the "context" node (e.g. lengths of node lists).  
5)  [JavaScript implementations only] Access properties of any sort on any  
    object without using XPCNativeWrapper (either explicitly or  
    implicitly).  Due to various DOM0 things, this leads to item 4.  
If you do any of these things in your shouldLoad implementation, expect  
unpredictable behavior, possibly including crashes, content not showing  
up, content showing up doubled, etc.  If you need to do any of the things  
above, do them off timeout or event.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aContentType</td>
<td>the type of content being tested. This will be one  
                         one of the TYPE_* constants.  
</td>
</tr>

<tr>
<td>aContentLocation</td>
<td>the location of the content being checked; must  
                         not be null  
</td>
</tr>

<tr>
<td>aRequestOrigin</td>
<td>OPTIONAL. the location of the resource that  
                         initiated this load request; can be null if  
                         inapplicable  
</td>
</tr>

<tr>
<td>aContext</td>
<td>OPTIONAL. the nsIDOMNode or nsIDOMWindow that  
                         initiated the request, or something that can QI  
                         to one of those; can be null if inapplicable.  
                         Note that for navigation events (new windows and  
                         link clicks), this is the NEW window.  
</td>
</tr>

<tr>
<td>aMimeTypeGuess</td>
<td>OPTIONAL. a guess for the requested content's  
                         MIME type, based on information available to  
                         the request initiator (e.g., an OBJECT's type  
                         attribute); does not reliably reflect the  
                         actual MIME type of the requested content  
</td>
</tr>

<tr>
<td>aExtra</td>
<td>an OPTIONAL argument, pass-through for non-Gecko  
                         callers to pass extra data to callees.  
</td>
</tr>

<tr>
<td>aRequestPrincipal</td>
<td>an OPTIONAL argument, defines the principal that  
                         caused the load. This is optional only for  
                         non-gecko code: all gecko code should set this  
                         argument.  For navigation events, this is  
                         the principal of the page that caused this load.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>ACCEPT or REJECT_*  
</td>
</tr>

</table>

### shouldProcess(aContentType, aContentLocation, aRequestOrigin, aContext, aMimeType, aExtra, aRequestPrincipal) ###
<pre>  
Should the resource be processed?  
ShouldProcess will be called once all the information passed to it has  
been determined about the resource, typically after part of the resource  
has been loaded.  
  
@param aContentType      the type of content being tested. This will be one  
                         one of the TYPE_* constants.  
  
@param aContentLocation  OPTIONAL; the location of the resource being  
                         requested: MAY be, e.g., a post-redirection URI  
                         for the resource.  
  
@param aRequestOrigin    OPTIONAL. the location of the resource that  
                         initiated this load request; can be null if  
                         inapplicable  
  
@param aContext          OPTIONAL. the nsIDOMNode or nsIDOMWindow that  
                         initiated the request, or something that can QI  
                         to one of those; can be null if inapplicable.  
  
@param aMimeType         the MIME type of the requested resource (e.g.,  
                         image/png), as reported by the networking library,  
                         if available (may be empty if inappropriate for  
                         the type, e.g., TYPE_REFRESH).  
  
@param aExtra            an OPTIONAL argument, pass-through for non-Gecko  
                         callers to pass extra data to callees.  
  
@return ACCEPT or REJECT_*  
  
@note shouldProcess can be called while the DOM and layout of the document  
involved is in an inconsistent state.  See the note on shouldLoad to see  
what this means for implementors of this method.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aContentType</td>
<td>the type of content being tested. This will be one  
                         one of the TYPE_* constants.  
</td>
</tr>

<tr>
<td>aContentLocation</td>
<td>OPTIONAL; the location of the resource being  
                         requested: MAY be, e.g., a post-redirection URI  
                         for the resource.  
</td>
</tr>

<tr>
<td>aRequestOrigin</td>
<td>OPTIONAL. the location of the resource that  
                         initiated this load request; can be null if  
                         inapplicable  
</td>
</tr>

<tr>
<td>aContext</td>
<td>OPTIONAL. the nsIDOMNode or nsIDOMWindow that  
                         initiated the request, or something that can QI  
                         to one of those; can be null if inapplicable.  
</td>
</tr>

<tr>
<td>aMimeType</td>
<td>the MIME type of the requested resource (e.g.,  
                         image/png), as reported by the networking library,  
                         if available (may be empty if inappropriate for  
                         the type, e.g., TYPE_REFRESH).  
</td>
</tr>

<tr>
<td>aExtra</td>
<td>an OPTIONAL argument, pass-through for non-Gecko  
                         callers to pass extra data to callees.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>ACCEPT or REJECT_*  
</td>
</tr>

</table>

## Constants ##

### TYPE_INVALID ###
<pre>  
Indicates a unset or bogus policy type.  
  
</pre>
### TYPE_OTHER ###
<pre>  
Gecko/Firefox developers: Do not use TYPE_OTHER under any circumstances.  
  
Extension developers: Whenever it is reasonable, use one of the existing  
content types. If none of the existing content types are right for  
something you are doing, file a bug in the Core/DOM component that  
includes a patch that adds your new content type to the end of the list of  
TYPE_* constants here. But, don't start using your new content type until  
your patch has been accepted, because it will be uncertain what exact  
value and name your new content type will have; in that interim period,  
use TYPE_OTHER. In your patch, document your new content type in the style  
of the existing ones. In the bug you file, provide a more detailed  
description of the new type of content you want Gecko to support, so that  
the existing implementations of nsIContentPolicy can be properly modified  
to deal with that new type of content.  
  
Implementations of nsIContentPolicy should treat this the same way they  
treat unknown types, because existing users of TYPE_OTHER may be converted  
to use new content types.  
  
</pre>
### TYPE_SCRIPT ###
<pre>  
Indicates an executable script (such as JavaScript).  
  
</pre>
### TYPE_IMAGE ###
<pre>  
Indicates an image (e.g., IMG elements).  
  
</pre>
### TYPE_STYLESHEET ###
<pre>  
Indicates a stylesheet (e.g., STYLE elements).  
  
</pre>
### TYPE_OBJECT ###
<pre>  
Indicates a generic object (plugin-handled content typically falls under  
this category).  
  
</pre>
### TYPE_DOCUMENT ###
<pre>  
Indicates a document at the top-level (i.e., in a browser).  
  
</pre>
### TYPE_SUBDOCUMENT ###
<pre>  
Indicates a document contained within another document (e.g., IFRAMEs,  
FRAMES, and OBJECTs).  
  
</pre>
### TYPE_REFRESH ###
<pre>  
Indicates a timed refresh.  
  
shouldLoad will never get this, because it does not represent content  
to be loaded (the actual load triggered by the refresh will go through  
shouldLoad as expected).  
  
shouldProcess will get this for, e.g., META Refresh elements and HTTP  
Refresh headers.  
  
</pre>
### TYPE_XBL ###
<pre>  
Indicates an XBL binding request, triggered either by -moz-binding CSS  
property.  
  
</pre>
### TYPE_PING ###
<pre>  
Indicates a ping triggered by a click on <A PING="..."> element.  
  
</pre>
### TYPE_XMLHTTPREQUEST ###
<pre>  
Indicates an XMLHttpRequest. Also used for document.load and for EventSource.  
  
</pre>
### TYPE_DATAREQUEST ###

### TYPE_OBJECT_SUBREQUEST ###
<pre>  
Indicates a request by a plugin.  
  
</pre>
### TYPE_DTD ###
<pre>  
Indicates a DTD loaded by an XML document.  
  
</pre>
### TYPE_FONT ###
<pre>  
Indicates a font loaded via @font-face rule.  
  
</pre>
### TYPE_MEDIA ###
<pre>  
Indicates a video or audio load.  
  
</pre>
### TYPE_WEBSOCKET ###
<pre>  
Indicates a WebSocket load.  
  
</pre>
### TYPE_CSP_REPORT ###
<pre>  
Indicates a Content Security Policy report.  
  
</pre>
### TYPE_XSLT ###
<pre>  
Indicates a style sheet transformation.  
  
</pre>
### TYPE_BEACON ###
<pre>  
Indicates a beacon post.  
  
</pre>
### TYPE_FETCH ###
<pre>  
Indicates a load initiated by the fetch() function from the Fetch  
specification.  
  
</pre>
### TYPE_IMAGESET ###
<pre>  
Indicates a <img srcset> or <picture> request.  
  
</pre>
### REJECT_REQUEST ###
<pre>  
Returned from shouldLoad or shouldProcess if the load or process request  
is rejected based on details of the request.  
  
</pre>
### REJECT_TYPE ###
<pre>  
Returned from shouldLoad or shouldProcess if the load/process is rejected  
based solely on its type (of the above flags).  
  
NOTE that it is not meant to stop future requests for this type--only the  
current request.  
  
</pre>
### REJECT_SERVER ###
<pre>  
Returned from shouldLoad or shouldProcess if the load/process is rejected  
based on the server it is hosted on or requested from (aContentLocation or  
aRequestOrigin), e.g., if you block an IMAGE because it is served from  
goatse.cx (even if you don't necessarily block other types from that  
server/domain).  
  
NOTE that it is not meant to stop future requests for this server--only the  
current request.  
  
</pre>
### REJECT_OTHER ###
<pre>  
Returned from shouldLoad or shouldProcess if the load/process is rejected  
based on some other criteria. Mozilla callers will handle this like  
REJECT_REQUEST; third-party implementors may, for example, use this to  
direct their own callers to consult the extra parameter for additional  
details.  
  
</pre>
### ACCEPT ###
<pre>  
Returned from shouldLoad or shouldProcess if the load or process request  
is not rejected.  
  
</pre>