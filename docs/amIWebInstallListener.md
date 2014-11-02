---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/mozapps/extensions/amIWebInstallListener.idl">Source file</a>
</div>

# amIWebInstallListener #
  
The registered amIWebInstallListener is used to notify about new installs  
triggered by websites. The default implementation displays a confirmation  
dialog when add-ons are ready to install and uses the observer service to  
notify when installations are blocked.  
  

## Methods ##

### onWebInstallDisabled(aOriginator, aUri, aInstalls, aCount) ###
  
Called when installation by websites is currently disabled.  
  
@param  aOriginator  
        The window or browser that triggered the installs  
@param  aUri  
        The URI of the site that triggered the installs  
@param  aInstalls  
        The AddonInstalls that were blocked  
@param  aCount  
        The number of AddonInstalls  
  

#### Parameters ####

<table>

<tr>
<td>aOriginator</td>
<td>        The window or browser that triggered the installs  
</td>
</tr>

<tr>
<td>aUri</td>
<td>        The URI of the site that triggered the installs  
</td>
</tr>

<tr>
<td>aInstalls</td>
<td>        The AddonInstalls that were blocked  
</td>
</tr>

<tr>
<td>aCount</td>
<td>        The number of AddonInstalls  
</td>
</tr>

</table>

### onWebInstallBlocked(aOriginator, aUri, aInstalls, aCount) ###
  
Called when the website is not allowed to directly prompt the user to  
install add-ons.  
  
@param  aWindow  
        The window or browser that triggered the installs  
@param  aUri  
        The URI of the site that triggered the installs  
@param  aInstalls  
        The AddonInstalls that were blocked  
@param  aCount  
        The number of AddonInstalls  
@return true if the caller should start the installs  
  

#### Parameters ####

<table>

<tr>
<td>aWindow</td>
<td>        The window or browser that triggered the installs  
</td>
</tr>

<tr>
<td>aUri</td>
<td>        The URI of the site that triggered the installs  
</td>
</tr>

<tr>
<td>aInstalls</td>
<td>        The AddonInstalls that were blocked  
</td>
</tr>

<tr>
<td>aCount</td>
<td>        The number of AddonInstalls  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>true if the caller should start the installs  
</td>
</tr>

</table>

### onWebInstallRequested(aOriginator, aUri, aInstalls, aCount) ###
  
Called when a website wants to ask the user to install add-ons.  
  
@param  aWindow  
        The window or browser that triggered the installs  
@param  aUri  
        The URI of the site that triggered the installs  
@param  aInstalls  
        The AddonInstalls that were requested  
@param  aCount  
        The number of AddonInstalls  
@return true if the caller should start the installs  
  

#### Parameters ####

<table>

<tr>
<td>aWindow</td>
<td>        The window or browser that triggered the installs  
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

#### Returns ####

<table>

<tr>
<td>true if the caller should start the installs  
</td>
</tr>

</table>
