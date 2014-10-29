---
layout: default
---

# nsIUpdateChecker #

An interface describing an object that knows how to check for updates.


## checkForUpdates ##

Checks for available updates, notifying a listener of the results.
@param   listener
         An object implementing nsIUpdateCheckListener which is notified
         of the results of an update check.
@param   force
         Forces the checker to check for updates, regardless of the
         current value of the user's update settings. This is used by
         any piece of UI that offers the user the imperative option to
         check for updates now, regardless of their update settings.
         force will not work if the system administrator has locked
         the app.update.enabled preference.


## CURRENT_CHECK ##

Constants for the |stopChecking| function that tell the Checker how long
to stop checking:

CURRENT_CHECK:     Stops the current (active) check only
CURRENT_SESSION:   Stops all checking for the current session
ANY_CHECKS:        Stops all checking, any session from now on
                   (disables update checking preferences)


## CURRENT_SESSION ##

## ANY_CHECKS ##

## stopChecking ##

Ends any pending update check.
@param   duration
         A value representing the set of checks to stop doing.

