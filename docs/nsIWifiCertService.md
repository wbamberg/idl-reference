---
layout: default
---

# nsIWifiCertService #

## Methods ##

### start ###

### shutdown ###

### importCert ###
  
Import a certificate file.  
  
@param id  
       Request ID.  
@param certBlob  
       A Blob object containing raw data of certificate to be imported.  
@param certPassword  
       Password of certificate.  
@param certNickname  
       User assigned nickname for imported certificate.  
  

### deleteCert ###
  
Delete an imported certificate file  
  
@param id  
       Request ID.  
@param certNickname  
       Certificate nickname to delete.  
  

## Constants ##

### WIFI_CERT_USAGE_FLAG_SERVER ###

### WIFI_CERT_USAGE_FLAG_USER ###
