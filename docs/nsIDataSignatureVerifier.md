---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/security/manager/ssl/public/nsIDataSignatureVerifier.idl">Source file</a>
</div>

# nsIDataSignatureVerifier #
  
An interface for verifying that a given string of data was signed by the  
private key matching the given public key.  
  

## Methods ##

### verifyData(aData, aSignature, aPublicKey) ###
  
Verifies that the data matches the data that was used to generate the  
signature.  
  
@param aData      The data to be tested.  
@param aSignature The signature of the data, base64 encoded.  
@param aPublicKey The public part of the key used for signing, DER encoded  
                  then base64 encoded.  
@returns true if the signature matches the data, false if not.  
  

#### Parameters ####

<table>

<tr>
<td>aData</td>
<td>The data to be tested.  
</td>
</tr>

<tr>
<td>aSignature</td>
<td>The signature of the data, base64 encoded.  
</td>
</tr>

<tr>
<td>aPublicKey</td>
<td>The public part of the key used for signing, DER encoded  
                  then base64 encoded.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>true if the signature matches the data, false if not.  
</td>
</tr>

</table>

### verifySignature(aSignature, aSignatureLen, plaintext, plaintextLen, errorCode) ###

## Constants ##

### VERIFY_OK ###

### VERIFY_ERROR_UNKNOWN_ISSUER ###

### VERIFY_ERROR_OTHER ###
