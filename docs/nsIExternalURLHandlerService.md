---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/uriloader/exthandler/nsIExternalURLHandlerService.idl">Source file</a>
</div>

# nsIExternalURLHandlerService #
<pre>  
The external URL handler service is used for finding  
platform-specific applications for handling particular URLs.  
  
</pre>
## Methods ##

### getURLHandlerInfoFromOS(aURL, aFound) ###
<pre>  
Given a URL, looks up the handler info from the OS. This should be  
overridden by each OS's implementation.  
  
@param aURL The URL we are looking for.  
@param aFound  Was an OS default handler for this URL found?  
@return  An nsIHanderInfo for the protocol.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aURL</td>
<td>The URL we are looking for.  
</td>
</tr>

<tr>
<td>aFound</td>
<td>Was an OS default handler for this URL found?  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>An nsIHanderInfo for the protocol.  
</td>
</tr>

</table>
