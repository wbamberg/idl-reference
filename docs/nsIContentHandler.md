---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/uriloader/base/nsIContentHandler.idl">Source file</a>
</div>

# nsIContentHandler #

## Methods ##

### handleContent(aContentType, aWindowContext, aRequest) ###
<pre>  
Tells the content handler to take over handling the content. If this  
function succeeds, the URI Loader will leave this request alone, ignoring  
progress notifications. Failure of this method will cause the request to be  
cancelled, unless the error code is NS_ERROR_WONT_HANDLE_CONTENT (see  
below).  
  
@param aWindowContext  
       Window context, used to get things like the current nsIDOMWindow  
       for this request. May be null.  
@param aContentType  
       The content type of aRequest  
@param aRequest  
       A request whose content type is already known.  
  
@throw NS_ERROR_WONT_HANDLE_CONTENT Indicates that this handler does not  
       want to handle this content. A different way for handling this  
       content should be tried.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aWindowContext</td>
<td>       Window context, used to get things like the current nsIDOMWindow  
       for this request. May be null.  
</td>
</tr>

<tr>
<td>aContentType</td>
<td>       The content type of aRequest  
</td>
</tr>

<tr>
<td>aRequest</td>
<td>       A request whose content type is already known.  
</td>
</tr>

</table>
