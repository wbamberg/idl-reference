---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/mozapps/extensions/amIAddonPathService.idl">Source file</a>
</div>

# amIAddonPathService #
<pre>  
This service maps file system paths where add-ons reside to the ID  
of the add-on. Paths are added by the add-on manager. They can  
looked up by anyone.  
  
</pre>
## Methods ##

### findAddonId(path) ###
<pre>  
Given a path to a file, return the ID of the add-on that the file belongs  
to. Returns an empty string if there is no add-on there. Note that if an  
add-on is located at /a/b/c, then looking up the path /a/b/c/d will return  
that add-on.  
  
</pre>
### insertPath(path, addonId) ###
<pre>  
Call this function to inform the service that the given file system path is  
associated with the given add-on ID.  
  
</pre>