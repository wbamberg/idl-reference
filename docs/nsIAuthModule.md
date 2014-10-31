---
layout: default
---

# nsIAuthModule #

## Methods ##

### init(aServiceName, aServiceFlags, aDomain, aUsername, aPassword) ###
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
  

#### Parameters ####

<table>

<tr>
<td>aServiceName</td>
<td>       the service name, which may be null if not applicable (e.g., for  
       NTLM, this parameter should be null).  
</td>
</tr>

<tr>
<td>aServiceFlags</td>
<td>       a bitwise-or of the REQ_ flags defined above (pass REQ_DEFAULT  
       for default behavior).  
</td>
</tr>

<tr>
<td>aDomain</td>
<td>       the authentication domain, which may be null if not applicable.  
</td>
</tr>

<tr>
<td>aUsername</td>
<td>       the user's login name  
</td>
</tr>

<tr>
<td>aPassword</td>
<td>       the user's password  
</td>
</tr>

</table>

### getNextToken(aInToken, aInTokenLength, aOutToken, aOutTokenLength) ###
  
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
  

#### Parameters ####

<table>

<tr>
<td>aInToken</td>
<td>       A buffer containing the input token (e.g., a challenge from a  
       server).  This may be null.  
</td>
</tr>

<tr>
<td>aInTokenLength</td>
<td>       The length of the input token.  
</td>
</tr>

<tr>
<td>aOutToken</td>
<td>       If getNextToken succeeds, then aOutToken will point to a buffer  
       to be sent in response to the server challenge.  The length of  
       this buffer is given by aOutTokenLength.  The buffer at aOutToken  
       must be recycled with a call to nsMemory::Free.  
</td>
</tr>

<tr>
<td>aOutTokenLength</td>
<td>       If getNextToken succeeds, then aOutTokenLength contains the  
       length of the buffer (number of bytes) pointed to by aOutToken.  
</td>
</tr>

</table>

### wrap(aInToken, aInTokenLength, confidential, aOutToken, aOutTokenLength) ###
   
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
  

#### Parameters ####

<table>

<tr>
<td>aInToken</td>
<td>       A buffer containing the data to be sent to the server  
</td>
</tr>

<tr>
<td>aInTokenLength</td>
<td>       The length of the input token  
</td>
</tr>

<tr>
<td>confidential</td>
<td>       If set to true, Wrap() will encrypt the data, otherwise data will  
       just be integrity protected (checksummed)  
</td>
</tr>

<tr>
<td>aOutToken</td>
<td>       A buffer containing the resulting data to be sent to the server  
</td>
</tr>

<tr>
<td>aOutTokenLength</td>
<td>       The length of the output token buffer  
</td>
</tr>

</table>

### unwrap(aInToken, aInTokenLength, aOutToken, aOutTokenLength) ###
   
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
  

#### Parameters ####

<table>

<tr>
<td>aInToken</td>
<td>       A buffer containing the data received from the server  
</td>
</tr>

<tr>
<td>aInTokenLength</td>
<td>       The length of the input token  
</td>
</tr>

<tr>
<td>aOutToken</td>
<td>       A buffer containing the plaintext data from the server  
</td>
</tr>

<tr>
<td>aOutTokenLength</td>
<td>       The length of the output token buffer  
</td>
</tr>

</table>

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
