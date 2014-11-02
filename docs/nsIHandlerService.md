---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/uriloader/exthandler/nsIHandlerService.idl">Source file</a>
</div>
# nsIHandlerService #

## Methods ##

### enumerate() ###
  
Retrieve a list of all handlers in the datastore.  This list is not  
guaranteed to be in any particular order, and callers should not assume  
it will remain in the same order in the future.  
  
@returns a list of all handlers in the datastore  
  

#### Returns ####

<table>

<tr>
<td>a list of all handlers in the datastore  
</td>
</tr>

</table>

### fillHandlerInfo(aHandlerInfo, aOverrideType) ###
  
Fill a handler info object with information from the datastore.  
  
Note: because of the way the external helper app service currently mixes  
OS and user handler info in the same handler info object, this method  
takes an existing handler info object (probably retrieved from the OS)  
and "fills it in" with information from the datastore, overriding any  
existing properties on the object with properties from the datastore.  
  
Ultimately, however, we're going to separate OS and user handler info  
into separate objects, at which point this method should be renamed to  
something like "get" or "retrieve", take a class and type (or perhaps  
a type whose class can be determined by querying the type, for example  
an nsIContentType which is also an nsIMIMEType or an nsIProtocolScheme),  
and return a handler info object representing only the user info.  
  
Note: if you specify an override type, then the service will fill in  
the handler info object with information about that type instead of  
the type specified by the object's nsIHandlerInfo::type attribute.  
  
This is useful when you are trying to retrieve information about a MIME  
type that doesn't exist in the datastore, but you have a file extension  
for that type, and nsIHandlerService::getTypeFromExtension returns another  
MIME type that does exist in the datastore and can handle that extension.  
  
For example, the user clicks on a link, and the content has a MIME type  
that isn't in the datastore, but the link has a file extension, and that  
extension is associated with another MIME type in the datastore (perhaps  
an unofficial MIME type preceded an official one, like with image/x-png  
and image/png).  
  
In that situation, you can call this method to fill in the handler info  
object with information about that other type by passing the other type  
as the aOverrideType parameter.  
  
@param aHandlerInfo   the handler info object  
@param aOverrideType  a type to use instead of aHandlerInfo::type  
  
Note: if there is no information in the datastore about this type,  
this method throws NS_ERROR_NOT_AVAILABLE. Callers are encouraged to  
check exists() before calling fillHandlerInfo(), to prevent spamming the  
console with XPCOM exception errors.  
  

#### Parameters ####

<table>

<tr>
<td>aHandlerInfo</td>
<td>the handler info object  
</td>
</tr>

<tr>
<td>aOverrideType</td>
<td>a type to use instead of aHandlerInfo::type  
</td>
</tr>

</table>

### store(aHandlerInfo) ###
  
Save the preferred action, preferred handler, possible handlers, and  
always ask properties of the given handler info object to the datastore.  
Updates an existing record or creates a new one if necessary.  
  
Note: if preferred action is undefined or invalid, then we assume  
the default value nsIHandlerInfo::useHelperApp.  
  
@param aHandlerInfo  the handler info object  
  

#### Parameters ####

<table>

<tr>
<td>aHandlerInfo</td>
<td>the handler info object  
</td>
</tr>

</table>

### exists(aHandlerInfo) ###
  
Whether or not a record for the given handler info object exists  
in the datastore. If the datastore is corrupt (or some other error  
is caught in the implementation), false will be returned.  
  
@param aHandlerInfo  a handler info object  
  
@returns whether or not a record exists  
  

#### Parameters ####

<table>

<tr>
<td>aHandlerInfo</td>
<td>a handler info object  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>whether or not a record exists  
</td>
</tr>

</table>

### remove(aHandlerInfo) ###
  
Remove the given handler info object from the datastore.  Deletes all  
records associated with the object, including the preferred handler, info,  
and type records plus the entry in the list of types, if they exist.  
Otherwise, it does nothing and does not return an error.  
  
@param aHandlerInfo  the handler info object  
  

#### Parameters ####

<table>

<tr>
<td>aHandlerInfo</td>
<td>the handler info object  
</td>
</tr>

</table>

### getTypeFromExtension(aFileExtension) ###
  
Get the MIME type mapped to the given file extension in the datastore.  
  
XXX If we ever support extension -> protocol scheme mappings, then this  
method should work for those as well.  
  
Note: in general, you should use nsIMIMEService::getTypeFromExtension  
to get a MIME type from a file extension, as that method checks a variety  
of other sources besides just the datastore.  Use this only when you want  
to specifically get only the mapping available in the datastore.  
  
@param aFileExtension  the file extension  
  
@returns the MIME type, if any; otherwise returns an empty string ("").  
  

#### Parameters ####

<table>

<tr>
<td>aFileExtension</td>
<td>the file extension  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>the MIME type, if any; otherwise returns an empty string ("").  
</td>
</tr>

</table>
