---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/system/nsIBlocklistService.idl">Source file</a>
</div>
# nsIBlocklistService #

## Methods ##

### isAddonBlocklisted(addon, appVersion, toolkitVersion) ###
  
Determine if an item is blocklisted  
@param   addon  
         The addon item to be checked.  
@param   appVersion  
         The version of the application we are checking in the blocklist.  
         If this parameter is null, the version of the running application  
         is used.  
@param   toolkitVersion  
         The version of the toolkit we are checking in the blocklist.  
         If this parameter is null, the version of the running toolkit  
         is used.  
@returns true if the item is compatible with this version of the  
         application or this version of the toolkit, false, otherwise.  
  

#### Parameters ####

<table>

<tr>
<td>addon</td>
<td>         The addon item to be checked.  
</td>
</tr>

<tr>
<td>appVersion</td>
<td>         The version of the application we are checking in the blocklist.  
         If this parameter is null, the version of the running application  
         is used.  
</td>
</tr>

<tr>
<td>toolkitVersion</td>
<td>         The version of the toolkit we are checking in the blocklist.  
         If this parameter is null, the version of the running toolkit  
         is used.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>true if the item is compatible with this version of the  
         application or this version of the toolkit, false, otherwise.  
</td>
</tr>

</table>

### getAddonBlocklistState(addon, appVersion, toolkitVersion) ###
  
Determine the blocklist state of an add-on  
@param   id  
         The addon item to be checked.  
@param   appVersion  
         The version of the application we are checking in the blocklist.  
         If this parameter is null, the version of the running application  
         is used.  
@param   toolkitVersion  
         The version of the toolkit we are checking in the blocklist.  
         If this parameter is null, the version of the running toolkit  
         is used.  
@returns The STATE constant.  
  

#### Parameters ####

<table>

<tr>
<td>id</td>
<td>         The addon item to be checked.  
</td>
</tr>

<tr>
<td>appVersion</td>
<td>         The version of the application we are checking in the blocklist.  
         If this parameter is null, the version of the running application  
         is used.  
</td>
</tr>

<tr>
<td>toolkitVersion</td>
<td>         The version of the toolkit we are checking in the blocklist.  
         If this parameter is null, the version of the running toolkit  
         is used.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The STATE constant.  
</td>
</tr>

</table>

### getPluginBlocklistState(plugin, appVersion, toolkitVersion) ###
  
Determine the blocklist state of a plugin  
@param   plugin  
         The plugin to get the state for  
@param   appVersion  
         The version of the application we are checking in the blocklist.  
         If this parameter is null, the version of the running application  
         is used.  
@param   toolkitVersion  
         The version of the toolkit we are checking in the blocklist.  
         If this parameter is null, the version of the running toolkit  
         is used.  
@returns The STATE constant.  
  

#### Parameters ####

<table>

<tr>
<td>plugin</td>
<td>         The plugin to get the state for  
</td>
</tr>

<tr>
<td>appVersion</td>
<td>         The version of the application we are checking in the blocklist.  
         If this parameter is null, the version of the running application  
         is used.  
</td>
</tr>

<tr>
<td>toolkitVersion</td>
<td>         The version of the toolkit we are checking in the blocklist.  
         If this parameter is null, the version of the running toolkit  
         is used.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The STATE constant.  
</td>
</tr>

</table>

### getAddonBlocklistURL(addon, appVersion, toolkitVersion) ###
  
Determine the blocklist web page of an add-on.  
@param   addon  
         The addon item whose url is required.  
@returns The URL of the description page.  
  

#### Parameters ####

<table>

<tr>
<td>addon</td>
<td>         The addon item whose url is required.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The URL of the description page.  
</td>
</tr>

</table>

### getPluginBlocklistURL(plugin) ###
  
Determine the blocklist web page of a plugin.  
@param   plugin  
         The blocked plugin that we are determining the web page for.  
@returns The URL of the description page.  
  

#### Parameters ####

<table>

<tr>
<td>plugin</td>
<td>         The blocked plugin that we are determining the web page for.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The URL of the description page.  
</td>
</tr>

</table>

### getPluginInfoURL(plugin) ###
  
Determine the blocklist infoURL of a plugin.  
@param   plugin  
         The blocked plugin that we are determining the infoURL for.  
@returns The preferred URL to present the user, or |null| if  
         it is not available.  
  

#### Parameters ####

<table>

<tr>
<td>plugin</td>
<td>         The blocked plugin that we are determining the infoURL for.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The preferred URL to present the user, or |null| if  
         it is not available.  
</td>
</tr>

</table>

## Constants ##

### STATE_NOT_BLOCKED ###

### STATE_SOFTBLOCKED ###

### STATE_BLOCKED ###

### STATE_OUTDATED ###

### STATE_VULNERABLE_UPDATE_AVAILABLE ###

### STATE_VULNERABLE_NO_UPDATE ###
