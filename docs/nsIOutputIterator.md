---
layout: default
---

# nsIOutputIterator #

...


## Methods ##

### putElement ###

Put |anElementToPut| into the underlying container or sequence at the position currently pointed to by this iterator.
The iterator and the underlying container or sequence cooperate to |Release()|
the replaced element, if any and if necessary, and to |AddRef()| the new element.

The result is undefined if this iterator currently points outside the
useful range of the underlying container or sequence.

@param anElementToPut the element to place into the underlying container or sequence


### stepForward ###

Advance this iterator to the next position in the underlying container or sequence.

