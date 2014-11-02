---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/mime/nsIMIMEInfo.idl">Source file</a>
</div>

# nsIWebHandlerApp #
  
nsIWebHandlerApp is a web-based handler, as speced by the WhatWG HTML5  
draft.  Currently, only GET-based handlers are supported.  At some point,   
we probably want to work with WhatWG to spec out and implement POST-based  
handlers as well.  
  

## Attributes ##

### uriTemplate ###
  
Template used to construct the URI to GET.  Template is expected to have  
a %s in it, and the escaped URI to be handled is inserted in place of   
that %s, as per the HTML5 spec.  
  
