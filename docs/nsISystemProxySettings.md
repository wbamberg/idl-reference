---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsISystemProxySettings.idl">Source file</a>
</div>

# nsISystemProxySettings #
<pre>   
This interface allows the proxy code to use platform-specific proxy  
settings when the proxy preference is set to "automatic discovery". This service  
acts like a PAC parser to netwerk, but it will actually read the system settings and  
either return the proper proxy data from the autoconfig URL specified in the system proxy,  
or generate proxy data based on the system's manual proxy settings.  
  
</pre>
## Methods ##

### getProxyForURI(testSpec, testScheme, testHost, testPort) ###
<pre>  
See ProxyAutoConfig::getProxyForURI; this function behaves similarly except  
a more relaxed return string is allowed that includes full urls instead of just  
host:port syntax. e.g. "PROXY http://www.foo.com:8080" instead of  
"PROXY www.foo.com:8080"  
  
</pre>
## Attributes ##

### mainThreadOnly ###
<pre>  
Whether or not it is appropriate to execute getProxyForURI off the main thread.  
If that method can block (e.g. for WPAD as windows does) then it must be  
not mainThreadOnly to avoid creating main thread jank. The main thread only option is  
provided for implementations that do not block but use other main thread only  
functions such as dbus.  
  
</pre>
### PACURI ###
<pre>  
If non-empty, use this PAC file. If empty, call getProxyForURI instead.  
  
</pre>