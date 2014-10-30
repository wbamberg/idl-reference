---
layout: default
---

# nsINetUtil #
  
nsINetUtil provides various network-related utility methods.  
  

## Methods ##

### parseContentType ###
  
Parse a content-type header and return the content type and  
charset (if any).  
  
@param aTypeHeader the header string to parse  
@param [out] aCharset the charset parameter specified in the  
             header, if any.  
@param [out] aHadCharset whether a charset was explicitly specified.  
@return the MIME type specified in the header, in lower-case.  
  

### protocolHasFlags ###
  
Test whether the given URI's handler has the given protocol flags.  
  
@param aURI the URI in question  
@param aFlags the flags we're testing for.  
  
@return whether the protocol handler for aURI has all the flags  
        in aFlags.  
  

### URIChainHasFlags ###
  
Test whether the protocol handler for this URI or that for any of  
its inner URIs has the given protocol flags.  This will QI aURI to  
nsINestedURI and walk the nested URI chain.  
  
@param aURI the URI in question  
@param aFlags the flags we're testing for.  
  
@return whether any of the protocol handlers involved have all the flags  
        in aFlags.  
  

### toImmutableURI ###
  
Take aURI and produce an immutable version of it for the caller.  If aURI  
is immutable this will be aURI itself; otherwise this will be a clone,  
marked immutable if possible.  Passing null to this method is allowed; in  
that case it will return null.  
  

### newSimpleNestedURI ###
  
Create a simple nested URI using the result of  
toImmutableURI on the passed-in aURI which may not be null.  
Note: The return URI will not have had its spec set yet.  
  

### escapeString ###
  
escape a string with %00-style escaping  
  

### escapeURL ###
  
%XX-Escape invalid chars in a URL segment.   
  
@param aStr the URL to be escaped  
@param aFlags the URL segment type flags  
  
@return the escaped string (the string itself if escaping did not happen)  
  
  

### unescapeString ###
  
Expands URL escape sequences  
  
@param aStr the URL to be unescaped  
@param aFlags only ESCAPE_URL_ONLY_NONASCII and ESCAPE_URL_SKIP_CONTROL  
              are recognized.  If |aFlags| is 0 all escape sequences are   
              unescaped  
@return unescaped string  
  

### extractCharsetFromContentType ###
  
Extract the charset parameter location and value from a content-type  
header.  
  
@param aTypeHeader the header string to parse  
@param [out] aCharset the charset parameter specified in the  
             header, if any.  
@param [out] aCharsetStart index of the start of the charset parameter  
             (the ';' separating it from what came before) in aTypeHeader.  
             If this function returns false, this argument will still be  
             set, to the index of the location where a new charset should  
             be inserted.  
@param [out] aCharsetEnd index of the end of the charset parameter (the  
             ';' separating it from what comes after, or the end  
             of the string) in aTypeHeader.  If this function returns  
             false, this argument will still be set, to the index of the  
             location where a new charset should be inserted.  
  
@return whether a charset parameter was found.  This can be false even in  
cases when parseContentType would claim to have a charset, if the type  
that won out does not have a charset parameter specified.  
  

## Constants ##

### ESCAPE_ALL ###
 Escape every character with its %XX-escaped equivalent */  

### ESCAPE_XALPHAS ###
 Leave alphanumeric characters intact and %XX-escape all others */  

### ESCAPE_XPALPHAS ###
 Leave alphanumeric characters intact, convert spaces to '+',  
%XX-escape all others */  

### ESCAPE_URL_PATH ###
 Leave alphanumeric characters and forward slashes intact,  
%XX-escape all others */  

### ESCAPE_URL_SCHEME ###
 %XX-escape URL scheme */  

### ESCAPE_URL_USERNAME ###
 %XX-escape username in the URL */  

### ESCAPE_URL_PASSWORD ###
 %XX-escape password in the URL */  

### ESCAPE_URL_HOST ###
 %XX-escape URL host */  

### ESCAPE_URL_DIRECTORY ###
 %XX-escape URL directory */  

### ESCAPE_URL_FILE_BASENAME ###
 %XX-escape file basename in the URL */  

### ESCAPE_URL_FILE_EXTENSION ###
 %XX-escape file extension in the URL */  

### ESCAPE_URL_PARAM ###
 %XX-escape URL parameters */  

### ESCAPE_URL_QUERY ###
 %XX-escape URL query */  

### ESCAPE_URL_REF ###
 %XX-escape URL ref */  

### ESCAPE_URL_FILEPATH ###
 %XX-escape URL path - same as escaping directory, basename and extension */  

### ESCAPE_URL_MINIMAL ###
 %XX-escape scheme, username, password, host, path, params, query and ref */  

### ESCAPE_URL_FORCED ###
 Force %XX-escaping of already escaped sequences */  

### ESCAPE_URL_ONLY_ASCII ###
 Skip non-ascii octets, %XX-escape all others */  

### ESCAPE_URL_ONLY_NONASCII ###
   
Skip graphic octets (0x20-0x7E) when escaping  
Skips all ASCII octets (0x00-0x7F) when unescaping   
  

### ESCAPE_URL_COLON ###
 Force %XX-escape of colon */  

### ESCAPE_URL_SKIP_CONTROL ###
 Skip C0 and DEL from unescaping */  
