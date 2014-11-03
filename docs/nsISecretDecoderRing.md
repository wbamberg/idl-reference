---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsISecretDecoderRing.idl">Source file</a>
</div>

# nsISecretDecoderRing #

## Methods ##

### encrypt(data, dataLen, result) ###
<pre>  
Encrypt a buffer - callable only from C++.  
  
@return The length of the data in the output buffer.  
  
</pre>
#### Returns ####

<table>

<tr>
<td>The length of the data in the output buffer.  
</td>
</tr>

</table>

### decrypt(data, dataLen, result) ###
<pre>  
Decrypt a buffer - callable only from C++.  
  
@return The length of the data in the output buffer.  
  
</pre>
#### Returns ####

<table>

<tr>
<td>The length of the data in the output buffer.  
</td>
</tr>

</table>

### encryptString(text) ###
<pre>  
Encrypt nul-terminated string to BASE64 output.  
  
</pre>
### decryptString(crypt) ###
<pre>  
Decrypt BASE64 input to nul-terminated string output.  There is  
no check for embedded nul values in the decrypted output.  
  
</pre>
### changePassword() ###
<pre>  
Prompt the user to change the password on the SDR key.  
  
</pre>
### logout() ###
<pre>  
Logout of the security device that protects the SDR key.  
  
</pre>
### logoutAndTeardown() ###
<pre>  
Logout of the security device that protects the SDR key and tear  
down authenticated objects.  
  
</pre>