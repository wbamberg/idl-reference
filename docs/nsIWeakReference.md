---
layout: default
---

# nsIWeakReference #

An instance of |nsIWeakReference| is a proxy object that cooperates with
its referent to give clients a non-owning, non-dangling reference.  Clients
own the proxy, and should generally manage it with an |nsCOMPtr| (see the
type |nsWeakPtr| for a |typedef| name that stands out) as they would any
other XPCOM object.  The |QueryReferent| member function provides a
(hopefully short-lived) owning reference on demand, through which clients
can get useful access to the referent, while it still exists.

@version 1.0
@see nsISupportsWeakReference
@see nsWeakReference
@see nsWeakPtr


## Methods ##

### QueryReferent ###

|QueryReferent| queries the referent, if it exists, and like |QueryInterface|, produces
an owning reference to the desired interface.  It is designed to look and act exactly
like (a proxied) |QueryInterface|.  Don't hold on to the produced interface permanently;
that would defeat the purpose of using a non-owning |nsIWeakReference| in the first place.

