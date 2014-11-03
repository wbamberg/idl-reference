---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/test/httpserver/nsIHttpServer.idl">Source file</a>
</div>

# nsIHttpServer #
<pre>  
An interface which represents an HTTP server.  
  
</pre>
## Methods ##

### start(port) ###
<pre>  
Starts up this server, listening upon the given port.  
  
@param port  
  the port upon which listening should happen, or -1 if no specific port is  
  desired  
@throws NS_ERROR_ALREADY_INITIALIZED  
  if this server is already started  
@throws NS_ERROR_NOT_AVAILABLE  
  if the server is not started and cannot be started on the desired port  
  (perhaps because the port is already in use or because the process does  
  not have privileges to do so)  
@note  
  Behavior is undefined if this method is called after stop() has been  
  called on this but before the provided callback function has been  
  called.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>port</td>
<td>  the port upon which listening should happen, or -1 if no specific port is  
  desired  
@throws NS_ERROR_ALREADY_INITIALIZED  
  if this server is already started  
@throws NS_ERROR_NOT_AVAILABLE  
  if the server is not started and cannot be started on the desired port  
  (perhaps because the port is already in use or because the process does  
  not have privileges to do so)  
@note  
  Behavior is undefined if this method is called after stop() has been  
  called on this but before the provided callback function has been  
  called.  
</td>
</tr>

</table>

### stop(callback) ###
<pre>  
Shuts down this server if it is running (including the period of time after  
stop() has been called but before the provided callback has been called).  
  
@param callback  
  an asynchronous callback used to notify the user when this server is  
  stopped and all pending requests have been fully served  
@throws NS_ERROR_NULL_POINTER  
  if callback is null  
@throws NS_ERROR_UNEXPECTED  
  if this server is not running  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>callback</td>
<td>  an asynchronous callback used to notify the user when this server is  
  stopped and all pending requests have been fully served  
@throws NS_ERROR_NULL_POINTER  
  if callback is null  
@throws NS_ERROR_UNEXPECTED  
  if this server is not running  
</td>
</tr>

</table>

### registerFile(path, file) ###
<pre>  
Associates the local file represented by the string file with all requests  
which match request.  
  
@param path  
  the path which is to be mapped to the given file; must begin with "/" and  
  be a valid URI path (i.e., no query string, hash reference, etc.)  
@param file  
  the file to serve for the given path, or null to remove any mapping that  
  might exist; this file must exist for the lifetime of the server  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>path</td>
<td>  the path which is to be mapped to the given file; must begin with "/" and  
  be a valid URI path (i.e., no query string, hash reference, etc.)  
</td>
</tr>

<tr>
<td>file</td>
<td>  the file to serve for the given path, or null to remove any mapping that  
  might exist; this file must exist for the lifetime of the server  
</td>
</tr>

</table>

### registerPathHandler(path, handler) ###
<pre>  
Registers a custom path handler.  
  
@param path  
  the path on the server (beginning with a "/") which is to be handled by  
  handler; this path must not include a query string or hash component; it  
  also should usually be canonicalized, since most browsers will do so  
  before sending otherwise-matching requests  
@param handler  
  an object which will handle any requests for the given path, or null to  
  remove any existing handler; if while the server is running the handler  
  throws an exception while responding to a request, an HTTP 500 response  
  will be returned  
@throws NS_ERROR_INVALID_ARG  
  if path does not begin with a "/"  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>path</td>
<td>  the path on the server (beginning with a "/") which is to be handled by  
  handler; this path must not include a query string or hash component; it  
  also should usually be canonicalized, since most browsers will do so  
  before sending otherwise-matching requests  
</td>
</tr>

<tr>
<td>handler</td>
<td>  an object which will handle any requests for the given path, or null to  
  remove any existing handler; if while the server is running the handler  
  throws an exception while responding to a request, an HTTP 500 response  
  will be returned  
@throws NS_ERROR_INVALID_ARG  
  if path does not begin with a "/"  
</td>
</tr>

</table>

### registerPrefixHandler(prefix, handler) ###
<pre>  
Registers a custom prefix handler.  
  
@param prefix  
  the path on the server (beginning and ending with "/") which is to be  
  handled by handler; this path must not include a query string or hash  
  component. All requests that start with this prefix will be directed to  
  the given handler.  
@param handler  
  an object which will handle any requests for the given path, or null to  
  remove any existing handler; if while the server is running the handler  
  throws an exception while responding to a request, an HTTP 500 response  
  will be returned  
@throws NS_ERROR_INVALID_ARG  
  if path does not begin with a "/" or does not end with a "/"  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>prefix</td>
<td>  the path on the server (beginning and ending with "/") which is to be  
  handled by handler; this path must not include a query string or hash  
  component. All requests that start with this prefix will be directed to  
  the given handler.  
</td>
</tr>

<tr>
<td>handler</td>
<td>  an object which will handle any requests for the given path, or null to  
  remove any existing handler; if while the server is running the handler  
  throws an exception while responding to a request, an HTTP 500 response  
  will be returned  
@throws NS_ERROR_INVALID_ARG  
  if path does not begin with a "/" or does not end with a "/"  
</td>
</tr>

</table>

### registerErrorHandler(code, handler) ###
<pre>  
Registers a custom error page handler.  
  
@param code  
  the error code which is to be handled by handler  
@param handler  
  an object which will handle any requests which generate the given status  
  code, or null to remove any existing handler.  If the handler throws an  
  exception during server operation, fallback is to the genericized error  
  handler (the x00 version), then to 500, using a user-defined error  
  handler if one exists or the server default handler otherwise.  Fallback  
  will never occur from a user-provided handler that throws to the same  
  handler as provided by the server, e.g. a throwing user 404 falls back to  
  400, not a server-provided 404 that might not throw.  
@note  
  If the error handler handles HTTP 500 and throws, behavior is undefined.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>code</td>
<td>  the error code which is to be handled by handler  
</td>
</tr>

<tr>
<td>handler</td>
<td>  an object which will handle any requests which generate the given status  
  code, or null to remove any existing handler.  If the handler throws an  
  exception during server operation, fallback is to the genericized error  
  handler (the x00 version), then to 500, using a user-defined error  
  handler if one exists or the server default handler otherwise.  Fallback  
  will never occur from a user-provided handler that throws to the same  
  handler as provided by the server, e.g. a throwing user 404 falls back to  
  400, not a server-provided 404 that might not throw.  
@note  
  If the error handler handles HTTP 500 and throws, behavior is undefined.  
</td>
</tr>

</table>

### registerDirectory(path, dir) ###
<pre>  
Maps all requests to paths beneath path to the corresponding file beneath  
dir.  
  
@param path  
  the absolute path on the server against which requests will be served  
  from dir (e.g., "/", "/foo/", etc.); must begin and end with a forward  
  slash  
@param dir  
  the directory to be used to serve all requests for paths underneath path  
  (except those further overridden by another, deeper path registered with  
  another directory); if null, any current mapping for the given path is  
  removed  
@throws NS_ERROR_INVALID_ARG  
  if dir is non-null and does not exist or is not a directory, or if path  
  does not begin with and end with a forward slash  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>path</td>
<td>  the absolute path on the server against which requests will be served  
  from dir (e.g., "/", "/foo/", etc.); must begin and end with a forward  
  slash  
</td>
</tr>

<tr>
<td>dir</td>
<td>  the directory to be used to serve all requests for paths underneath path  
  (except those further overridden by another, deeper path registered with  
  another directory); if null, any current mapping for the given path is  
  removed  
@throws NS_ERROR_INVALID_ARG  
  if dir is non-null and does not exist or is not a directory, or if path  
  does not begin with and end with a forward slash  
</td>
</tr>

</table>

### registerContentType(extension, type) ###
<pre>  
Associates files with the given extension with the given Content-Type when  
served by this server, in the absence of any file-specific information  
about the desired Content-Type.  If type is empty, removes any extant  
mapping, if one is present.  
  
@throws NS_ERROR_INVALID_ARG  
  if the given type is not a valid header field value, i.e. if it doesn't  
  match the field-value production in RFC 2616  
@note  
  No syntax checking is done of the given type, beyond ensuring that it is  
  a valid header field value.  Behavior when not given a string matching  
  the media-type production in RFC 2616 section 3.7 is undefined.  
  Implementations may choose to define specific behavior for types which do  
  not match the production, such as for CGI functionality.  
@note  
  Implementations MAY treat type as a trusted argument; users who fail to  
  generate this string from trusted data risk security vulnerabilities.  
  
</pre>
### setIndexHandler(handler) ###
<pre>  
Sets the handler used to display the contents of a directory if  
the directory contains no index page.  
  
@param handler  
  an object which will handle any requests for directories which  
  do not contain index pages, or null to reset to the default  
  index handler; if while the server is running the handler  
  throws an exception while responding to a request, an HTTP 500  
  response will be returned.  An nsIFile corresponding to the  
  directory is available from the metadata object passed to the  
  handler, under the key "directory".  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>handler</td>
<td>  an object which will handle any requests for directories which  
  do not contain index pages, or null to reset to the default  
  index handler; if while the server is running the handler  
  throws an exception while responding to a request, an HTTP 500  
  response will be returned.  An nsIFile corresponding to the  
  directory is available from the metadata object passed to the  
  handler, under the key "directory".  
</td>
</tr>

</table>

### getState(path, key) ###
<pre>  
Retrieves the string associated with the given key in this, for the given  
path's saved state.  All keys are initially associated with the empty  
string.  
  
</pre>
### setState(path, key, value) ###
<pre>  
Sets the string associated with the given key in this, for the given path's  
saved state.  
  
</pre>
### getSharedState(key) ###
<pre>  
Retrieves the string associated with the given key in this, in  
entire-server saved state.  All keys are initially associated with the  
empty string.  
  
</pre>
### setSharedState(key, value) ###
<pre>  
Sets the string associated with the given key in this, in entire-server  
saved state.  
  
</pre>
### getObjectState(key) ###
<pre>  
Retrieves the object associated with the given key in this in  
object-valued saved state.  All keys are initially associated with null.  
  
</pre>
### setObjectState(key, value) ###
<pre>  
Sets the object associated with the given key in this in object-valued  
saved state.  The value may be null.  
  
</pre>
## Attributes ##

### identity ###
<pre> Represents the locations at which this server is reachable. */  
</pre>