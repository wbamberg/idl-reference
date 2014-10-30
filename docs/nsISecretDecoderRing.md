---
layout: default
---

# nsISecretDecoderRing #

## Methods ##

### encrypt(data, dataLen, result) ###
  
Encrypt a buffer - callable only from C++.  
  
@return The length of the data in the output buffer.  
  

### decrypt(data, dataLen, result) ###
  
Decrypt a buffer - callable only from C++.  
  
@return The length of the data in the output buffer.  
  

### encryptString(text) ###
  
Encrypt nul-terminated string to BASE64 output.  
  

### decryptString(crypt) ###
  
Decrypt BASE64 input to nul-terminated string output.  There is  
no check for embedded nul values in the decrypted output.  
  

### changePassword() ###
  
Prompt the user to change the password on the SDR key.  
  

### logout() ###
  
Logout of the security device that protects the SDR key.  
  

### logoutAndTeardown() ###
  
Logout of the security device that protects the SDR key and tear  
down authenticated objects.  
  
