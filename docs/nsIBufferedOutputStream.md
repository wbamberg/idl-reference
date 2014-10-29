---
layout: default
---

# nsIBufferedOutputStream #

An output stream that stores up data to write out to another output stream
and does the entire write only when the buffer is full, so that fewer writes
to the underlying output stream are necessary.


## Methods ##

### init ###

@param sinkToStream - add buffering to this stream
@param bufferSize   - specifies the maximum buffer size

