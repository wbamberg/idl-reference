---
layout: default
---

# nsIBufferedInputStream #

An input stream that reads ahead and keeps a buffer coming from another input
stream so that fewer accesses to the underlying stream are necessary.


## Methods ##

### init ###

@param fillFromStream - add buffering to this stream
@param bufferSize     - specifies the maximum buffer size

