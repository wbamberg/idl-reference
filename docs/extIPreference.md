---
layout: default
---

# extIPreference #

Interface for accessing a single preference. The data is not cached.
All reads access the current state of the preference.


## name ##

The name of the preference.


## type ##

A string representing the type of preference (String, Boolean, or Number).


## value ##

Get/Set the value of the preference.


## locked ##

Get the locked state of the preference. Set to a boolean value to (un)lock it.


## modified ##

Check if a preference has been modified by the user, or not.


## branch ##

The preference branch that contains this preference.


## events ##

The events object for this preference.
supports: "change"


## reset ##

Resets a preference back to its default values.

