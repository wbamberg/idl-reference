---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/base/nsIErrorService.idl">Source file</a>
</div>

# nsIErrorService #
  
nsIErrorService: This is an interim service that allows nsresult codes to be mapped to   
string bundles that can be used to look up error messages. String bundle keys can also  
be mapped.   
  
This service will eventually get replaced by extending xpidl to allow errors to be defined.  
(http://bugzilla.mozilla.org/show_bug.cgi?id=13423).  
  

## Methods ##

### registerErrorStringBundle(errorModule, stringBundleURL) ###
  
Registers a string bundle URL for an error module. Error modules are obtained from  
nsresult code with NS_ERROR_GET_MODULE.  
  

### unregisterErrorStringBundle(errorModule) ###
  
Unregisters a string bundle URL for an error module.  
  

### getErrorStringBundle(errorModule) ###
  
Retrieves a string bundle URL for an error module.  
  
