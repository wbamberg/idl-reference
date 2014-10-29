---
layout: default
---

# nsINativeFileWatcherErrorCallback #

The interface for the callback invoked when there is an error.


## complete ##

@param xpcomError The XPCOM error code.
@param osError The native OS error (errno under Unix, GetLastError under Windows).

