---
layout: default
---

# nsICookie2 #
   
Main cookie object interface for use by consumers:  
extends nsICookie, a frozen interface for external  
access of cookie objects  
  

## Attributes ##

### rawHost ###
  
the host (possibly fully qualified) of the cookie,  
without a leading dot to represent if it is a  
domain cookie.  
  

### isSession ###
  
true if the cookie is a session cookie.  
note that expiry time will also be honored  
for session cookies (see below); thus, whichever is  
the more restrictive of the two will take effect.  
  

### expiry ###
  
the actual expiry time of the cookie, in seconds  
since midnight (00:00:00), January 1, 1970 UTC.  
  
this is distinct from nsICookie::expires, which  
has different and obsolete semantics.  
  

### isHttpOnly ###
  
true if the cookie is an http only cookie  
  

### creationTime ###
  
the creation time of the cookie, in microseconds  
since midnight (00:00:00), January 1, 1970 UTC.  
  

### lastAccessed ###
  
the last time the cookie was accessed (i.e. created,  
modified, or read by the server), in microseconds  
since midnight (00:00:00), January 1, 1970 UTC.  
  
note that this time may be approximate.  
  
