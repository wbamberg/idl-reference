---
layout: default
---

# mozIDownloadPlatform #

## Methods ##

### downloadDone(aSource, aTarget, aContentType, aIsPrivate) ###
  
Perform platform specific operations when a download is done.  
  
  Windows:  
    Add the download to the recent documents list  
    Set the file to be indexed for searching  
  Mac:  
    Bounce the downloads dock icon  
  GTK:  
    Add the download to the recent documents list  
    Save the source uri in the downloaded file's metadata  
  Android:  
    Scan media  
  
@param aSource  
       Source URI of the download  
@param aTarget  
       Downloaded file  
@param aContentType  
       The source's content type  
@param aIsPrivate  
       True for private downloads  
@return none  
  

#### Parameters ####

<table>

<tr>
<td>aSource</td>
<td>       Source URI of the download  
</td>
</tr>

<tr>
<td>aSource</td>
<td>       Source URI of the download  
</td>
</tr>

<tr>
<td>aSource</td>
<td>       Source URI of the download  
</td>
</tr>

<tr>
<td>aSource</td>
<td>       Source URI of the download  
</td>
</tr>

</table>

### mapUrlToZone(aURL) ###
  
Proxy for IInternetSecurityManager::MapUrlToZone().  
  
  Windows only.  
  
@param aURL  
       URI of the download  
@return Security Zone corresponding to aURL.  
  

#### Parameters ####

<table>

<tr>
<td>aURL</td>
<td>       URI of the download  
</td>
</tr>

</table>

## Constants ##

### ZONE_MY_COMPUTER ###
  
Security Zone constants. Used by mapUrlToZone().  
  

### ZONE_INTRANET ###

### ZONE_TRUSTED ###

### ZONE_INTERNET ###

### ZONE_RESTRICTED ###
