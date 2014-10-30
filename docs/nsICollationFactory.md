---
layout: default
---

# nsICollationFactory #

## Methods ##

### CreateCollation(locale) ###
  
Create the collation for a given locale.  
  
Use NULL as the locale parameter to use the user's locale preference  
from the operating system.  
  
@param locale  
       The locale for which to create the collation or null to use  
       user preference.  
@return A collation for the given locale.  
  
