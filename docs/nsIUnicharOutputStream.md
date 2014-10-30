---
layout: default
---

# nsIUnicharOutputStream #
  
An interface that allows writing unicode data.  
  

## Methods ##

### write ###
  
Write a single character to the stream. When writing many characters,  
prefer the string-taking write method.  
  
@retval true The character was written successfully  
@retval false Not all bytes of the character could be written.  
  

### writeString ###
  
Write a string to the stream.  
  
@retval true The string was written successfully  
@retval false Not all bytes of the string could be written.  
  

### flush ###
  
Flush the stream. This finishes the conversion and writes any bytes that  
finish the current byte sequence.  
  
It does NOT flush the underlying stream.  
  
@see nsIUnicodeEncoder::Finish  
  

### close ###
  
Close the stream and free associated resources. This also closes the  
underlying stream.  
  
