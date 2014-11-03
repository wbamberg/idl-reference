---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/wifi/nsIWifiCertService.idl">Source file</a>
</div>

# nsIWifiCertService #

## Methods ##

### start(listener) ###

### shutdown() ###

### importCert(id, certBlob, certPassword, certNickname) ###
<code>  
Import a certificate file.  
  
@param id  
       Request ID.  
@param certBlob  
       A Blob object containing raw data of certificate to be imported.  
@param certPassword  
       Password of certificate.  
@param certNickname  
       User assigned nickname for imported certificate.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>id</td>
<td>       Request ID.  
</td>
</tr>

<tr>
<td>certBlob</td>
<td>       A Blob object containing raw data of certificate to be imported.  
</td>
</tr>

<tr>
<td>certPassword</td>
<td>       Password of certificate.  
</td>
</tr>

<tr>
<td>certNickname</td>
<td>       User assigned nickname for imported certificate.  
</td>
</tr>

</table>

### deleteCert(id, certNickname) ###
<code>  
Delete an imported certificate file  
  
@param id  
       Request ID.  
@param certNickname  
       Certificate nickname to delete.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>id</td>
<td>       Request ID.  
</td>
</tr>

<tr>
<td>certNickname</td>
<td>       Certificate nickname to delete.  
</td>
</tr>

</table>

## Constants ##

### WIFI_CERT_USAGE_FLAG_SERVER ###

### WIFI_CERT_USAGE_FLAG_USER ###
