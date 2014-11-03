---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/exthelper/extIApplication.idl">Source file</a>
</div>

# extIApplication #

## Methods ##

### getExtensions(aCallback) ###
<pre>  
The extensions object for the application. Contains a list  
of all installed extensions.  
  
</pre>
### quit() ###
<pre>  
Quits the application (if nobody objects to quit-application-requested).  
@returns whether quitting will proceed  
  
</pre>
#### Returns ####

<table>

<tr>
<td>whether quitting will proceed  
</td>
</tr>

</table>

### restart() ###
<pre>  
Restarts the application (if nobody objects to quit-application-requested).  
@returns whether restarting will proceed  
  
</pre>
#### Returns ####

<table>

<tr>
<td>whether restarting will proceed  
</td>
</tr>

</table>

## Attributes ##

### id ###
<pre>  
The id of the application.  
  
</pre>
### name ###
<pre>  
The name of the application.  
  
</pre>
### version ###
<pre>  
The version number of the application.  
  
</pre>
### console ###
<pre>  
The console object for the application.  
  
</pre>
### prefs ###
<pre>  
The preferences object for the application. Defaults to an empty  
root branch.  
  
</pre>
### storage ###
<pre>  
The storage object for the application.  
  
</pre>
### events ###
<pre>  
The events object for the application.  
supports: "load", "ready", "quit", "unload"  
  
</pre>