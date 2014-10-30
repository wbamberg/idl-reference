---
layout: default
---

# nsIXULChromeRegistry #

## Methods ##

### reloadChrome ###

### getSelectedLocale ###

### isLocaleRTL ###

### refreshSkins ###

### allowScriptsForPackage ###
  
Installable skin XBL is not always granted the same privileges as other  
chrome. This asks the chrome registry whether scripts are allowed to be  
run for a particular chrome URI. Do not pass non-chrome URIs to this  
method.  
  

### allowContentToAccess ###
  
Content should only be allowed to load chrome JS from certain packages.  
This method reflects the contentaccessible flag on packages.  
Do not pass non-chrome URIs to this method.  
  
