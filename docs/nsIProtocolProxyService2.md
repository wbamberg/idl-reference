---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIProtocolProxyService2.idl">Source file</a>
</div>

# nsIProtocolProxyService2 #
<code>  
An extension of nsIProtocolProxyService  
  
</code>
## Methods ##

### reloadPAC() ###
<code>  
Call this method to cause the PAC file (if any is configured) to be  
reloaded.  The PAC file is loaded asynchronously.  
  
</code>
### deprecatedBlockingResolve(aURI, aFlags) ###
<code>  
This exists so Java(tm) can migrate to an asynchronous interface.  
Do not use this unless you are the plugin interface, and even then you  
ought to feel horribly guilty because you will create main thread jank.  
  
No documentation - it is deprecated!  
/  
</code>
### asyncResolve2(aURI, aFlags, aCallback) ###
<code>  
This method is identical to asyncResolve() except it may execute the  
callback function immediately (i.e from the stack of asyncResolve2()) if  
it is immediately ready to run. The nsICancelable return value will be  
null in that case.  
  
</code>