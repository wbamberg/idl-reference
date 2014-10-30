---
layout: default
---

# nsIContentHandler #

## Methods ##

### handleContent(aContentType, aWindowContext, aRequest) ###
  
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
  
