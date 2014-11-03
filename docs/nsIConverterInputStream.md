---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/io/nsIConverterInputStream.idl">Source file</a>
</div>

# nsIConverterInputStream #
  
A unichar input stream that wraps an input stream.  
This allows reading unicode strings from a stream, automatically converting  
the bytes from a selected character encoding.  
  

## Methods ##

### init(aStream, aCharset, aBufferSize, aReplacementChar) ###
  
Initialize this stream.  
  

#### Parameters ####

<table>

<tr>
<td>aStream</td>
<td>       The underlying stream to read from.  
</td>
</tr>

<tr>
<td>aCharset</td>
<td>       The character encoding to use for converting the bytes of the  
       stream. A null charset will be interpreted as UTF-8.  
</td>
</tr>

<tr>
<td>aBufferSize</td>
<td>       How many bytes to buffer.  
</td>
</tr>

<tr>
<td>aReplacementChar</td>
<td>       The character to replace unknown byte sequences in the stream  
       with. The standard replacement character is U+FFFD.  
       A value of 0x0000 will cause an exception to be thrown if unknown  
       byte sequences are encountered in the stream.  
</td>
</tr>

</table>

## Constants ##

### DEFAULT_REPLACEMENT_CHARACTER ###
  
Default replacement char value, U+FFFD REPLACEMENT CHARACTER.  
  
