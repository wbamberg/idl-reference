---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/feeds/nsIFeedProcessor.idl">Source file</a>
</div>

# nsIFeedProcessor #
<code>  
An nsIFeedProcessor parses feeds, triggering callbacks based on  
their contents.  
  
</code>
## Methods ##

### parseFromStream(stream, uri) ###
<code>  
Parse a feed from an nsIInputStream.  
  
@param stream The input stream.  
@param uri The base URI.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>stream</td>
<td>The input stream.  
</td>
</tr>

<tr>
<td>uri</td>
<td>The base URI.  
</td>
</tr>

</table>

### parseFromString(str, uri) ###
<code>  
Parse a feed from a string.  
  
@param str The string to parse.  
@param uri The base URI.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>str</td>
<td>The string to parse.  
</td>
</tr>

<tr>
<td>uri</td>
<td>The base URI.  
</td>
</tr>

</table>

### parseAsync(requestObserver, uri) ###
<code>  
Parse a feed asynchronously. The caller must then call the  
nsIFeedProcessor's nsIStreamListener methods to drive the  
parse. Do not call the other parse methods during an asynchronous  
parse.  
  
@param requestObserver The observer to notify on start/stop. This  
                       argument can be null.  
@param uri The base URI.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>requestObserver</td>
<td>The observer to notify on start/stop. This  
                       argument can be null.  
</td>
</tr>

<tr>
<td>uri</td>
<td>The base URI.  
</td>
</tr>

</table>

## Attributes ##

### listener ###
  
The listener that will respond to feed events.   
  
