---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/browser/components/feeds/nsIWebContentConverterRegistrar.idl">Source file</a>
</div>

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
  

#### Parameters ####

<table>

<tr>
<td>contentType</td>
<td>         The content type to automatically load with the specified handler  
</td>
</tr>

<tr>
<td>handler</td>
<td>         A web service handler. If this is null, no automatic action is  
         performed and the user must choose.  
@throws  NS_ERROR_NOT_AVAILABLE if the service refered to by |handler| is   
         not already registered.  
</td>
</tr>

</table>

### getAutoHandler(contentType) ###
  
Gets the auto handler specified for a particular content type  
@param   contentType  
         The content type to look up an auto handler for.  
@returns The web service handler that will automatically handle all   
         documents of the specified type. null if there is no automatic  
         handler. (Handlers may be registered, just none of them specified  
         as "automatic").  
  

#### Parameters ####

<table>

<tr>
<td>contentType</td>
<td>         The content type to look up an auto handler for.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The web service handler that will automatically handle all   
         documents of the specified type. null if there is no automatic  
         handler. (Handlers may be registered, just none of them specified  
         as "automatic").  
</td>
</tr>

</table>

### getWebContentHandlerByURI(contentType, uri) ###
  
Gets a web handler for the specified service URI  
@param   contentType  
         The content type of the service being located  
@param   uri  
         The service URI of the handler to locate.  
@returns A web service handler that uses the specified uri.  
  

#### Parameters ####

<table>

<tr>
<td>contentType</td>
<td>         The content type of the service being located  
</td>
</tr>

<tr>
<td>uri</td>
<td>         The service URI of the handler to locate.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>A web service handler that uses the specified uri.  
</td>
</tr>

</table>

### loadPreferredHandler(request) ###
  
Loads the preferred handler when content of a registered type is about  
to be loaded.  
@param   request  
         The nsIRequest for the load of the content  
  

#### Parameters ####

<table>

<tr>
<td>request</td>
<td>         The nsIRequest for the load of the content  
</td>
</tr>

</table>

### removeProtocolHandler(protocol, uri) ###
  
Removes a registered protocol handler  
@param   protocol  
         The protocol scheme to remove a service handler for  
@param   uri  
         The uri of the service handler to remove  
  

#### Parameters ####

<table>

<tr>
<td>protocol</td>
<td>         The protocol scheme to remove a service handler for  
</td>
</tr>

<tr>
<td>uri</td>
<td>         The uri of the service handler to remove  
</td>
</tr>

</table>

### removeContentHandler(contentType, uri) ###
  
Removes a registered content handler  
@param   contentType  
         The content type to remove a service handler for  
@param   uri  
         The uri of the service handler to remove  
  

#### Parameters ####

<table>

<tr>
<td>contentType</td>
<td>         The content type to remove a service handler for  
</td>
</tr>

<tr>
<td>uri</td>
<td>         The uri of the service handler to remove  
</td>
</tr>

</table>

### getContentHandlers(contentType, count, handlers) ###
  
Gets the list of content handlers for a particular type.  
@param   contentType  
         The content type to get handlers for  
@returns An array of nsIWebContentHandlerInfo objects  
  

#### Parameters ####

<table>

<tr>
<td>contentType</td>
<td>         The content type to get handlers for  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>An array of nsIWebContentHandlerInfo objects  
</td>
</tr>

</table>

### resetHandlersForType(contentType) ###
  
Resets the list of available content handlers to the default set from  
the distribution.  
@param   contentType  
         The content type to reset handlers for  
  

#### Parameters ####

<table>

<tr>
<td>contentType</td>
<td>         The content type to reset handlers for  
</td>
</tr>

</table>
