---
layout: default
---

# nsIUpdate #

An interface that describes an object representing an available update to
the current application - this update may have several available patches
from which one must be selected to download and install, for example we
might select a binary difference patch first and attempt to apply that,
then if the application process fails fall back to downloading a complete
file-replace patch. This object also contains information about the update
that the front end and other application services can use to learn more
about what is going on.


## Methods ##

### getPatchAt ###

Retrieves a patch.
@param   index
         The index of the patch to retrieve.
@returns The nsIUpdatePatch at the specified index.


### serialize ###

Serializes this update object into a DOM Element
@param   updates
         The document to serialize into
@returns The DOM Element created by the serialization process


## Attributes ##

### type ###

The type of update:
  "major"  A major new version of the Application
  "minor"  A minor update to the Application (e.g. security update)


### name ###

The name of the update, or "<Application Name> <Update Version>"


### displayVersion ###

The string to display in the user interface for the version. If you want
a real version number use appVersion.


### appVersion ###

The Application version of this update.


### platformVersion ###

The Toolkit version of this update.


### previousAppVersion ###

The Application version prior to the application being updated.


### buildID ###

The Build ID of this update. Used to determine a particular build, down
to the hour, minute and second of its creation. This allows the system
to differentiate between several nightly builds with the same |version|
for example.


### detailsURL ###

The URL to a page which offers details about the content of this
update. Ideally, this page is not the release notes but some other page
that summarizes the differences between this update and the previous,
which also links to the release notes.


### billboardURL ###

The URL to a page that is typically localized to display in the update
prompt.


### licenseURL ###

The URL to a HTML fragment that contains a license for this update. If
this is specified, the user is shown the license file after they choose
to install the update and they must agree to it before the download
commences.


### serviceURL ###

The URL to the Update Service that supplied this update.


### channel ###

The channel used to retrieve this update from the Update Service.


### showPrompt ###

Whether to show the update prompt which requires user confirmation when an
update is found during a background update check. This overrides the
default setting to download the update in the background.


### showNeverForVersion ###

Whether to show the "No Thanks" button in the update prompt. This allows
the user to never receive a notification for that specific update version
again.


### unsupported ###

Whether the update is no longer supported on this system.


### promptWaitTime ###

Allows overriding the default amount of time in seconds before prompting the
user to apply an update. If not specified, the value of
app.update.promptWaitTime will be used.


### isCompleteUpdate ###

Whether or not the update being downloaded is a complete replacement of
the user's existing installation or a patch representing the difference
between the new version and the previous version.


### isSecurityUpdate ###

Whether or not the update is a security update or not. If this is true,
then we present more serious sounding user interface messages to the
user.


### isOSUpdate ###

Whether or not the update being downloaded is an OS update. This is
generally only possible in Gonk right now.


### installDate ###

When the update was installed.


### statusText ###

A message associated with this update, if any.


### selectedPatch ###

The currently selected patch for this update.


### state ###

The state of the selected patch:
  "downloading"        The update is being downloaded.
  "pending"            The update is ready to be applied.
  "pending-service"    The update is ready to be applied with the service.
  "applying"           The update is being applied.
  "applied"            The update is ready to be switched to.
  "applied-os"         The update is OS update and to be installed.
  "applied-service"    The update is ready to be switched to with the service.
  "succeeded"          The update was successfully applied.
  "download-failed"    The update failed to be downloaded.
  "failed"             The update failed to be applied.


### errorCode ###

A numeric error code that conveys additional information about the state
of a failed update or failed certificate attribute check during an update
check. If the update is not in the "failed" state or the certificate
attribute check has not failed the value is zero.

TODO: Define typical error codes (for now, see updater/errors.h and the
      CERT_ATTR_CHECK_FAILED_* values in nsUpdateService.js)


### patchCount ###

The number of patches supplied by this update.

