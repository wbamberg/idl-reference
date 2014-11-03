---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/exthelper/extIApplication.idl">Source file</a>
</div>

# extIPreference #
<pre>  
Interface for accessing a single preference. The data is not cached.  
All reads access the current state of the preference.  
  
</pre>
## Methods ##

### reset() ###
<pre>  
Resets a preference back to its default values.  
  
</pre>
## Attributes ##

### name ###
<pre>  
The name of the preference.  
  
</pre>
### type ###
<pre>  
A string representing the type of preference (String, Boolean, or Number).  
  
</pre>
### value ###
<pre>  
Get/Set the value of the preference.  
  
</pre>
### locked ###
<pre>  
Get the locked state of the preference. Set to a boolean value to (un)lock it.  
  
</pre>
### modified ###
<pre>  
Check if a preference has been modified by the user, or not.  
  
</pre>
### branch ###
<pre>  
The preference branch that contains this preference.  
  
</pre>
### events ###
<pre>  
The events object for this preference.  
supports: "change"  
  
</pre>