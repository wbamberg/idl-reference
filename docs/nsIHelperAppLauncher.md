---
layout: default
---

# nsIHelperAppLauncher #

A helper app launcher is a small object created to handle the launching
of an external application.

Note that cancelling the load via the nsICancelable interface will release
the reference to the launcher dialog.


## Methods ##

### saveToDisk ###

Saves the final destination of the file. Does not actually perform the
save.
NOTE: This will release the reference to the
nsIHelperAppLauncherDialog.


### launchWithApplication ###

Remembers that aApplication should be used to launch this content. Does
not actually launch the application.
NOTE: This will release the reference to the nsIHelperAppLauncherDialog.
@param aApplication nsIFile corresponding to the location of the application to use.
@param aRememberThisPreference TRUE if we should remember this choice.


### saveDestinationAvailable ###

Callback invoked by nsIHelperAppLauncherDialog::promptForSaveToFileAsync
after the user has chosen a file through the File Picker (or dismissed it).
@param aFile The file that was chosen by the user (or null if dialog was dismissed).


### setWebProgressListener ###

The following methods are used by the progress dialog to get or set
information on the current helper app launcher download.
This reference will be released when the download is finished (after the
listener receives the STATE_STOP notification).


## Attributes ##

### MIMEInfo ###

The mime info object associated with the content type this helper app
launcher is currently attempting to load


### source ###

The source uri


### suggestedFileName ###

The suggested name for this file


### targetFile ###

The file we are saving to


### targetFileIsExecutable ###

The executable-ness of the target file


### timeDownloadStarted ###

Time when the download started


### contentLength ###

The download content length, or -1 if the length is not available.

