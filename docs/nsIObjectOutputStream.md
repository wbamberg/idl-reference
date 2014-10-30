---
layout: default
---

# nsIObjectOutputStream #
  
@See nsIObjectInputStream  
@See nsIBinaryOutputStream  
  

## Methods ##

### writeObject ###
  
Write the object whose "root" or XPCOM-identity nsISupports is aObject.  
The cause for writing this object is a strong or weak reference, so the  
aIsStrongRef argument must tell which kind of pointer is being followed  
here during serialization.  
  
If the object has only one strong reference in the serialization and no  
weak refs, use writeSingleRefObject.  This is a valuable optimization:  
it saves space in the stream, and cycles on both ends of the process.  
  
If the reference being serialized is a pointer to an interface not on  
the primary inheritance chain ending in the root nsISupports, you must  
call writeCompoundObject instead of this method.  
  

### writeSingleRefObject ###
  
Write an object referenced singly and strongly via its root nsISupports  
or a subclass of its root nsISupports.  There must not be other refs to  
aObject in memory, or in the serialization.  
  

### writeCompoundObject ###
  
Write the object referenced by an interface pointer at aObject that  
inherits from a non-primary nsISupports, i.e., a reference to one of  
the multiply inherited interfaces derived from an nsISupports other  
than the root or XPCOM-identity nsISupports; or a reference to an  
inner object in the case of true XPCOM aggregation.  aIID identifies  
this interface.  
  

### writeID ###

### getBuffer ###
  
Optimized serialization support -- see nsIStreamBufferAccess.idl.  
  

### putBuffer ###
