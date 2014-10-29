---
layout: default
---

# amIAddonPathService #

This service maps file system paths where add-ons reside to the ID
of the add-on. Paths are added by the add-on manager. They can
looked up by anyone.


## Methods ##

### findAddonId ###

Given a path to a file, return the ID of the add-on that the file belongs
to. Returns an empty string if there is no add-on there. Note that if an
add-on is located at /a/b/c, then looking up the path /a/b/c/d will return
that add-on.


### insertPath ###

Call this function to inform the service that the given file system path is
associated with the given add-on ID.

