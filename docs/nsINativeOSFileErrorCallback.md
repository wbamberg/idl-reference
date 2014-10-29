---
layout: default
---

# nsINativeOSFileErrorCallback #

A callback invoked in case of error.


## Methods ##

### complete ###

@param operation The name of the failed operation. Provided to aid
debugging only, may change without notice.
@param OSstatus The OS status of the operation (errno under Unix,
GetLastError under Windows).

