---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpfe/appshell/nsIPopupWindowManager.idl">Source file</a>
</div>
# nsIPopupWindowManager #

## Methods ##

### testPermission(principal) ###
  
Test whether a website has permission to show a popup window.  
@param   principal is the principal to be tested  
@return  one of the enumerated permission actions defined above  
  

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
  
These values are returned by the testPermission method  
  

### DENY_POPUP ###

### ALLOW_POPUP_WITH_PREJUDICE ###
