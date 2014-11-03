---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/permission/nsIPermissionPromptService.idl">Source file</a>
</div>

# nsIPermissionPromptService #
<pre>  
Generic permission service for access to WebAPIs, hardware, capabilities.  
  
</pre>
## Methods ##

### getPermission(aRequest) ###
<pre>  
Checks if the capability requires a permission, fires the corresponding cancel()   
or allow() method in aRequest after consulting PermissionSettings, etc.  
  
</pre>