---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/plugins/base/nsIPluginHost.idl">Source file</a>
</div>

# nsIPluginHost #

## Methods ##

### reloadPlugins() ###
<pre>  
Causes the plugins directory to be searched again for new plugin   
libraries.  
  
</pre>
### getPluginTags(aPluginCount, aResults) ###

### clearSiteData(plugin, domain, flags, maxAge) ###

### siteHasData(plugin, domain) ###

### registerPlayPreviewMimeType(mimeType, ignoreCTP, redirectURL) ###
<pre>  
Registers the play preview plugin mode for specific mime type  
  
@param mimeType: specifies plugin mime type.  
@param ignoreCTP: if true, the play preview ignores CTP rules, e.g.  
whitelisted websites, will not notify about plugin  
presence in the address bar.  
@param redirectURL: specifies url for the overlay iframe  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>mimeType:</td>
<td>specifies plugin mime type.  
</td>
</tr>

<tr>
<td>ignoreCTP:</td>
<td>if true, the play preview ignores CTP rules, e.g.  
whitelisted websites, will not notify about plugin  
presence in the address bar.  
</td>
</tr>

<tr>
<td>redirectURL:</td>
<td>specifies url for the overlay iframe  
</td>
</tr>

</table>

### unregisterPlayPreviewMimeType(mimeType) ###

### getPlayPreviewInfo(mimeType) ###

### getPermissionStringForType(mimeType) ###

### getPluginTagForType(mimeType) ###
<pre>  
Get the nsIPluginTag for this MIME type. This method works with both  
enabled and disabled/blocklisted plugins, but an enabled plugin will  
always be returned if available.  
  
@throws NS_ERROR_NOT_AVAILABLE if no plugin is available for this MIME  
        type.  
  
</pre>
### getStateForType(mimeType) ###
<pre>  
Get the nsIPluginTag state for this MIME type.  
  
</pre>
### getBlocklistStateForType(aMimeType) ###
<pre>  
Get the blocklist state for a MIME type.  
  
</pre>
## Constants ##

### FLAG_CLEAR_ALL ###

### FLAG_CLEAR_CACHE ###
