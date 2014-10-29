---
layout: default
---

# nsITokenPasswordDialogs #

nsITokenPasswordDialogs
 This is the interface for setting and changing password
 on a PKCS11 token.


## setPassword ##

setPassword - sets the password/PIN on the named token.
  The canceled output value should be set to TRUE when
  the user (or implementation) cancels the operation.


## getPassword ##
