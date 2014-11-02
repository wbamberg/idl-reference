---
layout: default
---

# nsIHttpRequest #
  
A representation of the data included in an HTTP request.  
  

## Methods ##

### getHeader(fieldName) ###
  
Returns the value for the header in this request specified by fieldName.  
  
@param fieldName  
  the name of the field whose value is to be gotten; note that since HTTP  
  header field names are case-insensitive, this method produces equivalent  
  results for "HeAdER" and "hEADer" as fieldName  
@returns  
  The result is a string containing the individual values of the header,  
  usually separated with a comma.  The headers WWW-Authenticate,  
  Proxy-Authenticate, and Set-Cookie violate the HTTP specification,  
  however, and for these headers only the separator string is '\n'.  
  
@throws NS_ERROR_INVALID_ARG  
  if fieldName does not constitute a valid header field name  
@throws NS_ERROR_NOT_AVAILABLE  
  if the given header does not exist in this  
  

#### Parameters ####

<table>

<tr>
<td>fieldName</td>
<td>  the name of the field whose value is to be gotten; note that since HTTP  
  header field names are case-insensitive, this method produces equivalent  
  results for "HeAdER" and "hEADer" as fieldName  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>  The result is a string containing the individual values of the header,  
  usually separated with a comma.  The headers WWW-Authenticate,  
  Proxy-Authenticate, and Set-Cookie violate the HTTP specification,  
  however, and for these headers only the separator string is '\n'.  
</td>
</tr>

</table>

### hasHeader(fieldName) ###
  
Returns true if a header with the given field name exists in this, false  
otherwise.  
  
@param fieldName  
  the field name whose existence is to be determined in this; note that  
  since HTTP header field names are case-insensitive, this method produces  
  equivalent results for "HeAdER" and "hEADer" as fieldName  
@throws NS_ERROR_INVALID_ARG  
  if fieldName does not constitute a valid header field name  
  

#### Parameters ####

<table>

<tr>
<td>fieldName</td>
<td>  the field name whose existence is to be determined in this; note that  
  since HTTP header field names are case-insensitive, this method produces  
  equivalent results for "HeAdER" and "hEADer" as fieldName  
@throws NS_ERROR_INVALID_ARG  
  if fieldName does not constitute a valid header field name  
</td>
</tr>

</table>

## Attributes ##

### method ###
  
The request type for this request (see RFC 2616, section 5.1.1).  
  

### scheme ###
  
The scheme of the requested path, usually 'http' but might possibly be  
'https' if some form of SSL tunneling is in use.  Note that this value  
cannot be accurately determined unless the incoming request used the  
absolute-path form of the request line; it defaults to 'http', so only  
if it is something else can you be entirely certain it's correct.  
  

### host ###
  
The host of the data being requested (e.g. "localhost" for the  
http://localhost:8080/file resource).  Note that the relevant port on the  
host is specified in this.port.  This value is in the ASCII character  
encoding.  
  

### port ###
  
The port on the server on which the request was received.  
  

### path ###
  
The requested path, without any query string (e.g. "/dir/file.txt").  It is  
guaranteed to begin with a "/".  The individual components in this string  
are URL-encoded.  
  

### queryString ###
  
The URL-encoded query string associated with this request, not including  
the initial "?", or "" if no query string was present.  
  

### httpVersion ###
  
A string containing the HTTP version of the request (i.e., "1.1").  Leading  
zeros for either component of the version will be omitted.  (In other  
words, if the request contains the version "1.01", this attribute will be  
"1.1"; see RFC 2616, section 3.1.)  
  

### headers ###
  
An nsISimpleEnumerator of nsISupportsStrings over the names of the headers  
in this request.  The header field names in the enumerator may not  
necessarily have the same case as they do in the request itself.  
  

### bodyInputStream ###
  
A stream from which data appearing in the body of this request can be read.  
  
