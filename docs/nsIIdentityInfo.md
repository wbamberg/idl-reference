---
layout: default
---

# nsIIdentityInfo #

## Methods ##

### getValidEVPolicyOid ###

This function uses the same test as attribute
  isExtendedValidation

If isExtendedValidation is true, this function will return
a policy identifier in dotted notation (like 1.2.3.4.5).

If isExtendedValidation is false, this function will return
an empty (length string) value.


## Attributes ##

### isExtendedValidation ###

A "true" value means:
  The object that implements this interface uses a certificate that
  was successfully verified as an Extended Validation (EV) cert.
  The test is bound to SSL Server Cert Usage.

