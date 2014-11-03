---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/intl/uconv/nsIScriptableUConv.idl">Source file</a>
</div>

# nsIScriptableUnicodeConverter #
  
This interface is a unicode encoder for use by scripts  
  
@created         8/Jun/2000  
@author          Makoto Kato [m_kato@ga2.so-net.ne.jp]  
  

## Methods ##

### ConvertFromUnicode(aSrc) ###
  
Converts the data from Unicode to one Charset.  
Returns the converted string. After converting, Finish should be called  
and its return value appended to this return value.  
  

### Finish() ###
  
Returns the terminator string.  
Should be called after ConvertFromUnicode() and appended to that  
function's return value.  
  

### ConvertToUnicode(aSrc) ###
  
Converts the data from one Charset to Unicode.  
  

### convertFromByteArray(aData, aCount) ###
  
Converts an array of bytes to a unicode string.  
  

### convertToByteArray(aString, aLen, aData) ###
  
Convert a unicode string to an array of bytes. Finish does not need to be  
called.  
  

### convertToInputStream(aString) ###
  
Converts a unicode string to an input stream. The bytes in the stream are  
encoded according to the charset attribute.  
The returned stream will be nonblocking.  
  

## Attributes ##

### charset ###
  
Current character set.  
  
@throw NS_ERROR_UCONV_NOCONV  
       The requested charset is not supported.  
  

### isInternal ###
  
Internal use  
  
When this attribute is set, all encodings may be accessed. Alias  
resolution is not performed for non-Encoding Standard encodings.  
MailNews callers should perform alias resolution first (e.g. using  
nsICharsetConverterManager::getCharsetAlias()) and use the result  
with this API.  
  
