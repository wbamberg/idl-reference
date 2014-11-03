---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/base/nsIMessageManager.idl">Source file</a>
</div>

# nsIFrameScriptLoader #

## Methods ##

### loadFrameScript(aURL, aAllowDelayedLoad, aRunInGlobalScope) ###
<code>  
Load a script in the (remote) frame. aURL must be the absolute URL.  
data: URLs are also supported. For example data:,dump("foo\n");  
If aAllowDelayedLoad is true, script will be loaded when the  
remote frame becomes available. Otherwise the script will be loaded  
only if the frame is already available.  
  
</code>
### removeDelayedFrameScript(aURL) ###
<code>  
Removes aURL from the list of scripts which support delayed load.  
  
</code>
### getDelayedFrameScripts() ###
<code>  
Returns all delayed scripts that will be loaded once a (remote)  
frame becomes available. The return value is a list of pairs  
[<URL>, <WasLoadedInGlobalScope>].  
  
</code>