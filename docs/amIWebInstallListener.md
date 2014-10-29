---
layout: default
---

# amIWebInstallListener #

The registered amIWebInstallListener is used to notify about new installs
triggered by websites. The default implementation displays a confirmation
dialog when add-ons are ready to install and uses the observer service to
notify when installations are blocked.


## Methods ##

### onWebInstallDisabled ###

Called when installation by websites is currently disabled.

@param  aOriginator
        The window or browser that triggered the installs
@param  aUri
        The URI of the site that triggered the installs
@param  aInstalls
        The AddonInstalls that were blocked
@param  aCount
        The number of AddonInstalls


### onWebInstallBlocked ###

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


### onWebInstallRequested ###

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

