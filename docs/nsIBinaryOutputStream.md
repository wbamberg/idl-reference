---
layout: default
---

# nsIBinaryOutputStream #

This interface allows writing of primitive data types (integers,
floating-point values, booleans, etc.) to a stream in a binary, untagged,
fixed-endianness format.  This might be used, for example, to implement
network protocols or to produce architecture-neutral binary disk files,
i.e. ones that can be read and written by both big-endian and little-endian
platforms.  Output is written in big-endian order (high-order byte first),
as this is traditional network order.

@See nsIBinaryInputStream


## Methods ##

### setOutputStream ###

### writeBoolean ###

Write a boolean as an 8-bit char to the stream.


### write8 ###

### write16 ###

### write32 ###

### write64 ###

### writeFloat ###

### writeDouble ###

### writeStringZ ###

Write an 8-bit pascal style string to the stream.
32-bit length field, followed by length 8-bit chars.


### writeWStringZ ###

Write a 16-bit pascal style string to the stream.
32-bit length field, followed by length PRUnichars.


### writeUtf8Z ###

Write an 8-bit pascal style string (UTF8-encoded) to the stream.
32-bit length field, followed by length 8-bit chars.


### writeBytes ###

Write an opaque byte array to the stream.


### writeByteArray ###

Write an opaque byte array to the stream.

