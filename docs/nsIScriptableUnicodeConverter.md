---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/intl/uconv/nsIScriptableUConv.idl">Source file</a>
</div>

# nsIScriptableUnicodeConverter #
<pre>  
This interface is a unicode encoder for use by scripts  
  
@created         8/Jun/2000  
@author          Makoto Kato [m_kato@ga2.so-net.ne.jp]  
  
</pre>
## Methods ##

### ConvertFromUnicode(aSrc) ###
<pre>  
Converts the data from Unicode to one Charset.  
Returns the converted string. After converting, Finish should be called  
and its return value appended to this return value.  
  
</pre>
### Finish() ###
<pre>  
Returns the terminator string.  
Should be called after ConvertFromUnicode() and appended to that  
function's return value.  
  
</pre>
### ConvertToUnicode(aSrc) ###
<pre>  
Converts the data from one Charset to Unicode.  
  
</pre>
### convertFromByteArray(aData, aCount) ###
<pre>  
Converts an array of bytes to a unicode string.  
  
</pre>
### convertToByteArray(aString, aLen, aData) ###
<pre>  
Convert a unicode string to an array of bytes. Finish does not need to be  
called.  
  
</pre>
### convertToInputStream(aString) ###
<pre>  
Converts a unicode string to an input stream. The bytes in the stream are  
encoded according to the charset attribute.  
The returned stream will be nonblocking.  
  
</pre>
## Attributes ##

### charset ###
<pre>  
Current character set.  
  
@throw NS_ERROR_UCONV_NOCONV  
       The requested charset is not supported.  
  
</pre>
### isInternal ###
<pre>  
Internal use  
  
When this attribute is set, all encodings may be accessed. Alias  
resolution is not performed for non-Encoding Standard encodings.  
MailNews callers should perform alias resolution first (e.g. using  
nsICharsetConverterManager::getCharsetAlias()) and use the result  
with this API.  
  
</pre>