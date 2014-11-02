---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/exthelper/extIApplication.idl">Source file</a>
</div>
# extIExtension #
  
Interface representing an extension  
  

## Attributes ##

### id ###
  
The id of the extension.  
  

### name ###
  
The name of the extension.  
  

### enabled ###
  
Check if the extension is currently enabled, or not.  
  

### version ###
  
The version number of the extension.  
  

### firstRun ###
  
Indicates whether this is the extension's first run after install  
  

### prefs ###
  
The preferences object for the extension. Defaults to the  
"extensions.<extensionid>." branch.  
  

### storage ###
  
The storage object for the extension.  
  

### events ###
  
The events object for the extension.  
supports: "uninstall"  
  
