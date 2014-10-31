---
layout: default
---

# nsIExternalHelperAppService #
  
The external helper app service is used for finding and launching  
platform specific external applications for a given mime content type.  
  

## Methods ##

### doContent(aMimeContentType, aRequest, aContentContext, aForceSave, aWindowContext) ###
  
Binds an external helper application to a stream listener. The caller  
should pump data into the returned stream listener. When the OnStopRequest  
is issued, the stream listener implementation will launch the helper app  
with this data.  
@param aMimeContentType The content type of the incoming data  
@param aRequest The request corresponding to the incoming data  
@param aContentContext Used in processing content document refresh  
 headers after target content is downloaded. Note in e10s land  
 this is likely a CPOW that points to a window in the child process.  
@param aForceSave True to always save this content to disk, regardless of  
 nsIMIMEInfo and other such influences.  
@param aWindowContext Used in parenting helper app dialogs, usually  
 points to the parent browser window. This parameter may be null,  
 in which case dialogs will be parented to aContentContext.  
@return A nsIStreamListener which the caller should pump the data into.  
  

#### Parameters ####

<table>

<tr>
<td>aMimeContentType</td>
<td>The content type of the incoming data  
</td>
</tr>

<tr>
<td>aMimeContentType</td>
<td>The content type of the incoming data  
</td>
</tr>

<tr>
<td>aMimeContentType</td>
<td>The content type of the incoming data  
</td>
</tr>

<tr>
<td>aMimeContentType</td>
<td>The content type of the incoming data  
</td>
</tr>

<tr>
<td>aMimeContentType</td>
<td>The content type of the incoming data  
</td>
</tr>

</table>

### applyDecodingForExtension(aExtension, aEncodingType) ###
  
Returns true if data from a URL with this extension combination  
is to be decoded from aEncodingType prior to saving or passing  
off to helper apps, false otherwise.  
  
