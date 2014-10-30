---
layout: default
---

# nsICryptoHash #
  
nsICryptoHash  
This interface provides crytographic hashing algorithms.  
  

## Methods ##

### init ###
  
Initialize the hashing object. This method may be  
called multiple times with different algorithm types.  
  
@param aAlgorithm the algorithm type to be used.  
       This value must be one of the above valid  
       algorithm types.  
  
@throws NS_ERROR_INVALID_ARG if an unsupported algorithm  
        type is passed.  
  
NOTE: This method or initWithString must be called  
      before any other method on this interface is called.  
  

### initWithString ###
  
Initialize the hashing object. This method may be  
called multiple times with different algorithm types.  
  
@param aAlgorithm the algorithm type to be used.  
  
@throws NS_ERROR_INVALID_ARG if an unsupported algorithm  
        type is passed.  
  
NOTE: This method or init must be called before any  
      other method on this interface is called.  
  

### update ###
  
@param aData a buffer to calculate the hash over  
  
@param aLen the length of the buffer |aData|  
  
@throws NS_ERROR_NOT_INITIALIZED if |init| has not been   
        called.  
  

### updateFromStream ###
  
Calculates and updates a new hash based on a given data stream.  
  
@param aStream an input stream to read from.  
  
@param aLen how much to read from the given |aStream|.  Passing  
       UINT32_MAX indicates that all data available will be used   
       to update the hash.   
  
@throws NS_ERROR_NOT_INITIALIZED if |init| has not been   
        called.  
  
@throws NS_ERROR_NOT_AVAILABLE if the requested amount of   
        data to be calculated into the hash is not available.  
  
  

### finish ###
  
Completes this hash object and produces the actual hash data.  
  
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
  

## Constants ##

### MD2 ###
  
Hashing Algorithms.  These values are to be used by the  
|init| method to indicate which hashing function to  
use.  These values map directly onto the values defined  
in mozilla/security/nss/lib/cryptohi/hasht.h.  
  

### MD5 ###

### SHA1 ###

### SHA256 ###

### SHA384 ###

### SHA512 ###
