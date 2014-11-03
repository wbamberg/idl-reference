---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/security/manager/boot/public/nsISecurityWarningDialogs.idl">Source file</a>
</div>

# nsISecurityWarningDialogs #
<pre>  
Functions that display warnings for transitions between secure  
and insecure pages, posts to insecure servers etc.  
  
</pre>
## Methods ##

### confirmPostToInsecureFromSecure(ctx) ###
<pre>  
 Inform the user: Although the currently displayed  
 page was loaded using a secure connection, and the UI probably  
 currently indicates a secure page,   
 that information is being submitted to an insecure page.  
  
 @param ctx A user interface context.  
  
 @return true if the user confirms to submit.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>ctx</td>
<td>A user interface context.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>true if the user confirms to submit.  
</td>
</tr>

</table>
