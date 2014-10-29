---
layout: default
---

# nsIPluginHost #

## Methods ##

### reloadPlugins ###

Causes the plugins directory to be searched again for new plugin 
libraries.


### getPluginTags ###

### clearSiteData ###

### siteHasData ###

### registerPlayPreviewMimeType ###

Registers the play preview plugin mode for specific mime type

@param mimeType: specifies plugin mime type.
@param ignoreCTP: if true, the play preview ignores CTP rules, e.g.
whitelisted websites, will not notify about plugin
presence in the address bar.
@param redirectURL: specifies url for the overlay iframe


### unregisterPlayPreviewMimeType ###

### getPlayPreviewInfo ###

### getPermissionStringForType ###

### getPluginTagForType ###

Get the nsIPluginTag for this MIME type. This method works with both
enabled and disabled/blocklisted plugins, but an enabled plugin will
always be returned if available.

@throws NS_ERROR_NOT_AVAILABLE if no plugin is available for this MIME
        type.


### getStateForType ###

Get the nsIPluginTag state for this MIME type.


### getBlocklistStateForType ###

Get the blocklist state for a MIME type.


## Constants ##

### FLAG_CLEAR_ALL ###

### FLAG_CLEAR_CACHE ###
