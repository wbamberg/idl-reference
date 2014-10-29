---
layout: default
---

# nsICertOverrideService #

This represents the global list of triples
  {host:port, cert-fingerprint, allowed-overrides} 
that the user wants to accept without further warnings. 


## Methods ##

### rememberValidityOverride ###

 The given cert should always be accepted for the given hostname:port,
 regardless of errors verifying the cert.
 Host:Port is a primary key, only one entry per host:port can exist.
 The implementation will store a fingerprint of the cert.
 The implementation will decide which fingerprint alg is used.

 @param aHostName The host (punycode) this mapping belongs to
 @param aPort The port this mapping belongs to, if it is -1 then it 
         is internaly treated as 443
 @param aCert The cert that should always be accepted
 @param aOverrideBits The errors we want to be overriden


### hasMatchingOverride ###

 The given cert should always be accepted for the given hostname:port,
 regardless of errors verifying the cert.
 Host:Port is a primary key, only one entry per host:port can exist.
 The implementation will store a fingerprint of the cert.
 The implementation will decide which fingerprint alg is used.

 @param aHostName The host (punycode) this mapping belongs to
 @param aPort The port this mapping belongs to, if it is -1 then it 
         is internaly treated as 443
 @param aCert The cert that should always be accepted
 @param aOverrideBits The errors that are currently overriden
 @return whether an override entry for aHostNameWithPort is currently on file
         that matches the given certificate


### getValidityOverride ###

 Retrieve the stored override for the given hostname:port.

 @param aHostName The host (punycode) whose entry should be tested
 @param aPort The port whose entry should be tested, if it is -1 then it 
         is internaly treated as 443
 @param aHashAlg On return value True, the fingerprint hash algorithm
                 as an OID value in dotted notation.
 @param aFingerprint On return value True, the stored fingerprint 
 @param aOverrideBits The errors that are currently overriden
 @return whether a matching override entry for aHostNameWithPort 
         and aFingerprint is currently on file


### clearValidityOverride ###

 Remove a override for the given hostname:port.

 @param aHostName The host (punycode) whose entry should be cleared.
 @param aPort The port whose entry should be cleared.
              If it is -1, then it is internaly treated as 443.
              If it is 0 and aHostName is "all:temporary-certificates",
              then all temporary certificates should be cleared.


### getAllOverrideHostsWithPorts ###

 Obtain the full list of hostname:port for which overrides are known.

 @param aCount The number of host:port entries returned
 @param aHostsWithPortsArray The array of host:port entries returned


### isCertUsedForOverrides ###

 Is the given cert used in rules?

 @param aCert The cert we're looking for
 @return how many override entries are currently on file
         for the given certificate


## Constants ##

### ERROR_UNTRUSTED ###

 Override Untrusted


### ERROR_MISMATCH ###

 Override hostname Mismatch


### ERROR_TIME ###

 Override Time error

