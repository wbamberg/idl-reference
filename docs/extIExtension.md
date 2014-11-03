---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/exthelper/extIApplication.idl">Source file</a>
</div>

# extIExtension #
<pre>  
Interface representing an extension  
  
</pre>
## Attributes ##

### id ###
<pre>  
The id of the extension.  
  
</pre>
### name ###
<pre>  
The name of the extension.  
  
</pre>
### enabled ###
<pre>  
Check if the extension is currently enabled, or not.  
  
</pre>
### version ###
<pre>  
The version number of the extension.  
  
</pre>
### firstRun ###
<pre>  
Indicates whether this is the extension's first run after install  
  
</pre>
### prefs ###
<pre>  
The preferences object for the extension. Defaults to the  
"extensions.<extensionid>." branch.  
  
</pre>
### storage ###
<pre>  
The storage object for the extension.  
  
</pre>
### events ###
<pre>  
The events object for the extension.  
supports: "uninstall"  
  
</pre>