---
layout: default
---

# nsIStreamCipher #

Stream cipher interface.  We're basically copying the interface from
nsICryptoHash interface.


## Methods ##

### init ###

Initialize a stream cipher.
@param aKey nsIKeyObject


### initWithIV ###

Initialize a stream cipher with an initialization vector.
@param aKey nsIKeyObject
@param aIV the initialization vector
@param aIVLen the length of the initialization vector


### update ###

Update from an array of bytes.


### updateFromStream ###

Update from a stream.


### updateFromString ###

A more script friendly method (not in nsICryptoHash interface).


### finish ###

@param aASCII if true then the returned value is a base-64
       encoded string.  if false, then the returned value is
       binary data.


### discard ###

Discard aLen bytes of the keystream.
These days 1536 is considered a decent amount to drop to get
the key state warmed-up enough for secure usage.

