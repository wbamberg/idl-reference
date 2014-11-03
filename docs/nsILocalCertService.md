---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/devtools/security/nsILocalCertService.idl">Source file</a>
</div>

# nsILocalCertService #

## Methods ##

### getOrCreateCert(nickname, cb) ###
<code>  
Get or create a new self-signed X.509 cert to represent this device over a  
secure transport, like TLS.  
  
The cert is stored permanently in the profile's key store after first use,  
and is valid for 1 year.  If an expired or otherwise invalid cert is found  
with the nickname supplied here, it is removed and a new one is made.  
  
@param nickname Nickname that identifies the cert  
@param cb       Callback to be notified with the result  
  
</code>
#### Parameters ####

<table>

<tr>
<td>nickname</td>
<td>Nickname that identifies the cert  
</td>
</tr>

<tr>
<td>cb</td>
<td>Callback to be notified with the result  
</td>
</tr>

</table>

### removeCert(nickname, cb) ###
<code>  
Remove a X.509 cert with the given nickname.  
  
@param nickname Nickname that identifies the cert  
@param cb       Callback to be notified with the result  
  
</code>
#### Parameters ####

<table>

<tr>
<td>nickname</td>
<td>Nickname that identifies the cert  
</td>
</tr>

<tr>
<td>cb</td>
<td>Callback to be notified with the result  
</td>
</tr>

</table>

## Attributes ##

### loginPromptRequired ###
  
Whether calling |getOrCreateCert| or |removeCert| will trigger a login  
prompt to be displayed.  Generally this happens if the user has set a  
master password, but has not yet logged in.  
  
