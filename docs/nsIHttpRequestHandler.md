---
layout: default
---

# nsIHttpRequestHandler #
  
A representation of a handler for HTTP requests.  The handler is used by  
calling its .handle method with data for an incoming request; it is the  
handler's job to use that data as it sees fit to make the desired response.  
  
@note  
  This interface uses the [function] attribute, so you can pass a  
  script-defined function with the functionality of handle() to any  
  method which has a nsIHttpRequestHandler parameter, instead of wrapping  
  it in an otherwise empty object.  
  

## Methods ##

### handle ###
  
Processes an HTTP request and initializes the passed-in response to reflect  
the correct HTTP response.  
  
If this method throws an exception, externally observable behavior depends  
upon whether is being processed asynchronously.  If such is the case, the  
output is some prefix (perhaps all, perhaps none, perhaps only some) of the  
data which would have been sent if, instead, the response had been finished  
at that point.  If no data has been written, the response has not had  
seizePower() called on it, and it is not being asynchronously created, an  
error handler will be invoked (usually 500 unless otherwise specified).  
  
Some uses of nsIHttpRequestHandler may require this method to never throw  
an exception; in the general case, however, this method may throw an  
exception (causing an HTTP 500 response to occur, if the above conditions  
are met).  
  
@param request  
  data representing an HTTP request  
@param response  
  an initially-empty response which must be modified to reflect the data  
  which should be sent as the response to the request described by metadata  
  
