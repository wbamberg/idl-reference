---
layout: default
---

# nsIProfileLock #

Hold on to a profile lock. Once you release the last reference to this
interface, the profile lock is released.


## Methods ##

### unlock ###

Unlock the profile.


## Attributes ##

### directory ###

The main profile directory.


### localDirectory ###

A directory corresponding to the main profile directory that exists for
the purpose of storing data on the local filesystem, including cache
files or other data files that may not represent critical user data.
(e.g., this directory may not be included as part of a backup scheme.)

In some cases, this directory may just be the main profile directory.


### replacedLockTime ###

The timestamp of an existing profile lock at lock time.

