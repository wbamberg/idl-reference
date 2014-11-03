---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsIMacWebAppUtils.idl">Source file</a>
</div>

# nsIMacWebAppUtils #
<pre>  
Allow MozApps API to locate and manipulate natively installed apps  
  
</pre>
## Methods ##

### pathForAppWithIdentifier(bundleIdentifier) ###
<pre>  
Find the path for an app with the given signature.  
  
</pre>
### launchAppWithIdentifier(bundleIdentifier) ###
<pre>  
Launch the app with the given identifier, if it exists.  
  
</pre>
### trashApp(path, callback) ###
<pre>  
Move the app from the given directory to the Trash.  
  
</pre>