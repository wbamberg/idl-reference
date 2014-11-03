---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/mime/nsIMIMEInfo.idl">Source file</a>
</div>

# nsIMIMEInfo #
  
nsIMIMEInfo extends nsIHandlerInfo with a bunch of information specific to  
MIME content-types. There is a one-to-many relationship between MIME types  
and file extensions. This means that a MIMEInfo object may have multiple  
file extensions associated with it.  However, the reverse is not true.  
  
MIMEInfo objects are generally retrieved from the MIME Service  
@see nsIMIMEService  
  

## Methods ##

### getFileExtensions() ###
  
Gives you an array of file types associated with this type.  
  
  

#### Returns ####

<table>

<tr>
<td>Array of extensions.  
</td>
</tr>

</table>

### setFileExtensions(aExtensions) ###
  
Set File Extensions. Input is a comma delimited list of extensions.  
  

### extensionExists(aExtension) ###
  
Returns whether or not the given extension is  
associated with this MIME info.  
  
  

#### Returns ####

<table>

<tr>
<td>TRUE if the association exists.   
</td>
</tr>

</table>

### appendExtension(aExtension) ###
  
Append a given extension to the set of extensions  
  

### equals(aMIMEInfo) ###
  
Returns whether or not these two nsIMIMEInfos are logically  
equivalent.  
  
  

#### Returns ####

<table>

<tr>
<td>PR_TRUE if the two are considered equal  
</td>
</tr>

</table>

### launchWithFile(aFile) ###
  
Launches the application with the specified file, in a way that  
depends on the value of preferredAction. preferredAction must be  
useHelperApp or useSystemDefault.  
  
  
@throw NS_ERROR_INVALID_ARG if action is not valid for this function.  
Other exceptions may be thrown.  
  

#### Parameters ####

<table>

<tr>
<td>aFile</td>
<td>The file to launch this application with.  
</td>
</tr>

</table>

## Attributes ##

### primaryExtension ###
  
Returns the first extension association in  
the internal set of extensions.  
  
@return The first extension.  
  

### MIMEType ###
  
The MIME type of this MIMEInfo.  
  
@return String representing the MIME type.  
  
@deprecated  use nsIHandlerInfo::type instead.  
  

### possibleLocalHandlers ###
   
Returns a list of nsILocalHandlerApp objects containing  
handlers associated with this mimeinfo. Implemented per   
platform using information in this object to generate the  
best list. Typically used for an "open with" style user   
option.  
  
@return nsIArray of nsILocalHandlerApp  
  
