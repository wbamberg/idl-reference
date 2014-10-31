---
layout: default
---

# nsIWifiCertService #

## Methods ##

### start(listener) ###

### shutdown() ###

### importCert(id, certBlob, certPassword, certNickname) ###
  
Import a certificate file.  
  
@param id  
       Request ID.  
@param certBlob  
       A Blob object containing raw data of certificate to be imported.  
@param certPassword  
       Password of certificate.  
@param certNickname  
       User assigned nickname for imported certificate.  
  

#### Parameters ####

<table>

<tr>
<td>id</td>
<td>       Request ID.  
</td>
</tr>

<tr>
<td>id</td>
<td>       Request ID.  
</td>
</tr>

<tr>
<td>id</td>
<td>       Request ID.  
</td>
</tr>

<tr>
<td>id</td>
<td>       Request ID.  
</td>
</tr>

</table>

### deleteCert(id, certNickname) ###
  
Delete an imported certificate file  
  
@param id  
       Request ID.  
@param certNickname  
       Certificate nickname to delete.  
  

#### Parameters ####

<table>

<tr>
<td>id</td>
<td>       Request ID.  
</td>
</tr>

<tr>
<td>id</td>
<td>       Request ID.  
</td>
</tr>

</table>

## Constants ##

### WIFI_CERT_USAGE_FLAG_SERVER ###

### WIFI_CERT_USAGE_FLAG_USER ###
