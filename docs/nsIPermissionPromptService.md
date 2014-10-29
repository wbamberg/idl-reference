---
layout: default
---

# nsIPermissionPromptService #

Generic permission service for access to WebAPIs, hardware, capabilities.


## Methods ##

### getPermission ###

Checks if the capability requires a permission, fires the corresponding cancel() 
or allow() method in aRequest after consulting PermissionSettings, etc.

