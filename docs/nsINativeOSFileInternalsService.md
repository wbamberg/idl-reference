---
layout: default
---

# nsINativeOSFileInternalsService #

A service providing native implementations of some of the features
of OS.File.


## read ##

Implementation of OS.File.read

@param path The absolute path to the file to read.
@param options An object that may contain some of the following fields
- {number} bytes The maximal number of bytes to read.
- {string} encoding If provided, return the result as a string, decoded
  using this encoding. Otherwise, pass the result as an ArrayBuffer.
  Invalid encodings cause onError to be called with the platform-specific
  "invalid argument" constant.
- {string} compression Unimplemented at the moment.
@param onSuccess The success callback.
@param onError The error callback.

