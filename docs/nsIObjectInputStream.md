---
layout: default
---

# nsIObjectInputStream #

@see nsIObjectOutputStream
@see nsIBinaryInputStream


## Methods ##

### readObject ###

Read an object from this stream to satisfy a strong or weak reference
to one of its interfaces.  If the interface was not along the primary
inheritance chain ending in the "root" or XPCOM-identity nsISupports,
readObject will QueryInterface from the deserialized object root to the
correct interface, which was specified when the object was serialized.

@see nsIObjectOutputStream


### readID ###

### getBuffer ###

Optimized deserialization support -- see nsIStreamBufferAccess.idl.


### putBuffer ###
