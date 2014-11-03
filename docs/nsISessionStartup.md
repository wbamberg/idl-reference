---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/browser/components/sessionstore/nsISessionStartup.idl">Source file</a>
</div>

# nsISessionStartup #
  
nsISessionStore keeps track of the current browsing state - i.e.  
tab history, cookies, scroll state, form data, and window features  
- and allows to restore everything into one window.  
  

## Methods ##

### doRestore() ###
  
Determines whether there is a pending session restore. Should only be  
called after initialization has completed.  
  

### isAutomaticRestoreEnabled() ###
  
Determines whether automatic session restoration is enabled for this  
launch of the browser. This does not include crash restoration, and will  
return false if restoration will only be caused by a crash.  
  

## Attributes ##

### onceInitialized ###
  
Return a promise that is resolved once initialization  
is complete.  
  

### state ###

### willOverrideHomepage ###
  
Returns whether we will restore a session that ends up replacing the  
homepage. The browser uses this to not start loading the homepage if  
we're going to stop its load anyway shortly after.  
  
This is meant to be an optimization for the average case that loading the  
session file finishes before we may want to start loading the default  
homepage. Should this be called before the session file has been read it  
will just return false.  
  

### sessionType ###

### previousSessionCrashed ###

## Constants ##

### NO_SESSION ###
  
What type of session we're restoring.  
NO_SESSION       There is no data available from the previous session  
RECOVER_SESSION  The last session crashed. It will either be restored or  
                 about:sessionrestore will be shown.  
RESUME_SESSION   The previous session should be restored at startup  
DEFER_SESSION    The previous session is fine, but it shouldn't be restored  
                 without explicit action (with the exception of pinned tabs)  
  

### RECOVER_SESSION ###

### RESUME_SESSION ###

### DEFER_SESSION ###
