---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/feeds/nsIFeedListener.idl">Source file</a>
</div>

# nsIFeedProgressListener #
  
nsIFeedProgressListener defines callbacks used during feed  
processing.  
  

## Methods ##

### reportError(errorText, lineNumber, bozo) ###
  
ReportError will be called in the event of fatal  
XML errors, or if the document is not a feed. The bozo   
bit will be set if the error was due to a fatal error.   
  
  

#### Parameters ####

<table>

<tr>
<td>errorText</td>
<td>       A short description of the error.  
</td>
</tr>

<tr>
<td>lineNumber</td>
<td>       The line on which the error occurred.  
</td>
</tr>

</table>

### handleStartFeed(result) ###
  
StartFeed will be called as soon as a reasonable start to  
a feed is detected.   
   
  

#### Parameters ####

<table>

<tr>
<td>result</td>
<td>       An object implementing nsIFeedResult representing the feed   
       and its metadata. At this point, the result has version   
       information.  
</td>
</tr>

</table>

### handleFeedAtFirstEntry(result) ###
  
Called when the first entry/item is encountered. In Atom, all  
feed data is required to preceed the entries. In RSS, the data  
usually does. If the type is one of the entry/item-only types,  
this event will not be called.  
  
  

#### Parameters ####

<table>

<tr>
<td>result</td>
<td>       An object implementing nsIFeedResult representing the feed   
       and its metadata. At this point, the result will likely have  
       most of its feed-level metadata.  
</td>
</tr>

</table>

### handleEntry(entry, result) ###
  
Called after each entry/item. If the document is a standalone  
item or entry, this HandleFeedAtFirstEntry will not have been  
called. Also, this entry's parent field will be null.  
  
  

#### Parameters ####

<table>

<tr>
<td>entry</td>
<td>       An object implementing nsIFeedEntry that represents the latest  
       entry encountered.  
</td>
</tr>

<tr>
<td>result</td>
<td>       An object implementing nsIFeedResult representing the feed   
       and its metadata.   
</td>
</tr>

</table>
