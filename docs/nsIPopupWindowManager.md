---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpfe/appshell/nsIPopupWindowManager.idl">Source file</a>
</div>

# nsIPopupWindowManager #

## Methods ##

### testPermission(principal) ###
<pre>  
Test whether a website has permission to show a popup window.  
@param   principal is the principal to be tested  
@return  one of the enumerated permission actions defined above  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>principal</td>
<td>is the principal to be tested  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>one of the enumerated permission actions defined above  
</td>
</tr>

</table>

## Constants ##

### ALLOW_POPUP ###
<pre>  
These values are returned by the testPermission method  
  
</pre>
### DENY_POPUP ###

### ALLOW_POPUP_WITH_PREJUDICE ###
