---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/protocol/viewsource/nsIViewSourceChannel.idl">Source file</a>
</div>

# nsIViewSourceChannel #

## Attributes ##

### originalContentType ###
  
The actual (MIME) content type of the data.  
  
nsIViewSourceChannel returns a content type of  
"application/x-view-source" if you ask it for the contentType  
attribute.  
  
However, callers interested in finding out or setting the  
actual content type can utilize this attribute.  
  

### isSrcdocChannel ###
  
Whether the channel was created to view the source of a srcdoc document.  
  

### baseURI ###
  
Set to indicate the base URI.  If this channel is a srcdoc channel, it  
returns the base URI provided by the embedded channel.  It is used to  
provide an indication of the base URI in circumstances where it isn't  
otherwise recoverable.  Returns null when it isn't set and isn't a  
srcdoc channel.  
  
