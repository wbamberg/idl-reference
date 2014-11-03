---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/io/nsIObjectInputStream.idl">Source file</a>
</div>

# nsIObjectInputStream #
<pre>  
@see nsIObjectOutputStream  
@see nsIBinaryInputStream  
  
</pre>
## Methods ##

### readObject(aIsStrongRef) ###
<pre>  
Read an object from this stream to satisfy a strong or weak reference  
to one of its interfaces.  If the interface was not along the primary  
inheritance chain ending in the "root" or XPCOM-identity nsISupports,  
readObject will QueryInterface from the deserialized object root to the  
correct interface, which was specified when the object was serialized.  
  
@see nsIObjectOutputStream  
  
</pre>
### readID(aID) ###

### getBuffer(aLength, aAlignMask) ###
<pre>  
Optimized deserialization support -- see nsIStreamBufferAccess.idl.  
  
</pre>
### putBuffer(aBuffer, aLength) ###
