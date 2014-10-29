---
layout: default
---

# nsIVariant #

XPConnect has magic to transparently convert between nsIVariant and JS types.
We mark the interface [scriptable] so that JS can use methods
that refer to this interface. But we mark all the methods and attributes
[noscript] since any nsIVariant object will be automatically converted to a
JS type anyway.


## dataType ##

## getAsInt8 ##

## getAsInt16 ##

## getAsInt32 ##

## getAsInt64 ##

## getAsUint8 ##

## getAsUint16 ##

## getAsUint32 ##

## getAsUint64 ##

## getAsFloat ##

## getAsDouble ##

## getAsBool ##

## getAsChar ##

## getAsWChar ##

## getAsID ##

## getAsAString ##

## getAsDOMString ##

## getAsACString ##

## getAsAUTF8String ##

## getAsString ##

## getAsWString ##

## getAsISupports ##

## getAsJSVal ##

## getAsInterface ##

## getAsArray ##

## getAsStringWithSize ##

## getAsWStringWithSize ##
