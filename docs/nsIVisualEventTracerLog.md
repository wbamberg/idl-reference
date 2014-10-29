---
layout: default
---

# nsIVisualEventTracerLog #

## JSONString ##

JSON string of the log.  Use JSON.parse to get it as an object.


## writeToProfilingFile ##

Write the JSON string returned by JSONString to the log defined by
the environment variable MOZ_PROFILING_FILE.

