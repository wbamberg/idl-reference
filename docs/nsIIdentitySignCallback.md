---
layout: default
---

# nsIIdentitySignCallback #
  
This interface provides a JavaScript callback object used to collect the  
AUTF8String signature  
  

## Methods ##

### signFinished(rv, base64urlSignature) ###
 On success, base64urlSignature is the base-64-URL-encoded signature  
  
For RS256 signatures, XXX bug 769858  
  
For DSA128 signatures, the signature is the r value concatenated with the  
s value, each component padded with leading zeroes as necessary.  
  
