---
layout: default
---

# nsIStreamCipher #
  
Stream cipher interface.  We're basically copying the interface from  
nsICryptoHash interface.  
  

## Methods ##

### init(aKey) ###
  
Initialize a stream cipher.  
@param aKey nsIKeyObject  
  

#### Parameters ####

<table>

<tr>
<td>aKey</td>
<td>nsIKeyObject  
</td>
</tr>

</table>

### initWithIV(aKey, aIV, aIVLen) ###
  
Initialize a stream cipher with an initialization vector.  
@param aKey nsIKeyObject  
@param aIV the initialization vector  
@param aIVLen the length of the initialization vector  
  

#### Parameters ####

<table>

<tr>
<td>aKey</td>
<td>nsIKeyObject  
</td>
</tr>

<tr>
<td>aIV</td>
<td>the initialization vector  
</td>
</tr>

<tr>
<td>aIVLen</td>
<td>the length of the initialization vector  
</td>
</tr>

</table>

### update(aData, aLen) ###
  
Update from an array of bytes.  
  

### updateFromStream(aStream, aLen) ###
  
Update from a stream.  
  

### updateFromString(aInput) ###
  
A more script friendly method (not in nsICryptoHash interface).  
  

### finish(aASCII) ###
  
@param aASCII if true then the returned value is a base-64  
       encoded string.  if false, then the returned value is  
       binary data.  
  

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

### discard(aLen) ###
  
Discard aLen bytes of the keystream.  
These days 1536 is considered a decent amount to drop to get  
the key state warmed-up enough for secure usage.  
  
