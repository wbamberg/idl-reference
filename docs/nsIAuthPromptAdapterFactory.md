---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIAuthPromptAdapterFactory.idl">Source file</a>
</div>

# nsIAuthPromptAdapterFactory #
  
An interface for wrapping nsIAuthPrompt interfaces to make  
them usable via an nsIAuthPrompt2 interface.  
  

## Methods ##

### createAdapter(aPrompt) ###
  
Wrap an object implementing nsIAuthPrompt so that it's usable via  
nsIAuthPrompt2.  
  
