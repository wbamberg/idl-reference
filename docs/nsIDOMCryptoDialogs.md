---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/security/manager/ssl/public/nsIDOMCryptoDialogs.idl">Source file</a>
</div>

# nsIDOMCryptoDialogs #

## Methods ##

### ConfirmKeyEscrow(escrowAuthority) ###
  
This method is used to warn the user the web site is  
trying to escrow the generated private key.  This   
method should return true if the user wants to proceed  
and false if the user cancels the action.  
  
