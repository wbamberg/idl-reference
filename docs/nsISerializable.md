---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/ds/nsISerializable.idl">Source file</a>
</div>

# nsISerializable #

## Methods ##

### read(aInputStream) ###
<code>  
Initialize the object implementing nsISerializable, which must have  
been freshly constructed via CreateInstance.  All data members that  
can't be set to default values must have been serialized by write,  
and should be read from aInputStream in the same order by this method.  
  
</code>
### write(aOutputStream) ###
<code>  
Serialize the object implementing nsISerializable to aOutputStream, by  
writing each data member that must be recovered later to reconstitute  
a working replica of this object, in a canonical member and byte order,  
to aOutputStream.  
  
NB: a class that implements nsISerializable *must* also implement  
nsIClassInfo, in particular nsIClassInfo::GetClassID.  
  
</code>