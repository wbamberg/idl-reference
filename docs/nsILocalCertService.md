---
layout: default
---

# nsILocalCertService #

## getOrCreateCert ##

Get or create a new self-signed X.509 cert to represent this device over a
secure transport, like TLS.

The cert is stored permanently in the profile's key store after first use,
and is valid for 1 year.  If an expired or otherwise invalid cert is found
with the nickname supplied here, it is removed and a new one is made.

@param nickname Nickname that identifies the cert
@param cb       Callback to be notified with the result


## removeCert ##

Remove a X.509 cert with the given nickname.

@param nickname Nickname that identifies the cert
@param cb       Callback to be notified with the result


## loginPromptRequired ##

Whether calling |getOrCreateCert| or |removeCert| will trigger a login
prompt to be displayed.  Generally this happens if the user has set a
master password, but has not yet logged in.

