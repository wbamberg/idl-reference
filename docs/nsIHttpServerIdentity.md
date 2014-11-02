---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/test/httpserver/nsIHttpServer.idl">Source file</a>
</div>

# nsIHttpServerIdentity #
  
Represents a set of names for a server, one of which is the primary name for  
the server and the rest of which are secondary.  By default every server will  
contain ("http", "localhost", port) and ("http", "127.0.0.1", port) as names,  
where port is what was provided to the corresponding server when started;  
however, except for their being removed when the corresponding server stops  
they have no special importance.  
  

## Methods ##

### add(scheme, host, port) ###
  
Adds a location at which this server may be accessed.  
  
@throws NS_ERROR_ILLEGAL_VALUE  
  if scheme or host do not match the scheme or host productions imported  
  into RFC 2616 from RFC 2396, or if port is not a valid port number  
  

### remove(scheme, host, port) ###
  
Removes this name from the list of names by which the corresponding server  
is known.  If name is also the primary name for the server, the primary  
name reverts to 'http://127.0.0.1' with the associated server's port.  
  
@throws NS_ERROR_ILLEGAL_VALUE  
  if scheme or host do not match the scheme or host productions imported  
  into RFC 2616 from RFC 2396, or if port is not a valid port number  
@returns  
  true if the given name was a name for this server, false otherwise  
  

#### Returns ####

<table>

<tr>
<td>  true if the given name was a name for this server, false otherwise  
</td>
</tr>

</table>

### has(scheme, host, port) ###
  
Returns true if the given name is in this, false otherwise.  
  
@throws NS_ERROR_ILLEGAL_VALUE  
  if scheme or host do not match the scheme or host productions imported  
  into RFC 2616 from RFC 2396, or if port is not a valid port number  
  

### getScheme(host, port) ###
  
Returns the scheme for the name with the given host and port, if one is  
present; otherwise returns the empty string.  
  
@throws NS_ERROR_ILLEGAL_VALUE  
  if host does not match the host production imported into RFC 2616 from  
  RFC 2396, or if port is not a valid port number  
  

### setPrimary(scheme, host, port) ###
  
Designates the given name as the primary name in this and adds it to this  
if it is not already present.  
  
@throws NS_ERROR_ILLEGAL_VALUE  
  if scheme or host do not match the scheme or host productions imported  
  into RFC 2616 from RFC 2396, or if port is not a valid port number  
  

## Attributes ##

### primaryScheme ###
  
The primary scheme at which the corresponding server is located, defaulting  
to 'http'.  This name will be the value of nsIHttpRequest.scheme for  
HTTP/1.0 requests.  
  
This value is always set when the corresponding server is running.  If the  
server is not running, this value is set only if it has been set to a  
non-default name using setPrimary.  In this case reading this value will  
throw NS_ERROR_NOT_INITIALIZED.  
  

### primaryHost ###
  
The primary name by which the corresponding server is known, defaulting to  
'localhost'.  This name will be the value of nsIHttpRequest.host for  
HTTP/1.0 requests.  
  
This value is always set when the corresponding server is running.  If the  
server is not running, this value is set only if it has been set to a  
non-default name using setPrimary.  In this case reading this value will  
throw NS_ERROR_NOT_INITIALIZED.  
  

### primaryPort ###
  
The primary port on which the corresponding server runs, defaulting to the  
associated server's port.  This name will be the value of  
nsIHttpRequest.port for HTTP/1.0 requests.  
  
This value is always set when the corresponding server is running.  If the  
server is not running, this value is set only if it has been set to a  
non-default name using setPrimary.  In this case reading this value will  
throw NS_ERROR_NOT_INITIALIZED.  
  
