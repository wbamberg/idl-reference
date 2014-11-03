---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/chrome/nsIChromeRegistry.idl">Source file</a>
</div>

# nsIChromeRegistry #

## Methods ##

### convertChromeURL(aChromeURL) ###
<pre>  
Resolve a chrome URL to an loadable URI using the information in the  
registry. Does not modify aChromeURL.  
  
Chrome URLs are allowed to be specified in "shorthand", leaving the  
"file" portion off. In that case, the URL is expanded to:  
  
  chrome://package/provider/package.ext  
  
where "ext" is:  
  
  "xul" for a "content" package,  
  "css" for a "skin" package, and  
  "dtd" for a "locale" package.  
  
@param aChromeURL the URL that is to be converted.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aChromeURL</td>
<td>the URL that is to be converted.  
</td>
</tr>

</table>

### checkForNewChrome() ###
<pre>  
refresh the chrome list at runtime, looking for new packages/etc  
  
</pre>
### wrappersEnabled(aURI) ###
<pre>  
returns whether XPCNativeWrappers are enabled for aURI.  
  
</pre>
## Constants ##

### NONE ###

### PARTIAL ###

### FULL ###
