---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/security/manager/ssl/public/nsIStreamCipher.idl">Source file</a>
</div>

# nsIStreamCipher #
<code>  
Stream cipher interface.  We're basically copying the interface from  
nsICryptoHash interface.  
  
</code>
## Methods ##

### init(aKey) ###
<code>  
Initialize a stream cipher.  
@param aKey nsIKeyObject  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aKey</td>
<td>nsIKeyObject  
</td>
</tr>

</table>

### initWithIV(aKey, aIV, aIVLen) ###
<code>  
Initialize a stream cipher with an initialization vector.  
@param aKey nsIKeyObject  
@param aIV the initialization vector  
@param aIVLen the length of the initialization vector  
  
</code>
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
<code>  
Update from an array of bytes.  
  
</code>
### updateFromStream(aStream, aLen) ###
<code>  
Update from a stream.  
  
</code>
### updateFromString(aInput) ###
<code>  
A more script friendly method (not in nsICryptoHash interface).  
  
</code>
### finish(aASCII) ###
<code>  
@param aASCII if true then the returned value is a base-64  
       encoded string.  if false, then the returned value is  
       binary data.  
  
</code>
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
<code>  
Discard aLen bytes of the keystream.  
These days 1536 is considered a decent amount to drop to get  
the key state warmed-up enough for secure usage.  
  
</code>