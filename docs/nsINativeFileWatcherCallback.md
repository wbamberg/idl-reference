---
layout: default
---

# nsINativeFileWatcherCallback #

The interface for the callback invoked when a change on a watched
resource is detected.


## Methods ##

### changed ###

@param resourcePath
       The path of the changed resource. If there were too many changes,
       the string "*" is passed.
@param flags Reserved for future uses, not currently used.

