---
layout: default
---

# nsIDialogParamBlock #

An interface to pass strings, integers and nsISupports to a dialog


## GetInt ##
 Get or set an integer to pass.
Index must be in the range 0..7


## SetInt ##

## SetNumberStrings ##
 Set the maximum number of strings to pass. Default is 16.
Use before setting any string (If you want to change it from the default).


## GetString ##
 Get or set an string to pass.
Index starts at 0


## SetString ##

## objects ##

A place where you can store an nsIMutableArray to pass nsISupports 

