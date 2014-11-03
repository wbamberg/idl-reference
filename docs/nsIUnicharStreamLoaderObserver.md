---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIUnicharStreamLoader.idl">Source file</a>
</div>

# nsIUnicharStreamLoaderObserver #

## Methods ##

### onDetermineCharset(aLoader, aContext, aSegment) ###
<code>  
Called as soon as at least 512 octets of data have arrived.  
If the stream receives fewer than 512 octets of data in total,  
called upon stream completion but before calling OnStreamComplete.  
Will not be called if the stream receives no data at all.  
  
@param aLoader the unichar stream loader  
@param aContext the context parameter of the underlying channel  
@param aSegment up to 512 octets of raw data from the stream  
  
@return the name of the character set to be used to decode this stream  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aLoader</td>
<td>the unichar stream loader  
</td>
</tr>

<tr>
<td>aContext</td>
<td>the context parameter of the underlying channel  
</td>
</tr>

<tr>
<td>aSegment</td>
<td>up to 512 octets of raw data from the stream  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>the name of the character set to be used to decode this stream  
</td>
</tr>

</table>

### onStreamComplete(aLoader, aContext, aStatus, aBuffer) ###
<code>  
Called when the entire stream has been loaded and decoded.  
  
@param aLoader the unichar stream loader  
@param aContext the context parameter of the underlying channel  
@param aStatus the status of the underlying channel  
@param aBuffer the contents of the stream, decoded to UTF-16.  
  
This method will always be called asynchronously by the  
nsUnicharIStreamLoader involved, on the thread that called the  
loader's init() method.  If onDetermineCharset fails,  
onStreamComplete will still be called, but aStatus will be an  
error code.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aLoader</td>
<td>the unichar stream loader  
</td>
</tr>

<tr>
<td>aContext</td>
<td>the context parameter of the underlying channel  
</td>
</tr>

<tr>
<td>aStatus</td>
<td>the status of the underlying channel  
</td>
</tr>

<tr>
<td>aBuffer</td>
<td>the contents of the stream, decoded to UTF-16.  
</td>
</tr>

</table>
