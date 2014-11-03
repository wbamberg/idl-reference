---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/protocol/http/nsIHttpProtocolHandler.idl">Source file</a>
</div>

# nsIHttpProtocolHandler #

## Attributes ##

### userAgent ###
<pre>  
Get the HTTP advertised user agent string.  
  
</pre>
### appName ###
<pre>  
Get the application name.  
  
@return The name of this application (eg. "Mozilla").  
  
</pre>
### appVersion ###
<pre>  
Get the application version string.  
  
@return The complete version (major and minor) string. (eg. "5.0")  
  
</pre>
### platform ###
<pre>  
Get the current platform.  
  
@return The platform this application is running on  
	   (eg. "Windows", "Macintosh", "X11")  
  
</pre>
### oscpu ###
<pre>  
Get the current oscpu.  
  
@return The oscpu this application is running on  
  
</pre>
### misc ###
<pre>  
Get the application comment misc portion.  
  
</pre>