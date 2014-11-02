---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/security/manager/ssl/public/nsIX509Cert.idl">Source file</a>
</div>

# nsIX509Cert #
  
This represents a X.509 certificate.  
  

## Methods ##

### getEmailAddresses(length, addresses) ###
  
 Obtain a list of all email addresses  
 contained in the certificate.  
  
 @param length The number of strings in the returned array.  
 @return An array of email addresses.  
  

### containsEmailAddress(aEmailAddress) ###
  
 Check whether a given address is contained in the certificate.  
 The comparison will convert the email address to lowercase.  
 The behaviour for non ASCII characters is undefined.  
  
 @param aEmailAddress The address to search for.  
  
 @return True if the address is contained in the certificate.  
  

### getChain() ###
  
 Obtain a list of certificates that contains this certificate  
 and the issuing certificates of all involved issuers,  
 up to the root issuer.  
  
 @return The chain of certifficates including the issuers.  
  

### getUsagesArray(localOnly, verified, count, usages) ###
  
 Obtain an array of human readable strings describing  
 the certificate's certified usages.  
  
 @param localOnly Do not hit the network, even if revocation information  
                  downloading is currently activated.  
 @param verified The certificate verification result, see constants.  
 @param count The number of human readable usages returned.  
 @param usages The array of human readable usages.  
  

### requestUsagesArrayAsync(cvl) ###
  
 Async version of nsIX509Cert::getUsagesArray()  
  
 Will not block, will request results asynchronously,  
 availability of results will be notified on the main thread.  
  

### getUsagesString(localOnly, verified, usages) ###
  
 Obtain a single comma separated human readable string describing  
 the certificate's certified usages.  
  
 @param localOnly Do not hit the network, even if revocation information  
                  downloading is currently activated.  
 @param verified The certificate verification result, see constants.  
 @param purposes The string listing the usages.  
  

### getRawDER(length, data) ###
  
 Obtain a raw binary encoding of this certificate  
 in DER format.  
  
 @param length The number of bytes in the binary encoding.  
 @param data The bytes representing the DER encoded certificate.  
  

### equals(other) ###
  
 Test whether two certificate instances represent the  
 same certificate.  
  
 @return Whether the certificates are equal  
  

### exportAsCMS(chainMode, length, data) ###
  
 Obtain the certificate wrapped in a PKCS#7 SignedData structure,  
 with or without the certificate chain  
  
 @param chainMode Whether to include the chain (with or without the root),  
see CMS_CHAIN_MODE constants.  
 @param length The number of bytes of the PKCS#7 data.  
 @param data The bytes representing the PKCS#7 wrapped certificate.  
  

### getCert() ###
  
Retrieves the NSS certificate object wrapped by this interface  
  

### getAllTokenNames(length, tokenNames) ###
  
Human readable names identifying all hardware or  
software tokens the certificate is stored on.  
  
@param length On success, the number of entries in the returned array.  
@return On success, an array containing the names of all tokens  
        the certificate is stored on (may be empty).  
        On failure the function throws/returns an error.  
  

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
  
Either delete the certificate from all cert databases,  
or mark it as untrusted.  
  

## Attributes ##

### nickname ###
  
 A nickname for the certificate.  
  

### emailAddress ###
  
 The primary email address of the certificate, if present.  
  

### subjectName ###
  
 The subject owning the certificate.  
  

### commonName ###
  
 The subject's common name.  
  

### organization ###
  
 The subject's organization.  
  

### organizationalUnit ###
  
 The subject's organizational unit.  
  

### sha256Fingerprint ###
  
 The fingerprint of the certificate's DER encoding,  
 calculated using the SHA-256 algorithm.  
  

### sha1Fingerprint ###
  
 The fingerprint of the certificate's DER encoding,  
 calculated using the SHA1 algorithm.  
  

### tokenName ###
  
 A human readable name identifying the hardware or  
 software token the certificate is stored on.  
  

### issuerName ###
  
 The subject identifying the issuer certificate.  
  

### serialNumber ###
  
 The serial number the issuer assigned to this certificate.  
  

### issuerCommonName ###
  
 The issuer subject's common name.  
  

### issuerOrganization ###
  
 The issuer subject's organization.  
  

### issuerOrganizationUnit ###
  
 The issuer subject's organizational unit.  
  

### issuer ###
  
 The certificate used by the issuer to sign this certificate.  
  

### validity ###
  
 This certificate's validity period.  
  

### dbKey ###
  
 A unique identifier of this certificate within the local storage.  
  

### windowTitle ###
  
 A human readable identifier to label this certificate.  
  

### certType ###
  
Type of this certificate  
  

### isSelfSigned ###
  
 True if the certificate is self-signed. CA issued  
 certificates are always self-signed.  
  

### ASN1Structure ###
  
 This is the attribute which describes the ASN1 layout  
 of the certificate.  This can be used when doing a  
 "pretty print" of the certificate's ASN1 structure.  
  

### sha256SubjectPublicKeyInfoDigest ###
  
The base64 encoding of the DER encoded public key info using the specified  
digest.  
  

## Constants ##

### UNKNOWN_CERT ###
  
 Constants to classify the type of a certificate.  
  

### CA_CERT ###

### USER_CERT ###

### EMAIL_CERT ###

### SERVER_CERT ###

### ANY_CERT ###

### VERIFIED_OK ###
  
 Constants for certificate verification results.  
  

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
  
 Constants that describe the certified usages of a certificate.  
  
 Deprecated and unused  
  

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
  
 Constants for specifying the chain mode when exporting a certificate  
  

### CMS_CHAIN_MODE_CertChain ###

### CMS_CHAIN_MODE_CertChainWithRoot ###
