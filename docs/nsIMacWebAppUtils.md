---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsIMacWebAppUtils.idl">Source file</a>
</div>

# nsIMacWebAppUtils #
<code>  
Allow MozApps API to locate and manipulate natively installed apps  
  
</code>
## Methods ##

### pathForAppWithIdentifier(bundleIdentifier) ###
<code>  
Find the path for an app with the given signature.  
  
</code>
### launchAppWithIdentifier(bundleIdentifier) ###
<code>  
Launch the app with the given identifier, if it exists.  
  
</code>
### trashApp(path, callback) ###
<code>  
Move the app from the given directory to the Trash.  
  
</code>