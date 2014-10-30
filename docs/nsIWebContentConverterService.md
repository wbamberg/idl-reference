---
layout: default
---

# nsIWebContentConverterService #

## Methods ##

### setAutoHandler(contentType, handler) ###
  
Specifies the handler to be used to automatically handle all links of a  
certain content type from now on.   
@param   contentType  
         The content type to automatically load with the specified handler  
@param   handler  
         A web service handler. If this is null, no automatic action is  
         performed and the user must choose.  
@throws  NS_ERROR_NOT_AVAILABLE if the service refered to by |handler| is   
         not already registered.  
  

### getAutoHandler(contentType) ###
  
Gets the auto handler specified for a particular content type  
@param   contentType  
         The content type to look up an auto handler for.  
@returns The web service handler that will automatically handle all   
         documents of the specified type. null if there is no automatic  
         handler. (Handlers may be registered, just none of them specified  
         as "automatic").  
  

### getWebContentHandlerByURI(contentType, uri) ###
  
Gets a web handler for the specified service URI  
@param   contentType  
         The content type of the service being located  
@param   uri  
         The service URI of the handler to locate.  
@returns A web service handler that uses the specified uri.  
  

### loadPreferredHandler(request) ###
  
Loads the preferred handler when content of a registered type is about  
to be loaded.  
@param   request  
         The nsIRequest for the load of the content  
  

### removeProtocolHandler(protocol, uri) ###
  
Removes a registered protocol handler  
@param   protocol  
         The protocol scheme to remove a service handler for  
@param   uri  
         The uri of the service handler to remove  
  

### removeContentHandler(contentType, uri) ###
  
Removes a registered content handler  
@param   contentType  
         The content type to remove a service handler for  
@param   uri  
         The uri of the service handler to remove  
  

### getContentHandlers(contentType, count, handlers) ###
  
Gets the list of content handlers for a particular type.  
@param   contentType  
         The content type to get handlers for  
@returns An array of nsIWebContentHandlerInfo objects  
  

### resetHandlersForType(contentType) ###
  
Resets the list of available content handlers to the default set from  
the distribution.  
@param   contentType  
         The content type to reset handlers for  
  
