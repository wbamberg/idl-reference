---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/security/manager/ssl/public/nsIX509CertValidity.idl">Source file</a>
</div>
# nsIX509CertValidity #
  
Information on the validity period of a X.509 certificate.  
  

## Attributes ##

### notBefore ###
  
 The earliest point in time where  
 a certificate is valid.  
  

### notBeforeLocalTime ###
  
 "notBefore" attribute formatted as a time string  
 according to the environment locale,  
 according to the environment time zone.  
  

### notBeforeLocalDay ###
  
 The day portion of "notBefore"   
 formatted as a time string  
 according to the environment locale,  
 according to the environment time zone.  
  

### notBeforeGMT ###
  
 "notBefore" attribute formatted as a string  
 according to the environment locale,  
 displayed as GMT / UTC.  
  

### notAfter ###
  
 The latest point in time where  
 a certificate is valid.  
  

### notAfterLocalTime ###
  
 "notAfter" attribute formatted as a time string  
 according to the environment locale,  
 according to the environment time zone.  
  

### notAfterLocalDay ###
  
 The day portion of "notAfter"   
 formatted as a time string  
 according to the environment locale,  
 according to the environment time zone.  
  

### notAfterGMT ###
  
 "notAfter" attribute formatted as a time string  
 according to the environment locale,  
 displayed as GMT / UTC.  
  
