---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/cookie/nsICookie.idl">Source file</a>
</div>

# nsICookie #

## Attributes ##

### name ###
<pre>  
the name of the cookie  
  
</pre>
### value ###
<pre>  
the cookie value  
  
</pre>
### isDomain ###
<pre>  
true if the cookie is a domain cookie, false otherwise  
  
</pre>
### host ###
<pre>  
the host (possibly fully qualified) of the cookie  
  
</pre>
### path ###
<pre>  
the path pertaining to the cookie  
  
</pre>
### isSecure ###
<pre>  
true if the cookie was transmitted over ssl, false otherwise  
  
</pre>
### expires ###
<pre>  
@DEPRECATED use nsICookie2.expiry and nsICookie2.isSession instead.  
  
expiration time in seconds since midnight (00:00:00), January 1, 1970 UTC.  
expires = 0 represents a session cookie.  
expires = 1 represents an expiration time earlier than Jan 1, 1970.  
  
</pre>
### status ###

### policy ###

## Constants ##

### STATUS_UNKNOWN ###
<pre>  
@DEPRECATED status implementation will return STATUS_UNKNOWN in all cases.  
  
</pre>
### STATUS_ACCEPTED ###

### STATUS_DOWNGRADED ###

### STATUS_FLAGGED ###

### STATUS_REJECTED ###

### POLICY_UNKNOWN ###
<pre>  
@DEPRECATED policy implementation will return POLICY_UNKNOWN in all cases.  
  
</pre>
### POLICY_NONE ###

### POLICY_NO_CONSENT ###

### POLICY_IMPLICIT_CONSENT ###

### POLICY_EXPLICIT_CONSENT ###

### POLICY_NO_II ###
