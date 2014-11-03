---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/system/nsIXULAppInfo.idl">Source file</a>
</div>

# nsIXULAppInfo #
<pre>  
A scriptable interface to the nsXULAppAPI structure. See nsXULAppAPI.h for  
a detailed description of each attribute.  
  
</pre>
## Attributes ##

### vendor ###
<pre>  
@see nsXREAppData.vendor  
@returns an empty string if nsXREAppData.vendor is not set.  
  
</pre>
### name ###
<pre>  
@see nsXREAppData.name  
  
</pre>
### ID ###
<pre>  
@see nsXREAppData.ID  
@returns an empty string if nsXREAppData.ID is not set.  
  
</pre>
### version ###
<pre>  
The version of the XUL application. It is different than the  
version of the XULRunner platform. Be careful about which one you want.  
  
@see nsXREAppData.version  
@returns an empty string if nsXREAppData.version is not set.  
  
</pre>
### appBuildID ###
<pre>  
The build ID/date of the application. For xulrunner applications,  
this will be different than the build ID of the platform. Be careful  
about which one you want.  
  
</pre>
### platformVersion ###
<pre>  
The version of the XULRunner platform.  
  
</pre>
### platformBuildID ###
<pre>  
The build ID/date of gecko and the XULRunner platform.  
  
</pre>
### UAName ###
<pre>  
@see nsXREAppData.UAName  
@returns an empty string if nsXREAppData.UAName is not set.  
  
</pre>