---
layout: default
---

# nsIURLParser #
  
nsIURLParser specifies the interface to an URL parser that attempts to  
follow the definitions of RFC 2396.  
  

## Methods ##

### parseURL ###
  
The string to parse in the following methods may be given as a null  
terminated string, in which case the length argument should be -1.  
  
Out parameters of the following methods are all optional (ie. the caller  
may pass-in a NULL value if the corresponding results are not needed).  
Signed out parameters may hold a value of -1 if the corresponding result  
is not part of the string being parsed.  
  
The parsing routines attempt to be as forgiving as possible.  
  
  
ParseSpec breaks the URL string up into its 3 major components: a scheme,  
an authority section (hostname, etc.), and a path.  
  
spec = <scheme>://<authority><path>  
  

### parseAuthority ###
  
ParseAuthority breaks the authority string up into its 4 components:  
username, password, hostname, and hostport.  
  
auth = <username>:<password>@<hostname>:<port>  
  

### parseUserInfo ###
  
userinfo = <username>:<password>  
  

### parseServerInfo ###
  
serverinfo = <hostname>:<port>  
  

### parsePath ###
  
ParsePath breaks the path string up into its 3 major components: a file path,  
a query string, and a reference string.  
  
path = <filepath>?<query>#<ref>  
  

### parseFilePath ###
  
ParseFilePath breaks the file path string up into: the directory portion,  
file base name, and file extension.  
  
filepath = <directory><basename>.<extension>  
  

### parseFileName ###
  
filename = <basename>.<extension>  
  
