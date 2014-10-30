---
layout: default
---

# nsIBadCertListener2 #
  
A mechanism to report a broken SSL status. The recipient should NOT block.  
Can be used to obtain the SSL handshake status of a connection  
that will be canceled because of improper cert status.  
  

## Methods ##

### notifyCertProblem ###
  
 @param socketInfo A network communication context that can be used to obtain more information  
                   about the active connection.  
 @param status The SSL status object that describes the problem(s).  
 @param targetSite The Site name that was used to open the current connection.  
  
 @return The consumer shall return true if it wants to suppress the error message  
         related to the bad cert (the connection will still get canceled).  
  
