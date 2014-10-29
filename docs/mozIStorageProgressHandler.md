---
layout: default
---

# mozIStorageProgressHandler #

mozIProgressHandler is to be implemented by storage consumers that
wish to receive callbacks during the request execution.


## onProgress ##

onProgress is invoked periodically during long running calls.

@param aConnection    connection, for which progress handler is
                      invoked.

@return true to abort request, false to continue work.

