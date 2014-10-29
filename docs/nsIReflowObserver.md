---
layout: default
---

# nsIReflowObserver #

## Methods ##

### reflow ###

Called when an uninterruptible reflow has occurred.

@param start timestamp when reflow ended, in milliseconds since
             navigationStart (accurate to 1/1000 of a ms)
@param end   timestamp when reflow ended, in milliseconds since
             navigationStart (accurate to 1/1000 of a ms)


### reflowInterruptible ###

Called when an interruptible reflow has occurred.

@param start timestamp when reflow ended, in milliseconds since
             navigationStart (accurate to 1/1000 of a ms)
@param end   timestamp when reflow ended, in milliseconds since
             navigationStart (accurate to 1/1000 of a ms)

