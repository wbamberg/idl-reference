---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/mozapps/extensions/amIWebInstaller.idl">Source file</a>
</div>

# amIWebInstaller #
<code>  
This interface is used to allow webpages to start installing add-ons.  
  
</code>
## Methods ##

### isInstallEnabled(aMimetype, aReferer) ###
<code>  
Checks if installation is enabled for a webpage.  
  
@param  aMimetype  
        The mimetype for the add-on to be installed  
@param  referer  
        The URL of the webpage trying to install an add-on  
@return true if installation is enabled  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aMimetype</td>
<td>        The mimetype for the add-on to be installed  
</td>
</tr>

<tr>
<td>referer</td>
<td>        The URL of the webpage trying to install an add-on  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>true if installation is enabled  
</td>
</tr>

</table>

### installAddonsFromWebpage(aMimetype, aOriginator, aReferer, aUris, aHashes, aNames, aIcons, aCallback, aInstallCount) ###
<code>  
Installs an array of add-ons at the request of a webpage  
  
@param  aMimetype  
        The mimetype for the add-ons  
@param  aOriginator  
        If not e10s, the window installing the add-ons, otherwise the  
        browser installing the add-ons.  
@param  aReferer  
        The URI for the webpage installing the add-ons  
@param  aUris  
        The URIs of add-ons to be installed  
@param  aHashes  
        The hashes for the add-ons to be installed  
@param  aNames  
        The names for the add-ons to be installed  
@param  aIcons  
        The icons for the add-ons to be installed  
@param  aCallback  
        An optional callback to notify about installation success and  
        failure  
@param  aInstallCount  
        An optional argument including the number of add-ons to install  
@return true if the installation was successfully started  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aMimetype</td>
<td>        The mimetype for the add-ons  
</td>
</tr>

<tr>
<td>aOriginator</td>
<td>        If not e10s, the window installing the add-ons, otherwise the  
        browser installing the add-ons.  
</td>
</tr>

<tr>
<td>aReferer</td>
<td>        The URI for the webpage installing the add-ons  
</td>
</tr>

<tr>
<td>aUris</td>
<td>        The URIs of add-ons to be installed  
</td>
</tr>

<tr>
<td>aHashes</td>
<td>        The hashes for the add-ons to be installed  
</td>
</tr>

<tr>
<td>aNames</td>
<td>        The names for the add-ons to be installed  
</td>
</tr>

<tr>
<td>aIcons</td>
<td>        The icons for the add-ons to be installed  
</td>
</tr>

<tr>
<td>aCallback</td>
<td>        An optional callback to notify about installation success and  
        failure  
</td>
</tr>

<tr>
<td>aInstallCount</td>
<td>        An optional argument including the number of add-ons to install  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>true if the installation was successfully started  
</td>
</tr>

</table>
