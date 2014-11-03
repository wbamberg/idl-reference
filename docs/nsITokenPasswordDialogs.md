---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/security/manager/ssl/public/nsITokenPasswordDialogs.idl">Source file</a>
</div>

# nsITokenPasswordDialogs #
<code>  
nsITokenPasswordDialogs  
 This is the interface for setting and changing password  
 on a PKCS11 token.  
  
</code>
## Methods ##

### setPassword(ctx, tokenName, canceled) ###
<code>  
setPassword - sets the password/PIN on the named token.  
  The canceled output value should be set to TRUE when  
  the user (or implementation) cancels the operation.  
  
</code>
### getPassword(ctx, tokenName, password, canceled) ###
