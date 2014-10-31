---
layout: default
---

# nsIExternalURLHandlerService #
  
The external URL handler service is used for finding  
platform-specific applications for handling particular URLs.  
  

## Methods ##

### getURLHandlerInfoFromOS(aURL, aFound) ###
  
Given a URL, looks up the handler info from the OS. This should be  
overridden by each OS's implementation.  
  
@param aURL The URL we are looking for.  
@param aFound  Was an OS default handler for this URL found?  
@return  An nsIHanderInfo for the protocol.  
  

#### Parameters ####

<table>

<tr>
<td>aURL</td>
<td>The URL we are looking for.  
</td>
</tr>

<tr>
<td>aURL</td>
<td>The URL we are looking for.  
</td>
</tr>

</table>
