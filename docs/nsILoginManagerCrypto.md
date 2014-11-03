---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/passwordmgr/nsILoginManagerCrypto.idl">Source file</a>
</div>

# nsILoginManagerCrypto #

## Methods ##

### encrypt(plainText) ###
  
encrypt  
  
@param plainText  
       The string to be encrypted.  
  
Encrypts the specified string, returning the ciphertext value.  
  
NOTE: The current implemention of this inferface simply uses NSS/PSM's  
"Secret Decoder Ring" service. It is not recommended for general  
purpose encryption/decryption.  
  
Can throw if the user cancels entry of their master password.  
  

#### Parameters ####

<table>

<tr>
<td>plainText</td>
<td>       The string to be encrypted.  
</td>
</tr>

</table>

### decrypt(cipherText) ###
  
decrypt  
  
@param cipherText  
       The string to be decrypted.  
  
Decrypts the specified string, returning the plaintext value.  
  
Can throw if the user cancels entry of their master password, or if the  
cipherText value can not be successfully decrypted (eg, if it was  
encrypted with some other key).  
  

#### Parameters ####

<table>

<tr>
<td>cipherText</td>
<td>       The string to be decrypted.  
</td>
</tr>

</table>

## Attributes ##

### uiBusy ###
  
uiBusy  
  
True when a master password prompt is being displayed.  
  

### isLoggedIn ###
  
isLoggedIn  
  
Current login state of the token used for encryption. If the user is  
not logged in, performing a crypto operation will result in a master  
password prompt.  
  

### defaultEncType ###
  
defaultEncType  
  
Default encryption type used by an implementation of this interface.  
  

## Constants ##

### ENCTYPE_BASE64 ###

### ENCTYPE_SDR ###
