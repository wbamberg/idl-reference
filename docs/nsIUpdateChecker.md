---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/mozapps/update/nsIUpdateService.idl">Source file</a>
</div>

# nsIUpdateChecker #
  
An interface describing an object that knows how to check for updates.  
  

## Methods ##

### checkForUpdates(listener, force) ###
  
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
  

#### Parameters ####

<table>

<tr>
<td>listener</td>
<td>         An object implementing nsIUpdateCheckListener which is notified  
         of the results of an update check.  
</td>
</tr>

<tr>
<td>force</td>
<td>         Forces the checker to check for updates, regardless of the  
         current value of the user's update settings. This is used by  
         any piece of UI that offers the user the imperative option to  
         check for updates now, regardless of their update settings.  
         force will not work if the system administrator has locked  
         the app.update.enabled preference.  
</td>
</tr>

</table>

### stopChecking(duration) ###
  
Ends any pending update check.  
@param   duration  
         A value representing the set of checks to stop doing.  
  

#### Parameters ####

<table>

<tr>
<td>duration</td>
<td>         A value representing the set of checks to stop doing.  
</td>
</tr>

</table>

## Constants ##

### CURRENT_CHECK ###
  
Constants for the |stopChecking| function that tell the Checker how long  
to stop checking:  
  
CURRENT_CHECK:     Stops the current (active) check only  
CURRENT_SESSION:   Stops all checking for the current session  
ANY_CHECKS:        Stops all checking, any session from now on  
                   (disables update checking preferences)  
  

### CURRENT_SESSION ###

### ANY_CHECKS ###
