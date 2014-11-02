---
layout: default
---

# nsICryptoHMAC #
  
nsICryptoHMAC  
This interface provides HMAC signature algorithms.  
  

## Methods ##

### init(aAlgorithm, aKeyObject) ###
  
Initialize the hashing object. This method may be  
called multiple times with different algorithm types.  
  
@param aAlgorithm the algorithm type to be used.  
       This value must be one of the above valid  
       algorithm types.  
  
@param aKeyObject  
       Object holding a key. To create the key object use for instance:  
       var keyObject = Components.classes["@mozilla.org/security/keyobjectfactory;1"]  
           .getService(Components.interfaces.nsIKeyObjectFactory)  
             .keyFromString(Components.interfaces.nsIKeyObject.HMAC, rawKeyData);  
  
WARNING: This approach is not FIPS compliant.  
  
@throws NS_ERROR_INVALID_ARG if an unsupported algorithm  
       type is passed.  
  
NOTE: This method must be called before any other method   
       on this interface is called.  
  

#### Parameters ####

<table>

<tr>
<td>aAlgorithm</td>
<td>the algorithm type to be used.  
       This value must be one of the above valid  
       algorithm types.  
</td>
</tr>

<tr>
<td>aKeyObject</td>
<td>       Object holding a key. To create the key object use for instance:  
       var keyObject = Components.classes["@mozilla.org/security/keyobjectfactory;1"]  
           .getService(Components.interfaces.nsIKeyObjectFactory)  
             .keyFromString(Components.interfaces.nsIKeyObject.HMAC, rawKeyData);  
</td>
</tr>

</table>

### update(aData, aLen) ###
  
@param aData a buffer to calculate the hash over  
  
@param aLen the length of the buffer |aData|  
  
@throws NS_ERROR_NOT_INITIALIZED if |init| has not been   
        called.  
  

#### Parameters ####

<table>

<tr>
<td>aData</td>
<td>a buffer to calculate the hash over  
</td>
</tr>

<tr>
<td>aLen</td>
<td>the length of the buffer |aData|  
</td>
</tr>

</table>

### updateFromStream(aStream, aLen) ###
  
Calculates and updates a new hash based on a given data stream.  
  
@param aStream an input stream to read from.  
  
@param aLen how much to read from the given |aStream|.  Passing  
       UINT32_MAX indicates that all data available will be used   
       to update the hash.   
  
@throws NS_ERROR_NOT_INITIALIZED if |init| has not been   
        called.  
  
@throws NS_ERROR_NOT_AVAILABLE if the requested amount of   
        data to be calculated into the hash is not available.  
  
  

#### Parameters ####

<table>

<tr>
<td>aStream</td>
<td>an input stream to read from.  
</td>
</tr>

<tr>
<td>aLen</td>
<td>how much to read from the given |aStream|.  Passing  
       UINT32_MAX indicates that all data available will be used   
       to update the hash.   
</td>
</tr>

</table>

### finish(aASCII) ###
  
Completes this HMAC object and produces the actual HMAC diegest data.  
  
@param aASCII if true then the returned value is a base-64   
       encoded string.  if false, then the returned value is  
       binary data.    
  
@return a hash of the data that was read by this object.  This can  
        be either binary data or base 64 encoded.  
  
@throws NS_ERROR_NOT_INITIALIZED if |init| has not been   
        called.  
  
NOTE: This method may be called any time after |init|  
      is called.  This call resets the object to its  
      pre-init state.  
  

#### Parameters ####

<table>

<tr>
<td>aASCII</td>
<td>if true then the returned value is a base-64   
       encoded string.  if false, then the returned value is  
       binary data.    
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>a hash of the data that was read by this object.  This can  
        be either binary data or base 64 encoded.  
</td>
</tr>

</table>

### reset() ###
  
Reinitialize HMAC context to be reused with the same  
settings (the key and hash algorithm) but on different   
set of data.  
  

## Constants ##

### MD2 ###
  
Hashing Algorithms.  These values are to be used by the  
|init| method to indicate which hashing function to  
use.  These values map onto the values defined in  
mozilla/security/nss/lib/softoken/pkcs11t.h and are   
switched to CKM_*_HMAC constant.  
  

### MD5 ###

### SHA1 ###

### SHA256 ###

### SHA384 ###

### SHA512 ###
