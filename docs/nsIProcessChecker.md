---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/base/nsIMessageManager.idl">Source file</a>
</div>

# nsIProcessChecker #

## Methods ##

### killChild() ###

### assertPermission(aPermission) ###
<pre>  
Return true if the "remote" process has |aPermission|.  This is  
intended to be used by JS implementations of cross-process DOM  
APIs, like so  
  
  recvFooRequest: function(message) {  
    if (!message.target.assertPermission("foo")) {  
      return false;  
    }  
    // service foo request  
  
This interface only returns meaningful data when our content is  
in a separate process.  If it shares the same OS process as us,  
then applying this permission check doesn't add any security,  
though it doesn't hurt anything either.  
  
Note: If the remote content process does *not* have |aPermission|,  
it will be killed as a precaution.  
  
</pre>
### assertContainApp(aManifestURL) ###
<pre>  
Return true if the "remote" process has |aManifestURL|.  This is  
intended to be used by JS implementations of cross-process DOM  
APIs, like so  
  
  recvFooRequest: function(message) {  
    if (!message.target.assertContainApp("foo")) {  
      return false;  
    }  
    // service foo request  
  
This interface only returns meaningful data when our content is  
in a separate process.  If it shares the same OS process as us,  
then applying this manifest URL check doesn't add any security,  
though it doesn't hurt anything either.  
  
Note: If the remote content process does *not* contain |aManifestURL|,  
it will be killed as a precaution.  
  
</pre>
### assertAppHasPermission(aPermission) ###

### assertAppHasStatus(aStatus) ###
<pre>  
Return true if the "remote" process' principal has an appStatus equal to  
|aStatus|.  
  
This interface only returns meaningful data when our content is  
in a separate process.  If it shares the same OS process as us,  
then applying this permission check doesn't add any security,  
though it doesn't hurt anything either.  
  
Note: If the remote content process does *not* has the |aStatus|,  
it will be killed as a precaution.  
  
</pre>