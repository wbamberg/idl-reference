---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/security/manager/ssl/public/nsIX509CertValidity.idl">Source file</a>
</div>

# nsIX509CertValidity #
<pre>  
Information on the validity period of a X.509 certificate.  
  
</pre>
## Attributes ##

### notBefore ###
<pre>  
 The earliest point in time where  
 a certificate is valid.  
  
</pre>
### notBeforeLocalTime ###
<pre>  
 "notBefore" attribute formatted as a time string  
 according to the environment locale,  
 according to the environment time zone.  
  
</pre>
### notBeforeLocalDay ###
<pre>  
 The day portion of "notBefore"   
 formatted as a time string  
 according to the environment locale,  
 according to the environment time zone.  
  
</pre>
### notBeforeGMT ###
<pre>  
 "notBefore" attribute formatted as a string  
 according to the environment locale,  
 displayed as GMT / UTC.  
  
</pre>
### notAfter ###
<pre>  
 The latest point in time where  
 a certificate is valid.  
  
</pre>
### notAfterLocalTime ###
<pre>  
 "notAfter" attribute formatted as a time string  
 according to the environment locale,  
 according to the environment time zone.  
  
</pre>
### notAfterLocalDay ###
<pre>  
 The day portion of "notAfter"   
 formatted as a time string  
 according to the environment locale,  
 according to the environment time zone.  
  
</pre>
### notAfterGMT ###
<pre>  
 "notAfter" attribute formatted as a time string  
 according to the environment locale,  
 displayed as GMT / UTC.  
  
</pre>