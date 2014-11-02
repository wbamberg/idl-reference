---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIByteRangeRequest.idl">Source file</a>
</div>

# nsIByteRangeRequest #

## Attributes ##

### isByteRangeRequest ###
   
Returns true IFF this request is a byte range request, otherwise it  
returns false (This is effectively the same as checking to see if   
|startRequest| is zero and |endRange| is the content length.)  
  

### startRange ###
   
Absolute start position in remote file for this request.  
  

### endRange ###
  
Absolute end postion in remote file for this request  
  
