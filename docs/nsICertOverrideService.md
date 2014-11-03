---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/security/manager/ssl/public/nsICertOverrideService.idl">Source file</a>
</div>

# nsICertOverrideService #
  
This represents the global list of triples  
  {host:port, cert-fingerprint, allowed-overrides}   
that the user wants to accept without further warnings.   
  

## Methods ##

### rememberValidityOverride(aHostName, aPort, aCert, aOverrideBits, aTemporary) ###
  
 The given cert should always be accepted for the given hostname:port,  
 regardless of errors verifying the cert.  
 Host:Port is a primary key, only one entry per host:port can exist.  
 The implementation will store a fingerprint of the cert.  
 The implementation will decide which fingerprint alg is used.  
  
  

#### Parameters ####

<table>

<tr>
<td>aHostName</td>
<td>The host (punycode) this mapping belongs to  
</td>
</tr>

<tr>
<td>aPort</td>
<td>The port this mapping belongs to, if it is -1 then it   
         is internaly treated as 443  
</td>
</tr>

<tr>
<td>aCert</td>
<td>The cert that should always be accepted  
</td>
</tr>

<tr>
<td>aOverrideBits</td>
<td>The errors we want to be overriden  
</td>
</tr>

</table>

### hasMatchingOverride(aHostName, aPort, aCert, aOverrideBits, aIsTemporary) ###
  
 The given cert should always be accepted for the given hostname:port,  
 regardless of errors verifying the cert.  
 Host:Port is a primary key, only one entry per host:port can exist.  
 The implementation will store a fingerprint of the cert.  
 The implementation will decide which fingerprint alg is used.  
  
  

#### Parameters ####

<table>

<tr>
<td>aHostName</td>
<td>The host (punycode) this mapping belongs to  
</td>
</tr>

<tr>
<td>aPort</td>
<td>The port this mapping belongs to, if it is -1 then it   
         is internaly treated as 443  
</td>
</tr>

<tr>
<td>aCert</td>
<td>The cert that should always be accepted  
</td>
</tr>

<tr>
<td>aOverrideBits</td>
<td>The errors that are currently overriden  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>whether an override entry for aHostNameWithPort is currently on file  
         that matches the given certificate  
</td>
</tr>

</table>

### getValidityOverride(aHostName, aPort, aHashAlg, aFingerprint, aOverrideBits, aIsTemporary) ###
  
 Retrieve the stored override for the given hostname:port.  
  
  

#### Parameters ####

<table>

<tr>
<td>aHostName</td>
<td>The host (punycode) whose entry should be tested  
</td>
</tr>

<tr>
<td>aPort</td>
<td>The port whose entry should be tested, if it is -1 then it   
         is internaly treated as 443  
</td>
</tr>

<tr>
<td>aHashAlg</td>
<td>On return value True, the fingerprint hash algorithm  
                 as an OID value in dotted notation.  
</td>
</tr>

<tr>
<td>aFingerprint</td>
<td>On return value True, the stored fingerprint   
</td>
</tr>

<tr>
<td>aOverrideBits</td>
<td>The errors that are currently overriden  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>whether a matching override entry for aHostNameWithPort   
         and aFingerprint is currently on file  
</td>
</tr>

</table>

### clearValidityOverride(aHostName, aPort) ###
  
 Remove a override for the given hostname:port.  
  
  

#### Parameters ####

<table>

<tr>
<td>aHostName</td>
<td>The host (punycode) whose entry should be cleared.  
</td>
</tr>

<tr>
<td>aPort</td>
<td>The port whose entry should be cleared.  
              If it is -1, then it is internaly treated as 443.  
              If it is 0 and aHostName is "all:temporary-certificates",  
              then all temporary certificates should be cleared.  
</td>
</tr>

</table>

### getAllOverrideHostsWithPorts(aCount, aHostsWithPortsArray) ###
  
 Obtain the full list of hostname:port for which overrides are known.  
  
  

#### Parameters ####

<table>

<tr>
<td>aCount</td>
<td>The number of host:port entries returned  
</td>
</tr>

<tr>
<td>aHostsWithPortsArray</td>
<td>The array of host:port entries returned  
</td>
</tr>

</table>

### isCertUsedForOverrides(aCert, aCheckTemporaries, aCheckPermanents) ###
  
 Is the given cert used in rules?  
  
  

#### Parameters ####

<table>

<tr>
<td>aCert</td>
<td>The cert we're looking for  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>how many override entries are currently on file  
         for the given certificate  
</td>
</tr>

</table>

## Constants ##

### ERROR_UNTRUSTED ###
  
 Override Untrusted  
  

### ERROR_MISMATCH ###
  
 Override hostname Mismatch  
  

### ERROR_TIME ###
  
 Override Time error  
  
