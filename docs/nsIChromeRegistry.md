---
layout: default
---

# nsIChromeRegistry #

## Methods ##

### convertChromeURL ###
  
Resolve a chrome URL to an loadable URI using the information in the  
registry. Does not modify aChromeURL.  
  
Chrome URLs are allowed to be specified in "shorthand", leaving the  
"file" portion off. In that case, the URL is expanded to:  
  
  chrome://package/provider/package.ext  
  
where "ext" is:  
  
  "xul" for a "content" package,  
  "css" for a "skin" package, and  
  "dtd" for a "locale" package.  
  
@param aChromeURL the URL that is to be converted.  
  

### checkForNewChrome ###
  
refresh the chrome list at runtime, looking for new packages/etc  
  

### wrappersEnabled ###
  
returns whether XPCNativeWrappers are enabled for aURI.  
  

## Constants ##

### NONE ###

### PARTIAL ###

### FULL ###
