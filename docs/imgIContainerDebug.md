---
layout: default
---

# imgIContainerDebug #

This interface is used in debug builds (and only there) in
order to let automatic tests running JavaScript access
internal state of imgContainers. This lets us test
things like animation.


## framesNotified ##

The # of frames this imgContainer has been notified about.
That is equal to the # of times the animation timer has
fired, and is usually equal to the # of frames actually
drawn (but actual drawing might be disabled).

