---
layout: default
---

# nsIFaviconDataCallback #

## Methods ##

### onComplete(aFaviconURI, aDataLen, aData, aMimeType) ###
  
Called when the required favicon's information is available.  
  
It's up to the invoking method to state if the callback is always invoked,  
or called on success only.  Check the method documentation to ensure that.  
  
The caller will receive the most information we can gather on the icon,  
but it's not guaranteed that all of them will be set.  For some method  
we could not know the favicon's data (it could just be too expensive to  
get it, or the method does not require we actually have any data).  
It's up to the caller to check aDataLen > 0 before using any data-related  
information like mime-type or data itself.  
  
@param aFaviconURI  
       Receives the "favicon URI" (not the "favicon link URI") associated  
       to the requested page.  This can be null if there is no associated  
       favicon URI, or the callback is notifying a failure.  
@param aDataLen  
       Size of the icon data in bytes.  Notice that a value of 0 does not  
       necessarily mean that we don't have an icon.  
@param aData  
       Icon data, or an empty array if aDataLen is 0.  
@param aMimeType  
       Mime type of the icon, or an empty string if aDataLen is 0.  
  
@note If you want to open a network channel to access the favicon, it's  
      recommended that you call the getFaviconLinkForIcon method to convert  
      the "favicon URI" into a "favicon link URI".  
  

#### Parameters ####

<table>

<tr>
<td>aFaviconURI</td>
<td>       Receives the "favicon URI" (not the "favicon link URI") associated  
       to the requested page.  This can be null if there is no associated  
       favicon URI, or the callback is notifying a failure.  
</td>
</tr>

<tr>
<td>aFaviconURI</td>
<td>       Receives the "favicon URI" (not the "favicon link URI") associated  
       to the requested page.  This can be null if there is no associated  
       favicon URI, or the callback is notifying a failure.  
</td>
</tr>

<tr>
<td>aFaviconURI</td>
<td>       Receives the "favicon URI" (not the "favicon link URI") associated  
       to the requested page.  This can be null if there is no associated  
       favicon URI, or the callback is notifying a failure.  
</td>
</tr>

<tr>
<td>aFaviconURI</td>
<td>       Receives the "favicon URI" (not the "favicon link URI") associated  
       to the requested page.  This can be null if there is no associated  
       favicon URI, or the callback is notifying a failure.  
</td>
</tr>

</table>
