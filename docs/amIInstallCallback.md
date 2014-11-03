---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/mozapps/extensions/amIWebInstaller.idl">Source file</a>
</div>

# amIInstallCallback #
<code>  
A callback function used to notify webpages when a requested install has  
ended.  
  
NOTE: This is *not* the same as InstallListener.  
  
</code>
## Methods ##

### onInstallEnded(aUrl, aStatus) ###
<code>  
Called when an install completes or fails.  
  
@param  aUrl  
        The url of the add-on being installed  
@param  aStatus  
        0 if the install was successful or negative if not  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aUrl</td>
<td>        The url of the add-on being installed  
</td>
</tr>

<tr>
<td>aStatus</td>
<td>        0 if the install was successful or negative if not  
</td>
</tr>

</table>
