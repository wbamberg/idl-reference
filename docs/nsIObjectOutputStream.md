---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/io/nsIObjectOutputStream.idl">Source file</a>
</div>

# nsIObjectOutputStream #
<code>  
@See nsIObjectInputStream  
@See nsIBinaryOutputStream  
  
</code>
## Methods ##

### writeObject(aObject, aIsStrongRef) ###
<code>  
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
  
</code>
### writeSingleRefObject(aObject) ###
<code>  
Write an object referenced singly and strongly via its root nsISupports  
or a subclass of its root nsISupports.  There must not be other refs to  
aObject in memory, or in the serialization.  
  
</code>
### writeCompoundObject(aObject, aIID, aIsStrongRef) ###
<code>  
Write the object referenced by an interface pointer at aObject that  
inherits from a non-primary nsISupports, i.e., a reference to one of  
the multiply inherited interfaces derived from an nsISupports other  
than the root or XPCOM-identity nsISupports; or a reference to an  
inner object in the case of true XPCOM aggregation.  aIID identifies  
this interface.  
  
</code>
### writeID(aID) ###

### getBuffer(aLength, aAlignMask) ###
<code>  
Optimized serialization support -- see nsIStreamBufferAccess.idl.  
  
</code>
### putBuffer(aBuffer, aLength) ###
