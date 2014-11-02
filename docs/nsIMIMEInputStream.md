---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIMIMEInputStream.idl">Source file</a>
</div>

# nsIMIMEInputStream #
  
The MIME stream separates headers and a datastream. It also allows  
automatic creation of the content-length header.  
  

## Methods ##

### addHeader(name, value) ###
  
Adds an additional header to the stream on the form "name: value". May  
not be called once the stream has been started to be read.  
@param name   name of the header  
@param value  value of the header  
  

#### Parameters ####

<table>

<tr>
<td>name</td>
<td>name of the header  
</td>
</tr>

<tr>
<td>value</td>
<td>value of the header  
</td>
</tr>

</table>

### setData(stream) ###
  
Sets data-stream. May not be called once the stream has been started  
to be read.  
The cursor of the new stream should be located at the beginning of the  
stream if the implementation of the nsIMIMEInputStream also is used as  
an nsISeekableStream.  
@param stream  stream containing the data for the stream  
  

#### Parameters ####

<table>

<tr>
<td>stream</td>
<td>stream containing the data for the stream  
</td>
</tr>

</table>

## Attributes ##

### addContentLength ###
  
When true a "Content-Length" header is automatically added to the  
stream. The value of the content-length is automatically calculated  
using the available() method on the data stream. The value is  
recalculated every time the stream is rewinded to the start.  
Not allowed to be changed once the stream has been started to be read.  
  
