---
layout: default
---

# extIApplication #

## id ##

The id of the application.


## name ##

The name of the application.


## version ##

The version number of the application.


## console ##

The console object for the application.


## getExtensions ##

The extensions object for the application. Contains a list
of all installed extensions.


## prefs ##

The preferences object for the application. Defaults to an empty
root branch.


## storage ##

The storage object for the application.


## events ##

The events object for the application.
supports: "load", "ready", "quit", "unload"


## quit ##

Quits the application (if nobody objects to quit-application-requested).
@returns whether quitting will proceed


## restart ##

Restarts the application (if nobody objects to quit-application-requested).
@returns whether restarting will proceed

