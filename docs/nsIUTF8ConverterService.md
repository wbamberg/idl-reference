---
layout: default
---

# nsIUTF8ConverterService #

## Methods ##

### convertStringToUTF8(aString, aCharset, aSkipCheck, aAllowSubstitution) ###
  
Ensure that |aString| is encoded in UTF-8.  If not,   
convert to UTF-8 assuming it's encoded in |aCharset|  
and return the converted string in UTF-8.  
  
@param aString a string to  ensure its UTF8ness  
@param aCharset the charset to convert from if |aString| is not in UTF-8  
@param aSkipCheck determines whether or not to skip 'ASCIIness' and   
       'UTF8ness' check. Set this to PR_TRUE only if you suspect that   
       aString can be mistaken for ASCII / UTF-8 but is actually NOT   
       in ASCII / UTF-8 so that aString has to go through the conversion.  
       skipping ASCIIness/UTF8ness check.  
       The most common case is the input is in 7bit non-ASCII charsets  
       like ISO-2022-JP, HZ or UTF-7 (in its original form or  
       a modified form used in IMAP folder names).  
@param aAllowSubstitution when true, allow the decoder to substitute  
       invalid input sequences by replacement characters (defaults to  
       true)  
@return the converted string in UTF-8.  
@throws NS_ERROR_UCONV_NOCONV when there is no decoder for aCharset  
        or error code of nsIUnicodeDecoder in case of conversion failure  
  

### convertURISpecToUTF8(aSpec, aCharset) ###
  
Ensure that |aSpec| (after URL-unescaping it) is encoded in UTF-8.    
If not,  convert it to UTF-8, assuming it's encoded in |aCharset|,    
and return the result.  
  
<p>Make sure that all characters outside US-ASCII in your input spec   
are url-escaped if  your spec is not in UTF-8 (before url-escaping)   
because the presence of non-ASCII characters is <strong>blindly</strong>  
regarded as an indication that your input spec is in unescaped UTF-8  
and it will be returned without further processing. No valid spec  
going around in Mozilla code would break this assumption.   
  
<p>XXX The above may change in the future depending on the usage pattern.  
  
@param aSpec an url-escaped URI spec to  ensure its UTF8ness  
@param aCharset the charset to convert from if |aSpec| is not in UTF-8  
@return the converted spec in UTF-8.  
@throws NS_ERROR_UCONV_NOCONV when there is no decoder for aCharset  
        or error code of nsIUnicodeDecoder in case of conversion failure  
  
