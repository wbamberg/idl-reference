---
layout: default
---

# nsISiteSpecificUserAgent #
  
nsISiteSpecificUserAgent provides you with site/window-specific User Agent strings.  
  

## Methods ##

### getUserAgentForURIAndWindow(aURI, aWindow) ###
  
Get the User Agent string for a given URI.  
  
@param aURI is the URI of the page the UA string is used for.  
  
@param aWindow is the window this UA is being requested for  
  
@returns the User Agent string for the given URI. If no override applies,  
the default User Agent string is used.  
  
