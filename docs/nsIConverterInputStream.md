---
layout: default
---

# nsIConverterInputStream #
  
A unichar input stream that wraps an input stream.  
This allows reading unicode strings from a stream, automatically converting  
the bytes from a selected character encoding.  
  

## Methods ##

### init(aStream, aCharset, aBufferSize, aReplacementChar) ###
  
Initialize this stream.  
@param aStream   
       The underlying stream to read from.  
@param aCharset  
       The character encoding to use for converting the bytes of the  
       stream. A null charset will be interpreted as UTF-8.  
@param aBufferSize  
       How many bytes to buffer.  
@param aReplacementChar  
       The character to replace unknown byte sequences in the stream  
       with. The standard replacement character is U+FFFD.  
       A value of 0x0000 will cause an exception to be thrown if unknown  
       byte sequences are encountered in the stream.  
  

## Constants ##

### DEFAULT_REPLACEMENT_CHARACTER ###
  
Default replacement char value, U+FFFD REPLACEMENT CHARACTER.  
  
