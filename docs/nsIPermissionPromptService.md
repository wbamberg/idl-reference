---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/permission/nsIPermissionPromptService.idl">Source file</a>
</div>
# nsIPermissionPromptService #
  
Generic permission service for access to WebAPIs, hardware, capabilities.  
  

## Methods ##

### getPermission(aRequest) ###
  
Checks if the capability requires a permission, fires the corresponding cancel()   
or allow() method in aRequest after consulting PermissionSettings, etc.  
  
