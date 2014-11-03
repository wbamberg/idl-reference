---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/io/nsIObjectInputStream.idl">Source file</a>
</div>

# nsIObjectInputStream #
<code>  
@see nsIObjectOutputStream  
@see nsIBinaryInputStream  
  
</code>
## Methods ##

### readObject(aIsStrongRef) ###
<code>  
Read an object from this stream to satisfy a strong or weak reference  
to one of its interfaces.  If the interface was not along the primary  
inheritance chain ending in the "root" or XPCOM-identity nsISupports,  
readObject will QueryInterface from the deserialized object root to the  
correct interface, which was specified when the object was serialized.  
  
@see nsIObjectOutputStream  
  
</code>
### readID(aID) ###

### getBuffer(aLength, aAlignMask) ###
<code>  
Optimized deserialization support -- see nsIStreamBufferAccess.idl.  
  
</code>
### putBuffer(aBuffer, aLength) ###
