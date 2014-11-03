---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/test/httpserver/nsIHttpServer.idl">Source file</a>
</div>

# nsIHttpResponse #
<code>  
Represents an HTTP response, as described in RFC 2616, section 6.  
  
</code>
## Methods ##

### setStatusLine(httpVersion, statusCode, description) ###
<code>  
Sets the status line for this.  If this method is never called on this, the  
status line defaults to "HTTP/", followed by the server's default HTTP  
version (e.g. "1.1"), followed by " 200 OK".  
  
@param httpVersion  
  the HTTP version of this, as a string (e.g. "1.1"); if null, the server  
  default is used  
@param code  
  the numeric HTTP status code for this  
@param description  
  a human-readable description of code; may be null if no description is  
  desired  
@throws NS_ERROR_INVALID_ARG  
  if httpVersion is not a valid HTTP version string, statusCode is greater  
  than 999, or description contains invalid characters  
@throws NS_ERROR_NOT_AVAILABLE  
  if this response is being processed asynchronously and data has been  
  written to this response's body, or if seizePower() has been called on  
  this  
  
</code>
#### Parameters ####

<table>

<tr>
<td>httpVersion</td>
<td>  the HTTP version of this, as a string (e.g. "1.1"); if null, the server  
  default is used  
</td>
</tr>

<tr>
<td>code</td>
<td>  the numeric HTTP status code for this  
</td>
</tr>

<tr>
<td>description</td>
<td>  a human-readable description of code; may be null if no description is  
  desired  
@throws NS_ERROR_INVALID_ARG  
  if httpVersion is not a valid HTTP version string, statusCode is greater  
  than 999, or description contains invalid characters  
@throws NS_ERROR_NOT_AVAILABLE  
  if this response is being processed asynchronously and data has been  
  written to this response's body, or if seizePower() has been called on  
  this  
</td>
</tr>

</table>

### setHeader(name, value, merge) ###
<code>  
Sets the specified header in this.  
  
@param name  
  the name of the header; must match the field-name production per RFC 2616  
@param value  
  the value of the header; must match the field-value production per RFC  
  2616  
@param merge  
  when true, if the given header already exists in this, the values passed  
  to this function will be merged into the existing header, per RFC 2616  
  header semantics (except for the Set-Cookie, WWW-Authenticate, and  
  Proxy-Authenticate headers, which will treat each such merged header as  
  an additional instance of the header, for real-world compatibility  
  reasons); when false, replaces any existing header of the given name (if  
  any exists) with a new header with the specified value  
@throws NS_ERROR_INVALID_ARG  
  if name or value is not a valid header component  
@throws NS_ERROR_NOT_AVAILABLE  
  if this response is being processed asynchronously and data has been  
  written to this response's body, or if seizePower() has been called on  
  this  
  
</code>
#### Parameters ####

<table>

<tr>
<td>name</td>
<td>  the name of the header; must match the field-name production per RFC 2616  
</td>
</tr>

<tr>
<td>value</td>
<td>  the value of the header; must match the field-value production per RFC  
  2616  
</td>
</tr>

<tr>
<td>merge</td>
<td>  when true, if the given header already exists in this, the values passed  
  to this function will be merged into the existing header, per RFC 2616  
  header semantics (except for the Set-Cookie, WWW-Authenticate, and  
  Proxy-Authenticate headers, which will treat each such merged header as  
  an additional instance of the header, for real-world compatibility  
  reasons); when false, replaces any existing header of the given name (if  
  any exists) with a new header with the specified value  
@throws NS_ERROR_INVALID_ARG  
  if name or value is not a valid header component  
@throws NS_ERROR_NOT_AVAILABLE  
  if this response is being processed asynchronously and data has been  
  written to this response's body, or if seizePower() has been called on  
  this  
</td>
</tr>

</table>

### write(data) ###
<code>  
Writes a string to the response's output stream.  This method is merely a  
convenient shorthand for writing the same data to bodyOutputStream  
directly.  
  
@note  
  This method is only guaranteed to work with ASCII data.  
@throws NS_ERROR_NOT_AVAILABLE  
  if called after this response has been fully constructed  
  
</code>
### processAsync() ###
<code>  
Signals that this response is being constructed asynchronously.  Requests  
are typically completely constructed during nsIHttpRequestHandler.handle;  
however, responses which require significant resources (time, memory,  
processing) to construct can be created and sent incrementally by calling  
this method during the call to nsIHttpRequestHandler.handle.  This method  
only has this effect when called during nsIHttpRequestHandler.handle;  
behavior is undefined if it is called at a later time.  It may be called  
multiple times with no ill effect, so long as each call occurs before  
finish() is called.  
  
@throws NS_ERROR_UNEXPECTED  
  if not initially called within a nsIHttpRequestHandler.handle call or if  
  called after this response has been finished  
@throws NS_ERROR_NOT_AVAILABLE  
  if seizePower() has been called on this  
  
</code>
### seizePower() ###
<code>  
Seizes complete control of this response (and its connection) from the  
server, allowing raw and unfettered access to data being sent in the HTTP  
response.  Once this method has been called the only property which may be  
accessed without an exception being thrown is bodyOutputStream, and the  
only methods which may be accessed without an exception being thrown are  
write(), finish(), and seizePower() (which may be called multiple times  
without ill effect so long as all calls are otherwise allowed).  
  
After a successful call, all data subsequently written to the body of this  
response is written directly to the corresponding connection.  (Previously-  
written data is silently discarded.)  No status line or headers are sent  
before doing so; if the response handler wishes to write such data, it must  
do so manually.  Data generation completes only when finish() is called; it  
is not enough to simply call close() on bodyOutputStream.  
  
@throws NS_ERROR_NOT_AVAILABLE  
  if processAsync() has been called on this  
@throws NS_ERROR_UNEXPECTED  
  if finish() has been called on this  
  
</code>
### finish() ###
<code>  
Signals that construction of this response is complete and that it may be  
sent over the network to the client, or if seizePower() has been called  
signals that all data has been written and that the underlying connection  
may be closed.  This method may only be called after processAsync() or  
seizePower() has been called.  This method is idempotent.  
  
@throws NS_ERROR_UNEXPECTED  
  if processAsync() or seizePower() has not already been properly called  
  
</code>
## Attributes ##

### bodyOutputStream ###
  
A stream to which data appearing in the body of this response (or in the  
totality of the response if seizePower() is called) should be written.  
After this response has been designated as being processed asynchronously,  
or after seizePower() has been called on this, subsequent writes will no  
longer be buffered and will be written to the underlying transport without  
delaying until the entire response is constructed.  Write-through may or  
may not be synchronous in the implementation, and in any case particular  
behavior may not be observable to the HTTP client as intermediate buffers  
both in the server socket and in the client may delay written data; be  
prepared for delays at any time.  
  
@throws NS_ERROR_NOT_AVAILABLE  
  if accessed after this response is fully constructed  
  
