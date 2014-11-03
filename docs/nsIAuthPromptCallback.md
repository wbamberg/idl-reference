---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIAuthPromptCallback.idl">Source file</a>
</div>

# nsIAuthPromptCallback #
  
Interface for callback methods for the asynchronous nsIAuthPrompt2 method.  
Callers MUST call exactly one method if nsIAuthPrompt2::promptPasswordAsync  
returns successfully. They MUST NOT call any method on this interface before  
promptPasswordAsync returns.  
  

## Methods ##

### onAuthAvailable(aContext, aAuthInfo) ###
  
Authentication information is available.  
  
  
@note  Any exceptions thrown from this method should be ignored.  
  

#### Parameters ####

<table>

<tr>
<td>aContext</td>
<td>       The context as passed to promptPasswordAsync  
</td>
</tr>

<tr>
<td>aAuthInfo</td>
<td>       Authentication information. Must be the same object that was passed  
       to promptPasswordAsync.  
</td>
</tr>

</table>

### onAuthCancelled(aContext, userCancel) ###
  
Notification that the prompt was cancelled.  
  
  

#### Parameters ####

<table>

<tr>
<td>aContext</td>
<td>       The context that was passed to promptPasswordAsync.  
</td>
</tr>

<tr>
<td>userCancel</td>
<td>       If false, this prompt was cancelled by calling the  
       the cancel method on the nsICancelable; otherwise,  
       it was cancelled by the user.  
</td>
</tr>

</table>
