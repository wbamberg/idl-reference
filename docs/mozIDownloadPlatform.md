---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/jsdownloads/public/mozIDownloadPlatform.idl">Source file</a>
</div>

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
  
  

#### Parameters ####

<table>

<tr>
<td>aSource</td>
<td>       Source URI of the download  
</td>
</tr>

<tr>
<td>aTarget</td>
<td>       Downloaded file  
</td>
</tr>

<tr>
<td>aContentType</td>
<td>       The source's content type  
</td>
</tr>

<tr>
<td>aIsPrivate</td>
<td>       True for private downloads  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>none  
</td>
</tr>

</table>

### mapUrlToZone(aURL) ###
  
Proxy for IInternetSecurityManager::MapUrlToZone().  
  
  Windows only.  
  
  

#### Parameters ####

<table>

<tr>
<td>aURL</td>
<td>       URI of the download  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>Security Zone corresponding to aURL.  
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
