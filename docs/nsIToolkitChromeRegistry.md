---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/chrome/nsIToolkitChromeRegistry.idl">Source file</a>
</div>

# nsIToolkitChromeRegistry #

## Methods ##

### checkForOSAccessibility() ###
<pre>  
If the OS has a "high-visibility" or "disabled-friendly" theme set,  
we want to force mozilla into the classic theme, which (for the most part  
obeys the system color/font settings. We cannot do this at initialization,  
because it depends on the toolkit (GTK2) being initialized, which is  
not the case in some embedding situations. Embedders have to manually  
call this method during the startup process.  
  
</pre>
### getLocalesForPackage(aPackage) ###
<pre>  
Get a list of locales available for the specified package.  
  
</pre>