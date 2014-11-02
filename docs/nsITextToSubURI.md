---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/intl/uconv/nsITextToSubURI.idl">Source file</a>
</div>

# nsITextToSubURI #

## Methods ##

### ConvertAndEscape(charset, text) ###

### UnEscapeAndConvert(charset, text) ###

### unEscapeURIForUI(aCharset, aURIFragment) ###
  
Unescapes the given URI fragment (for UI purpose only)  
Note:   
<ul>  
 <li> escaping back the result (unescaped string) is not guaranteed to   
      give the original escaped string  
 <li> In case of a conversion error, the URI fragment (escaped) is   
      assumed to be in UTF-8 and converted to AString (UTF-16)  
 <li> Always succeeeds (callers don't need to do error checking)  
</ul>  
  
@param aCharset the charset to convert from  
@param aURIFragment the URI (or URI fragment) to unescape  
@return Unescaped aURIFragment  converted to unicode  
  

#### Parameters ####

<table>

<tr>
<td>aCharset</td>
<td>the charset to convert from  
</td>
</tr>

<tr>
<td>aURIFragment</td>
<td>the URI (or URI fragment) to unescape  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>Unescaped aURIFragment  converted to unicode  
</td>
</tr>

</table>

### unEscapeNonAsciiURI(aCharset, aURIFragment) ###
  
Unescapes only non ASCII characters in the given URI fragment   
note: this method assumes the URI as UTF-8 and fallbacks to the given   
charset if the charset is an ASCII superset   
  
@param aCharset the charset to convert from  
@param aURIFragment the URI (or URI fragment) to unescape  
@return Unescaped aURIFragment  converted to unicode  
@throws NS_ERROR_UCONV_NOCONV when there is no decoder for aCharset  
        or error code of nsIUnicodeDecoder in case of conversion failure  
  

#### Parameters ####

<table>

<tr>
<td>aCharset</td>
<td>the charset to convert from  
</td>
</tr>

<tr>
<td>aURIFragment</td>
<td>the URI (or URI fragment) to unescape  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>Unescaped aURIFragment  converted to unicode  
@throws NS_ERROR_UCONV_NOCONV when there is no decoder for aCharset  
        or error code of nsIUnicodeDecoder in case of conversion failure  
</td>
</tr>

</table>
