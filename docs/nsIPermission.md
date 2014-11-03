---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIPermission.idl">Source file</a>
</div>

# nsIPermission #
<pre>  
This interface defines a "permission" object,  
used to specify allowed/blocked objects from  
user-specified sites (cookies, images etc).  
  
</pre>
## Attributes ##

### host ###
<pre>  
The name of the host for which the permission is set  
  
</pre>
### appId ###
<pre>  
The id of the app for which the permission is set.  
  
</pre>
### isInBrowserElement ###
<pre>  
Whether the permission has been set to a page inside a browser element.  
  
</pre>
### type ###
<pre>  
a case-sensitive ASCII string, indicating the type of permission  
(e.g., "cookie", "image", etc).  
This string is specified by the consumer when adding a permission   
via nsIPermissionManager.  
@see nsIPermissionManager  
  
</pre>
### capability ###
<pre>  
The permission (see nsIPermissionManager.idl for allowed values)  
  
</pre>
### expireType ###
<pre>  
The expiration type of the permission (session, time-based or none).  
Constants are EXPIRE_*, defined in nsIPermissionManager.  
@see nsIPermissionManager  
  
</pre>
### expireTime ###
<pre>  
The expiration time of the permission (milliseconds since Jan 1 1970  
0:00:00).  
  
</pre>