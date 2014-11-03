---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/ds/nsIVariant.idl">Source file</a>
</div>

# nsIWritableVariant #
<code>  
An object that implements nsIVariant may or may NOT also implement this  
nsIWritableVariant.  
  
If the 'writable' attribute is false then attempts to call any of the 'set'  
methods can be expected to fail. Setting the 'writable' attribute may or  
may not succeed.  
  
  
</code>
## Methods ##

### setAsInt8(aValue) ###

### setAsInt16(aValue) ###

### setAsInt32(aValue) ###

### setAsInt64(aValue) ###

### setAsUint8(aValue) ###

### setAsUint16(aValue) ###

### setAsUint32(aValue) ###

### setAsUint64(aValue) ###

### setAsFloat(aValue) ###

### setAsDouble(aValue) ###

### setAsBool(aValue) ###

### setAsChar(aValue) ###

### setAsWChar(aValue) ###

### setAsID(aValue) ###

### setAsAString(aValue) ###

### setAsDOMString(aValue) ###

### setAsACString(aValue) ###

### setAsAUTF8String(aValue) ###

### setAsString(aValue) ###

### setAsWString(aValue) ###

### setAsISupports(aValue) ###

### setAsInterface(iid, iface) ###

### setAsArray(type, iid, count, ptr) ###

### setAsStringWithSize(size, str) ###

### setAsWStringWithSize(size, str) ###

### setAsVoid() ###

### setAsEmpty() ###

### setAsEmptyArray() ###

### setFromVariant(aValue) ###

## Attributes ##

### writable ###
