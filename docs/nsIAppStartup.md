---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/startup/public/nsIAppStartup.idl">Source file</a>
</div>

# nsIAppStartup #

## Methods ##

### createHiddenWindow() ###
  
Create the hidden window.  
  

### destroyHiddenWindow() ###
  
Destroys the hidden window. This will have no effect if the hidden window  
has not yet been created.  
  

### run() ###
  
Runs an application event loop: normally the main event pump which  
defines the lifetime of the application. If there are no windows open  
and no outstanding calls to enterLastWindowClosingSurvivalArea this  
method will exit immediately.  
  
@returnCode NS_SUCCESS_RESTART_APP  
            This return code indicates that the application should be  
            restarted because quit was called with the eRestart flag.  
  
@returnCode NS_SUCCESS_RESTART_METRO_APP  
            This return code indicates that the application should be  
            restarted in metro because quit was called with the  
            eRestartTouchEnviroment flag.  
  
@returnCode NS_SUCCESS_RESTART_APP_NOT_SAME_PROFILE  
            This return code indicates that the application should be  
            restarted without necessarily using the same profile because  
            quit was called with the eRestartNotSameProfile flag.  
  

#### Returns ####

<table>

<tr>
<td>ode NS_SUCCESS_RESTART_APP_NOT_SAME_PROFILE  
            This return code indicates that the application should be  
            restarted without necessarily using the same profile because  
            quit was called with the eRestartNotSameProfile flag.  
</td>
</tr>

</table>

### enterLastWindowClosingSurvivalArea() ###
  
There are situations where all application windows will be  
closed but we don't want to take this as a signal to quit the  
app. Bracket the code where the last window could close with  
these.  
  

### exitLastWindowClosingSurvivalArea() ###

### restartInSafeMode(aQuitMode) ###
  
Restart the application in safe mode  
@param aQuitMode  
       This parameter modifies how the app is shutdown.  
@see nsIAppStartup::quit  
  

#### Parameters ####

<table>

<tr>
<td>aQuitMode</td>
<td>       This parameter modifies how the app is shutdown.  
@see nsIAppStartup::quit  
</td>
</tr>

</table>

### trackStartupCrashBegin() ###
  
If the last startup crashed then increment a counter.  
Set a flag so on next startup we can detect whether TrackStartupCrashEnd  
was called (and therefore the application crashed).  
@return whether safe mode is necessary  
  

#### Returns ####

<table>

<tr>
<td>whether safe mode is necessary  
</td>
</tr>

</table>

### trackStartupCrashEnd() ###
  
We have succesfully started without crashing. Clear flags that were  
tracking past crashes.  
  

### quit(aMode) ###
  
Exit the event loop, and shut down the app.  
  
@param aMode  
       This parameter modifies how the app is shutdown, and it is  
       constructed from the constants defined above.  
  

#### Parameters ####

<table>

<tr>
<td>aMode</td>
<td>       This parameter modifies how the app is shutdown, and it is  
       constructed from the constants defined above.  
</td>
</tr>

</table>

### doneStartingUp() ###
  
Mark the startup as completed.  
  
Called at the end of startup by nsAppRunner.  
  

### getStartupInfo() ###
   
Returns an object with main, process, firstPaint, sessionRestored properties.  
Properties may not be available depending on platform or application  
  

## Attributes ##

### automaticSafeModeNecessary ###
  
Startup Crash Detection  
  
Keeps track of application startup begining and success using flags to  
determine whether the application is crashing on startup.  
When the number of crashes crosses the acceptable threshold, safe mode  
or other repair procedures are performed.  
  
  
Whether automatic safe mode is necessary at this time.  This gets set  
in trackStartupCrashBegin.  
  
@see trackStartupCrashBegin  
  

### shuttingDown ###
  
True if the application is in the process of shutting down.  
  

### startingUp ###
  
True if the application is in the process of starting up.  
  
Startup is complete once all observers of final-ui-startup have returned.  
  

### restarting ###
  
True if the application is being restarted  
  

### wasRestarted ###
  
True if this is the startup following restart, i.e. if the application  
was restarted using quit(eRestart*).  
  

### restartingTouchEnvironment ###
  
True if the application is being restarted in a touch-optimized  
environment (such as Metro).  
  

### interrupted ###
  
True if startup was interrupted by an interactive prompt.  
  

## Constants ##

### eConsiderQuit ###
  
The following flags may be passed as the aMode parameter to the quit  
method.  One and only one of the "Quit" flags must be specified.  The  
eRestart flag may be bit-wise combined with one of the "Quit" flags to  
cause the application to restart after it quits.  
  
  
Attempt to quit if all windows are closed.  
  

### eAttemptQuit ###
  
Try to close all windows, then quit if successful.  
  

### eForceQuit ###
  
Quit, damnit!  
  

### eRestart ###
  
Restart the application after quitting.  The application will be  
restarted with the same profile and an empty command line.  
  

### eRestarti386 ###
  
When restarting attempt to start in the i386 architecture. Only supported  
on OSX.  
  

### eRestartx86_64 ###
  
When restarting attempt to start in the x86_64 architecture. Only  
supported on OSX.  
  

### eRestartTouchEnvironment ###
  
Restart the application in a touch-optimized environment (such as Metro)  
after quitting. The application will be restarted with the same profile  
and an empty command line.  
  

### eRestartNotSameProfile ###
  
Restart the application after quitting.  The application will be  
restarted with an empty command line and the normal profile selection  
process will take place on startup.  
  
