---
layout: default
---

# nsIFeedProgressListener #
  
nsIFeedProgressListener defines callbacks used during feed  
processing.  
  

## Methods ##

### reportError ###
  
ReportError will be called in the event of fatal  
XML errors, or if the document is not a feed. The bozo   
bit will be set if the error was due to a fatal error.   
  
@param errorText  
       A short description of the error.  
@param lineNumber  
       The line on which the error occurred.  
  

### handleStartFeed ###
  
StartFeed will be called as soon as a reasonable start to  
a feed is detected.   
   
@param result  
       An object implementing nsIFeedResult representing the feed   
       and its metadata. At this point, the result has version   
       information.  
  

### handleFeedAtFirstEntry ###
  
Called when the first entry/item is encountered. In Atom, all  
feed data is required to preceed the entries. In RSS, the data  
usually does. If the type is one of the entry/item-only types,  
this event will not be called.  
  
@param result  
       An object implementing nsIFeedResult representing the feed   
       and its metadata. At this point, the result will likely have  
       most of its feed-level metadata.  
  

### handleEntry ###
  
Called after each entry/item. If the document is a standalone  
item or entry, this HandleFeedAtFirstEntry will not have been  
called. Also, this entry's parent field will be null.  
  
@param entry  
       An object implementing nsIFeedEntry that represents the latest  
       entry encountered.  
@param result  
       An object implementing nsIFeedResult representing the feed   
       and its metadata.   
  
