---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/security/manager/ssl/public/nsISSLErrorListener.idl">Source file</a>
</div>

# nsISSLErrorListener #
  
A mechanism to report a broken SSL connection. The recipient should NOT block.  
  

## Methods ##

### notifySSLError(socketInfo, error, targetSite) ###
  
 @param socketInfo A network communication context that can be used to obtain more information  
                   about the active connection.  
 @param error The code associated with the error.  
 @param targetSite The Site name that was used to open the current connection.  
  
 @return The consumer shall return true if it wants to suppress the error message  
         related to the error (the connection will still get canceled).  
  
