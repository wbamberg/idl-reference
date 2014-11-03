---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/exthelper/extIApplication.idl">Source file</a>
</div>

# extIApplication #

## Methods ##

### getExtensions(aCallback) ###
<code>  
The extensions object for the application. Contains a list  
of all installed extensions.  
  
</code>
### quit() ###
<code>  
Quits the application (if nobody objects to quit-application-requested).  
@returns whether quitting will proceed  
  
</code>
#### Returns ####

<table>

<tr>
<td>whether quitting will proceed  
</td>
</tr>

</table>

### restart() ###
<code>  
Restarts the application (if nobody objects to quit-application-requested).  
@returns whether restarting will proceed  
  
</code>
#### Returns ####

<table>

<tr>
<td>whether restarting will proceed  
</td>
</tr>

</table>

## Attributes ##

### id ###
  
The id of the application.  
  

### name ###
  
The name of the application.  
  

### version ###
  
The version number of the application.  
  

### console ###
  
The console object for the application.  
  

### prefs ###
  
The preferences object for the application. Defaults to an empty  
root branch.  
  

### storage ###
  
The storage object for the application.  
  

### events ###
  
The events object for the application.  
supports: "load", "ready", "quit", "unload"  
  
