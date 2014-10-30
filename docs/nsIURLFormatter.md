---
layout: default
---

# nsIURLFormatter #

## Methods ##

### formatURL ###
   
formatURL - Formats a string URL  
  
The set of known variables is predefined.  
If a variable is unknown, it is left unchanged and a non-fatal error is reported.  
  
@param aFormat string Unformatted URL.  
  
@return The formatted URL.  
  

### formatURLPref ###
   
formatURLPref - Formats a string URL stored in a preference  
  
If the preference value cannot be retrieved, a fatal error is reported  
and the "about:blank" URL is returned.  
  
@param aPref string Preference name.  
  
@return The formatted URL returned by formatURL(), or "about:blank".  
  
