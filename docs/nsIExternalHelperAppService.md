---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/uriloader/exthandler/nsIExternalHelperAppService.idl">Source file</a>
</div>

# nsIExternalHelperAppService #
<code>  
The external helper app service is used for finding and launching  
platform specific external applications for a given mime content type.  
  
</code>
## Methods ##

### doContent(aMimeContentType, aRequest, aContentContext, aForceSave, aWindowContext) ###
<code>  
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
  
</code>
#### Parameters ####

<table>

<tr>
<td>aMimeContentType</td>
<td>The content type of the incoming data  
</td>
</tr>

<tr>
<td>aRequest</td>
<td>The request corresponding to the incoming data  
</td>
</tr>

<tr>
<td>aContentContext</td>
<td>Used in processing content document refresh  
 headers after target content is downloaded. Note in e10s land  
 this is likely a CPOW that points to a window in the child process.  
</td>
</tr>

<tr>
<td>aForceSave</td>
<td>True to always save this content to disk, regardless of  
 nsIMIMEInfo and other such influences.  
</td>
</tr>

<tr>
<td>aWindowContext</td>
<td>Used in parenting helper app dialogs, usually  
 points to the parent browser window. This parameter may be null,  
 in which case dialogs will be parented to aContentContext.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>A nsIStreamListener which the caller should pump the data into.  
</td>
</tr>

</table>

### applyDecodingForExtension(aExtension, aEncodingType) ###
<code>  
Returns true if data from a URL with this extension combination  
is to be decoded from aEncodingType prior to saving or passing  
off to helper apps, false otherwise.  
  
</code>