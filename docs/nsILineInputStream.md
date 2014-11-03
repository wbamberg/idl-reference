---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/io/nsILineInputStream.idl">Source file</a>
</div>

# nsILineInputStream #

## Methods ##

### readLine(aLine) ###
<pre>  
Read a single line from the stream, where a line is a   
possibly zero length sequence of 8bit chars terminated by a  
CR, LF, CRLF, LFCR, or eof.  
The line terminator is not returned.  
@retval false  
        End of file. This line is the last line of the file  
        (aLine is valid).  
@retval true  
        The file contains further lines.  
@note Do not mix readLine with other read functions.  
      Doing so can cause various problems and is not supported.  
  
</pre>