---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsIJumpListItem.idl">Source file</a>
</div>

# nsIJumpListLink #
<code>  
A URI link jump list item.  
  
Note the application must be the registered protocol  
handler for the protocol of the link.  
  
</code>
## Methods ##

### compareHash(uri) ###
<code>  
Compare this item's hash to another uri.  
  
Generates a spec hash of the incoming uri and compares  
it to this item's uri spec hash.  
  
</code>
## Attributes ##

### uri ###
  
Set or get the uri for this link item.  
  

### uriTitle ###
  
Set or get the title for a link item.    
  

### uriHash ###
  
Get a 'privacy safe' unique string hash of the uri's  
spec. Useful in tracking removed items using visible  
data stores such as prefs. Generates an MD5 hash of  
the URI spec using nsICryptoHash.  
  
