---
layout: default
---

# nsISyncStreamListener #

## inputStream ##

Returns an input stream that when read will fetch data delivered to the
sync stream listener.  The nsIInputStream implementation will wait for
OnDataAvailable events before returning from Read.

NOTE: Reading from the returned nsIInputStream may spin the current
thread's event queue, which could result in any event being processed.

