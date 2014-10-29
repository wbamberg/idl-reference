---
layout: default
---

# nsITLSServerSecurityObserver #

## onHandshakeDone ##

onHandsakeDone

This method is called once the TLS handshake is completed.  This takes
place after |onSocketAccepted| has been called, which typically opens the
streams to keep things moving along. It's important to be aware that the
handshake has not completed at the point that |onSocketAccepted| is called,
so no security verification can be done until this method is called.

