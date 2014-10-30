---
layout: default
---

# nsIExpandedPrincipal #
  
If nsSystemPrincipal is too risky to use, but we want a principal to access  
more than one origin, nsExpandedPrincipals letting us define an array of  
principals it subsumes. So script with an nsExpandedPrincipals will gain  
same origin access when at least one of its principals it contains gained  
sameorigin acccess. An nsExpandedPrincipal will be subsumed by the system  
principal, and by another nsExpandedPrincipal that has all its principals.  
It is added for jetpack content-scripts to let them interact with the  
content and a well defined set of other domains, without the risk of  
leaking out a system principal to the content. See: Bug 734891  
  

## Attributes ##

### whiteList ###
  
An array of principals that the expanded principal subsumes.  
Note: this list is not reference counted, it is shared, so  
should not be changed and should only be used ephemerally.  
  
