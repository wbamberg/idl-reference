---
layout: default
---

# nsIX509CertDB #
  
This represents a service to access and manipulate  
X.509 certificates stored in a database.  
  

## Methods ##

### findCertByNickname(aToken, aNickname) ###
  
 Given a nickname and optionally a token,  
 locate the matching certificate.  
  
 @param aToken Optionally limits the scope of  
               this function to a token device.  
               Can be null to mean any token.  
 @param aNickname The nickname to be used as the key  
                  to find a certificate.  
  
 @return The matching certificate if found.  
  

### findCertByDBKey(aDBkey, aToken) ###
  
 Will find a certificate based on its dbkey  
 retrieved by getting the dbKey attribute of  
 the certificate.  
  
 @param aDBkey Database internal key, as obtained using  
               attribute dbkey in nsIX509Cert.  
 @param aToken Optionally limits the scope of  
               this function to a token device.  
               Can be null to mean any token.  
  

### findCertNicknames(aToken, aType, count, certNameList) ###
  
 Obtain a list of certificate nicknames from the database.  
 What the name is depends on type:  
   user, ca, or server cert - the nickname  
   email cert - the email address  
  
 @param aToken Optionally limits the scope of  
               this function to a token device.  
               Can be null to mean any token.  
 @param aType Type of certificate to obtain  
              See certificate type constants in nsIX509Cert.  
 @param count The number of nicknames in the returned array  
 @param certNameList The returned array of certificate nicknames.  
  

### findEmailEncryptionCert(aNickname) ###
  
 Find user's own email encryption certificate by nickname.  
  
 @param aNickname The nickname to be used as the key  
                  to find the certificate.  
  
 @return The matching certificate if found.  
  

### findEmailSigningCert(aNickname) ###
  
 Find user's own email signing certificate by nickname.  
  
 @param aNickname The nickname to be used as the key  
                  to find the certificate.  
  
 @return The matching certificate if found.  
  

### findCertByEmailAddress(aToken, aEmailAddress) ###
  
 Find a certificate by email address.  
  
 @param aToken Optionally limits the scope of  
               this function to a token device.  
               Can be null to mean any token.  
 @param aEmailAddress The email address to be used as the key  
                      to find the certificate.  
  
 @return The matching certificate if found.  
  

### importCertificates(data, length, type, ctx) ###
  
 Use this to import a stream sent down as a mime type into  
 the certificate database on the default token.  
 The stream may consist of one or more certificates.  
  
 @param data The raw data to be imported  
 @param length The length of the data to be imported  
 @param type The type of the certificate, see constants in nsIX509Cert  
 @param ctx A UI context.  
  

### importEmailCertificate(data, length, ctx) ###
  
 Import another person's email certificate into the database.  
  
 @param data The raw data to be imported  
 @param length The length of the data to be imported  
 @param ctx A UI context.  
  

### importServerCertificate(data, length, ctx) ###
  
 Import a server machine's certificate into the database.  
  
 @param data The raw data to be imported  
 @param length The length of the data to be imported  
 @param ctx A UI context.  
  

### importUserCertificate(data, length, ctx) ###
  
 Import a personal certificate into the database, assuming  
 the database already contains the private key for this certificate.  
  
 @param data The raw data to be imported  
 @param length The length of the data to be imported  
 @param ctx A UI context.  
  

### deleteCertificate(aCert) ###
  
 Delete a certificate stored in the database.  
  
 @param aCert Delete this certificate.  
  

### setCertTrust(cert, type, trust) ###
  
 Modify the trust that is stored and associated to a certificate within  
 a database. Separate trust is stored for  
 One call manipulates the trust for one trust type only.  
 See the trust type constants defined within this interface.  
  
 @param cert Change the stored trust of this certificate.  
 @param type The type of the certificate. See nsIX509Cert.  
 @param trust A bitmask. The new trust for the possible usages.  
              See the trust constants defined within this interface.  
  

### setCertTrustFromString(cert, trustString) ###
  
@param cert        The certificate for which to modify trust.  
@param trustString decoded by CERT_DecodeTrustString. 3 comma separated  
                   characters, indicating SSL, Email, and Obj signing  
                   trust.  
  

### isCertTrusted(cert, certType, trustType) ###
  
 Query whether a certificate is trusted for a particular use.  
  
 @param cert Obtain the stored trust of this certificate.  
 @param certType The type of the certificate. See nsIX509Cert.  
 @param trustType A single bit from the usages constants defined  
                  within this interface.  
  
 @return Returns true if the certificate is trusted for the given use.  
  

### importCertsFromFile(aToken, aFile, aType) ###
  
 Import certificate(s) from file  
  
 @param aToken Optionally limits the scope of  
               this function to a token device.  
               Can be null to mean any token.  
 @param aFile Identifies a file that contains the certificate  
              to be imported.  
 @param aType Describes the type of certificate that is going to  
              be imported. See type constants in nsIX509Cert.  
  

### importPKCS12File(aToken, aFile) ###
  
 Import a PKCS#12 file containing cert(s) and key(s) into the database.  
  
 @param aToken Optionally limits the scope of  
               this function to a token device.  
               Can be null to mean any token.  
 @param aFile Identifies a file that contains the data  
              to be imported.  
  

### exportPKCS12File(aToken, aFile, count, aCerts) ###
  
 Export a set of certs and keys from the database to a PKCS#12 file.  
  
 @param aToken Optionally limits the scope of  
               this function to a token device.  
               Can be null to mean any token.  
 @param aFile Identifies a file that will be filled with the data  
              to be exported.  
 @param count The number of certificates to be exported.  
 @param aCerts The array of all certificates to be exported.  
  

### constructX509FromBase64(base64) ###

### constructX509(certDER, length) ###

### openSignedAppFileAsync(trustedRoot, aJarFile, callback) ###

### verifySignedManifestAsync(trustedRoot, aManifestStream, aSignatureStream, callback) ###
  
Given streams containing a signature and a manifest file, verifies  
that the signature is valid for the manifest. The signature must  
come from a certificate that is trusted for code signing and that  
was issued by the given trusted root.  
  
 On success, NS_OK and the trusted certificate that signed the  
 Manifest are returned.  
  
 On failure, an error code is returned.  
  

### addCert(certDER, aTrust, aName) ###

### verifyCertNow(aCert, aUsage, aFlags, verifiedChain, aHasEVPolicy) ###
 Warning: This interface is inteded to use only for testing only as:  
   1. It can create IO on the main thread.  
   2. It is in constant change, so in/out can change at any release.  
  
 Obtain the verification result for a cert given a particular usage.  
 On success, the call returns 0, the chain built during verification,  
 and whether the cert is good for EV usage.  
 On failure, the call returns the PRErrorCode for the verification failure  
  
 @param aCert Obtain the stored trust of this certificate  
 @param aUsage a integer representing the usage from NSS  
 @param aFlags flags as described above  
 @param verifedChain chain of verification up to the root if success  
 @param aHasEVPolicy bool that signified that the cert was an EV cert  
 @return 0 if success or the value or the error code for the verification  
         failure  
  

### clearOCSPCache() ###

### addCertFromBase64(base64, aTrust, aName) ###

### getCerts() ###

## Constants ##

### UNTRUSTED ###
  
 Constants that define which usages a certificate  
 is trusted for.  
  

### TRUSTED_SSL ###

### TRUSTED_EMAIL ###

### TRUSTED_OBJSIGN ###

### AppMarketplaceProdPublicRoot ###
  
 Verifies the signature on the given JAR file to verify that it has a  
 valid signature.  To be considered valid, there must be exactly one  
 signature on the JAR file and that signature must have signed every  
 entry. Further, the signature must come from a certificate that  
 is trusted for code signing.  
  
 On success, NS_OK, a nsIZipReader, and the trusted certificate that  
 signed the JAR are returned.  
  
 On failure, an error code is returned.  
  
 This method returns a nsIZipReader, instead of taking an nsIZipReader  
 as input, to encourage users of the API to verify the signature as the  
 first step in opening the JAR.  
  

### AppMarketplaceProdReviewersRoot ###

### AppMarketplaceDevPublicRoot ###

### AppMarketplaceDevReviewersRoot ###

### AppMarketplaceStageRoot ###

### AppXPCShellRoot ###

### TrustedHostedAppPublicRoot ###

### TrustedHostedAppTestRoot ###

### FLAG_LOCAL_ONLY ###

### FLAG_MUST_BE_EV ###
