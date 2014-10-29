---
layout: default
---

# nsIDownloadManagerUI #

## REASON_USER_INTERACTED ##

The reason that should be passed when the user requests to show the
download manager's UI.


## REASON_NEW_DOWNLOAD ##

The reason that should be passed to the show method when we are displaying
the UI because a new download is being added to it.


## show ##

Shows the Download Manager's UI to the user.

@param [optional] aWindowContext
       The parent window context to show the UI.
@param [optional] aDownload
       The download to be preselected upon opening.
@param [optional] aReason
       The reason to show the download manager's UI.  This defaults to
       REASON_USER_INTERACTED, and should be one of the previously listed
       constants.
@param [optional] aUsePrivateUI
       Pass true as this argument to hint to the implementation that it
       should only display private downloads in the UI, if possible.


## visible ##

Indicates if the UI is visible or not.


## getAttention ##

Brings attention to the UI if it is already visible

@throws NS_ERROR_UNEXPECTED if the UI is not visible.

