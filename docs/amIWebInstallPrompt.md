---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/mozapps/extensions/amIWebInstallListener.idl">Source file</a>
</div>

# amIWebInstallPrompt #
<pre>  
amIWebInstallPrompt is used, if available, by the default implementation of   
amIWebInstallInfo to display a confirmation UI to the user before running  
installs.  
  
</pre>
## Methods ##

### confirm(aWindow, aUri, aInstalls, aCount) ###
<pre>  
Get a confirmation that the user wants to start the installs.  
  
@param  aWindow  
        The window that triggered the installs  
@param  aUri  
        The URI of the site that triggered the installs  
@param  aInstalls  
        The AddonInstalls that were requested  
@param  aCount  
        The number of AddonInstalls  
  
</pre>
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
