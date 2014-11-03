---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/chrome/nsIChromeRegistry.idl">Source file</a>
</div>

# nsIXULChromeRegistry #

## Methods ##

### reloadChrome() ###

### getSelectedLocale(packageName) ###

### isLocaleRTL(package) ###

### refreshSkins() ###

### allowScriptsForPackage(url) ###
<pre>  
Installable skin XBL is not always granted the same privileges as other  
chrome. This asks the chrome registry whether scripts are allowed to be  
run for a particular chrome URI. Do not pass non-chrome URIs to this  
method.  
  
</pre>
### allowContentToAccess(url) ###
<pre>  
Content should only be allowed to load chrome JS from certain packages.  
This method reflects the contentaccessible flag on packages.  
Do not pass non-chrome URIs to this method.  
  
</pre>