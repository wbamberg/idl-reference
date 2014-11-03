---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/security/manager/ssl/public/nsIX509Cert.idl">Source file</a>
</div>

# nsIX509Cert #
<pre>  
This represents a X.509 certificate.  
  
</pre>
## Methods ##

### getEmailAddresses(length, addresses) ###
<pre>  
 Obtain a list of all email addresses  
 contained in the certificate.  
  
 @param length The number of strings in the returned array.  
 @return An array of email addresses.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>length</td>
<td>The number of strings in the returned array.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>An array of email addresses.  
</td>
</tr>

</table>

### containsEmailAddress(aEmailAddress) ###
<pre>  
 Check whether a given address is contained in the certificate.  
 The comparison will convert the email address to lowercase.  
 The behaviour for non ASCII characters is undefined.  
  
 @param aEmailAddress The address to search for.  
  
 @return True if the address is contained in the certificate.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aEmailAddress</td>
<td>The address to search for.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>True if the address is contained in the certificate.  
</td>
</tr>

</table>

### getChain() ###
<pre>  
 Obtain a list of certificates that contains this certificate  
 and the issuing certificates of all involved issuers,  
 up to the root issuer.  
  
 @return The chain of certifficates including the issuers.  
  
</pre>
#### Returns ####

<table>

<tr>
<td>The chain of certifficates including the issuers.  
</td>
</tr>

</table>

### getUsagesArray(localOnly, verified, count, usages) ###
<pre>  
 Obtain an array of human readable strings describing  
 the certificate's certified usages.  
  
 @param localOnly Do not hit the network, even if revocation information  
                  downloading is currently activated.  
 @param verified The certificate verification result, see constants.  
 @param count The number of human readable usages returned.  
 @param usages The array of human readable usages.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>localOnly</td>
<td>Do not hit the network, even if revocation information  
                  downloading is currently activated.  
</td>
</tr>

<tr>
<td>verified</td>
<td>The certificate verification result, see constants.  
</td>
</tr>

<tr>
<td>count</td>
<td>The number of human readable usages returned.  
</td>
</tr>

<tr>
<td>usages</td>
<td>The array of human readable usages.  
</td>
</tr>

</table>

### requestUsagesArrayAsync(cvl) ###
<pre>  
 Async version of nsIX509Cert::getUsagesArray()  
  
 Will not block, will request results asynchronously,  
 availability of results will be notified on the main thread.  
  
</pre>
### getUsagesString(localOnly, verified, usages) ###
<pre>  
 Obtain a single comma separated human readable string describing  
 the certificate's certified usages.  
  
 @param localOnly Do not hit the network, even if revocation information  
                  downloading is currently activated.  
 @param verified The certificate verification result, see constants.  
 @param purposes The string listing the usages.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>localOnly</td>
<td>Do not hit the network, even if revocation information  
                  downloading is currently activated.  
</td>
</tr>

<tr>
<td>verified</td>
<td>The certificate verification result, see constants.  
</td>
</tr>

<tr>
<td>purposes</td>
<td>The string listing the usages.  
</td>
</tr>

</table>

### getRawDER(length, data) ###
<pre>  
 Obtain a raw binary encoding of this certificate  
 in DER format.  
  
 @param length The number of bytes in the binary encoding.  
 @param data The bytes representing the DER encoded certificate.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>length</td>
<td>The number of bytes in the binary encoding.  
</td>
</tr>

<tr>
<td>data</td>
<td>The bytes representing the DER encoded certificate.  
</td>
</tr>

</table>

### equals(other) ###
<pre>  
 Test whether two certificate instances represent the  
 same certificate.  
  
 @return Whether the certificates are equal  
  
</pre>
#### Returns ####

<table>

<tr>
<td>Whether the certificates are equal  
</td>
</tr>

</table>

### exportAsCMS(chainMode, length, data) ###
<pre>  
 Obtain the certificate wrapped in a PKCS#7 SignedData structure,  
 with or without the certificate chain  
  
 @param chainMode Whether to include the chain (with or without the root),  
see CMS_CHAIN_MODE constants.  
 @param length The number of bytes of the PKCS#7 data.  
 @param data The bytes representing the PKCS#7 wrapped certificate.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>chainMode</td>
<td>Whether to include the chain (with or without the root),  
see CMS_CHAIN_MODE constants.  
</td>
</tr>

<tr>
<td>length</td>
<td>The number of bytes of the PKCS#7 data.  
</td>
</tr>

<tr>
<td>data</td>
<td>The bytes representing the PKCS#7 wrapped certificate.  
</td>
</tr>

</table>

### getCert() ###
<pre>  
Retrieves the NSS certificate object wrapped by this interface  
  
</pre>
### getAllTokenNames(length, tokenNames) ###
<pre>  
Human readable names identifying all hardware or  
software tokens the certificate is stored on.  
  
@param length On success, the number of entries in the returned array.  
@return On success, an array containing the names of all tokens  
        the certificate is stored on (may be empty).  
        On failure the function throws/returns an error.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>length</td>
<td>On success, the number of entries in the returned array.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>On success, an array containing the names of all tokens  
        the certificate is stored on (may be empty).  
        On failure the function throws/returns an error.  
</td>
</tr>

</table>

### markForPermDeletion() ###
<pre>  
Either delete the certificate from all cert databases,  
or mark it as untrusted.  
  
</pre>
## Attributes ##

### nickname ###
<pre>  
 A nickname for the certificate.  
  
</pre>
### emailAddress ###
<pre>  
 The primary email address of the certificate, if present.  
  
</pre>
### subjectName ###
<pre>  
 The subject owning the certificate.  
  
</pre>
### commonName ###
<pre>  
 The subject's common name.  
  
</pre>
### organization ###
<pre>  
 The subject's organization.  
  
</pre>
### organizationalUnit ###
<pre>  
 The subject's organizational unit.  
  
</pre>
### sha256Fingerprint ###
<pre>  
 The fingerprint of the certificate's DER encoding,  
 calculated using the SHA-256 algorithm.  
  
</pre>
### sha1Fingerprint ###
<pre>  
 The fingerprint of the certificate's DER encoding,  
 calculated using the SHA1 algorithm.  
  
</pre>
### tokenName ###
<pre>  
 A human readable name identifying the hardware or  
 software token the certificate is stored on.  
  
</pre>
### issuerName ###
<pre>  
 The subject identifying the issuer certificate.  
  
</pre>
### serialNumber ###
<pre>  
 The serial number the issuer assigned to this certificate.  
  
</pre>
### issuerCommonName ###
<pre>  
 The issuer subject's common name.  
  
</pre>
### issuerOrganization ###
<pre>  
 The issuer subject's organization.  
  
</pre>
### issuerOrganizationUnit ###
<pre>  
 The issuer subject's organizational unit.  
  
</pre>
### issuer ###
<pre>  
 The certificate used by the issuer to sign this certificate.  
  
</pre>
### validity ###
<pre>  
 This certificate's validity period.  
  
</pre>
### dbKey ###
<pre>  
 A unique identifier of this certificate within the local storage.  
  
</pre>
### windowTitle ###
<pre>  
 A human readable identifier to label this certificate.  
  
</pre>
### certType ###
<pre>  
Type of this certificate  
  
</pre>
### isSelfSigned ###
<pre>  
 True if the certificate is self-signed. CA issued  
 certificates are always self-signed.  
  
</pre>
### ASN1Structure ###
<pre>  
 This is the attribute which describes the ASN1 layout  
 of the certificate.  This can be used when doing a  
 "pretty print" of the certificate's ASN1 structure.  
  
</pre>
### sha256SubjectPublicKeyInfoDigest ###
<pre>  
The base64 encoding of the DER encoded public key info using the specified  
digest.  
  
</pre>
## Constants ##

### UNKNOWN_CERT ###
<pre>  
 Constants to classify the type of a certificate.  
  
</pre>
### CA_CERT ###

### USER_CERT ###

### EMAIL_CERT ###

### SERVER_CERT ###

### ANY_CERT ###

### VERIFIED_OK ###
<pre>  
 Constants for certificate verification results.  
  
</pre>
### NOT_VERIFIED_UNKNOWN ###

### CERT_REVOKED ###

### CERT_EXPIRED ###

### CERT_NOT_TRUSTED ###

### ISSUER_NOT_TRUSTED ###

### ISSUER_UNKNOWN ###

### INVALID_CA ###

### USAGE_NOT_ALLOWED ###

### SIGNATURE_ALGORITHM_DISABLED ###

### CERT_USAGE_SSLClient ###
<pre>  
 Constants that describe the certified usages of a certificate.  
  
 Deprecated and unused  
  
</pre>
### CERT_USAGE_SSLServer ###

### CERT_USAGE_SSLServerWithStepUp ###

### CERT_USAGE_SSLCA ###

### CERT_USAGE_EmailSigner ###

### CERT_USAGE_EmailRecipient ###

### CERT_USAGE_ObjectSigner ###

### CERT_USAGE_UserCertImport ###

### CERT_USAGE_VerifyCA ###

### CERT_USAGE_ProtectedObjectSigner ###

### CERT_USAGE_StatusResponder ###

### CERT_USAGE_AnyCA ###

### CMS_CHAIN_MODE_CertOnly ###
<pre>  
 Constants for specifying the chain mode when exporting a certificate  
  
</pre>
### CMS_CHAIN_MODE_CertChain ###

### CMS_CHAIN_MODE_CertChainWithRoot ###
