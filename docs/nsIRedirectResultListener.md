---
layout: default
---

# nsIRedirectResultListener #

## Methods ##

### onRedirectResult(proceeding) ###
  
 When an HTTP redirect has been processed (either successfully or not)  
 nsIHttpChannel will call this function if its callbacks implement this  
 interface.  
  
 @param proceeding  
        Indicated whether the redirect will be proceeding, or not (i.e.  
        has been canceled, or failed).  
  
