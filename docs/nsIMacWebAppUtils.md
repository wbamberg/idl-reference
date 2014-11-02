---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsIMacWebAppUtils.idl">Source file</a>
</div>

# nsIMacWebAppUtils #
  
Allow MozApps API to locate and manipulate natively installed apps  
  

## Methods ##

### pathForAppWithIdentifier(bundleIdentifier) ###
  
Find the path for an app with the given signature.  
  

### launchAppWithIdentifier(bundleIdentifier) ###
  
Launch the app with the given identifier, if it exists.  
  

### trashApp(path, callback) ###
  
Move the app from the given directory to the Trash.  
  
