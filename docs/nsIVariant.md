---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/ds/nsIVariant.idl">Source file</a>
</div>

# nsIVariant #
  
XPConnect has magic to transparently convert between nsIVariant and JS types.  
We mark the interface [scriptable] so that JS can use methods  
that refer to this interface. But we mark all the methods and attributes  
[noscript] since any nsIVariant object will be automatically converted to a  
JS type anyway.  
  

## Methods ##

### getAsInt8() ###

### getAsInt16() ###

### getAsInt32() ###

### getAsInt64() ###

### getAsUint8() ###

### getAsUint16() ###

### getAsUint32() ###

### getAsUint64() ###

### getAsFloat() ###

### getAsDouble() ###

### getAsBool() ###

### getAsChar() ###

### getAsWChar() ###

### getAsID(retval) ###

### getAsAString() ###

### getAsDOMString() ###

### getAsACString() ###

### getAsAUTF8String() ###

### getAsString() ###

### getAsWString() ###

### getAsISupports() ###

### getAsJSVal() ###

### getAsInterface(iid, iface) ###

### getAsArray(type, iid, count, ptr) ###

### getAsStringWithSize(size, str) ###

### getAsWStringWithSize(size, str) ###

## Attributes ##

### dataType ###
