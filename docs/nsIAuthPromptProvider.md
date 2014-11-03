---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIAuthPromptProvider.idl">Source file</a>
</div>

# nsIAuthPromptProvider #

## Methods ##

### getAuthPrompt(aPromptReason, iid, result) ###
<pre>  
Request a prompt interface for the given prompt reason;  
@throws NS_ERROR_NOT_AVAILABLE if no prompt is allowed or  
available for the given reason.  
  
@param aPromptReason   The reason for the auth prompt;  
                       one of #PROMPT_NORMAL or #PROMPT_PROXY  
@param iid             The desired interface, e.g.  
                       NS_GET_IID(nsIAuthPrompt2).  
@returns an nsIAuthPrompt2 interface, or throws NS_ERROR_NOT_AVAILABLE  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aPromptReason</td>
<td>The reason for the auth prompt;  
                       one of #PROMPT_NORMAL or #PROMPT_PROXY  
</td>
</tr>

<tr>
<td>iid</td>
<td>The desired interface, e.g.  
                       NS_GET_IID(nsIAuthPrompt2).  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>an nsIAuthPrompt2 interface, or throws NS_ERROR_NOT_AVAILABLE  
</td>
</tr>

</table>

## Constants ##

### PROMPT_NORMAL ###
<pre>  
Normal (non-proxy) prompt request.  
  
</pre>
### PROMPT_PROXY ###
<pre>  
Proxy auth request.  
  
</pre>