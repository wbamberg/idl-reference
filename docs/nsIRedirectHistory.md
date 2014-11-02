---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIRedirectHistory.idl">Source file</a>
</div>
# nsIRedirectHistory #

## Attributes ##

### redirects ###
  
An array of nsIPrincipal that store the redirects associated with this  
channel. This array is filled whether or not the channel has ever been  
opened. The last element of the array is associated with the most recent  
channel.  
  
