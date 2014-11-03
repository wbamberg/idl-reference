---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIURLParser.idl">Source file</a>
</div>

# nsIURLParser #
<code>  
nsIURLParser specifies the interface to an URL parser that attempts to  
follow the definitions of RFC 2396.  
  
</code>
## Methods ##

### parseURL(spec, specLen, schemePos, schemeLen, authorityPos, authorityLen, pathPos, pathLen) ###
<code>  
The string to parse in the following methods may be given as a null  
terminated string, in which case the length argument should be -1.  
  
Out parameters of the following methods are all optional (ie. the caller  
may pass-in a NULL value if the corresponding results are not needed).  
Signed out parameters may hold a value of -1 if the corresponding result  
is not part of the string being parsed.  
  
The parsing routines attempt to be as forgiving as possible.  
  
</code><code>  
ParseSpec breaks the URL string up into its 3 major components: a scheme,  
an authority section (hostname, etc.), and a path.  
  
spec = <scheme>://<authority><path>  
  
</code>
### parseAuthority(authority, authorityLen, usernamePos, usernameLen, passwordPos, passwordLen, hostnamePos, hostnameLen, port) ###
<code>  
ParseAuthority breaks the authority string up into its 4 components:  
username, password, hostname, and hostport.  
  
auth = <username>:<password>@<hostname>:<port>  
  
</code>
### parseUserInfo(userinfo, userinfoLen, usernamePos, usernameLen, passwordPos, passwordLen) ###
<code>  
userinfo = <username>:<password>  
  
</code>
### parseServerInfo(serverinfo, serverinfoLen, hostnamePos, hostnameLen, port) ###
<code>  
serverinfo = <hostname>:<port>  
  
</code>
### parsePath(path, pathLen, filepathPos, filepathLen, queryPos, queryLen, refPos, refLen) ###
<code>  
ParsePath breaks the path string up into its 3 major components: a file path,  
a query string, and a reference string.  
  
path = <filepath>?<query>#<ref>  
  
</code>
### parseFilePath(filepath, filepathLen, directoryPos, directoryLen, basenamePos, basenameLen, extensionPos, extensionLen) ###
<code>  
ParseFilePath breaks the file path string up into: the directory portion,  
file base name, and file extension.  
  
filepath = <directory><basename>.<extension>  
  
</code>
### parseFileName(filename, filenameLen, basenamePos, basenameLen, extensionPos, extensionLen) ###
<code>  
filename = <basename>.<extension>  
  
</code>