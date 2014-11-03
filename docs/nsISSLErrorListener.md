---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/security/manager/ssl/public/nsISSLErrorListener.idl">Source file</a>
</div>

# nsISSLErrorListener #
  
A mechanism to report a broken SSL connection. The recipient should NOT block.  
  

## Methods ##

### notifySSLError(socketInfo, error, targetSite) ###
  
 @param socketInfo A network communication context that can be used to obtain more information  
                   about the active connection.  
 @param error The code associated with the error.  
 @param targetSite The Site name that was used to open the current connection.  
  
 @return The consumer shall return true if it wants to suppress the error message  
         related to the error (the connection will still get canceled).  
  

#### Parameters ####

<table>

<tr>
<td>socketInfo</td>
<td>A network communication context that can be used to obtain more information  
                   about the active connection.  
</td>
</tr>

<tr>
<td>error</td>
<td>The code associated with the error.  
</td>
</tr>

<tr>
<td>targetSite</td>
<td>The Site name that was used to open the current connection.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The consumer shall return true if it wants to suppress the error message  
         related to the error (the connection will still get canceled).  
</td>
</tr>

</table>
