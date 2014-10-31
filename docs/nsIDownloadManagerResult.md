---
layout: default
---

# nsIDownloadManagerResult #

## Methods ##

### handleResult(aStatus, aDownload) ###
  
Process an asynchronous result from getDownloadByGUID.  
  
@param aStatus The result code of the operation:  
       * NS_OK: an item was found. No other success values are returned.  
       * NS_ERROR_NOT_AVAILABLE: no such item was found.  
       * Other error values are possible, but less well-defined.  
  

#### Parameters ####

<table>

<tr>
<td>aStatus</td>
<td>The result code of the operation:  
       * NS_OK: an item was found. No other success values are returned.  
       * NS_ERROR_NOT_AVAILABLE: no such item was found.  
       * Other error values are possible, but less well-defined.  
</td>
</tr>

</table>
