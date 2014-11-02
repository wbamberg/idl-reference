---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/identity/nsIIdentityCryptoService.idl">Source file</a>
</div>
# nsIIdentityKeyGenCallback #
  
This interface provides a JavaScript callback object used to collect the  
nsIIdentityServeKeyPair when the keygen operation is complete  
  
though there is discussion as to whether we need the nsresult,  
we keep it so we can track deeper crypto errors.  
  

## Methods ##

### generateKeyPairFinished(rv, keyPair) ###
