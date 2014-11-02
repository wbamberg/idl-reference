---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/services/crypto/component/nsISyncJPAKE.idl">Source file</a>
</div>

# nsISyncJPAKE #

## Methods ##

### round1(aSignerID, aGX1, aGV1, aR1, aGX2, aGV2, aR2) ###
  
Perform first round of the JPAKE exchange.  
  
@param aSignerID  
       String identifying the signer.  
@param aGX1  
       Schnorr signature value g^x1, in hex representation.  
@param aGV1  
       Schnorr signature value g^v1 (v1 is a random value), in hex  
       representation.  
@param aR1  
       Schnorr signature value r1 = v1 - x1 * h, in hex representation.  
@param aGX2  
       Schnorr signature value g^x2, in hex representation.  
@param aGV2  
       Schnorr signature value g^v2 (v2 is a random value), in hex  
       representation.  
@param aR2  
       Schnorr signature value r2 = v2 - x2 * h, in hex representation.  
  

#### Parameters ####

<table>

<tr>
<td>aSignerID</td>
<td>       String identifying the signer.  
</td>
</tr>

<tr>
<td>aGX1</td>
<td>       Schnorr signature value g^x1, in hex representation.  
</td>
</tr>

<tr>
<td>aGV1</td>
<td>       Schnorr signature value g^v1 (v1 is a random value), in hex  
       representation.  
</td>
</tr>

<tr>
<td>aR1</td>
<td>       Schnorr signature value r1 = v1 - x1 * h, in hex representation.  
</td>
</tr>

<tr>
<td>aGX2</td>
<td>       Schnorr signature value g^x2, in hex representation.  
</td>
</tr>

<tr>
<td>aGV2</td>
<td>       Schnorr signature value g^v2 (v2 is a random value), in hex  
       representation.  
</td>
</tr>

<tr>
<td>aR2</td>
<td>       Schnorr signature value r2 = v2 - x2 * h, in hex representation.  
</td>
</tr>

</table>

### round2(aPeerID, aPIN, aGX3, aGV3, aR3, aGX4, aGV4, aR4, aA, aGVA, aRA) ###
  
Perform second round of the JPAKE exchange.  
  
@param aPeerID  
       String identifying the peer.  
@param aPIN  
       String containing the weak secret (PIN).  
@param aGX3  
       Schnorr signature value g^x3, in hex representation.  
@param aGV3  
       Schnorr signature value g^v3 (v3 is a random value), in hex  
       representation.  
@param aR3  
       Schnorr signature value r3 = v3 - x3 * h, in hex representation.  
@param aGX4  
       Schnorr signature value g^x4, in hex representation.  
@param aGV4  
       Schnorr signature value g^v4 (v4 is a random value), in hex  
       representation.  
@param aR4  
       Schnorr signature value r4 = v4 - x4 * h, in hex representation.  
@param aA  
       Schnorr signature value A, in hex representation.  
@param aGVA  
       Schnorr signature value g^va (va is a random value), in hex  
       representation.  
@param aRA  
       Schnorr signature value ra = va - xa * h, in hex representation.  
  

#### Parameters ####

<table>

<tr>
<td>aPeerID</td>
<td>       String identifying the peer.  
</td>
</tr>

<tr>
<td>aPIN</td>
<td>       String containing the weak secret (PIN).  
</td>
</tr>

<tr>
<td>aGX3</td>
<td>       Schnorr signature value g^x3, in hex representation.  
</td>
</tr>

<tr>
<td>aGV3</td>
<td>       Schnorr signature value g^v3 (v3 is a random value), in hex  
       representation.  
</td>
</tr>

<tr>
<td>aR3</td>
<td>       Schnorr signature value r3 = v3 - x3 * h, in hex representation.  
</td>
</tr>

<tr>
<td>aGX4</td>
<td>       Schnorr signature value g^x4, in hex representation.  
</td>
</tr>

<tr>
<td>aGV4</td>
<td>       Schnorr signature value g^v4 (v4 is a random value), in hex  
       representation.  
</td>
</tr>

<tr>
<td>aR4</td>
<td>       Schnorr signature value r4 = v4 - x4 * h, in hex representation.  
</td>
</tr>

<tr>
<td>aA</td>
<td>       Schnorr signature value A, in hex representation.  
</td>
</tr>

<tr>
<td>aGVA</td>
<td>       Schnorr signature value g^va (va is a random value), in hex  
       representation.  
</td>
</tr>

<tr>
<td>aRA</td>
<td>       Schnorr signature value ra = va - xa * h, in hex representation.  
</td>
</tr>

</table>

### final(aB, aGVB, aRB, aHkdfInfo, aAES256Key, aHMAC256Key) ###
  
Perform the final step of the JPAKE exchange. This will compute  
the key and expand the key to two keys, an AES256 encryption key  
and a 256 bit HMAC key. It returns a key confirmation value  
(SHA256d of the key) and the encryption and HMAC keys.  
  
@param aB  
       Schnorr signature value B, in hex representation.  
@param aGVB  
       Schnorr signature value g^vb (vb is a random value), in hex  
       representation.  
@param aRB  
       Schnorr signature value rb = vb - xb * h, in hex representation.  
@param aAES256Key  
       The AES 256 encryption key, in base64 representation.  
@param aHMAC256Key  
       The 256 bit HMAC key, in base64 representation.  
  

#### Parameters ####

<table>

<tr>
<td>aB</td>
<td>       Schnorr signature value B, in hex representation.  
</td>
</tr>

<tr>
<td>aGVB</td>
<td>       Schnorr signature value g^vb (vb is a random value), in hex  
       representation.  
</td>
</tr>

<tr>
<td>aRB</td>
<td>       Schnorr signature value rb = vb - xb * h, in hex representation.  
</td>
</tr>

<tr>
<td>aAES256Key</td>
<td>       The AES 256 encryption key, in base64 representation.  
</td>
</tr>

<tr>
<td>aHMAC256Key</td>
<td>       The 256 bit HMAC key, in base64 representation.  
</td>
</tr>

</table>
