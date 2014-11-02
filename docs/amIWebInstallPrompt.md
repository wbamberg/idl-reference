---
layout: default
---

# amIWebInstallPrompt #
  
amIWebInstallPrompt is used, if available, by the default implementation of   
amIWebInstallInfo to display a confirmation UI to the user before running  
installs.  
  

## Methods ##

### confirm(aWindow, aUri, aInstalls, aCount) ###
  
Get a confirmation that the user wants to start the installs.  
  
@param  aWindow  
        The window that triggered the installs  
@param  aUri  
        The URI of the site that triggered the installs  
@param  aInstalls  
        The AddonInstalls that were requested  
@param  aCount  
        The number of AddonInstalls  
  

#### Parameters ####

<table>

<tr>
<td>aWindow</td>
<td>        The window that triggered the installs  
</td>
</tr>

<tr>
<td>aUri</td>
<td>        The URI of the site that triggered the installs  
</td>
</tr>

<tr>
<td>aInstalls</td>
<td>        The AddonInstalls that were requested  
</td>
</tr>

<tr>
<td>aCount</td>
<td>        The number of AddonInstalls  
</td>
</tr>

</table>
