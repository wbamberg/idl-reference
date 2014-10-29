---
layout: default
---

# nsIAuthModule #

## Methods ##

### init ###
 Other flags may be defined in the future */

Called to initialize an auth module.  The other methods cannot be called
unless this method succeeds.

@param aServiceName
       the service name, which may be null if not applicable (e.g., for
       NTLM, this parameter should be null).
@param aServiceFlags
       a bitwise-or of the REQ_ flags defined above (pass REQ_DEFAULT
       for default behavior).
@param aDomain
       the authentication domain, which may be null if not applicable.
@param aUsername
       the user's login name
@param aPassword
       the user's password


### getNextToken ###

Called to get the next token in a sequence of authentication steps.

@param aInToken
       A buffer containing the input token (e.g., a challenge from a
       server).  This may be null.
@param aInTokenLength
       The length of the input token.
@param aOutToken
       If getNextToken succeeds, then aOutToken will point to a buffer
       to be sent in response to the server challenge.  The length of
       this buffer is given by aOutTokenLength.  The buffer at aOutToken
       must be recycled with a call to nsMemory::Free.
@param aOutTokenLength
       If getNextToken succeeds, then aOutTokenLength contains the
       length of the buffer (number of bytes) pointed to by aOutToken.


### wrap ###
 
Once a security context has been established through calls to GetNextToken()
it may be used to protect data exchanged between client and server. Calls
to Wrap() are used to protect items of data to be sent to the server.

@param aInToken
       A buffer containing the data to be sent to the server
@param aInTokenLength
       The length of the input token
@param confidential
       If set to true, Wrap() will encrypt the data, otherwise data will
       just be integrity protected (checksummed)
@param aOutToken
       A buffer containing the resulting data to be sent to the server
@param aOutTokenLength
       The length of the output token buffer

Wrap() may return NS_ERROR_NOT_IMPLEMENTED, if the underlying authentication
mechanism does not support security layers.


### unwrap ###
 
Unwrap() is used to unpack, decrypt, and verify the checksums on data
returned by a server when security layers are in use.

@param aInToken
       A buffer containing the data received from the server
@param aInTokenLength
       The length of the input token
@param aOutToken
       A buffer containing the plaintext data from the server
@param aOutTokenLength
       The length of the output token buffer

Unwrap() may return NS_ERROR_NOT_IMPLEMENTED, if the underlying  
authentication mechanism does not support security layers.


## Constants ##

### REQ_DEFAULT ###

Default behavior.


### REQ_MUTUAL_AUTH ###

Client and server will be authenticated.


### REQ_DELEGATE ###

The server is allowed to impersonate the client.  The REQ_MUTUAL_AUTH
flag may also need to be specified in order for this flag to take
effect.


### REQ_PROXY_AUTH ###

The authentication is required for a proxy connection.


### NTLM_MODULE_SAMBA_AUTH_PROXY ###

Flags used for telemetry.


### NTLM_MODULE_SAMBA_AUTH_DIRECT ###

### NTLM_MODULE_WIN_API_PROXY ###

### NTLM_MODULE_WIN_API_DIRECT ###

### NTLM_MODULE_GENERIC_PROXY ###

### NTLM_MODULE_GENERIC_DIRECT ###

### NTLM_MODULE_KERBEROS_PROXY ###

### NTLM_MODULE_KERBEROS_DIRECT ###
