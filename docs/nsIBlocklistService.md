---
layout: default
---

# nsIBlocklistService #

## Methods ##

### isAddonBlocklisted ###

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


### getAddonBlocklistState ###

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


### getPluginBlocklistState ###

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


### getAddonBlocklistURL ###

Determine the blocklist web page of an add-on.
@param   addon
         The addon item whose url is required.
@returns The URL of the description page.


### getPluginBlocklistURL ###

Determine the blocklist web page of a plugin.
@param   plugin
         The blocked plugin that we are determining the web page for.
@returns The URL of the description page.


### getPluginInfoURL ###

Determine the blocklist infoURL of a plugin.
@param   plugin
         The blocked plugin that we are determining the infoURL for.
@returns The preferred URL to present the user, or |null| if
         it is not available.


## Constants ##

### STATE_NOT_BLOCKED ###

### STATE_SOFTBLOCKED ###

### STATE_BLOCKED ###

### STATE_OUTDATED ###

### STATE_VULNERABLE_UPDATE_AVAILABLE ###

### STATE_VULNERABLE_NO_UPDATE ###
