---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/security/manager/ssl/public/nsIStreamCipher.idl">Source file</a>
</div>

# nsIStreamCipher #
<pre>  
Stream cipher interface.  We're basically copying the interface from  
nsICryptoHash interface.  
  
</pre>
## Methods ##

### init(aKey) ###
<pre>  
Initialize a stream cipher.  
@param aKey nsIKeyObject  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aKey</td>
<td>nsIKeyObject  
</td>
</tr>

</table>

### initWithIV(aKey, aIV, aIVLen) ###
<pre>  
Initialize a stream cipher with an initialization vector.  
@param aKey nsIKeyObject  
@param aIV the initialization vector  
@param aIVLen the length of the initialization vector  
  
</pre>
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
<pre>  
Update from an array of bytes.  
  
</pre>
### updateFromStream(aStream, aLen) ###
<pre>  
Update from a stream.  
  
</pre>
### updateFromString(aInput) ###
<pre>  
A more script friendly method (not in nsICryptoHash interface).  
  
</pre>
### finish(aASCII) ###
<pre>  
@param aASCII if true then the returned value is a base-64  
       encoded string.  if false, then the returned value is  
       binary data.  
  
</pre>
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
<pre>  
Discard aLen bytes of the keystream.  
These days 1536 is considered a decent amount to drop to get  
the key state warmed-up enough for secure usage.  
  
</pre>