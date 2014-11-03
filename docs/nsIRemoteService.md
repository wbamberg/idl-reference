---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/remote/nsIRemoteService.idl">Source file</a>
</div>

# nsIRemoteService #
<pre>  
Start and stop the remote service (xremote/phremote), and register  
windows with the service for backwards compatibility with old xremote  
clients.  
  
@status FLUID This interface is not frozen and is not intended for embedders  
              who want a frozen API. If you are an embedder and need this  
              functionality, contact Benjamin Smedberg about the possibility  
              of freezing the functionality you need.  
  
</pre>
## Methods ##

### startup(appName, profileName) ###
<pre>  
Start the remote service. This should not be done until app startup  
appears to have been successful.  
  
@param appName     (Required) Sets a window property identifying the  
                   application.  
@param profileName (May be null) Sets a window property identifying the  
                   profile name.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>appName</td>
<td>(Required) Sets a window property identifying the  
                   application.  
</td>
</tr>

<tr>
<td>profileName</td>
<td>(May be null) Sets a window property identifying the  
                   profile name.  
</td>
</tr>

</table>

### registerWindow(aWindow) ###
<pre>  
Register a XUL window with the xremote service. The window will be  
configured to accept incoming remote requests. If this method is called  
before startup(), the registration will happen once startup() is called.  
  
</pre>
### shutdown() ###
<pre>  
Stop the remote service from accepting additional requests.  
  
</pre>